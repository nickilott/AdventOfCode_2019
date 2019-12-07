import numpy

## Part 1
def fuelAmount(value):
    return((numpy.floor(value/3))-2)

x = sum([fuelAmount(int(y[:-1])) for y in open("input.txt").readlines()])
print("answer 1 = ", x)

## Part 2
result = []
for line in open("input.txt").readlines():
    v = int(line[:-1])
    fuel = fuelAmount(v)
    total_fuel = fuel
    while fuelAmount(fuel) > 0:
        fuel = fuelAmount(fuel)
        total_fuel += fuel
    result.append(total_fuel)

print("answer 2 = ", sum(result))
