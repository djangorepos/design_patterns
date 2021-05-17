from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    file_cache = []

    @abstractmethod
    def sorting(self):
        pass


class Factory1(AbstractFactory):

    def sorting(self) -> object:
        with open('temp/autoexec.cfg', 'r') as file_handler:
            file1 = file_handler.readlines()
            new_file = sorted(file1)
        with open('temp/autoexec.cfg', 'w') as file_handler:
            file_handler.writelines(new_file)
            return new_file


class Factory2(AbstractFactory):
    def sorting(self) -> object:
        with open('temp/autoexec.cfg', 'r') as file_handler:
            file2 = file_handler.readlines()
            new_file = sorted(file2, reverse=True)
        with open('temp/autoexec.cfg', 'r+') as file_handler:
            file_handler.writelines(new_file)
            return new_file


file_sort = Factory1()
result = file_sort.sorting()
print(result)
