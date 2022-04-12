#get input

f = open("day9/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

for i in range(len(input)):
    row = []
    for char in input[i]:
        row.append(int(char))
    input[i] = row


def detect_low(i, j, grid):
    checks = []
    if(i != 0):
        checks.append((-1 + i, j))
    if(i != len(grid) -1):
        checks.append((1+i, j))
    if(j != 0):
        checks.append((i, j-1))
    if(j != len(grid[0])-1):
        checks.append((i, 1+j))
    
    for x in checks:
        if(grid[x[0]][x[1]] <= grid[i][j]):
            return False
    
    return True

def getAdjecentBasinNodes(i, j, grid):
    nodes = []
    checks = []
    if(i != 0):
        checks.append((-1 + i, j))
    if(i != len(grid) -1):
        checks.append((1+i, j))
    if(j != 0):
        checks.append((i, j-1))
    if(j != len(grid[0])-1):
        checks.append((i, 1+j))
    
    for x in checks:
        if(grid[x[0]][x[1]] >= grid[i][j] and grid[x[0]][x[1]] != 9):
            nodes.append(x)
    return nodes

def getBasin(i, j, grid):
    nodes = getAdjecentBasinNodes(i,j,grid)
    visited = set()
    visited.add((i,j))

    while len(nodes) > 0:
        node = nodes.pop()
        if node in visited:
            pass
        else:
            visited.add(node)
            nodes = getAdjecentBasinNodes(node[0], node[1], grid) + nodes

    return visited
        
    

low_points = []

for i in range(len(input)):
    for j in range(len(input[0])):
        if(detect_low(i,j,input)):
            low_points.append((i,j))

basins = []

for x in low_points:
    basin = getBasin(x[0], x[1], input)
    flag = True
    for y in basins:
        if basin == y:
            flag = False
    if(flag):
        basins.append(basin)

for i in range(len(basins)):
    basins[i] = len(basins[i])

basins.sort()

n = len(basins)

print(basins[n-3]*basins[n-2]*basins[n-1])


