def substringLength(substring: str):
    length = 0
    letters = []
    for char in substring:
        if char not in letters:
            length+=1
            letters.append(char)
        else:
            return length
    return length

def lengthOfLongestSubstring(s: str) -> int:
    longest_len = 0
    for index in range(len(s)+1):
        length = substringLength(s[index:])
        if length > longest_len:
            longest_len = length
    return longest_len

print(lengthOfLongestSubstring(s="abcabcbb"))