import time

with open('input/4.txt') as f:
    data = f.read().splitlines()


# ----- PART 1
start_p1 = time.time()

sum_points = 0

for card in data:
    winning = set([x for x in card.split(':')[1].split('|')[0].strip().split(' ') if x])
    my_numbers = set([x for x in card.split(':')[1].split('|')[1].strip().split(' ') if x])
    matches = my_numbers.intersection(winning)

    if len(matches) <= 1:
        sum_points += len(matches)
        continue

    card_points = 2 ** (len(matches) - 1)
    sum_points += card_points

time_p1 = (time.time() - start_p1)
print(f'Finished, part 1 -- {time_p1}')

# ----- PART 2


start_p2 = time.time()

my_cards = {
    k: v
    for k, v
    in zip(range(1,len(data)+1), [
        [set([x for x in data[y-1].split(':')[1].split('|')[1].strip().split(' ') if x])]
        for y
        in range(1,len(data)+1)])
    }


i = 0
while i < len(my_cards):
    #print(f'{i=} {len(my_cards)=}')
    winning = set([x for x in data[i].split(':')[1].split('|')[0].strip().split(' ') if x])

    for cards in my_cards[i+1]:
        new_match = cards.intersection(winning)

        for y in range(i+2,len(new_match)+2+i):
            my_cards[y].append(set([x for x in data[y-1].split(':')[1].split('|')[1].strip().split(' ') if x]))
            pass
    i+=1

total_value = sum([len(x) for x in my_cards.values()])
print(total_value)
time_p2 = (time.time() - start_p2)
print(f'Finished, part 2 -- {time_p2}')