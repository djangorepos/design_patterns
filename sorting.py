from copy import deepcopy
from itertools import groupby

with open('autoexec.cfg', 'r') as file_handler:
    file = file_handler.readlines()
    print(file)
    file_cache = deepcopy(file)
    file = file_cache
with open('autoexec.cfg', 'w') as file_handler:
    new_file = sorted(file)
    new_file_without_dub = [el for el, _ in groupby(new_file)]
    print(new_file)
    print(new_file_without_dub)
    if new_file_without_dub:
        file_handler.writelines(new_file_without_dub)
    else:
        file_handler.writelines(file_cache)
