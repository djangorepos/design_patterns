from __future__ import annotations
from abc import ABC, abstractmethod
from pyttsx3 import speak
from gtts import gTTS
from langdetect import detect
from playsound3 import playsound

def complex_speak(complex_stuff, accent=None):
    try:
        # Detect language of the user's message
        detected_language = accent or detect(complex_stuff)
    except Exception as e:
        detected_language = 'en'  # Default to English if detection fails
        print(f"Could not detect language, defaulting to English. Error: {e}")

    # Generate speech
    tts = gTTS(complex_stuff, lang=detected_language)
    audio_file_path = '/audio/output.mp3'
    tts.save(audio_file_path)
    playsound(audio_file_path)


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Hi! "
              f"{self._payload}")
        speak(f"Hi!"
              f"{self._payload}")


class ComplexCommand(Command):

    def __init__(self, rec: Receiver, a: str, b: str) -> None:
        self._receiver = rec
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        complex_speak("Complex stuff should be done by a receiver object", "en-us")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    @staticmethod
    def do_something(a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")
        complex_speak(f"Working on ({a}.)", "en-au")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
        complex_speak(f"Also working on ({b}.)", "en-au")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        complex_speak("Does anybody want something done before I begin?", "en-uk")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")
        complex_speak("doing something really important", "en-uk")

        print("Invoker: Does anybody want something done after I finish?")
        complex_speak("Does anybody want something done after I finish?", "en-uk")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("I can do simple things."))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
