from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from pyttsx3 import speak


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        result_product_a = randint(50, 100)
        return "Product A1: " + str(result_product_a) + '%'


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        result_product_a = randint(50, 100)
        return "Product A2: " + str(result_product_a) + '%'


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return f"The result of the product B1: {randint(0, 50)} %."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result_a = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the {result_a}"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return f"The result of the product B2: {randint(0, 50)} %."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result_b = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the {result_b}"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    speak("Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    speak("Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
