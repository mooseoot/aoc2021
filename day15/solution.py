from queue import PriorityQueue

#get input

f = open("day15/input.txt", "r")
input = f.read()
f.close()

#parse input into 2d-array

input = input.splitlines()

arr = []

for i in range(5*len(input)):
    row = []
    for y in input[i%len(input)]:
        row.append(int(y))
    full_row = []
    for j in range(5):
        for n in row:
            m = n+j + i//len(input)
            if(m > 9):
                full_row.append(m%10 + 1)
            else:
                full_row.append(m)
    arr.append(full_row)

def to_string(grid):
    for x in grid:
        for y in x:
            print(y, end="")
        print(" ")

#to_string(arr)

#make graph

def make_graph(risk_levels):
    graph = dict()

    for i in range(len(risk_levels)):
        for j in range(len(risk_levels[0])):

            graph[i,j] = []

            if(i != 0):
                graph[i,j].append((-1 + i, j, risk_levels[i-1][j]))
            if(i != len(risk_levels) -1):
                graph[i,j].append((1 + i, j, risk_levels[i+1][j]))
            if(j != 0):
                graph[(i,j)].append(( i, j-1, risk_levels[i][j-1]))
            if(j != len(risk_levels[0])-1):
                graph[i,j].append((i, j+1, risk_levels[i][j+1]))
    
    return graph

# dijkstra's algorithm

def find_shortest_path(graph, start, end):

    distances = {}
    pq = PriorityQueue()
    for k in graph.keys():
        d = 1000000000000000
        distances[k] = d #represents infinite distance
        pq.put((d, k))
    
    distances[start] = 0
    pq.put((0, start))
    pq.get()
    curr_node = start
    min_d = 0

    while end in distances:
        for k in graph[curr_node]:
            if k[:2] in distances:
                dist = distances[curr_node] + k[2]
                if dist < distances[k[:2]]:
                    distances[k[:2]] = dist
                    pq.put((dist, k[:2]))
        min_d = distances.pop(curr_node)

        m = pq.get()
        curr_node = m[1]

    
    return min_d

g = make_graph(arr)

print(find_shortest_path(g, (0,0), (499,499)))





        



