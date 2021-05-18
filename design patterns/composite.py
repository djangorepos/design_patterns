from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from text_to_speech import speak


class Component(ABC):

    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        pass

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):

    def is_composite(self) -> bool:
        return False

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    results = []

    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        for child in self._children:
            self.results.append(child.operation())
        return f"\nBranch({'+'.join(self.results)})"


def client_code(component: Component) -> None:

    print(f"RESULT: {component.operation()}", end='')


def client_code2(component1: Component, component2: Component) -> None:

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end='')


if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component:")
    speak("I've got a simple component")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    speak("Now I've got a composite tree")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    speak("I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
