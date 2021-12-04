#get input

f = open("day3/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

data = []

for x in input:
    clean = x.strip()
    subdata = []
    for i in range(len(clean)):
        subdata.append(int(clean[i]))
    data.append(subdata)

most_commmon = []

for i in range(len(data[0])):
    one = 0
    zero = 0
    for j in range(len(data)):
        if (data[j][i] == 0):
            one += 1
        else:
            zero += 1
    if(one > zero):
        most_commmon.append(1)
    else:
        most_commmon.append(0)

gamma = 0
m = 2**(len(most_commmon)) - 1

for i in range(len(most_commmon)):
    gamma += most_commmon[len(most_commmon) - 1 - i]*2**(i)

print(gamma*(m - gamma))



