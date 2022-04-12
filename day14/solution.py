#get input

f = open("day14/input.txt", "r")
input = f.read()
f.close()

#parse input

rules = {}
pairs = {}
counts = {}

input = input.splitlines()

#initialise element counts
for ch in input[0]:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1

#initialise pair counts
for i in range(len(input[0]) - 1):
    ch = input[0][i:i+2]
    if ch in pairs:
        pairs[ch] += 1
    else:
        pairs[ch] = 1

for i in range(2, len(input)):
    pair = input[i][:2]
    insert = input[i][6]

    if pair not in pairs:
        pairs[pair] = 0
    if insert not in counts:
        counts[insert] = 0

    rules[pair] = insert


def step(rules, counts, pairs):

    changes = {}

    for k in pairs.keys():
        ins = rules[k]
        counts[ins] += pairs[k]
        np1 = k[0] + ins
        np2 = ins + k[1]

        if np1 in changes:
            changes[np1] += pairs[k]
        else:
            changes[np1] = pairs[k]
        
        if np2 in changes:
            changes[np2] += pairs[k]
        else:
            changes[np2] = pairs[k]
        
        if k in changes:
            changes[k] -= pairs[k]
        else:
            changes[k] = -pairs[k]
    
    for k in changes.keys():
        pairs[k] += changes[k]

for i in range(40):
    step(rules, counts, pairs)

values = []

for k in counts.keys():
    if counts[k] != 0:
        values.append(counts[k])

print(max(values) - min(values))


