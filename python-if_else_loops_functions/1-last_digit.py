#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
if last_digit < 6 and last_digit != 0:
    comp5_6 = "and is less than 6 and not 0"
elif last_digit > 5:
    comp5_6 = "and is greater than 5"
else:
    comp5_6 = "and is 0"
print("Last digit of {} is {} {}".format(number, last_digit, comp5_6))
