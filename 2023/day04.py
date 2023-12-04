import time

with open('input/4.txt') as f:
    data = f.read().splitlines()


# ----- PART 1
start_p1 = time.time()

sum_points = 0
my_cards = {}

for card in data:
    winning = set([x for x in card.split(':')[1].split('|')[0].strip().split(' ') if x])
    my_numbers = set([x for x in card.split(':')[1].split('|')[1].strip().split(' ') if x])
    matches = my_numbers.intersection(winning)

    my_cards.update({data.index(card): {
        'card': my_numbers,
        'count': 1
    }})

    if len(matches) <= 1:
        sum_points += len(matches)
        continue

    card_points = 2 ** (len(matches) - 1)
    sum_points += card_points

time_p1 = (time.time() - start_p1)
print(f'Finished, part 1 -- {time_p1}')

# ----- PART 2


start_p2 = time.time()

i = 0
while i < len(my_cards):
    winning = set([x for x in data[i].split(':')[1].split('|')[0].strip().split(' ') if x])
    new_match = my_cards[i]['card'].intersection(winning)

    for x in range(0, my_cards[i]['count']):
        for y in range(i+1, len(new_match)+1+i):
            my_cards[y]['count'] = my_cards[y].get('count')+1
    i+=1

s = 0
for x in range(0,len(my_cards)):
    s += my_cards[x]['count']

print(s)
time_p2 = (time.time() - start_p2)
print(f'Finished, part 2 -- {time_p2}')