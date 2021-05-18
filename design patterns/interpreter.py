class RomanNumeralInterpreter(object):

    def __init__(self):
        self.grammar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self, text):
        numbers = list(map(self.grammar.get, text))
        if None in numbers:
            raise ValueError(f"Wrong input: {text}")
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
    interp = RomanNumeralInterpreter()
    print("MMMCMXCIX =", interp.interpret('MMMCMXCIX'))
    print("MCMLXXXVIII =", interp.interpret('MCMLXXXVIII'))
