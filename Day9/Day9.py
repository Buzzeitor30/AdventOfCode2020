data = []
prev = 25
not_found = 0

def find_pairs(input:list,sum:int):
    numbers = {}
    for num in input:
        if num not in numbers:
            numbers[sum-num] = num
        else:
            return True
    return False

def find_set(input:list,num:int):
    numbers = []
    sum_up = 0
    j = 0
    for i in range(0,len(input)):
        while sum_up < num and j<len(input):
            sum_up += input[j]
            numbers.append(input[j])
            j+=1
        if sum_up == num:
            break
        else:
            sum_up -= numbers.pop(0)
    numbers.sort()
    return numbers[0],numbers[-1]
        

with open('Day9.txt') as f:
    data = [x.rstrip() for x in f.readlines()]
    data = list(map(int,data))

previous = data[:prev]

for i in range(prev,len(data)):
    if not(find_pairs(previous,data[i])):
        not_found = data[i]
        break
    previous.pop(0)
    previous.append(data[i])

print(not_found)
x,y = find_set(data,not_found)
print(x+y)