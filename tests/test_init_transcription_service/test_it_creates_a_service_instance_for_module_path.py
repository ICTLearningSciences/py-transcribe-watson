from unittest.mock import patch
from transcribe import init_transcription_service, TranscriptionService
from .helpers import TEST_SERVICE_CONFIG


@patch("watson_developer_cloud.SpeechToTextV1")
def test_it_creates_a_service_instance_for_module_path(mock_watson):
    service = init_transcription_service(
        module_path="transcribe_watson", config=TEST_SERVICE_CONFIG
    )
    assert isinstance(service, TranscriptionService)
