from abc import ABC, abstractmethod
from time import perf_counter
import numpy as np

NUMBER: int = 10
SHOW_DICT = True


class Strategy(ABC):
    @abstractmethod
    def algorithm_interface(self): pass


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print('Algorithm: Using cycle for')
        cache = {1: 1, 2: 1}
        n = NUMBER
        fib1 = fib2 = 1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            cache[i + 1] = fib2
        n = fib2
        if SHOW_DICT:
            print(n, cache.values(), end=' ')
        else:
            print(n, end=' ')


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print('Algorithm: Using cycle while')
        cache = {1: 1, 2: 1}
        fib1 = fib2 = 1
        n = NUMBER - 2
        i = 2

        while n > 0:
            fib1, fib2 = fib2, fib1 + fib2
            cache[i + 1] = fib2
            i += 1
            n -= 1
        n = fib2
        if SHOW_DICT:
            print(n, cache.values(), end=' ')
        else:
            print(n, end=' ')


class ConcreteStrategyC(Strategy):

    def algorithm_interface(self):
        print('Algorithm: Using recursion')
        cache = {1: 1, 2: 1}

        def fib(n):
            result = cache.get(n)
            if result is None:
                result = fib(n - 2) + fib(n - 1)
                cache[n] = result
            return result

        if SHOW_DICT:
            print(fib(NUMBER), cache.values(), end=' ')
        else:
            print(fib(NUMBER), end=' ')


class ConcreteStrategyD(Strategy):

    def algorithm_interface(self):
        print('Algorithm: Using matrix')
        cache = {1: 1, 2: 1}

        def fib(n):
            for i in range(3, n+1):
                result = np.matrix([[1, 1], [1, 0]], dtype=object) ** i
                cache[i] = result[0, 1]
            return result[0, 1]

        if SHOW_DICT:
            print(fib(NUMBER), cache.values(), end=' ')
        else:
            print(fib(NUMBER), end=' ')


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        self._start = perf_counter()

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def context_interface(self) -> None:
        print(f"Context: Calculating {NUMBER} fibonacci numbers using the strategy (not sure how it'll do it)")
        self._strategy.algorithm_interface()
        print()
        print('Time run:', perf_counter() - self._start)
        print()


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to cycle for.")
    context.context_interface()

    print("Client: Strategy is set to cycle while.")
    context.strategy = ConcreteStrategyB()
    context.context_interface()

    context = Context(ConcreteStrategyC())
    print("Client: Strategy is set to recursion.")
    context.context_interface()

    context = Context(ConcreteStrategyD())
    print("Client: Strategy is set to matrix.")
    context.context_interface()
