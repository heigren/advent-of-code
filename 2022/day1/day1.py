data = []

with open('input.txt') as f:
    t = []
    
    for line in f.readlines():
        if line.strip('\n') == '':
            data.append(t)
            t = []
            continue
        
        t.append(int(line.strip('\n')))

print(sum(sorted([sum(x) for x in data])[-3:]))

###
# Optimal
#
# with open('input.txt') as f:
#    print(sum(sorted([sum(x) for x in [[int(y) for y in z.splitlines()] for z in f.read().split("\n\n")]])[-3:]))