#get input

f = open("day11/input.txt", "r")
input = f.read()
f.close()

octos = []

input = input.splitlines()

for x in input:
    row =[]
    for ch in x:
        row.append(int(ch))
    octos.append(row)

flashes = [0]

def getAdjacent(i,j,grid):
    checks = [(i+1,j), (i,j+1), (i+1,j+1), (i-1, j-1), (i, j-1), (i-1, j), (i+1, j-1), (i-1, j+1)]
    filtered = []

    for i in range(len(checks)):
        if(0 <= checks[i][0] < len(grid) and 0 <= checks[i][1] <  len(grid[0])):
            filtered.append(checks[i])    
    return filtered

def updateOcto(i,j, grid, flashes):
    flashes[0] += 1
    grid[i][j] = 0
    adj = getAdjacent(i,j,grid)
    for x in adj:
        if grid[x[0]][x[1]] != 0:
            grid[x[0]][x[1]] += 1
    for x in adj:
        if(grid[x[0]][x[1]] > 9):
            updateOcto(x[0], x[1], grid, flashes)
        

def step(octos, flashes):
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            octos[i][j] += 1
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            if octos[i][j] > 9:
                updateOcto(i,j,octos, flashes)

n = 0
flag = True

while flag:
    step(octos, flashes)
    flag2 = False
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            flag2 = flag2 or (octos[i][j] != 0)
    flag = flag2
    n += 1
    print(octos)

print(n)
            



    
    




