def check_palindrome(string: str) -> tuple:
    '''Checks if it is a palindrome'''
    return string == ''.join([char for char in reversed(string)]), len(string)

def longestPalindrome(s: str) -> str:
    longest_palindrome = 1
    palindrome = s[0]
    for i in range(2, len(s)+1):
        for j in range(len(s)-i):
            is_palindrome, length = check_palindrome(s[j:j+i])
            # print(s[j:j+i], is_palindrome, length)
            if is_palindrome and length > longest_palindrome:
                longest_palindrome =  length
                palindrome = s[j:j+i]
    return palindrome

print(longestPalindrome('babad'))
# print(check_palindrome('bab'))