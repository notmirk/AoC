import itertools

filename = 'day2-input'

# Part 1 and Part 2
data = []
with open(filename) as file:
    for line in file:
        data.append([int(e) for e in line.rstrip().split(' ') if e])

# Part 1
safe_count = 0
for a in data:
    #safe = True
    #o = 0
    #if (a[1] > a[0]):
    #    o = 1
    for i in range(len(a) - 1):
        #safe = (a[i + o] - a[i + 1 - o]) in range(1, 4)

        #safe = (lambda: (a[i] - a[i + 1]) in range(1, 4), lambda: (a[i + 1] - a[i]) in range(1, 4))[a[1] > a[0]]()
        safe = ((a[i] - a[i + 1]) in range(1, 4), (a[i + 1] - a[i]) in range(1, 4))[a[1] > a[0]]

        if not safe:
            break

    #print(safe, a)
    if safe:
        safe_count += 1

print("Part 1:", safe_count)

# Part 2
safe_count = 0
for a in data:
    for j in range(len(a)):
        b = a[:j] + a[(j + 1):]
        for k in range(len(b) - 1):
            p = (0, 1)[b[1] > b[0]]
            safe = (b[k + p] - b[k + 1 - p]) in range(1, 4)
            if not safe:
                break
        if safe:
            break
 
    if safe:
        safe_count += 1

print("Part 2:", safe_count)
