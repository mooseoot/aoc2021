f = open("day7/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.split(",")
positions = []
for x in input:
    positions.append(int(x))

def get_cost(y):
    s = 0
    for x in positions:
        n = int(abs(x - y))
        s += n*(n+1)//2
    return s

def get_min_value():
    inters = []
    positions.sort()
    for i in range(1, len(positions)):
        inters.append(positions[i] - positions[i-1])
    m = min(inters)
    j = inters.index(m)
    y = positions[j] + m//2
    return(get_cost(y))

print(get_min_value())