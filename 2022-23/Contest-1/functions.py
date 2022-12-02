class Functions:
    def text_input(text):
        '''Put text in input() method and get only user input.'''
        return str(((input(text)).split(text))[0])
    def swap(lists, pos1, pos2=-1):
        '''Swaps values in a list and returns it.'''
        value1, value2 = [lists.pop(pos1), lists.pop(pos2)]
        lists.insert(pos1, value2) 
        lists.insert(pos2, value1) 
        return lists
    def int_list(input_list):
        '''Takes an integer list and coverts it to a string list'''
        return [str(x) for x in input_list]
    def factor(number):
        factors = []
        for integer in range(1, number):
            if number%integer == 0:
                factors.append(integer)
        return factors