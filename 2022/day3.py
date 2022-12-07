import string

# Part 1
print(sum([dict(zip(string.ascii_letters, [l for l in range(1,53)])).get(''.join(set(y[0]).intersection(y[1]))) for y in [[x[i:i + round(len(x) / 2)] for i in range(0, len(x), round(len(x) / 2))] for x in open('input/3.txt').read().split('\n') if x]]))

# ---

# Part 2
print(sum([dict(zip(string.ascii_letters, [l for l in range(1,53)])).get(''.join(set(y[0]).intersection(*y))) for y in list(zip(*[iter([x for x in open('input/3.txt').read().split('\n') if x])]*3))]))