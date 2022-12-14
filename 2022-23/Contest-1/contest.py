def list_val(lists, val, add=0):
    '''Returns digit at place value. Digit location counted from left to right'''
    return int(list(str(lists))[val])+add

def list_sum(list: list):
    '''Sums up the values inside of a list with list elements'''
    sum = 0
    for x in list:
        for y in x:
            sum+=y
    return sum

def findDigitSum(num, base, start):
    numbers = []

    if start < 10:
        counter = start-1
        tens = 0
        hundreds = 0
        thousands = 0
        ten_thousands = 0
        hundred_thousands = 0
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 100 > start >= 10:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 0)
        thousands = 0
        hundreds = 0
        ten_thousands = 0
        hundred_thousands = 0
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 1000 > start >= 100:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 1)
        hundreds = list_val(start, 0)
        thousands = 0
        ten_thousands = 0
        hundred_thousands = 0
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 10_000 > start >= 1000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 2)
        hundreds = list_val(start, 1)
        thousands = list_val(start, 0)
        ten_thousands = 0
        hundred_thousands = 0
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 100_000 > start >= 10_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 3)
        hundreds = list_val(start, 2)
        thousands = list_val(start, 1)
        ten_thousands = list_val(start, 0)
        hundred_thousands = 0
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 1_000_000 > start >= 100_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 4)
        hundreds = list_val(start, 3)
        thousands = list_val(start, 2)
        ten_thousands = list_val(start, 1)
        hundred_thousands = list_val(start, 0)
        millions = 0
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 10_000_000 > start >= 1_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 5)
        hundreds = list_val(start, 4)
        thousands = list_val(start, 3)
        ten_thousands = list_val(start, 2)
        hundred_thousands = list_val(start, 1)
        millions = list_val(start, 0)
        ten_millions = 0
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 100_000_000 > start >= 10_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 6)
        hundreds = list_val(start, 5)
        thousands = list_val(start, 4)
        ten_thousands = list_val(start, 3)
        hundred_thousands = list_val(start, 2)
        millions = list_val(start, 1)
        ten_millions = list_val(start, 0)
        hundred_millions = 0
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 1_000_000_000 > start >= 100_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 7)
        hundreds = list_val(start, 6)
        thousands = list_val(start, 5)
        ten_thousands = list_val(start, 4)
        hundred_thousands = list_val(start, 3)
        millions = list_val(start, 2)
        ten_millions = list_val(start, 1)
        hundred_millions = list_val(start, 0)
        billions = 0
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 10_000_000_000 > start >= 100_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 8)
        hundreds = list_val(start, 7)
        thousands = list_val(start, 6)
        ten_thousands = list_val(start, 5)
        hundred_thousands = list_val(start, 4)
        millions = list_val(start, 3)
        ten_millions = list_val(start, 2)
        hundred_millions = list_val(start, 1)
        billions = list_val(start, 0)
        ten_billions = 0
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 100_000_000_000 > start >= 1_000_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 9)
        hundreds = list_val(start, 8)
        thousands = list_val(start, 7)
        ten_thousands = list_val(start, 6)
        hundred_thousands = list_val(start, 5)
        millions = list_val(start, 4)
        ten_millions = list_val(start, 3)
        hundred_millions = list_val(start, 2)
        billions = list_val(start, 1)
        ten_billions = list_val(start, 0)
        hundred_billions = 0
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 1_000_000_000_000 > start >= 10_000_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 10)
        hundreds = list_val(start, 9)
        thousands = list_val(start, 8)
        ten_thousands = list_val(start, 7)
        hundred_thousands = list_val(start, 6)
        millions = list_val(start, 5)
        ten_millions = list_val(start, 4)
        hundred_millions = list_val(start, 3)
        billions = list_val(start, 2)
        ten_billions = list_val(start, 1)
        hundred_billions = list_val(start, 0)
        trillions = 0
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 10_000_000_000_000 > start >= 100_000_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 11)
        hundreds = list_val(start, 10)
        thousands = list_val(start, 9)
        ten_thousands = list_val(start, 8)
        hundred_thousands = list_val(start, 7)
        millions = list_val(start, 6)
        ten_millions = list_val(start, 5)
        hundred_millions = list_val(start, 4)
        billions = list_val(start, 3)
        ten_billions = list_val(start, 2)
        hundred_billions = list_val(start, 1)
        trillions = list_val(start, 0)
        ten_trillions = 0
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 100_000_000_000_000 > start >= 1_000_000_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 12)
        hundreds = list_val(start, 11)
        thousands = list_val(start, 10)
        ten_thousands = list_val(start, 9)
        hundred_thousands = list_val(start, 8)
        millions = list_val(start, 7)
        ten_millions = list_val(start, 6)
        hundred_millions = list_val(start, 5)
        billions = list_val(start, 4)
        ten_billions = list_val(start, 3)
        hundred_billions = list_val(start, 2)
        trillions = list_val(start, 1)
        ten_trillions = list_val(start, 0)
        hundred_trillions = 0
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    elif 1_000_000_000_000_000 > start >= 10_000_000_000_000:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 13)
        hundreds = list_val(start, 12)
        thousands = list_val(start, 11)
        ten_thousands = list_val(start, 10)
        hundred_thousands = list_val(start, 9)
        millions = list_val(start, 8)
        ten_millions = list_val(start, 7)
        hundred_millions = list_val(start, 6)
        billions = list_val(start, 5)
        ten_billions = list_val(start, 4)
        hundred_billions = list_val(start, 3)
        trillions = list_val(start, 2)
        ten_trillions = list_val(start, 1)
        hundred_trillions = list_val(start, 0)
        quadrillions = 0
        ten_quadrillions = 0
        hundred_quadrillions = 0
    else:
        counter = list_val(start, -1, -1)
        tens = list_val(start, 14)
        hundreds = list_val(start, 13)
        thousands = list_val(start, 12)
        ten_thousands = list_val(start, 11)
        hundred_thousands = list_val(start, 10)
        millions = list_val(start, 9)
        ten_millions = list_val(start, 8)
        hundred_millions = list_val(start, 7)
        billions = list_val(start, 6)
        ten_billions = list_val(start, 5)
        hundred_billions = list_val(start, 4)
        trillions = list_val(start, 3)
        ten_trillions = list_val(start, 2)
        hundred_trillions = list_val(start, 1)
        quadrillions = list_val(start, 0)
        ten_quadrillions = 0
        hundred_quadrillions = 0

    for _ in range(num):
        counter+=1
        if counter>=base:
            tens+=1
            counter = 0
        if tens>=base:
            hundreds+=1
            tens = 0
        if hundreds>=base:
            thousands+=1
            hundreds = 0
        if thousands>=base:
            ten_thousands+=1
            thousands = 0
        if ten_thousands>=base:
            hundred_thousands+=1
            ten_thousands = 0
        if hundred_thousands>=base:
            millions+=1
            hundred_thousands = 0
        if millions>=base:
            ten_millions+=1
            millions = 0
        if ten_millions>=base:
            hundred_millions+=1
            ten_millions = 0
        if hundred_millions>=base:
            billions+=1
            hundred_millions = 0
        if billions>=base:
            ten_billions+=1
            billions = 0
        if ten_billions>=base:
            hundred_billions+=1
            ten_billions = 0
        if hundred_billions>=base:
            trillions+=1
            hundred_billions = 0
        if trillions>=base:
            ten_trillions+=1
            trillions = 0
        if ten_trillions>=base:
            hundred_trillions+=1
            ten_trillions = 0
        if hundred_trillions>=base:
            quadrillions+=1
            hundred_trillions = 0
        if quadrillions>=base:
            ten_quadrillions+=1
            quadrillions = 0
        if ten_quadrillions>=base:
            hundred_quadrillions+=1
            ten_quadrillions = 0
        numbers.append([hundred_quadrillions, ten_quadrillions, quadrillions, ten_trillions, trillions, hundred_billions, ten_billions, billions, hundred_millions, \
            ten_millions, millions, hundred_thousands, ten_thousands, thousands, hundreds, tens, counter])

    return list_sum(numbers)

print(findDigitSum(15, 8, 2))