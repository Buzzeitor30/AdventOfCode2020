import re
data = []
visited_inst = set()
with open('Day8.txt') as f:
    data = [x.replace(' ','').rstrip() for x in f.readlines()]

#Part 1

def end_accumulator(data:list,visited_inst):
    visited_inst.clear()
    current_inst = 0
    accumulator = 0
    while current_inst not in visited_inst and current_inst < len(data):
        visited_inst.add(current_inst)
        var = data[current_inst]
        if 'acc' in var:
            accumulator += int(var[3:])
            current_inst += 1
        elif 'jmp' in var:
            current_inst += int(var[3:])
        else:
            current_inst += 1
    return current_inst,accumulator

print(end_accumulator(data,visited_inst)[1])
acc = 0
data2 = []
#Part 2
for w in range(0,len(data)):
    data2 = data.copy()
    var = data2[w]
    if 'jmp' in var:
        data2[w] = data[w].replace('jmp','nop')
    elif 'nop' in var:
        data2[w] = data[w].replace('nop','jmp')
    condition,acc = end_accumulator(data2,visited_inst)
    if condition not in visited_inst:
        break

print(acc)

    


