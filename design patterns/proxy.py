from abc import ABC, abstractmethod
from pyttsx3 import speak


class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access:
            self._real_subject.request()
            self.log_access()

    @staticmethod
    def check_access() -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    @staticmethod
    def log_access() -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    speak("Executing the client code with a real subject")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    speak("Executing the same client code with a proxy")
    proxy = Proxy(real_subject)
    client_code(proxy)
