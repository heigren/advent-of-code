with open('input/7.txt') as f:
    data = [x for x in f.read().split('\n') if x]

file_data = {
    '/': {
        'parent': '',
        'dirs': [],
        'files': [],
        'size': 0 # SHOULD INCLUDE 'dirs' SIZE
    }
}

c = lambda dir, parent: {dir: {'parent': parent, 'dirs': [], 'files': [], 'size': 0}}

curr_dir = '/'
i = 0

while i < len(data):
    line = data[i].split(' ')

    if '/' in line: curr_dir = '/'; i += 1; continue
    if '..' in line: curr_dir = file_data[curr_dir]['parent']; i += 1; continue # { 'b': { 'parent': 'a' }}
    if 'cd' in line: curr_dir = line[2]; i += 1; continue

    if line[1] == 'ls':
        j = 1
        while True:
            r1 = data[i + j].split(' ')

            if (r1[0] == '$') or (i + j >= len(data) - 1): break

            if r1[0] == 'dir':
                file_data[curr_dir]['dirs'].append(r1[1])
                file_data.update(c(r1[1], curr_dir))
                j += 1
                continue
            else:
                file_data[curr_dir]['files'].append(int(r1[0]))
                j += 1
                continue
        
        # calculate size
        file_data[curr_dir]['size'] = sum(file_data[curr_dir]['files'])

    i += 1

for dir in sorted(file_data, key=lambda x: len(file_data[x]['dirs'])):
    file_data[dir]['size'] += sum([file_data[x]['size'] for x in file_data[dir]['dirs']])


# Now let's find the thing we need to find
m = 100000

#print(file_data)

print(
    sum([x['size'] for x in file_data.values() if x['size'] < m])
)