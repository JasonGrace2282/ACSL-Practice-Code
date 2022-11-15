from math import floor

print('Welcome to the ACSL Contest 1 Calculator!\nPlease type the letter of which function you would like to use.\
    \nA)Decimal to Binary\nB)Decimal to Octal\nC)Decimal to Hexadecimal\nD)Decimal to Custom Base\nE)Other bases to Decimal')
calc_choice = (input('Choose: ')).split('Choose: ')[0]
print(f'You have chosen letter {calc_choice.upper()}')

if calc_choice.upper() not in ['D', 'E'] and calc_choice.upper() in ['A', 'B', 'C']:
    decimal = (input('Input your decimal number: ')).split('Input your decimal number: ')[0]
    try:
        int(decimal)
    except ValueError:
        print('How many values after the decimal point should we calculate to? ')
        decimal_length = (int((input('Decimal places: ')).split('Decimal places: ')[0]))-1
    else:
        decimal_length = 5
    try:
        decimal = int(decimal)
    except ValueError:
        decimal = str(decimal)
    calc_choice2 = None

elif calc_choice.upper() == 'D':
    print('WARNING: This calculator does not work with custom bases greater than 9 or less than 1')
    base = int((input('Base: ')).split('Base: ')[0])
    decimal = float((input('Input your decimal number: ')).split('Input your decimal number: ')[0])
    calc_choice2 = None

elif calc_choice.upper() == 'E':
    print('Welcome to the convert to decimal calculator. \nPlease type the letter of the option you would like to choose\
        \nA)Binary to Decimal\nB)Octal to Decimal\nC)Hexadecimal to Decimal\nD)Custom base to Decimal')
    calc_choice2 = (input('Choose: ')).split('Choose: ')[0]
    print(f'You have chosen letter {calc_choice2.upper()}')

    if calc_choice2.upper() == 'A':
        base_value = int((input('Input your Binary number: ')).split('Input your Binary number: ')[0])
    elif calc_choice2.upper() == 'B':
        base_value = int((input('Input your Octal number: ')).split('Input your Octal number: ')[0])
    elif calc_choice2.upper() == 'C':
        base_value = (input('Input your Hexadecimal number: ')).split('Input your Hexadecimal number: ')[0]
    elif calc_choice2.upper() == 'D':
        print('WARNING: This calculator does not work with custom bases greater than 9 or less than 1')
        base2 = int((input('Base: ')).split('Base: ')[0])
        base_value = int((input(f'Input your Base {base2} number: ')).split(f'Input your Base {base2} number: ')[0])

def decimal_to_other(decimal, base, length):
    decimal_copy = float(decimal)
    if float(decimal)%1 == 0:
        return int_value(decimal, base)
    else:
        decimal_copy = (str(decimal)).split('.')
        # print(decimal_copy)
        integer = int_value(int(decimal_copy[0]), base, False)
        floating_point = float_value(int(decimal_copy[1]), base, length)
        # print(f'{integer}, {floating_point}')

        if base == 2:
            return f'{str(integer)}.{str(floating_point)}\u2082'
        elif base == 8:
            return f'{str(integer)}.{str(floating_point)}\u2088'
        elif base == 16:
            return f'{str(integer)}.{str(floating_point)}\u2081\u2086'
        else:
            return f'{str(integer)}.{str(floating_point)}'

def int_value(decimal, base, integer = True):
    answer=[]
    answer_str=''
    counter = 0
    while True:
        if counter == 0:
            newvalue = decimal
            counter+=1
        try:
            answer.insert(0, newvalue%base)
            newvalue = int(newvalue/base)
            # print(f'{answer}, {newvalue}')
        except ValueError:
            print('Try using numbers only in your input')
            exit(0)
        if newvalue == 0:
            for x in answer:
                digit = str(x)
                if base == 16 and x>=10:
                    if x == 10:
                        digit = 'A'
                    elif x == 11:
                        digit = 'B'
                    elif x == 12:
                        digit = 'C'
                    elif x == 13:
                        digit = 'D'
                    elif x == 14:
                        digit = 'E'
                    elif x == 15:
                        digit = 'F'
                answer_str = str(answer_str)+digit
            if integer:
                if base == 2:
                    answer_str = answer_str+'\u2082'
                elif base == 8:
                    answer_str = answer_str+'\u2088'
                elif base == 16:
                    answer_str = answer_str+'\u2081\u2086'
                return answer_str
            else:
                return int(answer_str)

def float_value(decimal, base, length):
    answer=[]
    answer_str=''
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    decimal_iterator = decimal*10**(-1*len(str(decimal)))
    for _ in range(0, length+1):
        answer.insert(0, floor(decimal_iterator*base))
        decimal_iterator = (decimal_iterator*base)%1
        # print(f'{answer}, {decimal_iterator}')
    for x in reversed(answer):
        digit = x
        if base == 16:
            if digit >=10:
                for number in range(10, 16):
                    index = number-10
                    if digit == number:
                        digit=letters[index]
        answer_str = str(answer_str)+str(digit)
    return answer_str


def other_to_decimal(other, base):
    try:
        int(other)
    except ValueError:
        input_list = str(other).split('.')
        integer_aspect = int_value_decimal(input_list[0], base, False)
        float_aspect = float_value_decimal(input_list[1], base)
        return integer_aspect+float_aspect
    else:
        return int_value_decimal(other, base)

def int_value_decimal(input, base, integer = True):
    list_other = reversed(list(str(input)))
    counter = 0
    answer = 0
    digit = 0
    if base <=9:
        for x in list_other:
            try:
                digit = int(x)
            except ValueError:
                print('Try using only numbers in your input')
                exit(0)
            answer+=digit*(base**counter)
            counter+=1
        if integer == True:
            answer = str(answer)+'\u2081\u2080'
        return answer
    elif base == 16:
        for x in list_other:
            if x in ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
                if x == ('A' or 'a'):
                    digit = 10
                elif x == ('B' or 'b'):
                    digit = 11
                elif x == ('C' or 'c'):
                    digit = 12
                elif x == ('D' or 'd'):
                    digit = 13
                elif x == ('E' or 'e'):
                    digit = 14
                elif x == ('F' or 'f'):
                    digit = 15
            else:
                digit = int(x)
            answer+=digit*(16**counter)
            counter+=1
            # print(f'{answer}, {digit}, {counter}')
        if integer == True:
            answer = str(answer)+'\u2081\u2086'
        return answer
    elif base != 16 and base > 9:
        print('Sorry, this calculator does not work with that base.\nPlease try again with a base less than 10')
        exit(0)

def float_value_decimal(float_value, base):
    total_sum = 0
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    float_list = list(float_value)
    if base <=9:
        for power, value in enumerate(float_list):
            total_sum+=value*base**(-1*(power+1))
    elif base == 16:
        for index, values in enumerate(float_list):
            if values in letters.keys:
                for x in letters:
                    if values == x:
                        float_list[index]=letters.get(x)
        for power, value in enumerate(float_list):
            total_sum+=value*base**(-1*(power+1))
    return total_sum

if calc_choice.upper() == 'A':
    print(f'Decimal: {decimal}\nBinary: {decimal_to_other(decimal, 2, decimal_length)}')
elif calc_choice.upper() == 'B':
    print(f'Decimal: {decimal}\nOctal: {decimal_to_other(decimal, 8, decimal_length)}')
elif calc_choice.upper() == 'C':
    print(f'Decimal: {decimal}\nHexadecimal: {decimal_to_other(decimal, 16, decimal_length)}')
elif calc_choice.upper() == 'D':
    print(f'Decimal: {decimal}\nBase {base}: {decimal_to_other(decimal, base, decimal_length)}')
if calc_choice2 != None:
    if calc_choice2.upper() == 'A':
        print(f'Binary: {base_value}\nDecimal: {other_to_decimal(base_value, 2)}')
    elif calc_choice2.upper() == 'B':
        print(f'Octal: {base_value}\nDecimal: {other_to_decimal(base_value, 8)}')
    elif calc_choice2.upper() == 'C':
        print(f'Hexadecimal: {base_value.upper()}\nDecimal: {other_to_decimal(base_value, 16)}')
    elif calc_choice2.upper() == 'D':
        print(f'Base {base2}: {base_value}\nDecimal: {other_to_decimal(base_value, base2)}')
