import sys

with open('input/3.txt') as f:
    data = [x.strip('\n') for x in f.readlines()]

s1 = [[y for y in x if y != '.'] for x in data]
s2 = [[y for y in x if not y.isdigit()] for x in s1]
symbols = list(dict.fromkeys([x for y in s2 for x in y if x]))

def number_valid(data, no, i, j) -> bool:
    #print(f'=> Number: {no=} {i=} {j=}')

    # need to check:
    # i +/- 1 (next/previous row)
    # j +/- 1

    # j = last index, first index is j-len(tmp_nr)
    #print(f'-- number_valid(data, {no=}, {i=}, {j=})')
    count = j - (len(no))
    if count < 0:
        #print(count)
        count += 1

    if data[i][count] in symbols or data[i][j+1] in symbols:
        #print(f'{count=} {j=} {data[i][count-1]=} {data[i][j+1]=}')
        return True

    if i == 0:
        
        while count < j + 2:
            #print(f'|| {data[i+1][count]=}')
            if data[i+1][count] in symbols:
                return True
            count += 1
        return False

    elif i+1 == len(data):
        #print('i+1 == len(data)')
        return True
        pass

    #check i-1
    else:
        count2 = j - (len(no))
        for x in range(i-1, i+2):
            print(f'{x=} {data[x]=}')
            while count2 < j + 2:
                #print(f'{data[x][count2]=} {x=} {count2=}')
                if data[x][count2] in symbols:
                    return True
                count2 += 1
            count2 = j - (len(no))
        
        return False
    
    # -------------

    

i = 0
part_sum = 0

while i < len(data):
    number = []

    j = 0
    tmp_no = []
    while j < len(data[i]):
        if data[i][j].isdigit():
            tmp_no.append(data[i][j])

        if (tmp_no and not data[i][j].isdigit()) or (tmp_no and j == len(data[i])-1): # FULL NUMBER FOUND, CHECK FOR COORDS
            print(f'------------\n=> FULL NUMBER FOUND, CHECKING | {tmp_no=} {j=} {data[i]=}')
            if number_valid(data, tmp_no, i, j-1):
                print('number_valid TRUE')
                part_sum += int(''.join(tmp_no))
                tmp_no = []
                j += 1
                continue
            else:
                print('number_valid FALSE')
                tmp_no = []
                j += 1
                continue

        j += 1

    i += 1

print(f'{part_sum=}')
