data    = [x for x in open('input.txt').read().split('\n\n') if x]

stacks  = [[z.strip('[]') for z in y] for y in [x.split(' ') for x in data[0].split('\n')]]
moves   = [x for x in data[1].split('\n') if x]

stacks.pop()

for stack in stacks:
    while True:
        try:
            stack[stack.index(''):stack.index('') + 4] = '-'
        except ValueError:
            break

#stacks = [[y for y in x if y] for x in list(zip(*[[z.strip('-') for z in y] for y in [x for x in stacks]][::-1]))]
part1 = [[y for y in x if y] for x in list(zip(*[[z.strip('-') for z in y] for y in [x for x in stacks]][::-1]))]
part2 = [[y for y in x if y] for x in list(zip(*[[z.strip('-') for z in y] for y in [x for x in stacks]][::-1]))]

for move in moves:
    no  = int(move.split(' ')[1])       # Number of crates to move
    src = int(move.split(' ')[3]) - 1   # Source stack
    dst = int(move.split(' ')[5]) - 1   # Destination stack

    # Part 1
    for i in range(no):
        part1[dst].append(part1[src].pop())

    # Part 2
    part2[dst] = part2[dst] + part2[src][-no:]
    part2[src] = part2[src][:-no]

part1_solution = ''.join([item for sublist in part1 for item in sublist[-1:]])
part2_solution = ''.join([item for sublist in part2 for item in sublist[-1:]])

print(f'-> Part 1: {part1_solution} -- Part 2: {part2_solution}')