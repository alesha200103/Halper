from pydantic_settings import BaseSettings


class VoiceControllerSettings:
    microphone_index: int = (
        2  # идекс используемого микрофона из speech_recognition.Microphone.list_working_microphones()
    )
    noise_duration: int = 2
    background_energy_threshold: int = 1000
    background_dynamic_energy_threshold: bool = False
    background_continue_speech_time: int = 5  # время больше которого реч не распознаётся на фоне
    background_phrase_time_limit: float | None = None
    background_recognizer_timeout: float | None = 3.5
    phrase_time_limit: float | None = None
    recognizer_timeout: float | None = 5

