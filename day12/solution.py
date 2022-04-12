#get input

f = open("day12/input.txt", "r")
input = f.read()
f.close()

#parse input

graph = dict()

input = input.splitlines()

for x in input:
    y = x.split("-")
    if y[0] in graph.keys():
        graph[y[0]].append(y[1])
    else:
        graph[y[0]] = [y[1]]
    if y[1] in graph.keys():
        graph[y[1]].append(y[0])
    else:
        graph[y[1]] = [y[0]]

#solution

def countPaths(node, prevs, doubled):
    if(node == "end"):
        return 1
    
    paths = []

    for x in graph[node]:
        if(not doubled):
            if(x not in prevs or x == x.upper()):
                paths.append(countPaths(x, prevs + [node], False))
            elif(x != "start"):
                paths.append(countPaths(x, prevs + [node], True))
        if (doubled):
            if(x not in prevs or x == x.upper()):
                paths.append(countPaths(x, prevs + [node], True))
    return sum(paths)

print(countPaths("start", [], False))
