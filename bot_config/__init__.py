import os
import re

init_arr = []

for path_file in os.listdir(os.path.dirname(__file__)):
    if re.search('^config\_(.*)\.py', path_file):
        init_arr.append(path_file[:-3])

print(init_arr)
__all__ = init_arr
