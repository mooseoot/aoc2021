#get input

f = open("day6/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.split(",")

fish = [0,0,0,0,0,0,0,0,0]

for x in input:
    fish[int(x)] += 1

def sim_day(fish):
    new_fish = [0,0,0,0,0,0,0,0,0]
    for i in range(1,len(fish)):
        new_fish[i-1] = fish[i]
    new_fish[8] = fish[0]
    new_fish[6] += fish[0]
    return new_fish
        

for i in range(256):
    fish = sim_day(fish)

print(sum(fish))
