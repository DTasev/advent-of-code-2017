with open('input.txt', 'r') as f:
    steps = [int(d.strip()) for d in f.readlines()]
step = 0
index = 0
try:
    while True:
        jump = steps[index]
        steps[index] += 1
        index += jump
        step += 1
except IndexError:
    print(step)
