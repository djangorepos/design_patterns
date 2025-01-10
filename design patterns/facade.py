from __future__ import annotations
from string import ascii_letters
import random

from pyttsx3 import speak

WORDS_SET = {'To', 'be', 'or', 'not', 'that', 'is', 'the', 'question', 'a'}
LETTERS = ascii_letters + "'"


class Facade:
    def __init__(self, subsys1: Subsystem1, subsys2: Subsystem2) -> None:
        self._subsystem1 = subsys1 or Subsystem1()
        self._subsystem2 = subsys2 or Subsystem2()

    @property
    def operation(self):
        print("Facade: Initializing subsystems:")
        speak("Initializing subsystems")
        w_s = self._subsystem1.operation1()
        print("Facade: Order subsystems to perform the action:")
        speak("Order subsystems to perform the action")
        a_s = self._subsystem2.operation1(w_s)
        founded = self._subsystem1.operation2(a_s)
        print(self._subsystem2.operation2(founded, w_s))
        print("Facade: Generating text from all known words:")
        speak("Generating text from all known words")
        self._subsystem1.operation2(w_s)
        return "Facade: All done!"


class Subsystem1:

    @staticmethod
    def operation1() -> set[str]:
        words_set = WORDS_SET
        word = ''
        with open('temp\hamlet.txt', 'r') as words_data:
            words_list = words_data.readlines()
            for i in range(len(words_list)):
                for j in range(len(words_list[i])):
                    if words_list[i][j] in LETTERS:
                        word += words_list[i][j]
                    else:
                        if len(word) > 1:
                            words_set.add(word.lower())
                            words_set.add(word.capitalize())
                        word = ''
        print("Subsystem1: Words set finished.")
        return words_set

    @staticmethod
    def operation2(ape_set=None) -> int:
        print("Subsystem1: Printing words:")
        i = 0
        cap = False
        used = False
        line = False
        for ape_word in ape_set:
            i += 1
            j = random.randint(1, 12)
            if i == 1 or cap:
                print(ape_word.capitalize(), end=' ')
                cap = False
            elif j == 2 == 12:
                print(ape_word, end=', ')
                used = True
            elif j == 3:
                print(ape_word, end=' ')
                if not line:
                    print(' -', end=' ')
                    cap = False
                    line = True
            elif j == 4:
                print(ape_word, end='. ')
                cap = True
                used = True
            elif j == 5:
                print(ape_word, end='.\n')
                cap = True
            elif j == 6:
                print(ape_word, end='? ')
                cap = True
                used = True
            elif j == 7:
                print(ape_word, end='! ')
                cap = True
                used = True
            elif j == 8:
                print(ape_word, end='')
                if not used:
                    print(':', end=' ')
                    cap = False
            else:
                print(ape_word, end=' ')
                cap = False
        print()
        return i


class Subsystem2:

    @staticmethod
    def operation1(words_set=None, ape_set=None):
        if ape_set is None:
            ape_set = set()
        print("Subsystem1: Searching for words...")
        with open('temp\monkeys.txt', 'r') as ape_words:
            ape_list = ape_words.readlines()
            ape_word: str = ''
            for i in range(len(ape_list)):
                for j in range(len(ape_list[i])):
                    if str(ape_list[i][j]) in LETTERS:
                        ape_word += str(ape_list[i][j])
                        if len(ape_word) > 1 and (ape_word in words_set):
                            ape_set.add(ape_word)
                            ape_word: str = ''
                    else:
                        ape_word: str = ''
        print("Subsystem2: Monkeys set completed.")
        print(ape_set)
        return ape_set

    @staticmethod
    def operation2(i: int, word_set=None) -> str:
        with open("temp\words.txt", "a") as ape_words:
            for j in word_set:
                ape_words.write(j)
                ape_words.write(' ')
        return f"Subsystem2: {i} words found."


def client_code(client_facade: Facade) -> None:
    print(client_facade.operation, end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)

