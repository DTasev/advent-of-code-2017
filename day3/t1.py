import math
number = 265149
# number = int(input("Enter the number:"))

side = math.ceil(math.sqrt(number))
diff = side**2 - number
print("Diff", diff)
steps = side - 1
print("Steps to reach the other side", steps)
middle = steps // 2

while diff > middle:
    diff -= middle
print("The middle", middle)
print(middle + (middle - diff))
