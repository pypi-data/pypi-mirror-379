""" Module to create a data iterator for streams and annotations

Author:
    Dominik Schiller <dominik.schiller@uni-a.de>
Date:
    18.8.2023

"""
import os
import sys
import warnings
from pathlib import Path
from typing import Union
from collections.abc import Iterator

import numpy as np
from discover_utils.data.handler.nova_db_handler import NovaSession
from discover_utils.data.provider.data_manager import SessionManager, DatasetManager
from discover_utils.data.stream import Stream, Audio
from discover_utils.data.annotation import FreeAnnotation, DiscreteAnnotation, ContinuousAnnotation
from discover_utils.utils import string_utils
from discover_utils.utils.anno_utils import data_contains_garbage


class DatasetIterator(DatasetManager):
    """Iterator class for processing data samples from the Nova dataset.

    The NovaIterator takes all information about what data should be loaded and how it should be processed. The class itself then takes care of loading all data and provides an iterator to directly apply a sliding window to the requested data.
    Every time based argument can be passed either as string or a numerical value. If the time is passed as string, the string should end with either 's' to indicate the time is specified in seconds or 'ms' for milliseconds.
    If the time is passed as a numerical value or as a string without indicating a specific unit it is assumed that an integer value represents milliseconds while a float represents seconds. All numbers will be represented as integer milliseconds internally.
    The highest time resolution for processing is therefore 1ms.

    Args:


        frame_size (Union[int, float, str], optional): Size of the data frame measured in time. Defaults to None.
        start (Union[int, float, str], optional): Start time for processing measured in time. Defaults to None.
        end (Union[int, float, str], optional): End time for processing measured in time. Defaults to None.
        left_context (Union[int, float, str], optional): Left context duration measured in time. Defaults to None.
        right_context (Union[int, float, str], optional): Right context duration measured in time. Defaults to None.
        stride (Union[int, float, str], optional): Stride for iterating over data measured in time. If stride is not set explicitly it will be set to frame_size. Defaults to None.
        add_rest_class (bool, optional): Whether to add a rest class for discrete annotations. Defaults to True.
        fill_missing_data (bool, optional): Whether to fill missing data. Defaults to True. THIS OPTION IS CURRENTLY NOT DOING ANYTHING

    Attributes:


        frame_size (int, float, str): Size of the data frame measured in time.
        start (int, float, str): Start time for processing measured in time.
        end (int, float, str): End time for processing measured in time.
        left_context (int, float, str): Left context duration measured in time.
        right_context (int, float, str): Right context duration measured in time.
        stride (int, float, str): Stride for iterating  data measured in time.
        add_rest_class (bool): Whether to add a rest class for discrete annotations.
        fill_missing_data (bool): Whether to fill missing data.

    Example:
        .. code-block:: python

            from dotenv import load_dotenv

            # Load environment variables
            IP = 127.0.0.1
            PORT = 1337
            USER = my_user
            PASSWORD = my_password
            DATA_DIR = /data

            # Define dataset and sessions
            dataset = "test_dataset"
            sessions = ["test_session"]

            # Define data descriptions
            annotation = {
                "id" : "my_transcript_1",
                "type": "input",
                "src": "db:anno",
                "scheme": "transcript",
                "annotator": "test_annotator",
                "role": "test_role",
            }

            stream = {
                "id" : "model_output",
                "type" : "input",
                "src": "db:stream",
                "role": "test_role",
                "name": "extracted_features",
            }

            file = {
                "id": "just_a_file",
                "type": "output",
                "src": "file:stream",
                "fp": "/path/to/my/video/test_video.mp4",
            }

            # Create a NovaIterator instance
            nova_iterator = NovaIterator(
                IP,
                PORT,
                USER,
                PASSWORD,
                dataset,
                DATA_DIR,
                sessions=sessions,
                data=[annotation, file],
                frame_size="5s",
                end="20s",
            )

            # Example: Get the next data sample and set a breakpoint
            a = next(nova_iterator)
    """

    def __init__(
            self,
            # Data
            #dataset_manager: DatasetManager,
            *args,

            # Iterator Window
            frame_size: Union[int, float, str] = None,
            start: Union[int, float, str] = None,
            end: Union[int, float, str] = None,
            left_context: Union[int, float, str] = None,
            right_context: Union[int, float, str] = None,
            stride: Union[int, float, str] = None,

            # Iterator properties
            add_rest_class: bool = True,
            fill_missing_data=True,

            **kwargs
    ):
        #self.dataset_manager = dataset_manager
        super().__init__(*args, **kwargs)
        # If stride has not been explicitly set it's the same as the frame size
        if stride is None:
            stride = frame_size

        # Parse all times to milliseconds
        self.left_context = string_utils.parse_time_string_to_ms(left_context)
        self.right_context = string_utils.parse_time_string_to_ms(right_context)
        self.frame_size = string_utils.parse_time_string_to_ms(frame_size)
        self.stride = string_utils.parse_time_string_to_ms(stride)
        self.start = string_utils.parse_time_string_to_ms(start)
        self.end = string_utils.parse_time_string_to_ms(end)

        # Frame size 0 or None indicates that the whole session should be returned as one sample
        if self.frame_size == 0:
            warnings.warn(
                "Frame size should be bigger than zero. Returning whole session as sample."
            )

        # If the end time has not been set we initialize it with sys.maxsize
        if self.end is None or self.end == 0:
            self.end = sys.maxsize

        self.add_rest_class = add_rest_class
        self.fill_missing_data = fill_missing_data
        self.current_session = None

        # Data handler
        self._iterable = self._yield_sample()

    def _guess_session_length(self, session):

        annotation_duration = -1
        stream_duration = sys.maxsize
        for id, data in session.input_data.items():
            # Discrete and free annotations do not need to be present at the end of a session. So we consider the maximum length.
            if isinstance(data, FreeAnnotation) or isinstance(data, DiscreteAnnotation):
                if data.meta_data.duration is not None and data.meta_data.duration > annotation_duration:
                    annotation_duration = data.meta_data.duration
            # Streams and continuous annotations do need to cover the whole session. Consider the minimum length.
            elif isinstance(data, Stream) or isinstance(data, ContinuousAnnotation):
                if data.meta_data.duration is not None and data.meta_data.duration < stream_duration:
                    stream_duration = data.meta_data.duration

        # If a datastream is present we use it to determine the length
        if stream_duration < sys.maxsize:
            return stream_duration
        else:
            return annotation_duration

    def _yield_sample(self) -> Iterator[dict]:
        """
        Yield examples.

        Yields:
            dict: Sampled data for the window.

        Example:
            {
                <scheme>_<annotator>_<role> : [[data1], [data2]... ],
                <file_path> : [[data1], [data2]... ]
            }
        """

        # Needed to sort the samples later and assure that the order is the same as in nova.
        # sample_counter = 1

        for session_name, session in self.sessions.items():
            # Init all data objects for the session and get necessary meta information
            self.session_manager: SessionManager
            self.session_info: NovaSession
            self.current_session = session.get('manager')
            self.current_session_info = session.get('info')
            self.current_session.load()

            # TODO: Check if we run into duration errors
            if self.current_session_info is None:
                self.current_session_info = NovaSession()
            if self.current_session_info.duration is None:
                self.current_session_info.duration = self._guess_session_length(self.current_session)

            # If frame size is zero or less we return the whole data from the whole session in one sample
            if self.frame_size <= 0:
                _frame_size = min(self.current_session_info.duration, self.end - self.start)
                _stride = _frame_size
            else:
                _frame_size = self.frame_size
                _stride = self.stride

            # Starting position of the first frame in seconds
            cpos = 0

            # TODO account for stride and framesize being None
            # Generate samples for this session
            while cpos + self.stride <= min(
                    self.end, self.current_session_info.duration
            ):
                frame_start = cpos
                frame_end = cpos + _frame_size

                window_start = frame_start - self.left_context
                window_end = frame_end + self.right_context

                window_info = (
                        self.current_session.session
                        + "_"
                        + str(window_start / 1000)
                        + "_"
                        + str(window_end / 1000)
                )

                data_for_window = {}
                warn_once = []

                for k, v in self.current_session.input_data.items():

                    # TODO current_session duration is not the correct way to end right padding. We could have longer streams
                    start_ = max(0, window_start)
                    end_ = min(self.current_session_info.duration, window_end)

                    try:
                        sample = v.sample_from_interval(start_, end_)
                    except Exception as e:
                        # Stream is shorter than session duration
                        if v.meta_data.__dict__.get('duration', sys.maxsize) < self.current_session_info.duration:
                            if not k in warn_once:
                                warn_once.append(k)
                                print(f'Error retreiving data for window {window_info} in stream {k}. Stream is shorter than session. From now on np.NaN values will be returned')

                        else:
                            print(f'Error retreiving data for window {window_info} in stream {k}. Exception caught when retreiving sample. Returning NaN values: {e}')
                        data_for_window[k] = np.nan

                    # TODO pad continuous annotations
                    # Apply padding
                    if isinstance(v, Stream):

                        # Don't pad anything but num_samples axis
                        sr = v.meta_data.sample_rate / 1000
                        left_pad = int((0 - window_start) * sr) if window_start < 0 else 0
                        right_pad = int((
                                                    window_end - self.current_session_info.duration) * sr) if window_end > self.current_session_info.duration else 0

                        # Currently all streams have timedim first. Keep for future reference.
                        time_dim_last = False

                        # In some cases sample sample_from_interval might return a frame number that is one frame off from what we expect.
                        # This is due to sampling issues when frame sizes do not match the samplerate. We fix this here.
                        num_samples_exp = int((abs(window_start) + window_end) * sr)
                        num_samples = int(left_pad + right_pad + sample.shape[0])
                        if num_samples > num_samples_exp:
                            diff = (num_samples - num_samples_exp)
                            if time_dim_last:
                                sample = sample[:,:-diff]
                            else:
                                sample = sample[:-diff]


                        if left_pad or right_pad:
                            lr_pad = ((left_pad, right_pad),)
                            n_pad = tuple([(0, 0)] * (len(sample.shape) - 1))

                            # Num samples last dim
                            if time_dim_last:
                                pad = n_pad + lr_pad
                            # Num samples first dim
                            else:
                                pad = lr_pad + n_pad

                            sample = np.pad(sample, pad_width=pad, mode='edge')
                    data_for_window[k] = sample

                # Performing sanity checks
                garbage_detected = any(
                    [data_contains_garbage(d) for k, d in data_for_window.items()]
                )

                # Incrementing counter
                cpos += _stride

                if garbage_detected:
                    continue

                data_for_window['info'] = window_info
                yield data_for_window

    def __iter__(self) -> Iterator[dict]:
        return self._iterable

    def __next__(self) -> dict:
        return self._iterable.__next__()


if __name__ == "__main__":
    from pathlib import Path
    import os
    import dotenv
    dotenv.load_dotenv()
    DISCOVER_TEST_FILE_DIR = Path(os.getenv("DISCOVER_DATA_DIR"))
    DISCOVER_OUR_DIR = Path(os.getenv("DISCOVER_TEST_DIR"))

    IP = os.getenv("NOVA_IP", "")
    PORT = int(os.getenv("NOVA_PORT", 0))
    USER = os.getenv("NOVA_USER", "")
    PASSWORD = os.getenv("NOVA_PASSWORD", "")
    DATA_DIR = Path(os.getenv("NOVA_DATA_DIR", None))

    DATASET = os.getenv("DISCOVER_ITERATOR_TEST_DATASET")
    SESSIONS = [os.getenv("DISCOVER_ITERATOR_TEST_SESSION")]
    SCHEME = os.getenv("DISCOVER_ITERATOR_TEST_SCHEME")
    ANNOTATOR = os.getenv("DISCOVER_ITERATOR_TEST_ANNOTATOR")
    ROLE = os.getenv("DISCOVER_ITERATOR_TEST_ROLE")
    FEATURE_STREAM = os.getenv("DISCOVER_ITERATOR_TEST_STREAM")

    annotation = {
        "src": "db:annotation",
        "scheme": SCHEME,
        "type": "input",
        "id": "annotation",
        "annotator": ANNOTATOR,
        "role": ROLE,
    }

    stream = {
        "src": "db:stream",
        "type": "input",
        "id": "featurestream",
        "role": ROLE,
        "name": FEATURE_STREAM,
    }

    file = {
        "src": "file:stream:Audio",
        "type": "input",
        "id": "file",
        "uri": DISCOVER_TEST_FILE_DIR/"test_audio.wav",
    }

    ctx = {
        "db": {
            "db_host": IP,
            "db_port": PORT,
            "db_user": USER,
            "db_password": PASSWORD,
            "data_dir": DATA_DIR,
        },
    }

    nova_iterator = DatasetIterator(
        dataset=DATASET,
        data_description=[file, annotation, stream],
        session_names=SESSIONS,
        source_context=ctx,
        frame_size="1s",
        left_context="2s",
        right_context="2s",
        end="100s",
    )

    while (a := next(nova_iterator)):
        breakpoint()
        continue
