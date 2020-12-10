data = []


def find_diff(data:list):
    data.sort()
    data.insert(0,0)
    data.append(data[-1] + 3)
    diff_1 = 0
    diff_3 = 0
    last = 0
    res = []
    var = []
    for w in data:
        if w - last == 1:
            diff_1 +=1
        elif w - last == 3:
            diff_3 += 1
            res.append(var)
            var = []
        last = w
        var.append(w)
    res[-1].append(w)
    return diff_1,diff_3,res

def create_graph(graph:dict,data:list,visited:dict):
    graph.clear()
    visited.clear()
    for w in data:
        graph[w] = []
        visited[w] = False
        for n in data:
            if n > w:
                if n - w > 3:
                    break
                graph[w].append(n)

def find_path(graph,orig,dest,visited):
    total = 0
    visited[orig] = True
    if orig == dest:
        total = 1
    else:
        for n in graph[orig]:
            if visited[n] == False:
                total += find_path(graph,n,dest,visited)
    
    visited[orig] = False
    return total


def find_all_path(input):
    graph = {}
    visited = {}
    total = 1
    for w in input:
        create_graph(graph,w,visited)
        total *= find_path(graph,w[0],w[-1],visited)
    return total

with open('Day10.txt') as f:
    data = [x.strip() for x in f.readlines()]

data = list(map(int,data))
x, y, sets= find_diff(data)

print(x*y)
print(find_all_path(sets))