from functions import Functions


def code(code_input = None):
    output = None
    final_output = ''

    if code_input is None:
        input_value = Functions.text_input('Please input a value or type \'Quit\': ')
        if input_value.upper() in ['QUIT', 'QUIT()']:
            exit(0)
        input_value = input_value.split(' ')
    elif code_input is not None:
        input_value = code_input
    print('Choose whether to calculate by using a function, or reversing the list')
    how = (Functions.text_input('Type \"Swap\", \"Function\" or \"Quit\": ')).upper()

    for idx, value in enumerate(input_value):
        input_value[idx] = list(str(value))
        input_value[idx] = list(map(int, input_value[idx]))

        # Evaluate [0,1,2,3] by adding 5 and finding the modulus of that and 10. Gives list in the form of [a,b,c,d]
        for index, value in enumerate(input_value[idx]):
            input_value[idx][index] = str((int(value)+5)%10)
            # print(f'{value}, {index}')
        
        # Swap [a,b,c,d] to get [d,c,b,a]
        if how=='FUNCTION':
            input_value[idx] = Functions.swap(Functions.swap(input_value[idx], 0), 1, 2)
            input_value[idx] = ''.join(input_value[idx])
            output = ' '.join(input_value)
        if how=='SWAP':
            input_value[idx]=reversed(input_value[idx])
            for val in input_value[idx]:
                if output is not None:
                    output = f'{output}{val}'
                else:
                    output = f'{val}'
                # print(f'Output: {output}')
            input_value[idx] = output
            output = ''
        elif how in ['QUIT', 'QUIT()']:
            exit(0)
        else:
            print('Sorry, try typing Swap, Function, or Quit.')
            return code(input_value)

    # print(f'Input_value list: {input_value}')
    if how == 'SWAP':
        final_output = ' '.join(input_value)
        return f'Output: {final_output}'
    elif how == 'FUNCTION':
        return output

print(code())