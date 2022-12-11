import numpy as np

with open('input_t.txt') as f:
    data = np.array([[int(y) for y in x] for x in f.read().split('\n') if x])

visible = 0

for row in data:
    pass

for col in data.T:
    pass

print(visible)