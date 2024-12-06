import re

filename = 'day3-input'

# Part 1
with open(filename) as file:
    program = "".join(line for line in file)

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
matches = regex.finditer(program)
total = sum(int(match.group(1)) * int(match.group(2)) for match in matches)

print("Part 1:", total)

# Part 2
with open(filename) as file:
    program = "".join(line for line in file)

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

pos = 0
total = 0
while pos != -1:
    end = program.find("don't()", pos)
    if end == -1:
        end = len(program)
    matches = regex.finditer(program[pos:end])
    subtotal = sum(int(match.group(1)) * int(match.group(2)) for match in matches)
    total += subtotal
    pos = program.find("do()", end)

print("Part 2:", total)
