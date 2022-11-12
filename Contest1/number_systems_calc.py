print('Welcome to the ACSL Contest 1 Calculator!\nPlease type the letter of which function you would like to use.\
    \nA)Decimal to Binary\nB)Decimal to Octal\nC)Decimal to Hexadecimal\nD)Decimal to Custom Base\nE)Other bases to Decimal')
calc_choice = (input('Choose: ')).split('Choose: ')[0]
print(f'You have chosen letter {calc_choice.upper()}')
if calc_choice.upper() not in ['D', 'E']:
    decimal = int((input('Input your decimal integer: ')).split('Input your decimal integer: ')[0])
    decimal_str=str(decimal)+u'\u2081\u2080'
    calc_choice2 = None
elif calc_choice.upper() == 'D':
    print('WARNING: This calculator does not work with custom bases greater than 9 or less than 1')
    base = int((input('Base: ')).split('Base: ')[0])
    decimal = int((input('Input your decimal integer: ')).split('Input your decimal integer: ')[0])
    calc_choice2 = None
elif calc_choice.upper() == 'E':
    print('Welcome to the convert to decimal calculator. \nPlease type the letter of the option you would like to choose\
        \nA)Binary to Decimal\nB)Octal to Decimal\nC)Hexadecimal to Decimal\nD)Custom base to Decimal')
    calc_choice2 = (input('Choose: ')).split('Choose: ')[0]
    print(f'You have chosen letter {calc_choice2.upper()}')
    if calc_choice2.upper() == 'A':
        base_value = int((input('Input your Binary integer: ')).split('Input your Binary integer: ')[0])
    elif calc_choice2.upper() == 'B':
        base_value = int((input('Input your Octal integer: ')).split('Input your Octal integer: ')[0])
    elif calc_choice2.upper() == 'C':
        base_value = (input('Input your Hexadecimal integer: ')).split('Input your Hexadecimal integer: ')[0]
    elif calc_choice2.upper() == 'D':
        print('WARNING: This calculator does not work with custom bases greater than 9 or less than 1')
        base2 = int((input('Base: ')).split('Base: ')[0])
        base_value = int((input(f'Input your Base {base2} integer: ')).split(f'Input your Base {base2} integer: ')[0])

def decimal_to_other(decimal, base):
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
                if base == 16:
                    if 10<=x<=15:
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
            if base == 2:
                answer_str = answer_str+u'\u2082'
            elif base == 8:
                answer_str = answer_str+u'\u2088'
            elif base == 16:
                answer_str = answer_str+u'\u2081\u2086'
            return answer_str

def other_to_decimal(other, base):
    list_other = reversed(list(str(other)))
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
        answer = str(answer)+u'\u2081\u2080'
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
        answer = str(answer)+u'\u2081\u2086'
        return answer
    elif base != 16 and base > 9:
        print('Sorry, this calculator does not work with that base.\nPlease try again with a base less than 10')
        exit(0)


if calc_choice.upper() == 'A':
    print(f'Decimal: {decimal_str}\nBinary: {decimal_to_other(decimal, 2)}')
elif calc_choice.upper() == 'B':
    print(f'Decimal: {decimal}\nOctal: {decimal_to_other(decimal, 8)}')
elif calc_choice.upper() == 'C':
    print(f'Decimal: {decimal}\nHexadecimal: {decimal_to_other(decimal, 16)}')
elif calc_choice.upper() == 'D':
    print(f'Decimal: {decimal}\nBase {base}: {decimal_to_other(decimal, base)}')
if calc_choice2 != None:
    if calc_choice2.upper() == 'A':
        print(f'Binary: {base_value}\nDecimal: {other_to_decimal(base_value, 2)}')
    elif calc_choice2.upper() == 'B':
        print(f'Octal: {base_value}\nDecimal: {other_to_decimal(base_value, 8)}')
    elif calc_choice2.upper() == 'C':
        print(f'Hexadecimal: {base_value.upper()}\nDecimal: {other_to_decimal(base_value, 16)}')
    elif calc_choice2.upper() == 'D':
        print(f'Base {base2}: {base_value}\nDecimal: {other_to_decimal(base_value, base2)}')
