from logging import basicConfig, debug, DEBUG
from sys import path
path.insert(0, './2022-23/Contest-1')
from functions import Functions
import numpy as np
basicConfig(level=DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')

arr = np.full((3, 1), 'A')
arr = np.append(arr, [['B']]*3, 1)
print(arr.tolist())
print(''.join(sum(arr.tolist(), [])))