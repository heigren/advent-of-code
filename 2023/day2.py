from functools import reduce

with open('input/2.txt') as f:
    data = [x.strip('\n').split(':') for x in f.readlines()]

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# --------------- PART 1

sum_id_p1 = 0

for game_p1 in data:
    game_id_p1 = int(game_p1[0].split(' ')[1])
    possible = True

    for round in game_p1[1].split(';'):
        for handful in round.split(','):
            number = handful.split(' ')[1]
            color = handful.split(' ')[2]

            if int(number) > max_cubes.get(color):
                possible = False
                break
    
    if possible:
        sum_id_p1 += game_id_p1

print(sum_id_p1)

# --------------- PART 2

power_set = []

for game_p2 in data:
    game_id_p2 = int(game_p2[0].split(' ')[1])
    possible = True
    lowest = {'red': 0, 'green': 0, 'blue': 0}

    for round in game_p2[1].split(';'):
        for handful in round.split(','):
            number = int(handful.split(' ')[1])
            color = handful.split(' ')[2]

            if lowest.get(color) < number:
                lowest.update({color: number})

    power_set.append(
        reduce(lambda x, y: x * y, [x for x in lowest.values()])
    )
    
print(sum(power_set))