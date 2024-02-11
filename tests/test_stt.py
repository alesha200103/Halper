import pytest

from stt.stt import STT
from speech_recognition import AudioData, UnknownValueError, RequestError


class TestSTT:
    @pytest.mark.parametrize("user_text", ["kek lol"])
    def test_success_google_recognize(self, stt: STT, audio_data: AudioData, user_text: str):
        stt._recognizer.recognize_google.return_value = user_text
        assert stt._google_recognize(audio_data=audio_data) == user_text
        stt._recognizer.recognize_google.assert_called_once()

    @pytest.mark.parametrize("exception", [UnknownValueError(), RequestError()])
    def test_unsuccess_google_recognize(self, stt: STT, audio_data: AudioData, exception: Exception):
        stt._recognizer.recognize_google.side_effect = exception
        assert stt._google_recognize(audio_data=audio_data) is None
        stt._recognizer.recognize_google.assert_called_once()

    @pytest.mark.parametrize("user_text", ["kek lol"])
    def test_success_recognize(self, stt: STT, audio_data: AudioData, user_text: str):
        stt._recognizer.recognize_google.return_value = user_text
        assert stt.recognize(audio_data=audio_data) == user_text
        stt._recognizer.recognize_google.assert_called_once()

    @pytest.mark.parametrize("exception", [UnknownValueError(), RequestError()])
    def test_unsuccess_recognize(self, stt: STT, audio_data: AudioData, exception: Exception):
        stt._recognizer.recognize_google.side_effect = exception
        assert stt.recognize(audio_data=audio_data) is None
        stt._recognizer.recognize_google.assert_called_once()

    def test_recognize_with_wrong_recognizer(self, stt: STT, audio_data: AudioData):
        stt._settings.default_recognizer = "kek"
        assert stt.recognize(audio_data=audio_data) is None
        stt._recognizer.recognize_google.assert_not_called()
