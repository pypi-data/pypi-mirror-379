"""Data Storage Class for session specific data
Author: Dominik Schiller <dominik.schiller@uni-a.de>
Date: 25.10.2023
"""
from pathlib import Path
from discover_utils.data.annotation import FreeAnnotation, FreeAnnotationScheme, ContinuousAnnotation, \
    ContinuousAnnotationScheme, DiscreteAnnotation, DiscreteAnnotationScheme
from discover_utils.utils import path_utils
from discover_utils.data.data import Data
from discover_utils.data.handler import (
    file_handler,
    nova_db_handler,
    url_handler,
    request_handler,
)
from discover_utils.data.stream import SSIStream, Video, Audio, Stream
from  discover_utils.data.static import Image, Text
from discover_utils.utils.request_utils import Origin, SuperType, SubType, parse_src_tag, data_description_to_string, \
    infer_dtype


class SessionManager:
    """
    Class to aggregate and manage interrelated incoming and outgoing datastreams belonging to a single session (e.g multimodal data from the same recording).

    Attributes:
        input_data (dict, optional):  Annotation or Stream data that can be processed by a module.
        dataset (str, optional): The dataset or category the session belongs to.
        data_description (list[dict[str, str]], optional): List of data descriptions. Defaults to None. The dictionary should have the following mandatory fields:
        source_context (dict[str, dict]) : Dict of parameters that are need to interact with a source. E.g. database credentials or data directories. Must match constructor arguments of the respective data handler.
        session (str, optional): The name or title of the session.
        duration (int, optional): The duration of the session in minutes.
        location (str, optional): The location or venue of the session.
        language (str, optional): The language used in the session.
        date (datetime, optional): The date and time of the session.
        is_valid (bool, optional): Whether the session is considered valid.
        extra_data (dict, optional): Additional stream or annotation information for the session. Might only contain meta information.
        output_data_templates (dict, optional): Empty data objects that contain meta information for outputs. Modules can fill the data here.

    Args:
        dataset (str, optional): The dataset or category the session belongs to. Must match NovaDB entries if 'db' is
        data_description (list[dict[str, str]], optional): List of data descriptions. Defaults to None. The dictionary should have the following mandatory fields:
            ``"id"``:
                Unique id to map the data to a given input / output.
            ``"name"``:
                Output name for streams
            ``"type"``:
                IO type of the data. Either "input" or "output"
            ``"src"``
                The source and datatype to load the data from separated by ':' . Source corresponds to any Origin.value and datatype has the format '<SuperType.value>:<SubType.value>:str'
                E.g. 'db:stream:video:specification'

            In addition, each entry should provide the information that is need to identify the exact input and output targets.
            Must match the input parameters of the respective data handlers save and load function (dataset and session are already specified as properties).
            E.g. to load an annotation from NovaDB we use the data.handler.nova_db_handler.AnnotationHandler we need the following additional fields.
                ``"scheme"``
                    The scheme name of the annotations to load. Only necessary when loading annotations from the database.
                ``"annotator"``
                    The annotator of the annotations to load. Only necessary when loading annotations from the database.
                ``"role"``
                    The role to which the data belongs. Only necessary when accessing data from the database.
            To load a stream file from disk using data.handler.file_handler.FileHandler we only need a filepath
            ``"uri"``
                The filepath from which to load the data from. Only necessary when loading files from disk.

        session (str, optional): The name or title of the session.
        source_context (dict[str, dict]) : List of parameters that are need to interact with a source. E.g. database credentials or data directories. Must match constructor arguments of the respective data handler.
        duration (int, optional): The duration of the session in milliseconds.
        location (str, optional): The location or venue of the session.
        language (str, optional): The language used in the session.
        date (datetime, optional): The date and time of the session.
        is_valid (bool, optional): Whether the session is considered valid.
        input_data (dict, optional): Annotation or Stream data that can be processed by a module.
        extra_data (dict, optional): Additional stream or annotation information for the session. Might only contain meta information.
        output_data_templates (dict, optional): Empty data objects that contain meta information for outputs. Modules can fill the data here.
    """

    def __init__(
            self,
            dataset: str = None,
            data_description: list[dict[str, str]] = None,
            session: str = None,
            source_context: dict[str, dict] = None,
            input_data: dict = None,
            extra_data: dict = None,
            output_data_templates: dict = None,
            video_backend: file_handler.VideoBackend = file_handler.VideoBackend.IMAGEIO,
    ):
        self.dataset = dataset
        self.data_description = data_description
        self.session = session
        self.input_data = {} if input_data is None else input_data
        self.extra_data = {} if extra_data is None else extra_data
        self.output_data_templates = (
            {} if output_data_templates is None else output_data_templates
        )
        self.source_context = {}
        if source_context is not None:
            for src, context in source_context.items():
                src_ = Origin(src)
                self.add_source_context(src_, context)

        self.video_backend = video_backend

    def add_source_context(self, source: Origin, context: dict):
        """Add all parameters that are necessary to initialize source specific data handler for reading and writing data objects."""
        self.source_context[source] = context

    def _update_data_description(self, data_description=None):
        if data_description is not None:
            self.data_description = data_description
        return self.data_description

    def load(self, data_description=None):
        """
        Args:
            data_description (list[dict[str, str]], optional): List of data descriptions. Defaults to None. The dictionary should have the following mandatory fields:
            ``"id"``:
                Unique id to map the data to a given input / output.
            ``"name"``:
                Output name for streams
            ``"type"``:
                IO type of the data. Either "input" or "output"
            ``"src"``
                The source and datatype to load the data from separated by ':' . Source corresponds to any Origin.value and datatype has the format '<SuperType.value>:<SubType.value>:str'
                E.g. 'db:stream:video:specification'

            In addition, each entry should provide the information that is need to identify the exact input and output targets.
            Must match the input parameters of the respective data handlers save and load function (dataset and session are already specified as properties).
            E.g. to load an annotation from NovaDB we use the data.handler.nova_db_handler.AnnotationHandler we need the following additional fields.
                ``"scheme"``
                    The scheme name of the annotations to load. Only necessary when loading annotations from the database.
                ``"annotator"``
                    The annotator of the annotations to load. Only necessary when loading annotations from the database.
                ``"role"``
                    The role to which the data belongs. Only necessary when accessing data from the database.
            To load a stream file from disk using data.handler.file_handler.FileHandler we only need a filepath
            ``"fp"``
                The filepath from which to load the data from. Only necessary when loading files from disk.

        Returns:

        """

        data_description = self._update_data_description(data_description)
        if data_description is None:
            raise ValueError(
                "Data description is empty. Either pass a data description to load() or set it as class attribute."
            )

        for desc in data_description:
            src, super_dtype, sub_dtype, specific_dtype = parse_src_tag(desc)

            header_only = False
            if desc.get("type") == "input":
                io_dst = self.input_data
            elif desc.get("type") == "output":
                io_dst = self.output_data_templates
                header_only = True
            else:
                io_dst = self.extra_data

            data_id = data_description_to_string(desc)
            data = None

            if src in [Origin.DB] and not src in self.source_context.keys():
                raise ValueError(
                    f"Missing context information source {src}. Call add_source_context() first."
                )
            try:
                # DATABASE
                if src == Origin.DB:
                    ctx = self.source_context[src]
                    if super_dtype == SuperType.ANNO:
                        handler = nova_db_handler.AnnotationHandler(**ctx)
                        data = handler.load(
                            dataset=self.dataset,
                            session=self.session,
                            scheme=desc["scheme"],
                            annotator=desc["annotator"],
                            role=desc["role"],
                            header_only=header_only
                        )
                    elif super_dtype == SuperType.STREAM:
                        handler = nova_db_handler.StreamHandler(**ctx)
                        data = handler.load(
                            dataset=self.dataset,
                            session=self.session,
                            name=desc["name"],
                            role=desc["role"],
                            header_only=header_only
                        )
                # FILE
                elif src == Origin.FILE:
                    fp = Path(path_utils.get_tmp_dir()) / desc['uri']
                    handler = file_handler.FileHandler(video_backend=self.video_backend)
                    data = handler.load(fp=fp, header_only=header_only)
                # URL
                elif src == Origin.URL:
                    handler = url_handler.URLHandler()
                    data = handler.load(url=desc["uri"])
                # REQUEST
                elif src == Origin.REQUEST:
                    target_dtype = infer_dtype(super_dtype, sub_dtype)
                    handler = request_handler.RequestHandler()
                    data = handler.load(data=desc.get("data"), dtype=target_dtype, header_only=header_only)

            except FileNotFoundError as e:
                # Only raise file not found error if stream is requested as input
                if not header_only:
                    raise e

                # Create empty data objects with known params
                else:
                    if super_dtype == SuperType.STREAM:
                        if sub_dtype == SubType.SSIStream:
                            data_cls = SSIStream
                        elif sub_dtype == SubType.VIDEO:
                            data_cls = Video
                        elif sub_dtype == SubType.AUDIO:
                            data_cls = Audio
                        else:
                            data_cls = Stream
                        data = data_cls(
                            None,
                            name=desc.get("name"),
                            role=desc.get("role"),
                            sample_rate=1,
                            dataset=self.dataset,
                            session=self.session,
                        )
                    elif super_dtype == SuperType.IMAGE:
                        data_cls = Image
                        data = data_cls(
                            None,
                            name=desc.get("name"),
                            role=desc.get("role"),
                            dataset=self.dataset,
                            session=self.session,
                        )
                    elif super_dtype == SuperType.TEXT:
                        data_cls = Text
                        data = data_cls(
                            None,
                            name=desc.get("name"),
                            role=desc.get("role"),
                            dataset=self.dataset,
                            session=self.session,
                        )
                    elif super_dtype == SuperType.ANNO:
                        if sub_dtype is None:
                            sub_dtype = SubType.FREE
                        print(
                            f'No predefined annotation scheme available. Creating generic {sub_dtype.value} template annotation for {desc}')
                        if sub_dtype == SubType.FREE:
                            data = FreeAnnotation(scheme=FreeAnnotationScheme(name='generic'), data=None)
                        elif sub_dtype == SubType.CONTINUOUS:
                            data = ContinuousAnnotation(
                                scheme=ContinuousAnnotationScheme(name='generic', sample_rate=1, min_val=0, max_val=1),
                                data=None)
                        elif sub_dtype == SubType.DISCRETE:
                            data = DiscreteAnnotation(scheme=DiscreteAnnotationScheme(name='generic', classes={'1' : 'class_one', '2': 'class_two'}))
                        else:
                            raise ValueError(
                                f"Can\'t create template for {desc} because no scheme information is available.")

                    else:
                        # Todo Handle other cases where no header might be loaded
                        data = Data()

            io_dst[data_id] = data

    def save(self, data_description=None, overwrite=True):
        """
        Args:
          data_description (list[dict[str, str]], optional): List of data descriptions. Defaults to None. The dictionary should have the following mandatory fields:
          ``"id"``:
              Unique id to map the data to a given input / output.
          ``"name"``:
              Output name for streams
          ``"type"``:
              IO type of the data. Either "input" or "output"
          ``"src"``
              The source and datatype to load the data from separated by ':' . Source is of typ Source.value and datatype of type DType.value
              E.g. 'db:anno'

          In addition, each entry should provide the information that is need to identify the exact input and output targets.
          Must match the input parameters of the respective data handlers save and load function (dataset and session are already specified as properties).
          E.g. to load an annotation from NovaDB we use the data.handler.nova_db_handler.AnnotationHandler we need the following additional fields.
              ``"scheme"``
                  The scheme name of the annotations to load. Only necessary when loading annotations from the database.
              ``"annotator"``
                  The annotator of the annotations to load. Only necessary when loading annotations from the database.
              ``"role"``
                  The role to which the data belongs. Only necessary when accessing data from the database.
          To load a stream file from disk using data.handler.file_handler.FileHandler we only need a filepath
          ``"fp"``
              The filepath from which to load the data from. Only necessary when loading files from disk.

        Returns:
        """

        data_description = self._update_data_description(data_description)
        if data_description is None:
            raise ValueError(
                "Data description is empty. Either pass a data description to save() or set it as class attribute."
            )

        success = False

        for desc in data_description:

            # Do not write the output if active flag is not set
            if not desc.get('active', True):
                continue

            src, super_dtype, sub_dtype, specific_dtype = parse_src_tag(desc)

            if not desc.get("type") == "output":
                continue

            data_id = data_description_to_string(desc)

            if src in [Origin.DB] and not src in self.source_context.keys():
                raise ValueError(
                    f"Missing context information source {src}. Call add_source_context() first."
                )

            data = self.output_data_templates[data_id]
            if src == Origin.DB:
                ctx = self.source_context[src]
                if super_dtype == SuperType.ANNO:
                    role = desc.get('role')
                    scheme = desc.get('scheme')
                    annotator = desc.get('annotator')
                    handler = nova_db_handler.AnnotationHandler(**ctx)
                    success = handler.save(dataset=self.dataset, session=self.session, annotation=data, overwrite=overwrite, role=role, annotator=annotator, scheme=scheme)
                elif super_dtype == SuperType.STREAM:
                    name = desc.get('name')
                    role = desc.get('role')
                    handler = nova_db_handler.StreamHandler(**ctx)
                    success = handler.save(dataset=self.dataset, session=self.session, stream=data, role=role, name=name)
            elif src == Origin.FILE:
                handler = file_handler.FileHandler()
                success = handler.save(data=data, fp=Path(desc["uri"]))
            elif src == Origin.URL:
                raise NotImplementedError
            elif src == Origin.REQUEST:
                rq = self.source_context.get(Origin.REQUEST)
                shared_dir = rq.get('shared_dir')
                job_id = rq.get('job_id')
                handler = request_handler.RequestHandler()
                handler.save(data=data, shared_dir=shared_dir, job_id=job_id, dataset=self.dataset,
                             session=self.session)

        return success


class DatasetManager:
    def __init__(
            self, data_description: list[dict[str, str]], source_context: dict = None, dataset: str = None,
            session_names: list = None, video_backend: file_handler.VideoBackend = file_handler.VideoBackend.IMAGEIO
    ):
        self.dataset = dataset
        self.data_description = data_description
        self.session_names = session_names
        self.source_ctx = source_context
        self.sessions = {}
        self.video_backend = video_backend
        self._init_sessions()

    def _init_sessions(self):
        db_required = any([parse_src_tag(dd)[0] == Origin.DB for dd in self.data_description])

        # Load session information from database
        if db_required:
            sh = nova_db_handler.SessionHandler(**self.source_ctx["db"])
            sessions = sh.load(self.dataset, self.session_names)
            for sess in sessions:
                sm = SessionManager(
                    self.dataset, self.data_description, sess.name, self.source_ctx, video_backend = self.video_backend
                )
                self.sessions[sess.name] = {"manager": sm, "info": sess}
            self.session_names = list(self.sessions.keys())

        else:
            if not self.session_names:
                self.session_names = ['dummy_session']

            if self.dataset is None:
                self.dataset = 'dummy_dataset'

            for session in self.session_names:
                sm = SessionManager(
                    self.dataset, self.data_description, session, self.source_ctx, video_backend = self.video_backend
                )
                self.sessions[session] = {"manager": sm, "info": None}

    def load_session(self, session_name):
        self.sessions[session_name]["manager"].load(self.data_description)

    def save_session(self, session_name):
        self.sessions[session_name]["manager"].save(self.data_description)

    def load(self):
        for session in self.session_names:
            self.load_session(session)

    def save(self):
        for session in self.session_names:
            self.save_session(session)


# class NovaDatasetManager(DatasetManager):
#
#     def _init_sessions(self):
#         sh = nova_db_handler.SessionHandler(**self.source_ctx["db"])
#         sessions = sh.load(self.dataset, self.session_names)
#         for session_info in sessions:
#             sm = SessionManager(
#                 self.dataset, self.data_description, session_info.name, self.source_ctx
#             )
#             self.sessions[session_info.name] = {"manager": sm, "info": session_info}


if __name__ == "__main__":
    from dotenv import load_dotenv
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


    #dataset = "test"
    #sessions = ["01_AffWild2_video1"]

    annotation = {
        "src": "db:annotation",
        "scheme": SCHEME,
        "type": "input",
        "id": "annotation",
        "annotator": ANNOTATOR,
        "role": ROLE,
    }

    # stream = {
    #     "src": "db:stream",
    #     "type": "input",
    #     "id": "featurestream",
    #     "role": ROLE,
    #     "name": FEATURE_STREAM,
    # }

    # file = {
    #     "src": "file:stream:Audio",
    #     "type": "input",
    #     "id": "file",
    #     "uri": DISCOVER_TEST_FILE_DIR/"test_audio.wav",
    # }

    # request = {
    #     "src": "request:text:video:dum:dum:dum",
    #     "type": "input",
    #     "id": "reqeust_test",
    #     "data": "this is some input"
    # }

    ctx = {
        "db": {
            "db_host": IP,
            "db_port": PORT,
            "db_user": USER,
            "db_password": PASSWORD,
            "data_dir": DATA_DIR,
        },
    }

    annotation_out = {
        "src": "file:annotation",
        "type": "output",
        "id": "annotation_out",
        "uri": DISCOVER_OUR_DIR/"test_output.annotation",
    }

    dsm = DatasetManager(
        dataset=DATASET, session_names=SESSIONS, data_description=[annotation, annotation_out], source_context=ctx)

    # Loading session and set as output
    session_manager = dsm.sessions['01_AffWild2_video1']['manager']
    session_manager.load()
    session_manager.output_data_templates["annotation_out"] = session_manager.input_data["annotation"]

    dsm.save()

    breakpoint()
