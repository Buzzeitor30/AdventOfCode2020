import math
from functools import reduce
data = [x.strip() for x in open('Day13.txt').readlines()]
timestamp = int(data.pop(0))

data = ''.join(data)

orig = data.split(',')
#PART 1
data = [int(x) for x in data.split(',') if x != 'x']
time = [x*math.ceil(timestamp/x) for x in data]
next_time_bus = min(time)
bus_id = data[time.index(next_time_bus)]
total = (next_time_bus - timestamp)*bus_id

#PART 2
#x mod n1 = a1

#Get a1
def find_rest(input:list,orig:list):
    rest = []
    for n in range(len(input)):
        if n!=0:
            #In case MOD operation is negative
            var = ((input[n] - orig.index(str(data[n]))) % input[n] + input[n]) % input[n]
            rest.append(var)
        else:
            rest.append(0)
    return rest

a1 = find_rest(data,orig)
N = math.prod(data)
n = data.copy()

def chineseRemainder(n, N, a):
    result = 0
    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = N // ni
        #Since we have a to sum it up all
        result += ai * bi * invmod(bi,ni)
    #Get mod of result
    return result % N

def ExtendedEuclid(x, y):
    #Euclides algorithm to determine gcd
    x0, x1, y0, y1 = 1, 0, 0, 1    
    while y > 0:
        q, x, y = math.floor(x / y), y, x % y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0

#Find inverse
def invmod(a, m):
    x,y = ExtendedEuclid(a, m)
    return x % m

print(chineseRemainder(n,N,a1))