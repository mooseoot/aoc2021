#get input

f = open("day1/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

values = []

for x in input:
    values.append(int(x))

counter = 0

for i in range(len(values)-1):
    if(values[i+1] > values[i]):
        counter += 1

print(counter)
