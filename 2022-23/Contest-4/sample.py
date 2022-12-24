def count(N: int, string: str):
    array = []
    letters = []
    alphabet = [chr(lttr) for lttr in range(ord('A'), ord('Z')+1)]
    for char in string:
        if char.upper() in alphabet:
            try:
                array.append(char.upper())
                array.sort()
                letters.append(array[N-1])
            except IndexError:
                pass
    return len(list(set(letters)))

def run():
    print('Please type PRACTICE, TEST, or QUIT to proceed.')
    submission = input().upper()

    if submission == 'PRACTICE':
        print('Please choose practice number')
        number = int(input())
        print('RESULT')
        if number == 1:
            return f'{count(2, "Computer")}\nCorrect: {count(2, "Computer")==3}'
        elif number == 2:
            return f'{count(2, "COMPUTER bat")}\nCorrect: {count(2, "COMPUTER bat")==5}'
        elif number == 3:
            return f'{count(3, "COMPUTER")}\nCorrect: {count(3, "COMPUTER")==2}'
        elif number == 4:
            return f'{count(4, "ACSL is fun")}\nCorrect: {count(4, "ACSL is fun")==3}'
        elif number == 5:
            return f'{count(9, "the xylophone")}\nCorrect: {count(9, "the xylophone")==4}'
    elif submission == 'QUIT':
        exit(0)
    elif submission == 'TEST':
        print('Please choose practice number')
        number = int(input())
        print('RESULT')
        if number == 1:
            return f'{count(3, "python")}\nCorrect: {count(3, "python")==4}'
        elif number == 2:
            return f'{count(3, "computers")}\nCorrect: {count(3, "computers")==2}'
        elif number == 3:
            return f'{count(7, "the quick brown fox")}\nCorrect: {count(7, "the quick brown fox")==6}'
        elif number == 4:
            return f'{count(9, "she sells sea shells by the sea shore")}\nCorrect: {count(9, "she sells sea shells by the sea shore")==4}'
        elif number == 5:
            return f'{count(5, "american computer science league")}\nCorrect: {count(5, "american computer science league")==5}'
    else:
        print('Sorry, I didn\'nt understand that.')
        return run()

print(run())
