from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    file_cache = []

    @abstractmethod
    def sorting(self):
        pass


class Factory1(AbstractFactory):

    def sorting(self) -> object:
        with open('autoexec.cfg', 'r') as file_handler:
            file1 = file_handler.readlines()
        with open('autoexec.cfg', 'w') as file_handler:
            new_file = sorted(file1)
            file_handler.writelines(new_file)
            return new_file


class Factory2(AbstractFactory):
    def sorting(self) -> object:
        with open('autoexec.cfg', 'r') as file_handler:
            file2 = file_handler.readlines()
        with open('autoexec.cfg', 'w') as file_handler:
            new_file = sorted(file2, reverse=True)
            file_handler.writelines(new_file)
            return new_file


file_sort = Factory1()
# file_sort = Factory2()
result = file_sort.sorting()
print(result)
