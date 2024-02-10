import pytest
from voice_controller.voice_controller import VoiceController
from voice_controller.settings import VoiceControllerSettings
from unittest.mock import MagicMock
from speech_recognition import AudioData
from faker import Faker


@pytest.fixture()
def voice_controller() -> VoiceController:
    voice_controller = VoiceController(settings=VoiceControllerSettings())
    voice_controller._recognizer = MagicMock()
    voice_controller._microphone = MagicMock()
    return voice_controller


@pytest.fixture()
def audio_data() -> AudioData:
    fake = Faker()
    return AudioData(frame_data=fake.random.randbytes(100), sample_rate=44100, sample_width=2)
