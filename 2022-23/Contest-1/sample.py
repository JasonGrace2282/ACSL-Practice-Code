def reverse(value):
    return list(reversed(list(str(value))))

def pos_val(val, pos, left: bool=True):
    if left:
        return int((list(str(val)))[pos-1])
    elif not left:
        return int((reverse(val)[pos-1]))

def operation(N, P, D):
    num = [int(x) for x in reverse(N)]

    if 0<=pos_val(N, P, False)<=4:
        num[P-1]+=D
        num[P-1]=pos_val(num[P-1], 0)
        num.reverse()

        for idx in range(len(num)-P+1, len(num)):
            num[idx]=0

        return int(''.join([str(x) for x in num]))
    elif 5<=pos_val(N, P, False)<=9:
        num[P-1]-=D
        num[P-1]=pos_val(abs(num[P-1]), 1)
        num.reverse()

        for idx in range(len(num)-P+1, len(num)):
            num[idx]=0

        return int(''.join([str(x) for x in num]))
    

print(operation(314159265358, 8, 428))