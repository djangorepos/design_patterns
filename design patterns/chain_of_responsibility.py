from abc import ABCMeta, abstractmethod
from random import randint
from pyttsx3 import speak


class IHandler(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, payload):
        pass


class Successor1(IHandler):

    def handle(self, payload):
        print(f"Successor1: payload = {payload}")
        test = randint(1, 2)
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload


class Successor2(IHandler):

    def handle(self, payload):
        print(f"Successor2 payload = {payload}")
        test = randint(1, 10)
        if test in (1, 2, 3, 4, 5):
            payload = payload * 2
            payload = Successor1().handle(payload)
        if test in (5, 6, 7, 8, 9):
            payload = payload / 2
            payload = Successor2().handle(payload)
        return payload


class Client:

    @staticmethod
    def start(payload):
        return Successor1().handle(payload)


if __name__ == "__main__":
    CHAIN = Client()
    PAYLOAD = 1
    OUT = CHAIN.start(PAYLOAD)
    print(f"Client: Finished result = {OUT}")
    speak(f"Finished result = {OUT}")
