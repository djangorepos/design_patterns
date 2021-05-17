from abc import ABC, abstractmethod
from copy import copy, deepcopy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ConcretePrototype1(Prototype):
    def __init__(self, arg):
        self.field = arg

    def __operation__(self):
        self.performed_operation = True

    def clone(self) -> object:
        return copy(self)


class ConcretePrototype2(Prototype):
    def __init__(self, arg):
        self.field = arg

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    p1 = ConcretePrototype1([1, 2, 3, 4, 5])
    print("Client: Object created ", p1.field, "id =", id(p1))

    p2 = p1.clone()
    print("Client: Object copy    ", p2.field, "id =", id(p2))

    p2.field[0] = 7
    p2.field.pop()
    p2.field.append(7)

    print()

    print("Client: Original list  ", p1.field, "id =", id(p1))
    print("Client: List copy      ", p2.field, "id =", id(p2))

    print()

    if p1.field is p2.field:
        print("Objects is the same")

    if id(p1.field) == id(p2.field):
        print("Prototype copy works, both variables depends each other.")
    else:
        print("Prototype failed, variables contain different instances.")

    print()

    p_1 = ConcretePrototype2([1, 2, 3, 4, 5])
    print("Client: Object created ", p_1.field, "id =", id(p_1))

    p_2 = p1.clone()
    print("Client: Object deepcopy", p_2.field, "id =", id(p_2))

    p_2.field[0] = 7
    p_2.field.pop()
    p_2.field.append(7)

    print()

    print("Client: Original list  ", p_1.field, "id =", id(p_1))
    print("Client: List deepcopy  ", p_2.field, "id =", id(p_2))

    print()

    if p_1.field is p_2.field:
        print("Objects is the same")

    if id(p_1.field) == id(p_2.field):
        print("Prototype deepcopy failed, both variables depends each other.")
    else:
        print("Prototype deepcopy works, variables contain different instances.")

