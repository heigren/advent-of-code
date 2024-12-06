

with open('input/6.txt') as f:
    data = [x for x in f.read().splitlines()]

def get_direction(d: int) -> tuple:
    match d:
        case 0:
            return (-1, 0)
        case 90:
            return (0, 1)
        case 180:
            return (1, 0)
        case 270:
            return (0,-1)
        case _:
            return (-1, 0)

# first find the index of the guard at the start
for line in data:
    try:
        idx_x: int = line.index('^')
        idx_y: int = data.index(line)
    except ValueError:
        continue
        

finished = False
direction = 0
changeY, changeX = get_direction(direction)

visited = []
n_map = [x for x in data]

while not finished:
    try:
        if data[idx_y + changeY][idx_x + changeX] == '#':            
            direction += 90
            if direction > 270: direction = 0
            changeY, changeX = get_direction(direction)

        if not (idx_y, idx_x) in visited:
            tmp = list(n_map[idx_y])
            tmp[idx_x] = 'X'
            n_map[idx_y] = ''.join(tmp)

            visited.append((idx_y, idx_x))


        if (idx_y + changeY) > 130 or (idx_y + changeY) < 0 or (idx_x + changeX) > 130 or (idx_x + changeX) < 0:
            break

        idx_y += changeY
        idx_x += changeX
            
    except IndexError:
        tmp = list(n_map[idx_y])
        tmp[idx_x] = 'X'
        n_map[idx_y] = ''.join(tmp)

        visited.append((idx_y, idx_x))

        finished = True

print(f'Part 1: {len(visited)}')