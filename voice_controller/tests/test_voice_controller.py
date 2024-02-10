from voice_controller.voice_controller import VoiceController
from speech_recognition import AudioData, WaitTimeoutError
import pytest


class TestVoiceController:
    def test_success_listen(self, voice_controller: VoiceController, audio_data: AudioData):
        voice_controller._recognizer.listen.return_value = audio_data
        assert voice_controller._listen() == audio_data
        voice_controller._recognizer.adjust_for_ambient_noise.assert_called_once()
        voice_controller._recognizer.listen.assert_called_once()

    def test_unsuccess_listen(self, voice_controller: VoiceController, audio_data: AudioData):
        voice_controller._recognizer.listen.side_effect = WaitTimeoutError()
        assert voice_controller._listen() is None
        voice_controller._recognizer.adjust_for_ambient_noise.assert_called_once()
        voice_controller._recognizer.listen.assert_called_once()

    def test_success_background_listen(self, voice_controller: VoiceController, audio_data: AudioData):
        voice_controller._recognizer.listen.return_value = audio_data
        assert voice_controller._background_listen() == audio_data
        voice_controller._recognizer.listen.assert_called_once()
