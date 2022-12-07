from collections import Counter

with open('input/6.txt') as f:
    data = f.read().split('\n')[0]

sop = 4     # start-of-packet
som = 14    # start-of-message

while True:
    for i in range(len(data) - sop + 1):
        if len(Counter(data[i:i + sop]).items()) == sop:
            print(f'-> Part 1: {i + sop}')
            break
    
    for i in range(len(data) - som + 1):
        if len(Counter(data[i:i + som]).items()) == som:
            print(f'-> Part 2: {i + som}')
            break
    break

# - - - - - - -

# If I had been smart enough I would have made it like this:
print(*map(lambda l: [i + l for i in range(len(data)) if len(set(data[i:i + l])) == l][0], [4, 14]))