from numpy import empty

def double_list(input: list, size):
    pos_counter = 0
    pos_tuples = []
    element_pos = []
    for ele in input:
        element_pos.append(ele)
        pos_counter+=1
        if pos_counter>=size:
            pos_counter = 0
            pos_tuples.append(element_pos)
            element_pos = []
    return pos_tuples

def swap(tuples, pos1: int=0, pos2: int=1):
    pos_list = list(tuples)
    var_1 = pos_list[pos1]
    var_2 = pos_list[pos2]
    pos_list.pop(pos2)
    pos_list.pop(pos1)
    pos_list.insert(pos2, var_1)
    pos_list.insert(pos1, var_2)
    return tuple(pos_list)

def check_row(input: list):
    abc = [chr(i) for i in range(ord('A'), ord('C')+1)]
    indexs = []
    for index, elem in enumerate(input):
        if elem in abc:
            abc.remove(elem)
        else:
            indexs.append(index)
    if len(abc)==1:
        return (abc[0], indexs[0])
    else:
        return None

def check_column(input:list):
    abc = [chr(i) for i in range(ord('A'), ord('C')+1)]
    indexs = []
    for index, elem in enumerate(input):
        if elem in abc:
            abc.remove(elem)
        else:
            indexs.append(index)
    if len(abc)==1:
        return (abc[0], indexs[0])
    else:
        return None

def parse_rows(arr: list):
    result = arr
    changed = False
    for row_1 in range(3):
        if check_row(arr[row_1]) != None:
            letter, index = check_row(arr[row_1])
            result[row_1][index]=letter
            changed = True
    return (result, changed)

def parse_columns(arr: list):
    result = arr
    changed = False
    for row_1 in range(3):
        if check_row(arr[:, row_1]) != None:
            letter, index = check_row(arr[:, row_1])
            result[row_1][index]=letter
            changed = True
    return (result, changed)

def check_options(row: list, column: list):
    abc_row = [chr(i) for i in range(ord('A'), ord('C')+1)]
    abc_column = [chr(i) for i in range(ord('A'), ord('C')+1)]
    for elem in row:
        if elem in abc_row:
            abc_row.remove(elem)
    for elem in column:
        if elem in abc_column:
            abc_column.remove(elem)
    return {'row': abc_row, 'column': abc_column}

def concatenate(arr):
    string = ''
    for idx1 in range(3):
        for idx2 in range(3):
            string+=arr[idx1][idx2]
    return string

def smart_logic(array):
    matrix = array
    for indx1 in range(3):
        for indx2 in range(3):
            if not array[indx1][indx2]:
                options_dict = check_options(array[indx1], array[:, indx2])
                for lettr in options_dict.get('row'):
                    if lettr in options_dict.get('column'):
                        matrix[indx1][indx2]=lettr
    return matrix

def code(length: int, inputs: str):
    array = empty((3, 3), dtype=str)
    pos_tuples = double_list(inputs.split(', '), 2)
    initial_pos = []
    initial_letters = []
    changed1 = True
    changed2 = False

    for pair in pos_tuples:
        initial_letters.append(pair[1])
        integer = int(pair[0])
        if 1<=integer<=3:
            initial_pos.append([0, integer-1])
        elif 4<=integer<=6:
            initial_pos.append([1, integer-4])
        elif 7<=integer<=9:
            initial_pos.append([2, integer-7])
    
    for loc, lttr in zip(initial_pos, initial_letters):
        array[loc[0]][loc[1]] = lttr
    
    while (changed1 or changed2) == True:
        # print(changed1, changed2)
        array, changed1 = parse_rows(array)
        array, changed1 = parse_columns(array)
      
    array = smart_logic(array)
    

    return concatenate(array)
def run():
    print('Please type PRACTICE, TEST, or QUIT to proceed.')
    submission = input().upper()

    if submission == 'PRACTICE':
        print('Please choose practice number')
        number = int(input())
        if number == 1:
            print(code(3, '1, A, 3, C, 8, A'))
        elif number == 2:
            print(code(3, '1, A, 6, C, 8, B'))
        elif number == 3:
            print(code(3, '1, B, 6, B, 9, C'))
        elif number == 4:
            print(code(2, '1, C, 5, B'))
        elif number == 5:
            print(code(2, '3, B, 7, A'))
    elif submission == 'QUIT':
        exit(0)
    elif submission == 'TEST':
        number = int(input())
        if number == 1:
            print(code(4, '1, A, 2, B, 8, A. 9, B'))
        elif number == 2:
            # Doesn't work
            print(code(3, '1, A, 2, B, 9, A'), code(3, '1, A, 2, B, 9, A')=='ABCCABBCA')
        elif number == 3:
            print(code(3, '3, C, 6, B, 7, C'))
        elif number == 4:
            print(code(2, '7, A, 6, C'))
        elif number == 5:
            # Doesn't work
            print(code(2, '1, C, 6, A'), code(2, '1, C, 6, A')=='CABBCAABC')
run()