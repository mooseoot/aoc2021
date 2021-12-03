#get input

f = open("day2/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

values = []

for x in input:
    arg = x.split()
    values.append((arg[0], int(arg[1])))

depth = 0
hor = 0

for x in values:
    if x[0] == "forward":
        hor += x[1]
    if x[0] == "up":
        depth -= x[1]
    if x[0] == "down":
        depth += x[1]

print(depth*hor)