print('Welcome to the decimal to binary calculator!')
decimal = int((input('To start, input your decimal integer: ')).split('To start, input your decimal integer: ')[0])
decimal_str=str(decimal)+u'\u2081\u2080'

def decimal_to_binary(decimal):
    answer=[]
    binary2=''
    counter = 0
    while True:
        if counter == 0:
            newvalue = decimal
            counter+=1
        answer.insert(0, newvalue%2)
        newvalue = int(newvalue/2)
        # print(f'{answer}, {newvalue}')
        if newvalue == 0:
            for x in answer:
                binary2 = str(binary2)+str(x)
            binary2 = binary2+u'\u2082'
            return binary2

print(f'Decimal: {decimal_str}\nBinary: {decimal_to_binary(decimal)}')