#get input

f = open("day8/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

outputs_str = []

for x in input:
    outputs_str.append((x.split("|")[1].split()))

outputs_set = []

for x in outputs_str:
    row = []
    for y in x:
        word = []
        for char in y:
            word.append(char)
        row.append(set(word))
    outputs_set.append(row)

inputs_str = []

for x in input:
    inputs_str.append((x.split("|")[0].split()))

inputs_set = []

for x in inputs_str:
    row = []
    for y in x:
        word = []
        for char in y:
            word.append(char)
        row.append(set(word))
    inputs_set.append(row)

def getDigit(one, four, seven, eight, x):
    if(x == one):
        return 1
    if(x == four):
        return 4
    if(x == seven):
        return 7
    if(x == eight):
        return 8
    
    if(len(x) == 5):
        if(one.issubset(x)):
            return 3
        if(len(four.intersection(x)) == 3):
            return 5
        return 2
    
    if(len(x) == 6):
        if(not one.issubset(x)):
            return 6
        if(four.issubset(x)):
            return 9
        return 0



def solveRow(rowInputs, rowOutputs):
    one = None
    four = None
    seven = None
    eight = None

    for x in rowInputs:
        if(len(x) == 2):
            one = x
        elif(len(x) == 4):
            four = x
        elif(len(x) == 3):
            seven = x 
        elif(len(x) == 7):
            eight = x
    s = 0
    for i in range(len(rowOutputs)):
        s += getDigit(one, four, seven, eight, rowOutputs[i])*10**(3-i)
    return s

somme = 0

for i in range(len(inputs_set)):
    somme += solveRow(inputs_set[i], outputs_set[i])

print(somme)




