from abc import ABC, abstractmethod
from time import perf_counter

Number: int = 100


class Strategy(ABC):
    @abstractmethod
    def algorithm_interface(self): pass


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print('Using cycle for')
        fib1 = fib2 = 1
        n = Number
        print(fib1, fib2, end=' ')

        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end=' ')


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print('Using cycle while')
        fib1 = fib2 = 1
        print(fib1, fib2, end=' ')
        n = Number - 2

        while n > 0:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
            print(fib2, end=' ')


class ConcreteStrategyC(Strategy):

    def algorithm_interface(self):
        print('Using recursion')
        cache = {1: 1, 2: 1}

        def fib(n):
            result = cache.get(n)
            if result is None:
                result = fib(n - 2) + fib(n - 1)
                cache[n] = result
            return result

        print(fib(Number), cache.values())


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        self._start = perf_counter();

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def context_interface(self) -> None:
        print("Context: Calculating fibonacci number using the strategy (not sure how it'll do it)")
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
