"""Tests gather_metadata module"""

import json
import os
import unittest
import warnings
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import requests
from aind_data_schema.core.metadata import Metadata, MetadataStatus
from aind_data_schema.core.processing import DataProcess, PipelineProcess
from aind_data_schema_models.modalities import Modality
from aind_data_schema_models.organizations import Organization
from aind_data_schema_models.process_names import ProcessName
from pydantic import ValidationError
from requests import Response

from aind_metadata_mapper.bergamo.models import (
    JobSettings as BergamoSessionJobSettings,
)
from aind_metadata_mapper.bruker.models import (
    JobSettings as BrukerSessionJobSettings,
)
from aind_metadata_mapper.core_models import JobResponse
from aind_metadata_mapper.fip.models import (
    JobSettings as FipSessionJobSettings,
)
from aind_metadata_mapper.gather_metadata import GatherMetadataJob
from aind_metadata_mapper.mesoscope.models import (
    JobSettings as MesoscopeSessionJobSettings,
)
from aind_metadata_mapper.models import (
    AcquisitionSettings,
    InstrumentSettings,
    JobSettings,
    MetadataSettings,
    ProceduresSettings,
    ProcessingSettings,
    RawDataDescriptionSettings,
    RigSettings,
    SessionSettings,
    SubjectSettings,
)
from aind_metadata_mapper.smartspim.acquisition import (
    JobSettings as SmartSpimAcquisitionJobSettings,
)

RESOURCES_DIR = (
    Path(os.path.dirname(os.path.realpath(__file__)))
    / "resources"
    / "gather_metadata_job"
)
METADATA_DIR = RESOURCES_DIR / "metadata_files"
METADATA_DIR_WITH_RIG_ISSUE = RESOURCES_DIR / "schema_files_with_issues"
EXAMPLE_BERGAMO_CONFIGS = RESOURCES_DIR / "test_bergamo_configs.json"


class TestGatherMetadataJob(unittest.TestCase):
    """Tests methods in GatherMetadataJob class"""

    @classmethod
    def setUpClass(cls):
        """Load json files."""
        with open(RESOURCES_DIR / "example_subject_response.json", "r") as f:
            example_subject_response = json.load(f)
        with open(
            RESOURCES_DIR / "example_procedures_response.json", "r"
        ) as f:
            example_procedures_response = json.load(f)
        with open(RESOURCES_DIR / "example_funding_response.json", "r") as f:
            example_funding_response = json.load(f)
        with open(
            RESOURCES_DIR / "example_funding_multiple_response.json", "r"
        ) as f:
            example_funding_multi_response = json.load(f)
        with open(RESOURCES_DIR / "example_rig_response.json", "r") as f:
            example_rig_response = json.load(f)
        with open(
            RESOURCES_DIR / "example_instrument_response.json", "r"
        ) as f:
            example_instrument_response = json.load(f)
        cls.example_subject_response = example_subject_response
        cls.example_procedures_response = example_procedures_response
        cls.example_funding_response = example_funding_response
        cls.example_funding_multi_response = example_funding_multi_response
        cls.example_rig_response = example_rig_response
        cls.example_instrument_response = example_instrument_response

    def test_class_constructor(self):
        """Tests class is constructed properly"""
        job_settings = JobSettings(directory_to_write_to=RESOURCES_DIR)
        metadata_job = GatherMetadataJob(settings=job_settings)
        self.assertIsNotNone(metadata_job)

    @patch("pathlib.Path.is_file")
    def test_does_file_exist_in_user_defined_dir_path_true(
        self, mock_is_file: MagicMock
    ):
        """Tests _does_file_exist_in_user_defined_dir method returns true
        when path exists"""

        mock_is_file.return_value = True
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR, metadata_dir="some_path"
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        self.assertTrue(
            metadata_job._does_file_exist_in_user_defined_dir("subject.json")
        )

    @patch("pathlib.Path.is_file")
    def test_does_file_exist_in_user_defined_dir_path_false(
        self, mock_is_file: MagicMock
    ):
        """Tests _does_file_exist_in_user_defined_dir method when path does
        not exist"""

        mock_is_file.return_value = False
        job_settings1 = JobSettings(directory_to_write_to=RESOURCES_DIR)
        metadata_job = GatherMetadataJob(settings=job_settings1)
        job_settings2 = JobSettings(
            directory_to_write_to=RESOURCES_DIR, metadata_dir="some_path"
        )
        metadata_job2 = GatherMetadataJob(settings=job_settings2)
        self.assertFalse(
            metadata_job._does_file_exist_in_user_defined_dir("subject.json")
        )
        self.assertFalse(
            metadata_job2._does_file_exist_in_user_defined_dir("subject.json")
        )

    def test_get_file_from_user_defined_directory(self):
        """Tests json contents are pulled correctly"""
        metadata_dir = RESOURCES_DIR / "metadata_files"
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR, metadata_dir=metadata_dir
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job._get_file_from_user_defined_directory(
            "subject.json"
        )
        self.assertIsNotNone(contents)

    @patch("requests.Session.get")
    def test_get_subject(self, mock_get: MagicMock):
        """Tests get_subject method when use service is true"""
        mock_response = Response()
        mock_response.status_code = 200
        body = json.dumps(self.example_subject_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response
        service_session = requests.Session()

        job_settings = JobSettings(
            metadata_service_domain="http://example.com",
            directory_to_write_to=RESOURCES_DIR,
            subject_settings=SubjectSettings(
                subject_id="632269",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_subject(service_session)
        self.assertEqual("632269", contents["subject_id"])
        mock_get.assert_called_once_with("http://example.com/subject/632269")

    @patch("requests.Session.get")
    def test_get_subject_from_dir(self, mock_get: MagicMock):
        """Tests get_subject method when use service is false"""
        mock_response = Response()
        mock_response.status_code = 200
        body = json.dumps(self.example_subject_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        metadata_dir = RESOURCES_DIR / "metadata_files"
        job_settings = JobSettings(
            metadata_service_domain="http://example.com",
            directory_to_write_to=RESOURCES_DIR,
            subject_settings=SubjectSettings(
                subject_id="632269",
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_subject(service_session)
        self.assertEqual("632269", contents["subject_id"])
        mock_get.assert_not_called()

    @patch("requests.Session.get")
    def test_get_subject_error(self, mock_get: MagicMock):
        """Tests get_subject when an error is raised"""
        mock_response = Response()
        mock_response.status_code = 500
        body = json.dumps({"message": "Internal Server Error"})
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            subject_settings=SubjectSettings(
                subject_id="632269",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        with self.assertRaises(AssertionError) as e:
            metadata_job.get_subject(service_session)
        expected_error_message = (
            "Subject metadata is not valid! "
            "{'message': 'Internal Server Error'}"
        )
        self.assertTrue(expected_error_message in str(e.exception))

    @patch("requests.Session.get")
    def test_get_procedures(self, mock_get: MagicMock):
        """Tests get_procedures method"""
        mock_response = Response()
        mock_response.status_code = 406
        body = json.dumps(self.example_procedures_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            procedures_settings=ProceduresSettings(
                subject_id="632269",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_procedures(service_session)
        self.assertEqual("632269", contents["subject_id"])
        mock_get.assert_called_once_with(
            "http://example.com/procedures/632269"
        )

    @patch("requests.Session.get")
    def test_get_procedures_from_dir(self, mock_get: MagicMock):
        """Tests get_procedures method from dir"""
        mock_response = Response()
        mock_response.status_code = 406
        body = json.dumps(self.example_procedures_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response
        metadata_dir = RESOURCES_DIR / "metadata_files"
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            procedures_settings=ProceduresSettings(
                subject_id="632269",
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_procedures(service_session)
        self.assertEqual("632269", contents["subject_id"])
        mock_get.assert_not_called()

    @patch("requests.Session.get")
    def test_get_procedures_error(self, mock_get: MagicMock):
        """Tests get_procedures when an error is raised"""
        mock_response = Response()
        mock_response.status_code = 500
        body = json.dumps({"message": "Internal Server Error"})
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            procedures_settings=ProceduresSettings(
                subject_id="632269",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        with self.assertRaises(AssertionError) as e:
            metadata_job.get_procedures(service_session)
        expected_error_message = (
            "Procedures metadata is not valid! "
            "{'message': 'Internal Server Error'}"
        )
        self.assertTrue(expected_error_message in str(e.exception))

    @patch("requests.Session.get")
    def test_get_raw_data_description(self, mock_get: MagicMock):
        """Tests get_raw_data_description method with valid model"""

        mock_response = Response()
        mock_response.status_code = 200
        body = json.dumps(self.example_funding_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            raw_data_description_settings=RawDataDescriptionSettings(
                project_name="Ephys Platform",
                name="ecephys_632269_2023-10-10_10-10-10",
                modality=[Modality.ECEPHYS, Modality.BEHAVIOR_VIDEOS],
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_raw_data_description(service_session)
        expected_investigators = ["Anna Apple"]
        actual_investigators = [i["name"] for i in contents["investigators"]]
        self.assertEqual(expected_investigators, actual_investigators)
        self.assertEqual("ecephys", contents["platform"]["abbreviation"])
        self.assertEqual("632269", contents["subject_id"])
        self.assertEqual(
            "ecephys_632269_2023-10-10_10-10-10", contents["name"]
        )
        mock_get.assert_called_once_with(
            "http://example.com/funding/Ephys Platform"
        )

    @patch("requests.Session.get")
    def test_get_raw_data_description_from_dir(self, mock_get: MagicMock):
        """Tests get_raw_data_description method from dir"""

        mock_response = Response()
        mock_response.status_code = 200
        body = json.dumps(self.example_funding_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            raw_data_description_settings=RawDataDescriptionSettings(
                project_name="Ephys Platform",
                name="ecephys_632269_2023-10-10_10-10-10",
                modality=[Modality.ECEPHYS, Modality.BEHAVIOR_VIDEOS],
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_raw_data_description(service_session)
        expected_investigators = ["Anna Apple", "John Smith"]
        actual_investigators = [i["name"] for i in contents["investigators"]]
        self.assertEqual(expected_investigators, actual_investigators)
        self.assertEqual("ecephys", contents["platform"]["abbreviation"])
        self.assertEqual("632269", contents["subject_id"])
        self.assertEqual(
            "ecephys_632269_2023-10-10_10-10-10", contents["name"]
        )
        mock_get.assert_not_called()

    @patch("requests.Session.get")
    def test_get_raw_data_description_multi_response(
        self, mock_get: MagicMock
    ):
        """Tests get_raw_data_description method with valid model and multiple
        items in funding response"""

        mock_response = Response()
        mock_response.status_code = 300
        body = json.dumps(self.example_funding_multi_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            raw_data_description_settings=RawDataDescriptionSettings(
                project_name="Ephys Platform",
                name="ecephys_632269_2023-10-10_10-10-10",
                modality=[Modality.ECEPHYS, Modality.BEHAVIOR_VIDEOS],
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_raw_data_description(service_session)
        expected_investigators = ["Anna Apple"]
        actual_investigators = [i["name"] for i in contents["investigators"]]
        self.assertEqual(2, len(contents["funding_source"]))
        self.assertEqual(expected_investigators, actual_investigators)
        self.assertEqual("ecephys", contents["platform"]["abbreviation"])
        self.assertEqual("632269", contents["subject_id"])
        self.assertEqual(
            "ecephys_632269_2023-10-10_10-10-10", contents["name"]
        )
        mock_get.assert_called_once_with(
            "http://example.com/funding/Ephys Platform"
        )

    @patch("requests.Session.get")
    def test_get_raw_data_description_invalid(self, mock_get: MagicMock):
        """Tests get_raw_data_description method with invalid model"""
        mock_response = Response()
        mock_response.status_code = 500
        body = json.dumps({"message": "Internal Server Error"})
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            raw_data_description_settings=RawDataDescriptionSettings(
                project_name="foo",
                name="ecephys_632269_2023-10-10_10-10-10",
                modality=[Modality.ECEPHYS, Modality.BEHAVIOR_VIDEOS],
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_raw_data_description(service_session)
        self.assertEqual("ecephys", contents["platform"]["abbreviation"])
        self.assertEqual("632269", contents["subject_id"])
        self.assertEqual(
            "ecephys_632269_2023-10-10_10-10-10", contents["name"]
        )
        self.assertEqual([], contents["investigators"])

    def test_get_processing_metadata(self):
        """Tests get_processing_metadata method"""
        data_process = DataProcess(
            name=ProcessName.COMPRESSION,
            software_version="0.0.15",
            start_date_time=datetime(
                2020, 10, 10, 10, 10, 10, tzinfo=timezone.utc
            ),
            end_date_time=datetime(
                2020, 10, 10, 11, 10, 10, tzinfo=timezone.utc
            ),
            input_location="/source/open_ephys",
            output_location="/tmp/stage",
            code_url=(
                "https://github.com/AllenNeuralDynamics/"
                "aind-data-transformation"
            ),
            parameters={},
            outputs={},
        )
        processing_pipeline = PipelineProcess(
            data_processes=[data_process], processor_full_name="Anna Apple"
        )

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            processing_settings=ProcessingSettings(
                pipeline_process=json.loads(
                    processing_pipeline.model_dump_json()
                )
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_processing_metadata()
        self.assertEqual(
            "Compression",
            contents["processing_pipeline"]["data_processes"][0]["name"],
        )

    def test_get_processing_metadata_from_dir(self):
        """Tests get_processing_metadata method from dir"""
        data_process = DataProcess(
            name=ProcessName.COMPRESSION,
            software_version="0.0.15",
            start_date_time=datetime(
                2020, 10, 10, 10, 10, 10, tzinfo=timezone.utc
            ),
            end_date_time=datetime(
                2020, 10, 10, 11, 10, 10, tzinfo=timezone.utc
            ),
            input_location="/source/open_ephys",
            output_location="/tmp/stage",
            code_url=(
                "https://github.com/AllenNeuralDynamics/"
                "aind-data-transformation"
            ),
            parameters={},
            outputs={},
        )
        processing_pipeline = PipelineProcess(
            data_processes=[data_process], processor_full_name="Anna Apple"
        )

        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            processing_settings=ProcessingSettings(
                pipeline_process=json.loads(
                    processing_pipeline.model_dump_json()
                )
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_processing_metadata()
        self.assertEqual(
            "Compression",
            contents["processing_pipeline"]["data_processes"][0]["name"],
        )

    def test_get_processing_metadata_invalid(self):
        """Tests get_processing_metadata method with validation errors"""
        data_process = DataProcess.model_construct()
        processing_pipeline = PipelineProcess.model_construct(
            data_processes=[data_process]
        )

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            processing_settings=ProcessingSettings(
                pipeline_process=json.loads(
                    processing_pipeline.model_dump_json()
                )
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            contents = metadata_job.get_processing_metadata()
        self.assertIsNotNone(contents)
        self.assertEqual(1, len(w))

    def test_get_session_metadata(self):
        """Tests get_session_metadata"""
        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertIsNotNone(contents)

    @patch("aind_metadata_mapper.bergamo.session.BergamoEtl.run_job")
    def test_get_session_metadata_bergamo_success(
        self, mock_run_job: MagicMock
    ):
        """Tests get_session_metadata bergamo"""
        mock_run_job.return_value = JobResponse(
            status_code=200, data=json.dumps({"some_key": "some_value"})
        )
        bergamo_session_settings = BergamoSessionJobSettings.model_construct()
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings(
                job_settings=bergamo_session_settings
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertEqual({"some_key": "some_value"}, contents)
        mock_run_job.assert_called_once()

    @patch("aind_metadata_mapper.bruker.session.MRIEtl.run_job")
    def test_get_session_metadata_bruker_success(
        self, mock_run_job: MagicMock
    ):
        """Tests get_session_metadata bruker creates MRIEtl"""
        mock_run_job.return_value = JobResponse(
            status_code=200, data=json.dumps({"some_key": "some_value"})
        )
        bruker_session_settings = BrukerSessionJobSettings.model_construct()
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings(
                job_settings=bruker_session_settings,
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertEqual({"some_key": "some_value"}, contents)
        mock_run_job.assert_called_once()

    @patch("aind_metadata_mapper.fip.session.FIBEtl.run_job")
    def test_get_session_metadata_fip_success(self, mock_run_job: MagicMock):
        """Tests ETL"""
        mock_run_job.return_value = JobResponse(
            status_code=200, data=json.dumps({"some_key": "some_value"})
        )
        fip_session_settings = FipSessionJobSettings.model_construct()
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings(
                job_settings=fip_session_settings,
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertEqual({"some_key": "some_value"}, contents)
        mock_run_job.assert_called_once()

    @patch("aind_metadata_mapper.mesoscope.session.MesoscopeEtl.run_job")
    @patch("aind_metadata_mapper.stimulus.camstim.Camstim.__init__")
    def test_get_session_metadata_mesoscope_success(
        self, mock_camstim: MagicMock, mock_run_job: MagicMock
    ):
        """Tests get_session_metadata bruker creates MRIEtl"""
        mock_camstim.return_value = None
        mock_run_job.return_value = JobResponse(
            status_code=200, data=json.dumps({"some_key": "some_value"})
        )
        mesoscope_session_settings = (
            MesoscopeSessionJobSettings.model_construct(
                behavior_source="abc",
                input_source="some/path",
                session_id="123",
                output_directory="some/output",
                session_start_time=datetime.now(),
                session_end_time=datetime.now(),
                subject_id="123",
                project="some_project",
                experimenter_full_name=["John Doe"],
            )
        )
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings(
                job_settings=mesoscope_session_settings,
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertEqual({"some_key": "some_value"}, contents)
        mock_run_job.assert_called_once()

    def test_session_settings_error(self):
        """Tests SessionSettings raises error if JobSettings is not expected"""
        session_settings = SmartSpimAcquisitionJobSettings.model_construct()
        with self.assertRaises(ValidationError):
            JobSettings(
                directory_to_write_to=RESOURCES_DIR,
                session_settings=SessionSettings(
                    job_settings=session_settings,
                ),
            )

    @patch("aind_metadata_mapper.bergamo.session.BergamoEtl.run_job")
    def test_get_session_metadata_error(self, mock_run_job: MagicMock):
        """Tests get_session_metadata returns None when requesting
        Bergamo metadata and a 500 response is returned."""
        mock_run_job.return_value = JobResponse(status_code=500, data=None)
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings(
                job_settings=BergamoSessionJobSettings.model_construct()
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertIsNone(contents)

    def test_get_session_metadata_error_unknown_session(self):
        """Tests get_session_metadata raises and error"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            session_settings=SessionSettings.model_construct(
                job_settings={"job_settings_name": "def"}
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        with self.assertRaises(ValueError):
            metadata_job.get_session_metadata()

    def test_get_session_metadata_none(self):
        """Tests get_session_metadata returns none"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_session_metadata()
        self.assertIsNone(contents)

    @patch("requests.Session.get")
    def test_get_rig_metadata(self, mock_get: MagicMock):
        """Tests get_rig_metadata from metadata service path"""
        mock_response = Response()
        mock_response.status_code = 422
        body = json.dumps(self.example_rig_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            rig_settings=RigSettings(
                rig_id="323_EPHYS1",
                metadata_service_path="rig",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_rig_metadata(service_session)
        self.assertEqual("323_EPHYS1", contents["rig_id"])
        mock_get.assert_called_once_with("http://example.com/rig/323_EPHYS1")

    @patch("requests.Session")
    def test_get_rig_metadata_from_dir(self, mock_session: MagicMock):
        """Tests get_rig_metadata from directory"""
        metadata_dir = RESOURCES_DIR / "metadata_files"
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            rig_settings=RigSettings(
                rig_id="323_EPHYS1",
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_rig_metadata(mock_session)
        self.assertIsNotNone(contents)
        mock_session.assert_not_called()

    @patch("requests.Session")
    def test_get_rig_metadata_none(self, mock_session: MagicMock):
        """Tests get_rig_metadata when no file or settings are provided."""
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_rig_metadata(mock_session)
        self.assertIsNone(contents)
        mock_session.assert_not_called()

    @patch("requests.Session.get")
    @patch("logging.warning")
    def test_get_rig_metadata_warning(
        self, mock_warn: MagicMock, mock_get: MagicMock
    ):
        """Tests get_rig_metadata when an error is raised"""
        mock_response = Response()
        mock_response.status_code = 500
        body = json.dumps({"message": "Internal Server Error"})
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            rig_settings=RigSettings(
                rig_id="323_EPHYS1",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        output = metadata_job.get_rig_metadata(service_session)
        self.assertIsNone(output)
        mock_warn.assert_called_once_with("Rig metadata is not valid! 500")

    def test_get_quality_control_metadata(self):
        """Tests get_quality_control_metadata"""
        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_quality_control_metadata()
        self.assertIsNotNone(contents)

    def test_get_quality_control_metadata_none(self):
        """Tests get_quality_control_metadata returns none"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_quality_control_metadata()
        self.assertIsNone(contents)

    @patch("requests.Session")
    def test_get_problematic_rig_metadata(self, mock_session: MagicMock):
        """Tests get_rig_metadata when there is a pydantic serialization
        issue."""
        metadata_dir = METADATA_DIR_WITH_RIG_ISSUE

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_rig_metadata(mock_session)
        self.assertIsNotNone(contents)
        mock_session.assert_not_called()

    def test_get_acquisition_metadata(self):
        """Tests get_acquisition_metadata"""
        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_acquisition_metadata()
        self.assertIsNotNone(contents)

    def test_get_acquisition_metadata_none(self):
        """Tests get_acquisition_metadata returns none"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_acquisition_metadata()
        self.assertIsNone(contents)

    @patch("aind_metadata_mapper.smartspim.acquisition.SmartspimETL.run_job")
    def test_get_acquisition_metadata_smartspim_success(
        self, mock_run_job: MagicMock
    ):
        """Tests get_acquisition_metadata returns something when requesting
        SmartSPIM metadata"""

        mock_run_job.return_value = JobResponse(
            status_code=200, data=json.dumps({"some_key": "some_value"})
        )

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            acquisition_settings=AcquisitionSettings(
                job_settings=SmartSpimAcquisitionJobSettings(
                    subject_id="695464",
                    input_source=Path("SmartSPIM_695464_2023-10-18_20-30-30"),
                    metadata_service_path="http://example.com/test",
                )
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_acquisition_metadata()
        self.assertEqual({"some_key": "some_value"}, contents)

    @patch("aind_metadata_mapper.smartspim.acquisition.SmartspimETL.run_job")
    def test_get_acquisition_metadata_smartspim_error(
        self, mock_run_job: MagicMock
    ):
        """Tests get_acquisition_metadata returns None when requesting
        SmartSPIM metadata and a 500 response is returned."""

        mock_run_job.return_value = JobResponse(status_code=500, data=None)

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            acquisition_settings=AcquisitionSettings(
                job_settings=SmartSpimAcquisitionJobSettings(
                    subject_id="695464",
                    input_source=Path("SmartSPIM_695464_2023-10-18_20-30-30"),
                    metadata_service_path="http://example.com/test",
                )
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_acquisition_metadata()
        self.assertIsNone(contents)

    @patch("requests.Session.get")
    def test_get_instrument_metadata(self, mock_get: MagicMock):
        """Tests get_instrument_metadata from metadata service path"""
        mock_response = Response()
        mock_response.status_code = 422
        body = json.dumps(self.example_instrument_response)
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            instrument_settings=InstrumentSettings(
                instrument_id="exaSPIM1-1",
                metadata_service_path="instrument",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        contents = metadata_job.get_instrument_metadata(service_session)
        self.assertEqual("exaSPIM1-1", contents["instrument_id"])
        mock_get.assert_called_once_with(
            "http://example.com/instrument/exaSPIM1-1"
        )

    @patch("requests.Session")
    def test_get_instrument_metadata_from_dir(self, mock_session: MagicMock):
        """Tests get_instrument_metadata from directory"""
        metadata_dir = RESOURCES_DIR / "metadata_files"
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            instrument_settings=InstrumentSettings(
                instrument_id="exaSPIM1-1",
                metadata_service_path="instrument",
            ),
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_instrument_metadata(mock_session)
        self.assertIsNotNone(contents)
        mock_session.assert_not_called()

    @patch("requests.Session")
    def test_get_instrument_metadata_none(self, mock_session: MagicMock):
        """Tests get_instrument_metadata when no file or settings."""
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        contents = metadata_job.get_instrument_metadata(mock_session)
        self.assertIsNone(contents)
        mock_session.assert_not_called()

    @patch("requests.Session.get")
    @patch("logging.warning")
    def test_get_instrument_metadata_warning(
        self, mock_warn: MagicMock, mock_get: MagicMock
    ):
        """Tests get_instrument_metadata when an error is raised"""
        mock_response = Response()
        mock_response.status_code = 500
        body = json.dumps({"message": "Internal Server Error"})
        mock_response._content = body.encode("utf-8")
        mock_get.return_value = mock_response

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            instrument_settings=InstrumentSettings(
                instrument_id="exaSPIM1-1",
                metadata_service_path="instrument",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        service_session = requests.Session()
        output = metadata_job.get_instrument_metadata(service_session)
        self.assertIsNone(output)
        mock_warn.assert_called_once_with(
            "Instrument metadata is not valid! 500"
        )

    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob."
        "_write_json_file"
    )
    def test_gather_non_automated_metadata(self, mock_write_file: MagicMock):
        """Tests _gather_non_automated_metadata method"""
        metadata_dir = RESOURCES_DIR / "metadata_files"

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_dir=metadata_dir,
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        metadata_job._gather_non_automated_metadata()
        mock_write_file.assert_called()

    def test_get_location(self):
        """Tests _get_location method with no location_map"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="asset_name", location="some_bucket"
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        location = metadata_job._get_location(
            metadata_status=MetadataStatus.VALID
        )
        self.assertEqual("some_bucket", location)

    def test_get_location_with_location_map(self):
        """Tests _get_location method with location_map"""

        job_settings = JobSettings(
            directory_to_write_to="abc",
            metadata_settings=MetadataSettings(
                name="asset_name",
                location_map={
                    "Valid": "valid_bucket",
                    "Invalid": "invalid_bucket",
                },
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        valid_location = metadata_job._get_location(
            metadata_status=MetadataStatus.VALID
        )
        invalid_location = metadata_job._get_location(
            metadata_status=MetadataStatus.INVALID
        )
        missing_location = metadata_job._get_location(
            metadata_status=MetadataStatus.MISSING
        )
        self.assertEqual("valid_bucket", valid_location)
        self.assertEqual("invalid_bucket", invalid_location)
        # Check default falls back to the invalid value
        self.assertEqual("invalid_bucket", missing_location)

    def test_get_location_with_location_map_error(self):
        """Tests _get_location method when location_map is corrupt"""

        job_settings = JobSettings(
            directory_to_write_to="abc",
            metadata_settings=MetadataSettings(
                name="asset_name", location_map={"Valid": "valid_bucket"}
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        with self.assertRaises(ValueError) as e:
            metadata_job._get_location(metadata_status=MetadataStatus.INVALID)
        self.assertIn("Unable to set location", str(e.exception))

    @patch("logging.warning")
    def test_get_main_metadata_with_warnings(self, mock_warn: MagicMock):
        """Tests get_main_metadata method raises validation warnings"""
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location="s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
                subject_filepath=(METADATA_DIR / "subject.json"),
                data_description_filepath=(
                    METADATA_DIR / "data_description.json"
                ),
                procedures_filepath=(METADATA_DIR / "procedures.json"),
                session_filepath=None,
                rig_filepath=None,
                processing_filepath=(METADATA_DIR / "processing.json"),
                acquisition_filepath=None,
                instrument_filepath=None,
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        with self.assertWarns(UserWarning) as w:
            main_metadata = metadata_job.get_main_metadata()
        # Issues with incomplete Procedures model raises warnings
        self.assertIsNotNone(w.warning)
        self.assertEqual(
            "s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
            main_metadata["location"],
        )
        self.assertEqual("Missing", main_metadata["metadata_status"])
        self.assertEqual("632269", main_metadata["subject"]["subject_id"])
        mock_warn.assert_called_once()

    @patch("logging.warning")
    def test_get_main_metadata_with_ser_issues(self, mock_log: MagicMock):
        """Tests get_main_metadata method when rig.json file has
        serialization issues."""
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location="s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
                subject_filepath=(METADATA_DIR / "subject.json"),
                data_description_filepath=(
                    METADATA_DIR / "data_description.json"
                ),
                procedures_filepath=(METADATA_DIR / "procedures.json"),
                session_filepath=None,
                rig_filepath=(METADATA_DIR_WITH_RIG_ISSUE / "rig.json"),
                processing_filepath=(METADATA_DIR / "processing.json"),
                acquisition_filepath=None,
                instrument_filepath=None,
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        main_metadata = metadata_job.get_main_metadata()
        mock_log.assert_called_once()
        self.assertIsNotNone(main_metadata["rig"]["schema_version"])

    @patch("logging.warning")
    def test_get_main_metadata_with_validation_errors(
        self, mock_warn: MagicMock
    ):
        """Tests get_main_metadata method handles validation errors"""
        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location="s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
                subject_filepath=(METADATA_DIR / "subject.json"),
                data_description_filepath=(
                    METADATA_DIR / "data_description.json"
                ),
                procedures_filepath=(METADATA_DIR / "procedures.json"),
                session_filepath=(METADATA_DIR / "session.json"),
                rig_filepath=(METADATA_DIR / "rig.json"),
                processing_filepath=(METADATA_DIR / "processing.json"),
                acquisition_filepath=(METADATA_DIR / "acquisition.json"),
                instrument_filepath=(METADATA_DIR / "instrument.json"),
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        main_metadata = metadata_job.get_main_metadata()
        self.assertIsNotNone(main_metadata["subject"])
        self.assertIsNotNone(main_metadata["procedures"])
        self.assertIsNotNone(main_metadata["data_description"])
        self.assertIsNotNone(main_metadata["session"])
        self.assertIsNotNone(main_metadata["rig"])
        self.assertIsNotNone(main_metadata["processing"])
        self.assertIsNotNone(main_metadata["acquisition"])
        self.assertIsNotNone(main_metadata["instrument"])
        mock_warn.assert_called_once()

    @patch("builtins.open", new_callable=mock_open())
    @patch("json.dump")
    def test_write_json_file(
        self, mock_json_dump: MagicMock, mock_file: MagicMock
    ):
        """Tests write_json_file method"""
        mock_file.return_value.__enter__.return_value = (
            RESOURCES_DIR / "subject.json"
        )

        job_settings = JobSettings(directory_to_write_to=RESOURCES_DIR)
        metadata_job = GatherMetadataJob(settings=job_settings)
        metadata_job._write_json_file(
            filename="subject.json", contents={"subject_id": "123456"}
        )

        mock_json_dump.assert_called_once_with(
            {"subject_id": "123456"}, RESOURCES_DIR / "subject.json", indent=3
        )

    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob.get_subject"
    )
    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob.get_procedures"
    )
    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob"
        ".get_raw_data_description"
    )
    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob"
        ".get_processing_metadata"
    )
    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob"
        ".get_main_metadata"
    )
    @patch(
        "aind_metadata_mapper.gather_metadata.GatherMetadataJob"
        "._write_json_file"
    )
    @patch("builtins.open", new_callable=mock_open())
    @patch("json.dump")
    def test_run_job(
        self,
        mock_json_dump: MagicMock,
        mock_open_file: MagicMock,
        mock_write_json_file: MagicMock,
        mock_get_main_metadata: MagicMock,
        mock_get_processing_metadata: MagicMock,
        mock_get_raw_data_description: MagicMock,
        mock_get_procedures: MagicMock,
        mock_get_subject: MagicMock,
    ):
        """Tests run_job calls all the sub processes"""
        data_process = DataProcess(
            name=ProcessName.COMPRESSION,
            software_version="0.0.15",
            start_date_time=datetime(
                2020, 10, 10, 10, 10, 10, tzinfo=timezone.utc
            ),
            end_date_time=datetime(
                2020, 10, 10, 11, 10, 10, tzinfo=timezone.utc
            ),
            input_location="/source/open_ephys",
            output_location="/tmp/stage",
            code_url=(
                "https://github.com/AllenNeuralDynamics/"
                "aind-data-transformation"
            ),
            parameters={},
            outputs={},
        )
        processing_pipeline = PipelineProcess(
            data_processes=[data_process], processor_full_name="Anna Apple"
        )

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_service_domain="http://example.com",
            subject_settings=SubjectSettings(
                subject_id="632269",
            ),
            procedures_settings=ProceduresSettings(
                subject_id="632269",
            ),
            raw_data_description_settings=RawDataDescriptionSettings(
                project_name="Ephys Platform",
                name="ecephys_632269_2023-10-10_10-10-10",
                modality=[Modality.ECEPHYS, Modality.BEHAVIOR_VIDEOS],
            ),
            processing_settings=ProcessingSettings(
                pipeline_process=json.loads(
                    processing_pipeline.model_dump_json()
                )
            ),
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location="s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
                subject_filepath=(METADATA_DIR / "subject.json"),
                data_description_filepath=(
                    METADATA_DIR / "data_description.json"
                ),
                procedures_filepath=(METADATA_DIR / "procedures.json"),
                session_filepath=None,
                rig_filepath=None,
                processing_filepath=(METADATA_DIR / "processing.json"),
                acquisition_filepath=None,
                instrument_filepath=None,
            ),
        )

        # TODO: Add better mocked response
        mock_get_main_metadata.return_value = Metadata.model_construct()

        metadata_job = GatherMetadataJob(settings=job_settings)

        metadata_job.run_job()

        mock_get_subject.assert_called_once()
        mock_get_procedures.assert_called_once()
        mock_get_raw_data_description.assert_called_once()
        mock_get_processing_metadata.assert_called_once()
        mock_get_main_metadata.assert_called_once()
        mock_write_json_file.assert_called()
        mock_open_file.assert_called()
        mock_json_dump.assert_called()

    @patch("builtins.open", new_callable=mock_open())
    @patch("json.dump")
    def test_run_job_main_metadata(
        self, mock_json_dump: MagicMock, mock_write_file: MagicMock
    ):
        """Tests run job writes metadata json correctly"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location="s3://some-bucket/ecephys_632269_2023-10-10_10-10-10",
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        metadata_job.run_job()
        json_contents = mock_json_dump.mock_calls[0].args[0]
        mock_write_file.assert_called()
        self.assertIsNotNone(json_contents.get("_id"))
        self.assertIsNone(json_contents.get("id"))

    @patch("builtins.open", new_callable=mock_open())
    @patch("json.dump")
    def test_run_job_main_metadata_with_location_map(
        self, mock_json_dump: MagicMock, mock_write_file: MagicMock
    ):
        """Tests run job writes metadata json correctly when location_map is
        set"""

        job_settings = JobSettings(
            directory_to_write_to=RESOURCES_DIR,
            metadata_settings=MetadataSettings(
                name="ecephys_632269_2023-10-10_10-10-10",
                location_map={
                    "Valid": (
                        "s3://some-open-bucket/"
                        "ecephys_632269_2023-10-10_10-10-10"
                    ),
                    "Invalid": (
                        "s3://some-private-bucket/"
                        "ecephys_632269_2023-10-10_10-10-10"
                    ),
                },
            ),
        )
        metadata_job = GatherMetadataJob(settings=job_settings)
        metadata_job.run_job()
        json_contents = mock_json_dump.mock_calls[0].args[0]
        mock_write_file.assert_called()
        self.assertEqual(
            "s3://some-private-bucket/ecephys_632269_2023-10-10_10-10-10",
            json_contents.get("location"),
        )
        self.assertIsNotNone(json_contents.get("_id"))
        self.assertIsNone(json_contents.get("id"))

    def test_from_job_settings_file(self):
        """Tests that users can set a session config file when requesting
        GatherMetadataJob"""

        bergamo_settings = BergamoSessionJobSettings(
            user_settings_config_file=EXAMPLE_BERGAMO_CONFIGS
        )
        test_configs = {
            "directory_to_write_to": RESOURCES_DIR,
            "session_settings": {
                "job_settings": bergamo_settings.model_dump(),
            },
        }
        job_settings = JobSettings.model_validate_json(
            json.dumps(test_configs, default=str)
        )
        self.assertEqual(
            ["John Apple"],
            job_settings.session_settings.job_settings.experimenter_full_name,
        )

    @patch("requests.Session")
    def test_project_name_is_set(self, mock_session: MagicMock):
        """Tests project_name makes it to the data_description file"""

        settings = JobSettings(
            job_settings_name="GatherMetadata",
            metadata_service_domain="http://example.com",
            raw_data_description_settings=RawDataDescriptionSettings(
                name="behavior_123456_2024-10-01_09-00-23",
                project_name="Cognitive flexibility in patch foraging",
                modality=[Modality.BEHAVIOR, Modality.BEHAVIOR_VIDEOS],
                institution=Organization.AIND,
                metadata_service_path="funding",
            ),
            directory_to_write_to="/some/dir/data_dir",
        )

        job = GatherMetadataJob(settings=settings)
        data_description_contents = job.get_raw_data_description(mock_session)
        self.assertEqual(
            "Cognitive flexibility in patch foraging",
            data_description_contents["project_name"],
        )
        mock_session.assert_not_called()


if __name__ == "__main__":
    unittest.main()
