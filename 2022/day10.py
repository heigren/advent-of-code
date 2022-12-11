with open('input/10.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n') if x]

cpu = 0
x = 1
cycles = 0

for op in data:
    match op[0]:
        case 'noop':
            cpu += 1
            if (- 20 + cpu) % 40 == 0: cycles += (cpu * x)

        case 'addx':
            cpu += 1
            if (- 20 + cpu) % 40 == 0: cycles += (cpu * x)
            
            cpu += 1
            if (- 20 + cpu) % 40 == 0: cycles += (cpu * x)
            x += int(op[1])

print(f'-> Part 1: {cycles}')

# -----------

crt = [[] for x in range(6)]
cycle = 0
addx = 1
pos = 0
crt_row = 0

def add_pixel(addx, pos, crt, crt_row):
    if (addx == pos) or (addx - 1 == pos) or (addx + 1 == pos):
        crt[crt_row].append('#')
    else:
        crt[crt_row].append('.')

for op in data:
    match op[0]:
        case 'noop':
            cycle += 1
            add_pixel(addx, pos, crt, crt_row)
            pos += 1
            if pos > 39: crt_row += 1; pos = 0
            

        case 'addx':
            cycle += 1
            add_pixel(addx, pos, crt, crt_row)
            pos += 1
            if pos > 39: crt_row += 1; pos = 0

            cycle += 1
            add_pixel(addx, pos, crt, crt_row)
            pos += 1
            if pos > 39: crt_row += 1; pos = 0
            
            addx += int(op[1])
            
for row in crt:
    print(''.join(row))