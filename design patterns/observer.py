from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

from pyttsx3 import speak


class Subject(ABC):
    state: int = None

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self.state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self.state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, sub: Subject) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, sub: Subject) -> None:
        if sub.state < 3:
            print("ConcreteObserverA: Reacted to the event")
            speak("Unbelievable!")


class ConcreteObserverB(Observer):
    def update(self, sub: Subject) -> None:
        if sub.state == 0 or sub.state >= 2:
            print("ConcreteObserverB: Reacted to the event")
            speak("WoW!")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
