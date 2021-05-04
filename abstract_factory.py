from abc import ABCMeta, abstractmethod
from decimal import *

JSON = '{"total": 9.61, "items": ["Americano", "Omelet"]}' \
       '{"total": 5.45, "items": ["Cappuccino", "Cookie"]}'


class AbstractFactory(metaclass=ABCMeta):

    @abstractmethod
    def build_sequence(self):
        pass

    @abstractmethod
    def build_number(self, string):
        pass


class Factory(AbstractFactory):
    def build_sequence(self):
        return []

    def build_number(self, string):
        return Decimal(string)

    @staticmethod
    def load(string, factory):
        sequence = factory.build_sequence()
        for substring in string.split(','):
            item = factory.build_number(substring)
            sequence.append(item)
        return sequence


f1 = Factory()
result = f1.load('1.23, 4.56', f1)
print(result)

f2 = Factory()
result = f2.load(JSON[10:16]+JSON[59:63], f2)
print(result)
