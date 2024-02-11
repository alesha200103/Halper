from enum import StrEnum

from pydantic_settings import BaseSettings


class RecognizerType(StrEnum):
    GOOGLE = "google"


class STTSettings(BaseSettings):
    default_recognizer: RecognizerType = RecognizerType.GOOGLE
    recognize_language: str = "ru-RU"
    # google_preferred_phrases: str | None = None  # помогает google распознать фразу
