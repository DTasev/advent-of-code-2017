import os

data = []

with open('input', 'r') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = int(data[i].strip())

total_fuel = 0
for fuel in data:
    current_fuel = fuel
    while current_fuel > 0:
        current_fuel = current_fuel / 3 - 2
        print(current_fuel)
        if current_fuel > 0:
           total_fuel += current_fuel


print(total_fuel)
