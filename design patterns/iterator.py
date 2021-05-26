from __future__ import annotations
from collections.abc import Iterable, Iterator
from time import sleep
from typing import Any
from text_to_speech import speak


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, col: WordsCollection, reverse: bool = False) -> None:
        self._collection = col
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, col=None) -> None:
        if col is None:
            col = []
        self._collection = col

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def __getitem__(self, key):
        return getattr(self, key)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("One")
    collection.add_item("Two")
    collection.add_item("Three")
    collection.add_item("Four")
    collection.add_item("Five")
    collection.add_item("Six")
    collection.add_item("Seven")
    collection.add_item("Eight")
    collection.add_item("Nine")
    collection.add_item("Ten")
    collection.add_item("Eleven")
    collection.add_item("Twelve")

    print("Client: Checking Systems:")
    speak("Checking Systems")
    for _ in range(101):
        print('\r', _, '%', end='#' * _)
        sleep(0.01)
    print("")
    print(" ".join(collection))
    print("")
    print("Client: Thirty seconds and counting. Astronauts report it feels good. T-25 seconds. Twenty seconds and "
          "counting. T-15 seconds, guidance is internal.")

    reverse_count = collection.get_reverse_iterator()
    for word in reverse_count:
        if word == "Six":
            print("Client: Ignition sequence start.")
            speak("Ignition sequence start")
        print(word)
        speak(word)
    print("Client: All engines running.")
    speak("All engines running.")
    print("Client: Liftoff!")
    speak("Liftoff!")
