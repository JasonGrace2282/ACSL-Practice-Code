letters = [chr(nums) for nums in range(ord('A'), ord('G')+1)]
letters.pop(3)
print(f'Initial: {letters}')
letters.append('D')
letters.append('G')
print(f'Appended: {letters}')
letters.sort()
print(f'Sorted: {letters}')