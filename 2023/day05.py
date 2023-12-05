with open('input/5.txt') as f:
    data = f.read().splitlines()
seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]

def update_values(seeds: list, src: list, dst: list, u_values: list) -> list:
    updated_list = seeds.copy()

    for seed in seeds:
        if (seed in src) and (seed not in u_values):
            new_val = dst[src.index(seed)]
            updated_list[updated_list.index(seed)] = new_val
            u_values.append(new_val)

    return updated_list, u_values

i = 1
s_map = []
u_values = []

while i < len(data):
    if data[i] == '': i += 1; continue

    if data[i].split(' ')[1] == 'map:':
        u_values = []
        s_map = []
        curr_map = data[i].split(' ')[0]
        print(f"-> Now processing {curr_map}")
        i += 1
        continue
    
    line = [int(x) for x in data[i].split(' ')]

    src = line[1] # SEED NUMBER
    dst = line[0] # SOIL NUMBER
    r_len = line[2]

    src_range = range(src, src + r_len)
    dst_range = range(dst, dst + r_len)

    seeds, u_values = update_values(seeds, src_range, dst_range, u_values)   

    i += 1

seeds.sort()
print(seeds[0])