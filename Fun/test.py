from sys import getsizeof
import logging as lg
from sys import path
path.insert(0, './2022-23/Contest-1')
from functions import Functions

lg.basicConfig(level=lg.DEBUG, format='[%(levelname)s] %(asctime)s - %(message)s')
def generator():
    num = 0
    while True:
        yield num
        num+=1
        if num == 1_000_000_000:
            break
letters = [chr(i) for i in range(ord('A'), ord('I')+1)]
abc = 'abc'[1:][1:]
print(abc)
empty = ''
if not empty:
    print('Test')
if empty == '':
    print('Test2')