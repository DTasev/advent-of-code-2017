import os

data = []

with open('input', 'r') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = (int(data[i].strip()) / 3) - 2

print(sum(data))
