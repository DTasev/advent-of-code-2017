import os
import operator

data = []

with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
    data = [int(x) for x in f.readline().split(",")]

def run_with(data, i1,i2):
    data[1] = i1
    data[2] = i2
    for i in range(0, len(data), 4):
        if data[i] == 99:
            return data[0]

        r1 = data[i+1]
        r2 = data[i+2]
        store = data[i+3]
        if data[i] == 1:
            op = operator.add
        elif data[i] == 2:
            op = operator.mul
        data[store] = op(data[r1], data[r2])

for i1 in range(100):
    for i2 in range(100):
        out = run_with(data[:], i1, i2)
        if out == 19690720:
            print(i1, i2)
            print(100*i1+ i2)
            exit()