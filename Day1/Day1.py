path = 'day.txt'
numbers = {}
x = 0
y = 0
z = 0
with open(path) as f:
    data = f.read().splitlines()
    for num in data:
        var = int(num)
        if var not in numbers:
            numbers[2020-var] = var
        else:
            x = var
            y = numbers[var]
            break
    print("The first year is " + str(x) + " and the second year is  " + str(y) + " Total: " + str(x*y))

    data.sort()

    for i in range(0,len(data) - 2):
        left = i+1
        right = len(data) - 2
        while left < right:
            x = int(data[i])
            y = int(data[left])
            z = int(data[right])
            if ((x+y+z) == 2020):
                print("The first year is " + str(x) + ", the second year is  " + str(y) + " and lastly the third year is " + str(z) + " Total: " + str(x*y*z))
                break
            elif ((x+y+z) < 2020):
                left += 1
            else:
                right -= 1
        

