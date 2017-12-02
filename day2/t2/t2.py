from typing import List

data = List[str]

with open('input.txt', 'r') as f:
    data = f.readlines()

data = map(lambda line: sorted([int(x) for x in line.strip().split(" ")], reverse=True), data)
sums = []
for line in data:
    for num in line:
        res = list(filter(lambda n: num % n == 0, line))
        if len(res) > 1:
            sums.append(res[0] // res[1])
total = 0
for s in sums:
    total += s
print(total)
