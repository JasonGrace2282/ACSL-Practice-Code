def reverse(x: int):
    reverse_x = int(''.join([dgt for dgt in reversed(str(x)) if dgt != '-']))
    return reverse_x.bit_length()

print(reverse(1563847412))