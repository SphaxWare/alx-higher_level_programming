#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig = -lastdig
result = "Last digit of " + str(number) + " is " + str(lastdig)
if lastdig > 5:
    result += " and is greater than 5"
if lastdig == 0:
    result += " and is 0"
if lastdig < 6 and lastdig != 0:
    result += " and is less than 6 and not 0"
print(result)
