import re, sys

with open('input.txt') as f:
    data = [x.strip('\n') for x in f.readlines()]

lookup = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

newdata = []
i = 0

while i < len(data):
    #search = re.findall(r"(one|two|three|four|five|six|seven|eight|nine)", data[i])
    newstring = data[i]
    newline = []
    all_found = False
    while not all_found:
        search = re.findall(r"(one|two|three|four|five|six|seven|eight|nine)", newstring)

        j = 0
        while j < len(search):
            newstring = re.sub(search[j], lookup.get(search[j]), newstring) # abcone2threexyz -> abc123xyz
            j+=1

        if len(search) == 0:
            all_found = True

    for char in newstring: # Remove any normal chars, keep numbers: abc123xyz -> 123 
        try:
           newline.append(int(char))
        except:
            continue
    
    if len(newline) == 1: # hack something if there's only one number left
        t1 = [[y for y in (x, x)] for x in newline]
        newline = [z for z in t1[0]]

    #print('=> i:', i, '| pre:', data[i], '| post:', newstring, '| newline:', newline, '| newline_slice:', newline[::len(newline)-1])

    newdata.append(''.join([str(x) for x in newline]))
    i+=1

newdata = [int(x[::len(x)-1]) for x in newdata] # only first and last digit is what we want: 123 -> 13
print('sum:', sum(newdata))

sys.exit(0)

# PART 1

# for line in data:
#     newline = []
#     for char in line:
#         try:
#            newline.append(int(char))
#         except:
#             continue

#     l1 = ''.join([str(x) for x in newline])
#     if len(l1) > 2:
#         l1 = l1[::len(l1)-1]
    
#     if len(l1) == 1:
#         l1 = ''.join([x*2 for x in l1])

#     newdata.append(int(l1))