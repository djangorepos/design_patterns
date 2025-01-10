from abc import ABC, abstractmethod

from pyttsx3 import speak


class AbstractClass(ABC):

    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.hook2()
        self.required_operations2()
        self.base_operation3()

    @staticmethod
    def base_operation1() -> None:
        print("AbstractClass says: I am doing the bulk of the work")
        speak("I am doing the bulk of the work")

    @staticmethod
    def base_operation2() -> None:
        print("AbstractClass says: But I let subclasses override some operations")
        speak("But I let subclasses override some operations")

    @staticmethod
    def base_operation3() -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")
        speak("But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")
        speak("Implemented Operation one")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")
        speak("Implemented Operation two")

    def hook1(self) -> None:
        print("ConcreteClass1 says: Overridden Hook1")
        speak("Overridden Hook one")


class ConcreteClass2(AbstractClass):

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")
        speak("Implemented Operation one")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")
        speak("Implemented Operation two")

    def hook2(self) -> None:
        print("ConcreteClass2 says: Overridden Hook2")
        speak("Overridden Hook two")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
