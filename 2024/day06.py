

with open('input/6.txt') as f:
    data = [x for x in f.read().splitlines()]

for line in data:
    try:
        idx_x: int = line.index('^')
        idx_y: int = data.index(line)

        break
    except ValueError:
        continue
        
directions = {
    0: (-1, 0),
    90: (0, 1),
    180: (1, 0),
    270: (0, -1),
}

finished = False
direction = 0
changeY, changeX = directions.get(direction)
visited = []

while not finished:
    try:
        if (idx_y + changeY) < 0 or (idx_x + changeX) < 0:
            raise IndexError('Negative indices!')

        if data[idx_y + changeY][idx_x + changeX] == '#': 
            direction += 90
            if direction > 270: direction = 0
            changeY, changeX = directions.get(direction)
            

        if not (idx_y, idx_x) in visited:
            visited.append((idx_y, idx_x))

        idx_y += changeY
        idx_x += changeX
            
    except IndexError:
        visited.append((idx_y, idx_x))

        finished = True

print(f'Part 1: {len(visited)}')