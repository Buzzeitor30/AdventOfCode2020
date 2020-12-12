input = [x.strip() for x in open('Day12.txt').readlines()]

def part2(input):
    position = [0,0]
    waypoint = [10,1]
    for m in input:
        mov = m[0]
        t = int(m[1:])
        if mov == 'R':
            t = t//90
            while t > 0:
                waypoint = [waypoint[1],waypoint[0]*-1]
                t -= 1
        elif mov == 'L':
            t = t//90
            while t > 0:
                waypoint = [waypoint[1]*-1,waypoint[0]]
                t-=1
        elif mov == 'E':
            waypoint[0] += t
        elif mov == 'W':
            waypoint[0] -= t
        elif mov == 'S':
            waypoint[1] -= t
        elif mov == 'N':
            waypoint[1] += t
        else:
            position[0] += waypoint[0] * t
            position[1] += waypoint[1] * t
    return position

manhattan =  sum([abs(x) for x in part2(input)])
print(f'Manhattan distance with waypoint is {manhattan}')