from __future__ import annotations
from collections.abc import Iterable, Iterator
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

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":

    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    speak("Straight traversal")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    speak("Reverse traversal")
    print("\n".join(collection.get_reverse_iterator()), end="")