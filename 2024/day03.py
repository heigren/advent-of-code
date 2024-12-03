import re

def find_mul(m: list) -> list:
    return [[int(y) for y in x] for x in [re.search(r"\d+,\d+", match).group().split(',') for match in m]]

with open('input/3.txt') as f:
    data = [line for line in f.read().splitlines()]
    
mul_pattern = r"mul\(\d+,\d+\)"
matches = []

for line in data:
    reg_match = re.findall(mul_pattern, line)

    for match in reg_match:
        matches.append(match)

print(f'Part 2: {sum([x * y for x, y in find_mul(matches)])}')

# -----

segments1 = [re.split(r"(do\(\)|don't\(\))", line) for line in data]
segments = [x for y in segments1 for x in y]

is_matching = True
new_matches = []

# Iterate through segments
for segment in segments:
    if segment == "do()":
        is_matching = True  # Start matching when "do()" is found
        continue
    elif segment == "don't()":
        is_matching = False  # Stop matching when "don't()" is found
        continue
    elif is_matching:
        # Find all "mul(...)" patterns in the current segment
        new_matches.extend(re.findall(mul_pattern, segment))

print(f'Part 2: {sum([x * y for x, y in find_mul(new_matches)])}')
