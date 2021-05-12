from __future__ import annotations

from itertools import groupby
from string import ascii_letters

WORDS_SET = {'To', 'be', 'or', 'not', 'that', 'is', 'the', 'question'}


# noinspection PyListCreation


class Facade:

    def __init__(self, subsys1: Subsystem1, subsys2: Subsystem2) -> None:
        self._subsystem1 = subsys1 or Subsystem1()
        self._subsystem2 = subsys2 or Subsystem2()

    @property
    def operation(self):
        results: list[str] = ["Facade initializes subsystems:",
                              self._subsystem1.operation1(),
                              self._subsystem2.operation1(), "Facade orders subsystems to perform the action:",
                              self._subsystem1.operation2(), self._subsystem2.operation2()]
        # return "\n".join(results)


class Subsystem1:

    @staticmethod
    def operation1():
        words_set = WORDS_SET
        word = ''
        print("Subsystem1: Ready!")
        with open('LICENSE', 'r') as words_data:
            words_list = words_data.readlines()
            for i in range(len(words_list)):
                for j in range(len(words_list[i])):
                    if words_list[i][j] in ascii_letters:
                        word += words_list[i][j]
                    else:
                        if len(word) > 1:
                            words_set.add(word.lower())
                            words_set.add(word.lower().capitalize())
                        word = ''
            print(sorted(words_set))

    @staticmethod
    def operation2() -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    @staticmethod
    def operation1() -> str:
        with open('monkeys.txt', 'r') as ape_any_key:
            monkey_text = ape_any_key.readlines()
        return "Subsystem2: Get ready!"

    @staticmethod
    def operation2() -> str:
        return "Subsystem2: Fire!"


def client_code(client_facade: Facade) -> None:
    print(client_facade.operation, end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
