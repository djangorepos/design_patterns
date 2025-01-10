from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from pyttsx3 import speak


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    @staticmethod
    def exclusive_method_of_concrete_component_a() -> str:
        return "A"


class ConcreteComponentB(Component):

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    @staticmethod
    def special_method_of_concrete_component_b() -> str:
        return "B"


class Visitor(ABC):

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(comp: List[Component], visitor: Visitor) -> None:

    for component in comp:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("Client: The client code works with all visitors via the base Visitor interface:")
    speak("The client code works with all visitors via the base Visitor interface")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("Client: It allows the same client code to work with different types of visitors:")
    speak("It allows the same client code to work with different types of visitors")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
