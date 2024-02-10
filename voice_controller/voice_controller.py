from time import time

import speech_recognition  # распознавание пользовательской речи
from voice_controller.settings import VoiceControllerSettings
from speech_recognition import AudioData, WaitTimeoutError
from logging_helper import get_logging_helper


logger = get_logging_helper(__name__)


class VoiceController:
    def __init__(self, settings: VoiceControllerSettings):
        self._settings = settings
        self._recognizer = speech_recognition.Recognizer()
        self._microphone = speech_recognition.Microphone(
            device_index=self._settings.microphone_index
        )

    def _listen(self) -> AudioData | None:
        """
        Запись и распознавание аудио.
        """
        with self._microphone:
            # регулирование уровня окружающего шума
            self._recognizer.adjust_for_ambient_noise(
                self._microphone, duration=self._settings.noise_duration
            )

            try:
                logger.info("Start listening")
                audio = self._recognizer.listen(
                    self._microphone,
                    timeout=self._settings.recognizer_timeout,
                    phrase_time_limit=self._settings.phrase_time_limit,
                )
                logger.info("Stop listening")
            except WaitTimeoutError:
                logger.error("Wait listen timeout")
                return

            return audio

    def _background_listen(self) -> AudioData:
        self._recognizer.energy_threshold = self._settings.background_energy_threshold
        self._recognizer.dynamic_energy_threshold = (
            self._settings.background_dynamic_energy_threshold
        )

        while True:
            logger.info("Start listen in background")

            try:
                with self._microphone as source:
                    start_time = time()
                    recorded_data = self._recognizer.listen(
                        source=source,
                        timeout=self._settings.background_recognizer_timeout,
                        phrase_time_limit=self._settings.background_phrase_time_limit,
                    )
                    if (
                        delta_time := time() - start_time
                        > self._settings.background_continue_speech_time
                    ):
                        logger.info(
                            "Very long speech %s, skip it and continue listen",
                            delta_time,
                        )
                        continue
            except WaitTimeoutError:
                logger.info("Did not hear anything, continue listen")
                continue
            return recorded_data

