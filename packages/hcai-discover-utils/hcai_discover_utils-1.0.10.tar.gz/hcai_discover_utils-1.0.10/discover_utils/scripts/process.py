"""Standalone script for general processing

Author:
    Dominik Schiller <dominik.schiller@uni-a.de>
Date:
    20.09.2023

This script performs generall data processing to extract either annotations to NOVA-Database or streams to disk using a provided nova-server module for inference.

.. argparse::
   :module: discover_utils.scripts.process
   :func: parser
   :prog: du-process

Returns:
    None

Example:
    >>> du-process --dataset "test" --db_host "127.0.0.1" --db_port "37317" --db_user "my_user" --db_password "my_password" --trainer_file_path "test\\test_predict.trainer" --sessions "[\"test_session_1\", \"test_session_2\"]" --data "[{\"src\": \"db:anno\", \"scheme\": \"transcript\", \"annotator\": \"test\", \"role\": \"testrole\"}]" --frame_size "0" --left_context "0" --right_context "0" --job_i_d "test_job" --opt_str "num_speakers=2;speaker_ids=testrole,testrole2" --cml_dir "./cml" --data_dir "./data" --log_dir "./log" --cache_dir "./cache" --tmp_dir "./tmp"
"""

import argparse
import sys
import os
import shutil
import traceback
from importlib.machinery import SourceFileLoader
from pathlib import Path, PureWindowsPath
from typing import Union, Type

import discover_utils.data.handler.file_handler
from discover_utils.data.provider.data_manager import DatasetManager, SessionManager
from discover_utils.data.provider.dataset_iterator import DatasetIterator
from discover_utils.interfaces.server_module import Predictor, Extractor
from discover_utils.scripts.parsers import (
    dm_parser,
    nova_db_parser,
    request_parser,
    nova_iterator_parser,
    nova_server_module_parser,
    io_parser
)
from discover_utils.utils import ssi_xml_utils, string_utils
from discover_utils.utils.string_utils import string_to_bool, parse_time_string_to_ms
from discover_utils.utils.anno_utils import pack_remove
from discover_utils.data.annotation import DiscreteAnnotation

# Main parser for predict specific options
parser = argparse.ArgumentParser(
    description="Use a provided nova-server module for inference and save results to NOVA-DB",
    parents=[dm_parser,
             nova_db_parser,
             request_parser,
             nova_iterator_parser,
             nova_server_module_parser,
             io_parser],
    fromfile_prefix_chars='@',
)
parser.add_argument(
    "--trainer_file_path",
    type=str,
    required=True,
    help="Path to the trainer file using Windows UNC-Style",
)

parser.add_argument(
    "--anno_min_dur",
    type=str,
    required=False,
    default=-999999999,
    help="Minimum duration for discrete annotations in either seconds (float or 's'-suffix) or milliseconds (int or 'ms'-suffix)",
)

parser.add_argument(
    "--anno_min_gap",
    type=str,
    required=False,
    default=-999999999,
    help="Minimum gap between labels of the same class to be considered separate labels. Specified in either seconds (float or 's'-suffix) or milliseconds (int or 'ms'-suffix)",
)


def main(args):

    process_args, _ = parser.parse_known_args(args)

    # Create argument groups
    db_args, _ = nova_db_parser.parse_known_args(args)
    req_args, _ = request_parser.parse_known_args(args)
    dm_args, _ = dm_parser.parse_known_args(args)
    iter_args, _ = nova_iterator_parser.parse_known_args(args)
    module_args, _ = nova_server_module_parser.parse_known_args(args)
    io_args, _ = io_parser.parse_known_args(args)

    # Set environment variables
    os.environ['CACHE_DIR'] = module_args.cache_dir
    os.environ['TMP_DIR'] = module_args.tmp_dir

    caught_ex = False

    # Preprocess options
    anno_min_dur = parse_time_string_to_ms(process_args.anno_min_dur)
    anno_min_gap = parse_time_string_to_ms(process_args.anno_min_gap)

    # Load trainer
    trainer = ssi_xml_utils.Trainer()
    trainer_file_path = Path(module_args.cml_dir).joinpath(
        PureWindowsPath(process_args.trainer_file_path)
    )
    if not trainer_file_path.is_file():
        raise FileNotFoundError(f"Trainer file not available: {trainer_file_path}")
    else:
        trainer.load_from_file(trainer_file_path)
        print("Trainer successfully loaded.")

    # Load module
    if not trainer.model_script_path:
        raise ValueError('Trainer has no attribute "script" in model tag.')

    model_script_path = (
            trainer_file_path.parent / PureWindowsPath(trainer.model_script_path)
    ).resolve()
    source = SourceFileLoader(
        "ns_cl_" + model_script_path.stem, str(model_script_path)
    ).load_module()
    print(f"Trainer module {Path(model_script_path).name} loaded")

    opts = module_args.options
    if module_args.options is None:
        opts = string_utils.parse_nova_option_string(process_args.opt_str)
        print('Option --opt_str is deprecated. Use --options in the future.')

    processor_class: Union[Type[Predictor], Type[Extractor]] = getattr(
        source, trainer.model_create
    )
    processor = processor_class(model_io=trainer.meta_io, opts=opts, trainer=trainer)
    print(f"Model {trainer.model_create} created")


    # Build data loaders
    ctx = {
        'db' : {
            **vars(db_args)
        },
        'request' : {
            **vars(req_args)
        }
    }

    # Clear output directory for job id
    shared_dir = ctx['request'].get('shared_dir')
    job_id = ctx['request'].get('job_id')
    if shared_dir and job_id:
        output_dir = Path(shared_dir) / job_id
        if output_dir.exists():
            if output_dir.is_dir():
                shutil.rmtree(output_dir)
        if output_dir.is_file():
            output_dir.unlink()

    single_session_data_provider = []

    # Create one dataset per session
    video_backend = discover_utils.data.handler.file_handler.VideoBackend[io_args.video_backend]
    for session in dm_args.sessions:
        is_iterable = string_to_bool(trainer.meta_is_iterable)
        if is_iterable:
            data_provider = DatasetIterator(dataset=dm_args.dataset, data_description=dm_args.data, source_context=ctx, session_names=[session], video_backend= video_backend, **vars(iter_args))
        else:
            data_provider = DatasetManager(dataset=dm_args.dataset, data_description=dm_args.data, source_context=ctx, session_names=[session],  video_backend= video_backend)

        single_session_data_provider.append(data_provider)
    print("Data managers initialized")

    # Iterate over all sessions
    total_sessions = len(single_session_data_provider)
    for session_idx, provider in enumerate(single_session_data_provider):
        session = provider.session_names[0]
        #data_provider = provider
        try:
            if isinstance(provider, DatasetManager):
                provider.load()

            # Data processing with progress information
            print(f"Processing session ({session_idx + 1}/{total_sessions}): {session}...")

            data_processed = processor.process_data(provider)
            data_output = processor.to_output(data_processed)

            # Data Saving
            session_manager : SessionManager
            session_manager = provider.sessions[session]['manager']
            for io_id, data_object in data_output.items():
                if isinstance(data_object, DiscreteAnnotation):
                    data_object.data = pack_remove(data_object.data, min_gap=anno_min_gap, min_dur=anno_min_dur)
                session_manager.output_data_templates[io_id] = data_object

            provider.save()
            print(f"Completed session ({session_idx + 1}/{total_sessions}): {session}...")

        except Exception as e:
            traceback.print_exc()
            print(
                f"\tProcessor exited with error: '{str(e)}'.\nContinuing with next session ({session_idx + 1}/{total_sessions})."
            )
            caught_ex = True
            continue

    print("Processing completed!")
    if caught_ex:
        print(
            "Processing job encountered errors for some sessions. Check logs for details."
        )
        exit(1)

# Entry point for du-process
def cl_main():
    main(sys.argv[1:])

# Entry point for python
if __name__ == "__main__":
    main(sys.argv[1:])
