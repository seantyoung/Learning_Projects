import random
import math

print("We're going to calculate Pi by throwing darts at a dart board.")
darts = int(input("How many darts would you like to throw? "))

while darts > 10 ** 7:
    print("\nThat's too many, try throwing less than 10,000,000.")
    darts = int(input("How many darts would you like to throw? "))

print("\nAlright, lets throw %i darts" % darts)

count = 0.0
for n in range(darts):
    x = random.random()
    y = random.random()
    z = (x ** 2 + y ** 2) ** 0.5
    if z <= 1:
        count += 1

piEst = (count / darts * 4)

print("Pi estimate: %.6f" % piEst)
print("Pi actual: %.6f" % math.pi)
print("Error: %.4f%%" % (abs(math.pi - piEst) / math.pi * 100))
