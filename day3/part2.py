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

current_index = list(range(len(data)))

for i in range(len(data[0])):
    one = 0
    zero = 0
    one_index = []
    zero_index = []
    for j in current_index:
        if (data[j][i] == 1):
            one += 1
            one_index.append(j)
        else:
            zero += 1
            zero_index.append(j)

    if(one >= zero):
            current_index = one_index
    else:
            current_index = zero_index
    if(len(current_index) == 1):
        break

oxy = current_index[0]

current_index = list(range(len(data)))

for i in range(len(data[0])):
    one = 0
    zero = 0
    one_index = []
    zero_index = []
    for j in current_index:
        if (data[j][i] == 1):
            one += 1
            one_index.append(j)
        else:
            zero += 1
            zero_index.append(j)

    if(one >= zero):
            current_index = zero_index
    else:
            current_index = one_index
    if(len(current_index) == 1):
        break

co2 = current_index[0]

oxy_num = 0
co2_num = 0

for i in range(len(data[0])):
    oxy_num += data[oxy][len(data[0]) - 1 - i]*2**(i)
    co2_num += data[co2][len(data[0]) - 1 - i]*2**(i)

print(oxy_num*co2_num)