#!/usr/bin/python

test = False
if test:
    f = open("input.test")
else:
    f = open("input")

crabs = list(map(int, f.readline().split(",")))
min_crab = min(crabs)
max_crab = max(crabs)
crabs_count = len(crabs)

positions = [0] * (max_crab - min_crab + 1)
sum_lengths = 0
sum_fuels = 0

for crab in crabs:
    positions[crab] += 1
    length = crab - min_crab
    sum_lengths += length
    fuel = length * (length + 1) / 2
    sum_fuels += fuel

print("positions: %s " % positions)
print("[0] sum lengths %d fuels %d" % (sum_lengths, sum_fuels))

min_fuel = sum_fuels
min_fuel_crab = min_crab

lower_lengths = 0
lower_fuel = 0
lower_count = positions[0]

upper_fuel = sum_fuels
upper_lengths = sum_lengths
upper_count = crabs_count - lower_count

sum_fuel = upper_fuel + lower_fuel

print("[%d] lower (count %d, lengths %d, fuel %d) upper (count %d, length %d, fuek %d) sum fuel %d" % (0, lower_count, lower_lengths, lower_fuel, upper_count, upper_lengths, upper_fuel, sum_fuel))

for index in range(1, max_crab - min_crab + 1):
    lower_lengths += lower_count
    lower_fuel += lower_lengths
    lower_count += positions[index]

    upper_fuel -= upper_lengths
    upper_lengths -= upper_count
    upper_count -= positions[index]

    sum_fuel = upper_fuel + lower_fuel

    print("[%d] lower (count %d, lengths %d, fuel %d) upper (count %d, length %d, fuek %d) sum fuel %d" % (index, lower_count, lower_lengths, lower_fuel, upper_count, upper_lengths, upper_fuel, sum_fuel))
    
    if sum_fuel < min_fuel:
        min_fuel = sum_fuel
        min_fuel_crab = index + min_crab


print("min fuel %d crab %d" % (min_fuel, min_fuel_crab))

    