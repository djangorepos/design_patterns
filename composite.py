from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from os import listdir


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

    def operation(self):
        hand_history = []
        list_of_files = listdir("C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix")
        for file in list_of_files:
            with open(f"C:\\Users\\Admin\\AppData\\Local\\PokerStars\\HandHistory\\EatTwix\\{file}", "r") as lines:
                with open("spin&go.txt", "r") as spingo:
                    if spingo.read() not in hand_history:
                        hand_history.append(lines.readlines())
        return hand_history


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
        return f"Branch({'+'.join(self.results)})"


def client_code(component1: Component, component2: Component) -> str:
    if component1.is_composite():
        component1.add(component2)
        return component2.operation()


if __name__ == "__main__":
    leaf = Leaf()
    comp = Composite()
    print("Client: I've got a simple component:")


    def hands(hand, tour, i, j):
        spin_go1 = (client_code(comp, leaf))
        for line1 in spin_go1:
            for string in line1:
                hand_index = string.find(hand)
                tour_index = string.find(tour)
                if ("-1" not in str(hand_index)) and ("-1" not in str(tour_index)):
                    with open("spin&go.txt", "r") as spin_go_r:
                        if string[hand_index + i:tour_index + j] not in spin_go_r.readline():
                            with open("spin&go.txt", "a") as spin_go_txt:
                                spin_go_txt.write(string[hand_index + i:tour_index + j])
                                spin_go_txt.write(" ")


    hands("Hand #", "Tournament #", 6, -2)


    def players(p1, p2, i, j, spin_list=None):
        if spin_list is None:
            spin_list = []
        with open("spin&go.txt", "a") as spin_go_txt3:
            spin_go_txt3.write("\n")
        spin_go2 = (client_code(comp, leaf))
        for line2 in spin_go2:
            for string in line2:
                player_index = string.find(p1)
                end_index = string.find(p2)
                if ("-1" not in str(player_index)) and ("-1" not in str(end_index)):
                    keys = string[player_index + i: end_index + j]
                    values = string[end_index + 1: end_index + 4]
                    spin_list.append((keys, values))
                    print(spin_list)
                    with open("spin&go.txt", "a") as spin_go_txt3:
                        spin_go_txt3.write(str(spin_list))
                        spin_go_txt3.write(" ")


    players("Seat", "(", 8, -1)
