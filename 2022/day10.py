with open('input/10.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n') if x]

cpu = 0
x = 1
i = 0
cycles = []


def check(cpu: int, x: int) -> None:
    if cpu in [20, 60, 100, 140, 180, 220]: cycles.append(cpu * x)


for op in data:
    match op[0]:
        case 'noop':
            cpu += 1
            check(cpu, x)

        case 'addx':
            cpu += 1
            check(cpu, x)
            
            cpu += 1
            check(cpu, x)
            x += int(op[1])

print(f'-> Part 1: {sum(cycles)}')