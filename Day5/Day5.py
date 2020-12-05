maxID = 0
currentID = 0

def calculateSeatID(input:list, rows:int, columns:int):
    #Rows are the first 7 letters
    row = input[:7]
    lower_row = 0
    upper_row = rows - 1

    for r in row:
        if r == 'F':
            upper_row -= (upper_row - lower_row+1)//2
        else:
            lower_row += (upper_row - lower_row+1)//2

    column = input[7:]
    lower_column = 0
    upper_column = columns - 1

    for c in column:
        if c == 'L':
            upper_column -= (upper_column - lower_column + 1)//2
        else:
            lower_column += (upper_column - lower_column + 1)//2
    return 8*upper_row + upper_column


with open('day5.txt') as f:
    data = f.readlines()
    data = [x.rstrip() for x in data]
    seatIDS = []
    for i in data:
        currentID = calculateSeatID(i,128,8)
        #We store all the seatID of the plane
        seatIDS.append(currentID)
        if currentID > maxID:
            maxID = currentID
    
    #We order them to make it easier the empty one
    seatIDS.sort()
    missingID = 0
    for j in range(0,len(seatIDS) - 2):
        #If the next seat minus the current one has a difference of 2 that means we have an empty seat there
        if seatIDS[j+1] - seatIDS[j] == 2:
            missingID = seatIDS[j] + 1
            break
        
    print(f"The max seat ID is {maxID} and your seat ID is {missingID}")
