from speech_recognition import AudioData, Recognizer, RequestError, UnknownValueError

from logging_helper import get_logging_helper
from stt.settings import RecognizerType, STTSettings

logger = get_logging_helper(__name__)


class STT:
    def __init__(self, recognizer: Recognizer, settings: STTSettings):
        self._recognizer = recognizer
        self._settings = settings

    def recognize(self, audio_data: AudioData) -> str | None:
        match self._settings.default_recognizer:
            case RecognizerType.GOOGLE:
                logger.info("Use Google recognizer")
                recognized_text = self._google_recognize(
                    audio_data=audio_data,
                )
                if recognized_text:
                    return recognized_text
                logger.warn("No rekognize text with google")
            case _:
                logger.error("Wrong recognizer type")

        logger.info(
            "Use default local recognizer (Not work now!)"
        )  # ToDo: add local recognizer
        return

    def _google_recognize(self, audio_data: AudioData) -> str | None:
        try:
            logger.info("Start recognition")
            recognized_data = self._recognizer.recognize_google(
                audio_data,
                language=self._settings.recognize_language,
            ).lower()
            logger.info("Finish recognition with phrase '%s'", recognized_data)
        except UnknownValueError:
            logger.error("Wrong data for recognize")
            return

        except RequestError:
            logger.error("Recognize request error")
            return

        return recognized_data
