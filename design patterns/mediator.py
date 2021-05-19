from __future__ import annotations
from abc import ABC
from text_to_speech import speak


class Mediator(ABC):

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):

    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:

        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            speak("I am reacting on A and trigger following operations")
            self._component2.do_c()

        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            speak("I am reacting on D and trigger following operations")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:

    def __init__(self, med: Mediator = None) -> None:
        self._mediator = med

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, media: Mediator) -> None:
        self._mediator = media


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        speak("I am doing A")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        speak("I am doing B")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        speak("I am doing C")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        speak("I am doing D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
