#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

output = "The string Last digit of {} is {} and is ".format(number, last_digit)

if last_digit > 5:
    output += "greater than 5"
elif last_digit == 0:
    output += "0"
else:
    output += "less than 6 and not 0"

print(output)
