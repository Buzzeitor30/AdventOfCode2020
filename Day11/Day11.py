data = [x.strip() for x in open('Day11.txt').readlines()]
last = {}
current = {(x,y):data[x][y] for x in range(len(data)) for y in range(len(data[x])) if data[x][y] != '.'}
len_rows = len(data)
len_columns = len(data[0])

def howCorrect(input:dict):
    correct = 0
    for k in current:
        if current[k] == '#':
            correct += 1
    return correct

def apply_all_rules(input:dict):
    res = {}
    for k in input:
        row,column = k
        var = 0
        var += check_diagonal(input,row,column)
        var += check_horizontal(input,row,column)
        var += check_vertical(input,row,column)
        if var == 0:
            res[(row,column)] = '#'
        elif var >= 5:
            res[(row,column)] = 'L'
        else:
            res[(row,column)] = input[(row,column)]
    return res

def check_diagonal(input,x,y):
    i,j = x - 1,y + 1
    total = 0
    while i > -1 and j < len_columns:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i -= 1
        j += 1

    i, j = x+1,y-1
    while i < len_rows and j > -1:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i += 1
        j -= 1
 
    i, j = x-1,y-1       
    while i > -1 and j > -1:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i -= 1
        j -= 1
    
    i, j = x+1,y+1
    while i < len_rows and j < len_columns:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i += 1
        j += 1
    return total

def check_vertical(input,x,y):
    i, j = x, y - 1
    total = 0
    while j > -1:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        j -= 1
    j = y+1
    while j < len_columns:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        j += 1
    return total

def check_horizontal(input,x,y):
    i, j = x-1, y
    total = 0
    while i > -1:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i -= 1
    i = x+1
    while i < len_rows:
        if input.get((i,j),'.') == '#':
            total += 1
            break
        elif input.get((i,j),'.') == 'L':
            break
        i += 1
    return total

def apply_rules(input:dict):
    res = {}
    for k in input:
        count = 0
        row,column = k
        for i in range(row-1,row+2):
            for j in range(column-1,column+2):
                if i != row or j!=column:
                    if input.get((i,j),'.') == '#':
                        count += 1
        if count == 0:
            res[(row,column)] = '#'
        elif count >= 4:
            res[(row,column)] = 'L'
        else:
            res[(row,column)] = input[(row,column)]  
    return res

while last != current:
    last = current.copy()
    current = apply_rules(current)

correct = howCorrect(current)
print(f'There are {correct} people seated')

last.clear()
current = {(x,y):data[x][y] for x in range(len(data)) for y in range(len(data[x])) if data[x][y] != '.'}
while last != current:
    last = current.copy()
    current = apply_all_rules(current)
correct = howCorrect(current)
print(f'There are {correct} people seated')