from typing import List

data = List[str]

with open('input.txt', 'r') as f:
    data = f.readlines()

data = map(lambda line: [int(x) for x in line.strip().split(" ")], data)
sums = []
for line in data:
    sums.append(max(line) - min(line))

total = 0
for s in sums:
    total += s
print(total)
