#get input

f = open("day10/inut.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

points = {")": 1, "]": 2, "}": 3, ">": 4}
reverse = {"(": ")", "[": "]", "{": "}", "<": ">"}

def findCorrupt(line):
    stack = []
    for ch in line:
        if ch in points.keys():
            if(reverse[stack.pop()] != ch):
                return 0
        else:
            stack.append(ch)
    p = 0
    while len(stack) > 0:
        p *= 5
        p += points[reverse[stack.pop()]]
    return p
    
s = []

print(findCorrupt("(({"))

for x in input:
    n = findCorrupt(x)
    if (n != 0):
        s.append(n)

s.sort()


print(s[len(s)//2])