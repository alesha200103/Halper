from stt import STT
from voice_controller import VoiceController


class TextManager:
    def __init__(self, stt: STT, voice_controller: VoiceController):
        self._stt = stt
        self._voice_controller = voice_controller

    def start_listen(self) -> str | None:
        audio_data = self._voice_controller.listen()
        if audio_data:
            return self._stt.recognize(audio_data)
        return

    def start_listen_background(self) -> str:
        audio_data = self._voice_controller.background_listen()
        return self._stt.recognize(audio_data)


# if __name__ == "__main__":
#     from voice_controller import VoiceControllerSettings
#     from stt import STTSettings
#     import speech_recognition
#
#     recognizer = speech_recognition.Recognizer()
#     microphone = speech_recognition.Microphone()
#     stt = STT(recognizer=recognizer, settings=STTSettings())
#     voice_controller = VoiceController(recognizer=recognizer, microphone=microphone, settings=VoiceControllerSettings())
#     text_manager = TextManager(stt=stt, voice_controller=voice_controller)
#     print(text_manager.start_listen())
