def units_digit(num: int | str):
    return str(num)[-1]

def number_transformation(N, P):
    number = list(str(N))
    digit = int(number[-P])
    for idx, char in enumerate(number):
        if idx == len(number)-P: # Ignores Pth Digit
            continue
        elif idx < len(number)-P: # Takes the unit digit of the sum of char and digit
            number[idx]=units_digit(int(char)+digit)
        elif idx > len(number)-P:
            number[idx]=str(abs(int(char)-digit))
    return int(''.join(number))

print(f'{number_transformation(296351, 5)} is {"CORRECT" if number_transformation(296351, 5)==193648 else "INCORRECT"}')