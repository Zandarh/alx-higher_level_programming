#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10
if number < 0:
	last_number = -last_number
	print(f"Last digit of {number} is {last_number} and is less than 6 and not zero")
elif last_number > 5:
	print(f"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
	print(f"Last digit of {number} is {last_number} and is zero")
				
else:
	print(f"Last digit of {number} is {last_number} and is less than 6 and not zero")
