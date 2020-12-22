input=[16,12,1,0,15,7,11]
times = 30000000
numbers = {}
turn = 0
for w in input:
    #number[id] = (1st appeareance, 2nd appereance)
    turn +=1
    numbers[w] = (turn,-1)
last_num = input[-1]

while turn < times:
    turn += 1
    x, y = numbers[last_num]
    if y == -1:
        last_num = 0
    else:
        last_num = y - x
    
    if last_num not in numbers:
        numbers[last_num] = (turn,-1)
    else:
        x,y = numbers[last_num]
        if y == -1:
            numbers[last_num] = (x,turn)
        else:
            numbers[last_num] = (y,turn)
print(f' The number that appears in the turn {times} is {last_num}')
