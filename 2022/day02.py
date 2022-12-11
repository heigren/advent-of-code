with open('input/2.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n') if x]

shape_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

win = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

# ---
# Part 1

score1 = 0

for r in data:
    op = shapes.get(r[0])
    me = shapes.get(r[1])

    if me == op:
        score1 += shape_score.get(me) + 3
        continue

    if win.get(me) == op:
        score1 += shape_score.get(me) + 6
        continue

    if win.get(op) == me:
        score1 += shape_score.get(me)
        continue

print(score1)

# ---
# Part 2

score2 = 0

for n in data:
    op = shapes.get(n[0])
    me = n[1]

    if me == 'X':
        score2 += shape_score.get(win.get(op))
        continue
    if me == 'Y':
        score2 += shape_score.get(op) + 3
        continue
    if me == 'Z':
        score2 += shape_score.get({v: k for k, v in win.items()}.get(op)) + 6
        continue

print(score2)