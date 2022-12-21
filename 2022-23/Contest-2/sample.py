def remove_punc(words: list):
    '''Removes punctuation from strings inside list. Returns updated list'''
    punctuation = '~!@#$%^&*()`\';:"<>,.?/\\_+-={}[]'
    for position, string in enumerate(words):
        text = list(string)
        for ele in text:
            if ele in punctuation:
                text.remove(ele)
        words[position]=''.join(text)
    return words

def unique_letters(uppercase: str):
    '''Counts the amount of unique letters in input, and returns it. Input must be UPPERCASE'''
    letters = [(chr(letter)) for letter in range(ord('A'), ord('Z')+1)]
    letter_counter = 0
    for letter in letters:
        if letter in list(uppercase):
            letter_counter+=1
    return letter_counter

def vowels(uppercase: str):
    '''Counts the amount of vowels in input, and returns it. Input must be UPPERCASE'''
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_counter = 0
    for char in list(uppercase):
        if char in vowels:
            vowel_counter+=1
    return vowel_counter

def uppercase_letters(sentence: str):
    '''Counts the number of uppercase letters in a string'''
    letters = [(chr(letter)) for letter in range(ord('A'), ord('Z')+1)]
    uppercase_counter = 0
    for character in sentence:
        if character in letters:
            uppercase_counter+=1
    return uppercase_counter

def frequency(uppercase: str):
    '''Finds the amount of times the most frequent letter appears.'''
    letters = [(chr(letter)) for letter in range(ord('A'), ord('Z')+1)]
    frequent_letter_count = 0
    for letr in letters:
        if uppercase.count(letr)>frequent_letter_count:
            frequent_letter_count = uppercase.count(letr)
    return frequent_letter_count

def longest_word(sentence: str):
    '''Returns the longest word in a sentence'''
    words = remove_punc(sentence.split(' '))
    longest_word = words[[int(indx) for indx, item in enumerate(words) if len(item) == max([len(word) for word in words])][0]]
    return longest_word

def code(sentence: str):
    '''Formats output. 1. Unique Letters, 2. Vowels, 3. Uppercase Letters, 4. Most Common Letter's Frequency, and 5. Longest Word'''
    uppercase = sentence.upper()
    return f'1. {unique_letters(uppercase)}\n2. {vowels(uppercase)}\n3. {uppercase_letters(sentence)}\n4. {frequency(uppercase)}\n5. {longest_word(sentence)}'

def execute():
    print('Please type either \'Sample\' or \'Test\', \'Custom\', or type \'Quit\'.')
    answer = input().upper()
    if answer == 'SAMPLE':
        return code('The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.')
    elif answer == 'TEST':
        return code('The 2019 All-Star Competition is at Wayne Hills HS in Wayne, New Jersey.')
    elif answer == 'CUSTOM':
        print('Please type your sentence.')
        return code(input())
    elif answer == 'QUIT':
        exit(0)
    else:
        print('Sorry, I didn\'t understand that')
        return execute()

print(execute())
