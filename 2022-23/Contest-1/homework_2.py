print('Please input a value')
input_value = input()
print('Type 0 or 1')
boolean = input()
input_value = input_value.split(' ')

def swap(lists, pos1, pos2=-1):
    print(f'{lists}, {pos1}, {pos2}')
    value1 = lists.pop(pos1)  
    value2 = lists.pop(pos2)
    lists.insert(pos1, value2) 
    lists.insert(pos2, value1) 
    print(f'After Swap: {lists}, {pos1}, {pos2}')
    return lists

## Evaluate [[0,1,2,3]. [5,8,9,0]]
for idx, x in enumerate(input_value):
    input_value[idx] = list(str(x))
    input_value[idx] = list(map(int, input_value[idx]))

    ## Evaluate [0,1,2,3] by adding 5 and divinding by 10 to get remainder which will give [a,b,c,d]
    for index, value in enumerate(input_value[idx]):
        input_value[idx][index] = (int(value)+5)%10
        print(f'{value}, {index}')
    
   ## Swap [a,b,c,d] to get [d,c,b,a]
    if int(boolean)==0:
        index2=0
        input_value[idx] = swap(swap(input_value[idx], index2), index2+1, index2+2)
        output = input_value
    if int(boolean)==1:
        input_value[idx]=reversed(input_value[idx])
print(output)



    

