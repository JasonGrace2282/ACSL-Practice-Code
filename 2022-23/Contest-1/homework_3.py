from functions import Functions

inputs = Functions.text_input('Input: ')
answer = ''
sums = 0

def factor(number):
    factors = []
    for integer in range(1, number):
        if number%integer == 0:
            factors.append(integer)
    return factors

num = factor(int(inputs))

for val in num:
    sums+=int(val)

if sums == int(inputs):
    answer = 'Yes'
elif sums != int(inputs):
    answer = 'No'

print(f'{" ".join([str(x) for x in num])} {answer}')