import itertools
values = {}
data = [x.strip() for x in open('Day14.txt').readlines()]
data = [x.replace(' ','') for x in data]
mask = ''
#PART 1
for val in data:
    i = val.index('=')
    if 'mask' in val:
        #Get mask
        mask = val[i+1:]
    else:
        #Get position where we will store
        pos = int(val[4:i-1])
        #Number to binary
        number = bin(int(val[i+1:]))[2:].zfill(36)
        #Loop through the mask
        for m in range(len(mask)):
            #Replace in the number
            if mask[m] != 'X':
                number = number[:m] + mask[m] + number[m+1:]
        #Get int from binary
        values[pos] = int(number,2)

print(sum(values.values()))

#PART 2
values.clear()
def apply_mask(mask,pose):
    pose = pose
    for m in range(len(mask)):
        if mask[m] == 'X':
            pose = pose[:m] + mask[m] + pose[m+1:]
        else:
            pose = pose[:m] + str(int(mask[m]) | int(pose[m])) + pose[m+1:]
    return pose

def allCombinations(position:str,res:set):
    if 'X' not in position:
        res.add(int(position,2))
        return res
    t0 = position.replace('X','0',1)
    t1 = position.replace('X','1',1)
    allCombinations(t0,res)
    allCombinations(t1,res)

for val in data:
    i = val.index('=')
    if 'mask' in val:
        mask = val[i+1:]
    else:
        #Get position where we will store
        pos = bin(int(val[4:i-1]))[2:].zfill(36)
        #Apply mask
        pos = apply_mask(mask,pos)
        #Number to binary
        number = bin(int(val[i+1:]))[2:].zfill(36)
        positions = set()
        allCombinations(pos,positions)
        for w in positions:
            values[w] = int(number,2)
    
print(sum(values.values()))
