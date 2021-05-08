from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from time import sleep


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        print('Server: Loading, please wait...')
        self.transition_to(state)
        print('Server: Online mode.')

    def transition_to(self, state: State):
        print(f'Server: Changing state to {type(state).__name__}')
        for i in range(42):
            print('#', end='')
            sleep(0.05)
        print()
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


# noinspection PyAttributeOutsideInit
class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, concrete_context: Context) -> None:
        self._context = concrete_context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print('Server: Working online. Received offline request.')
        print('Server: Switching to offline mode. Please wait...')
        self.context.transition_to(ConcreteStateB())
        print('Server: Offline mode.')

    def handle2(self) -> None:
        for i in range(4):
            _ping: int = randint(1, 100)
            print(f'Server: Working online. Ping {_ping} ms. Packet loss is 0%')
            sleep(1)


class ConcreteStateB(State):
    def handle1(self) -> None:
        print(f'Server: Offline mode.')

    def handle2(self) -> None:
        print('Server: Received online request.')
        print('Server: Switching to online mode. Please wait...')
        self.context.transition_to(ConcreteStateA())
        print('Server: Online mode.')


if __name__ == '__main__':
    server = Context(ConcreteStateA())
    print()

    print('Client: Reboot server')
    server.request1()
    server.request2()
    print()

    print('Client: Echo server')
    server.request2()
    print()

    print('Client: Shutdown server')
    server.request1()
