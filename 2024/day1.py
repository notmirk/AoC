import itertools

filename = 'day1-input'

# Part 1 and Part 2
data = []
with open(filename) as file:
    for line in file:
        data.append([e for e in line.rstrip().split(' ') if e])

# Part 1
c0 = sorted(list(map(lambda e: e[0], data)))
c1 = sorted(list(map(lambda e: e[1], data)))

diff = 0
for v0, v1 in zip(c0, c1):
    #print(v0, ",", v1, "=", abs(int(v1) - int(v0)))
    diff = diff + abs(int(v1) - int(v0))
print("Part 1:", diff)

# Part 2
c0 = list(map(lambda e: e[0], data))
c1 = list(map(lambda e: e[1], data))

simularity = 0
for v0, v1 in zip(c0, c1):
    #print(v0, ",", v1, "=", c1.count(v0))
    simularity = simularity + (int(v0) * c1.count(v0))
print("Part 2:", simularity)
