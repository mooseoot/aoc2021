#get input

f = open("day5/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

lines = []

for x in input:
    line = []
    y = x.split()
    start = y[0]
    start_coord = start.split(",")
    start = (int(start_coord[0]), int(start_coord[1]))

    end = y[2]
    end_coord = end.split(",")
    end = (int(end_coord[0]), int(end_coord[1]))

    line = [start, end]
    lines.append(line)

def get_line_points(line1):
    start = line1[0]

    dx1_full = line1[1][0] - line1[0][0]
    dy1_full = line1[1][1] - line1[0][1]

    # get divisors

    divs = []

    for i in range(1, max(int(abs(dy1_full)), int(abs(dx1_full))) + 2):
        if(dy1_full%i == 0 and dx1_full%i == 0):
            divs.append(i)
    
    gcd = max(divs)

    dx1 = dx1_full//gcd
    dy1 = dy1_full//gcd

    line_ints = set()

    for i in range(gcd + 1):
        x = start[0] + dx1*i
        y = start[1] + dy1*i
        line_ints.add((x,y))
    
    return line_ints


intersections = set()

new_lines = []

for i in range(len(lines)):
    #print(lines[i])
    new_lines.append(get_line_points(lines[i]))


for i in range(len(new_lines)):
    for j in range(i+1, len(new_lines)):
        inter = new_lines[i].intersection(new_lines[j])
        if(len(inter) > 0):
            intersections = intersections.union(inter)

print(len(intersections))


    
