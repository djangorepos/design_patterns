from __future__ import annotations
from abc import ABC, abstractmethod
from text_to_speech import speak
import pyttsx3


def complex_speak(complex_stuff, token):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\' + token)
    engine.say(complex_stuff)
    engine.runAndWait()


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
        complex_speak("Complex stuff should be done by a receiver object", 'TTS_MS_EN-US_ZIRA_11.0')
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    @staticmethod
    def do_something(a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")
        complex_speak(f"Working on ({a}.)", 'TTS_MS_EN-GB_HAZEL_11.0')

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
        complex_speak(f"Also working on ({b}.)", 'TTS_MS_EN-GB_HAZEL_11.0')


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        complex_speak("Does anybody want something done before I begin?", 'TTS_MS_EN-US_DAVID_11.0')
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")
        complex_speak("doing something really important", 'TTS_MS_EN-US_DAVID_11.0')

        print("Invoker: Does anybody want something done after I finish?")
        complex_speak("Does anybody want something done after I finish?", 'TTS_MS_EN-US_DAVID_11.0')
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("I can do simple things."))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
