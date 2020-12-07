import re
possible_way = 0
graph = {}
edges = {}

important_bag = 'shiny gold bag'

def find_path(graph, origin, dest, path = []):
    path = path + [origin]
    if origin == dest:
        return path
    for n in graph[origin]:
        newpath = find_path(graph,n,dest,path)
        if newpath:
            return newpath

def find_path_all(graph,important_bag=important_bag):
    total = 0
    for node in graph:
        if node != important_bag:
            if find_path(graph,node,important_bag):
                total +=1
    return total

def find_total_nodes(graph,origin=important_bag):
    total = 0
    for n in graph[origin]:
        total += edges[origin,n] + edges[origin,n]*find_total_nodes(graph,n)
    return total

with open('Day7.txt') as f:
    data = [x.strip() for x in f.readlines()]
    #We create the graph with all the bags
    for bag in data:
        var = re.findall(r'[a-z]+\s[a-z]+\sbag',bag)
        times = re.findall(r'\d',bag)
        graph[var[0]] = []
        if 'no other bag' not in var:
            graph[var[0]] = var[1:]
            for t in range(0,len(times)):
                edges[(var[0], var[t+1])] = int(times[t])
    
    print(find_path_all(graph))
    print(find_total_nodes(graph))
