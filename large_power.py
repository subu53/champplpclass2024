"""Coding Question
Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""

def large_power(base, exponent):
    return base**exponent

if large_power (10,10) > 5000:
    print(True)
else:
    print(False)
