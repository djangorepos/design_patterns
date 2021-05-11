from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

SPEECH = "To be, or not to be, that is the question:"


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        random_string = ""
        for _ in range(len(SPEECH)):
            random_string += product.operation()
        result = f"Ape: pressinganykey: {random_string}"
        return result


class ConcreteCreator(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct(Product):
    def operation(self, random_string=str) -> str:
        return chr(randint(32, 122))


def client_code(creator: Creator) -> str:
    return (f"William Shakespeare: {SPEECH} \n"
            f"{creator.some_operation()}")


if __name__ == "__main__":
    Apes = 0
    while True:
        monkey_code = client_code(ConcreteCreator())
        Apes += 1
        if SPEECH != monkey_code:
            print(monkey_code)
            print(f"Shakespeare wins, Apes = {Apes}\n")
            with open('monkeys.txt', 'a') as file:
                file.write(f"{monkey_code}\n"
                           f"Shakespeare wins, Apes = {Apes}\n")
        else:
            SPEECH = "Monkeys wins"
            print(SPEECH)
            break
