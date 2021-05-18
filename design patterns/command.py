from __future__ import annotations
from abc import ABC, abstractmethod
from text_to_speech import speak
import pyttsx3


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

        def complex_speak(complex_stuff):
            engine = pyttsx3.init()
            engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN'
                                        '-US_ZIRA_11.0')
            engine.say(complex_stuff)
            engine.runAndWait()

        complex_speak("Complex stuff should be done by a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:

    @staticmethod
    def do_something(a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")
        speak(f"\nReceiver: Working on ({a}.)")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
        speak(f"\nReceiver: Also working on ({b}.)")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:

        def invoker_speak(complex_stuff):
            engine = pyttsx3.init()
            engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN'
                                        '-US_DAVID_11.0')
            engine.say(complex_stuff)
            engine.runAndWait()

        print("Invoker: Does anybody want something done before I begin?")
        invoker_speak("Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")
        invoker_speak("doing something really important")

        print("Invoker: Does anybody want something done after I finish?")
        invoker_speak("Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("I can do simple things."))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()
