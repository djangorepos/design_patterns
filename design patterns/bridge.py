from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, imp: Implementation) -> None:
        self._implementation = imp

    def operation(self) -> str:
        return (f"Abstraction: Base operation with ConcreteImplementation:\n"
                f"{self._implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with ConcreteImplementation:\n"
                f"{self._implementation.operation_implementation()}")


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstract: Abstraction) -> None:
    print(abstract.operation(), end="")


if __name__ == "__main__":

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
