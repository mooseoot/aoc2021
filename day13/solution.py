#get input

f = open("day13/input.txt", "r")
input = f.read()
f.close()

#solution

paper = dict()
instr = []

lines = input.splitlines()

i = 0

while True:
    pair = lines[i].split(",")
    if (len(pair) != 2):
        i += 1
        break
    else:
        paper[(int(pair[0]), int(pair[1]))] = 1
    i += 1

for j in range(i, len(lines)):
    args = lines[j].split()
    arg = args[2].split("=")
    instr.append((arg[0], int(arg[1])))


for inst in instr:

    used_keys = []
    write_keys = []

    if inst[0] == 'x':
        for k in paper.keys():
            if(k[0] >= inst[1]):
                if(k[0] <= 2*inst[1]):
                    write_keys.append((2*inst[1]-k[0], k[1]))
                used_keys.append(k)

    if inst[0] == 'y':
        for k in paper.keys():
            if(k[1] >= inst[1]):
                if(k[1] <= 2*inst[1]):
                    write_keys.append((k[0], 2*inst[1]-k[1]))
                used_keys.append(k)
    
    for k in used_keys:
        paper.pop(k)
    for k in write_keys:
        paper[k] = 1

def draw_paper(paper):
    Xs = []
    Ys = []

    for k in paper.keys():
        Xs.append(k[0])
        Ys.append(k[1])
    
    minx = min(Xs)
    maxx = max(Xs)
    miny = min(Ys)
    maxy = max(Ys)

    row = ""

    for i in range(miny, maxy + 1):
        for j in range(minx, maxx+1):
            if((j,i) in paper.keys()):
                row += "#"
            else:
                row += "."
        print(row)
        row = ""

draw_paper(paper)
        


    

    
    