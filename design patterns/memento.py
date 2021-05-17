from __future__ import annotations
from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime
from random import randint
from string import ascii_lowercase, digits
from time import sleep

DATA = ascii_lowercase + digits


def loading():
    for i in range(101):
        print(f'\r{i}% ', end=i * '#')
        sleep(0.01)
    print()


class Originator:
    _state = Noney

    def __init__(self, state: list[str]) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state[0][:39]}")

    def create_new_file(self) -> None:
        print("Originator: Generating new file.")
        loading()
        self._state = self._generate_random_file(len(self._state))
        with open('temp/mt86plus', 'w') as mt86plus:
            mt86plus.writelines(self._state)
        print(f"Originator: My state has changed to: {self._state[0][:39]}")

    @staticmethod
    def _generate_random_file(length: int):
        seq = ''
        result = []
        for i in range(length):
            for j in range(8):
                for k in range(4):
                    seq += DATA[randint(0, 35)]
                if j < 7:
                    seq += ' '
                else:
                    seq += '\n'
                    result.append(seq)
                    seq = ''
        return result

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has restored to: {self._state[0][:39]}")
        with open('temp/mt86plus', 'w') as mt86plus:
            mt86plus.writelines(self._state)


class Memento(ABC):

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: list[str]) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> list[str]:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / {self._state[0][:39]}"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    backups = 0

    def __init__(self, orig: Originator) -> None:
        self._mementos = []
        self._originator = orig

    def backup(self) -> None:
        loading()
        self._mementos.append(self._originator.save())
        self.backups += 1

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        loading()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":

    with open('temp/mt86plus', 'r') as file_handler:
        file = file_handler.readlines()
        temp = deepcopy(file)
    try:
        open('temp/mt86plus.backup')
    except FileNotFoundError:
        with open('temp/mt86plus.backup', 'w') as file_backup:
            temp = file_backup
            file_backup.writelines(file)

    originator = Originator(file)
    caretaker = Caretaker(originator)

    for _ in range(3):
        caretaker.backup()
        originator.create_new_file()

    while True:
        print(f"\nClient: There are {caretaker.backups} restore points:")
        caretaker.show_history()
        if caretaker.backups > 1:
            print("Client: Rollback? y/n\n")
        elif caretaker.backups == 1:
            print("Client: Return to original state? y/n\n")
        elif caretaker.backups == 0:
            break
        key = input()
        if key == 'y' or key == 'Y':
            caretaker.undo()
            caretaker.backups -= 1
        elif key == 'n' or key == 'N':
            break
        else:
            print('Wrong symbol, try again')

    print("Client: No mementos, find mt86plus.backup")
