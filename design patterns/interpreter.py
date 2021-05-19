import abc


class AbstractExpression(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        self._expression.interpret()


class TerminalExpression(AbstractExpression):

    def __init__(self, text):
        self.text = text
        self.grammar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self):
        numbers = list(map(self.grammar.get, self.text))
        if None in numbers:
            raise ValueError(f"Wrong input: {self.text}")
        result = 0
        temp = None
        while numbers:
            num = numbers.pop(0)
            if temp is None or temp >= num:
                result += num
            else:
                result += (num - temp * 2)
            temp = num
        return result


if __name__ == "__main__":
    interp = NonterminalExpression(TerminalExpression(''))
    print(interp.interpret())
    interp2 = TerminalExpression('MMMCMXCIX')
    print("MMMCMXCIX =", interp2.interpret())
    interp3 = TerminalExpression('MCMLXXXVIII')
    print("MCMLXXXVIII =", interp3.interpret())
