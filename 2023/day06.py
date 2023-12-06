from functools import reduce

with open('input/6.txt') as f:
    data = f.read().splitlines()

#time = [int(x.strip()) for x in data[0].split(' ')[1:] if x]
#dist = [int(x.strip()) for x in data[1].split(' ')[1:] if x]

time = int(''.join([x.strip() for x in data[0].split(' ')[1:] if x]))
dist = int(''.join([x.strip() for x in data[1].split(' ')[1:] if x]))

races = [(time, dist)]
ways = []

for race in races:
    t_duration = race[0]
    record = race[1]

    speed = 0
    duration = t_duration
    
    win = 0

    for x in range(0, t_duration):
        go = x * duration
        if go > record:
            win += 1
        duration -= 1
        print(duration)
    
    ways.append(win)

print(ways)
#print(reduce((lambda x, y: x * y), ways))

# --------- PART 2

#time_p2 = int(''.join([x.strip() for x in data[0].split(' ')[1:] if x]))
#dist_p2 = int(''.join([x.strip() for x in data[1].split(' ')[1:] if x]))

pass