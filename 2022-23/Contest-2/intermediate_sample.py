def remove_duplicate(str: str):
    set = set()
    result = ''
    for char in str:
        set.add(char)
    for object in set:
        result+=object
    return result

def common_char(string: str, comparison_string: str, left_to_right: bool):
    common_chars = ''
    string_copy = string
    loop_string = comparison_string
    start = 0
    if left_to_right:
        for index, char in enumerate(string_copy):
            if char in loop_string[start:]:
                print(char, common_chars, loop_string)
                common_chars+=char
                start = index if index != 0 else index+1
                string_copy = string[start:]
        return common_chars
    else:
        for char in reversed(string):
            if char in comparison_string:
                common_chars+=char
        return common_chars

def four_str_intersection(string1, string2, string3, string4):
    return (set(string1).intersection(string2).intersection(string3).intersection(string4))

def diff(string: str):
    string_1, string_2 = string.lower().split(' ')
    common_string_list = ['', '', '', '']
    common_string_list[0] = common_char(string_1, string_2, True)
    common_string_list[1] = common_char(string_2, string_1, True)
    common_string_list[2] = common_char(string_1, string_2, False)
    common_string_list[3] = common_char(string_2, string_1, False)
    common_chars = ''.join(sorted((set(common_string_list[0]).intersection(common_string_list[1])).intersection(common_string_list[2]).intersection(common_string_list[3])))
    if common_chars == '':
        common_chars = 'NONE'
    return common_chars

# print(diff('delicious indiginous')) # wrong
print(diff('shalom saaalaaam')) # wrong