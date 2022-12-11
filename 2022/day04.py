data = [[tuple(int(z) for z in y.split('-')) for y in x.split(',')] for x in open('input/4.txt').read().split('\n') if x]

full_overlap = 0
part_overlap = 0

for pair in data:
    r1 = range(pair[0][0], pair[0][1] + 1)
    r2 = range(pair[1][0], pair[1][1] + 1)

    if (set(r1).issuperset(r2) or set(r1).issubset(r2)) :
        full_overlap += 1
    
    if bool(set(r1) & set(r2)):
        part_overlap += 1

print(f'-> Part 1: {full_overlap} -- Part 2: {part_overlap}')