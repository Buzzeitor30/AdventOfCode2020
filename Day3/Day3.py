total = 1
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
with open('day3.txt') as f:
    content = f.readlines()
    #Get each line without \n character
    content = [x.strip() for x in content]
    #How wide is the grid is determined from the len of the first
    wide = len(content[0])
    #We loop through the slopes
    for i in slopes:
        moveX = i[0]
        moveY = i[1]
        #First movement to begin
        x = moveX
        y = moveY
        #trees found
        encounter = 0
        while y < len(content):
            #if we found a tree update counter
            if content[y][x%wide] == '#':
                encounter += 1
            #update positions
            x += moveX
            y += moveY
        #multiply and add it 
        total *= encounter
    print(total)
    