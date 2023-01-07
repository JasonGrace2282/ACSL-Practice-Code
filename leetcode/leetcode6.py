import numpy as np
from math import ceil

def init_arr(length: int, numRows: int):
    if numRows==1:
        return np.full((1, length), '')

    arr_col = ceil(length/(numRows+numRows-2))
    return np.full((numRows, arr_col), '')

def arr_sum(arr) -> str:
    return ''.join(sum(arr.tolist(), []))

def convert(s: str, numRows: int) -> str:
    global convert_input
    convert_input = s
    arr = init_arr(len(s), numRows)
    reset = True
    height = -1
    length = 0
    counter = 0
    if numRows == 1:
        return s
    for char in s:
        try:
            if not reset:
                raise IndexError
            height+=1
            arr[height][length]=char
        except IndexError:
            if counter == 0:
                height-=2
                counter = 1
            elif counter == 1:
                height-=1
            length+=1
            arr[height][length]=char
            if height==0:
                reset = True
                counter = 0
            else:
                reset = False
    return arr_sum(arr)

answer = convert("PAYPALISHIRING", 3)
print(f"Input: {convert_input}\nAnswer: {answer}\nCorrect: {answer=='PAHNAPLSIIGYIR'}")