import itertools

with open('input/1.txt') as f:
    data = [x.strip('\n').split('   ') for x in f.readlines()]
    data = list(itertools.chain.from_iterable(data))
    data = [int(x) for x in data]


l1 = list(sorted(data[::2]))
l2 = list(sorted(data[::-2]))

i = 0
diff = 0
score = 0

while i < len(l1):
    diff += abs(l1[i] - l2[i])
    score += l1[i] * l2.count(l1[i])

    i += 1

# Part 1
print(f'Part 1: {diff}')

# Part 2
print(f'Part 2: {score}')