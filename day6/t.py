import math
# start = [0, 2, 7, 0]
start = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
inputlen = len(start)
previous = []

current = start
cycle = 0
while current not in previous:
    previous.append(current[:])
    max_num = max(current)
    idx = current.index(max_num)
    # set the highest number to 0
    current[idx] = 0

    increment = math.ceil(max_num / inputlen)
    for i in range(idx + 1, inputlen + idx + 1):
        if max_num - increment > 0:
            max_num -= increment
            current[i % inputlen] += increment
        else:
            current[i % inputlen] += max_num
            break
    cycle += 1

print("Task 1:", cycle)
print("Task 2:", abs(previous.index(current) - len(previous)))
