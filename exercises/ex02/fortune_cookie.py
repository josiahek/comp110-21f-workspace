"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730214639"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

fortune: int = int(randint(1, 4))
print("Your fortune cookie says...")
if fortune == 1:
    print("A beautiful and smart person will come into your life.")
else:
    if fortune == 2:
        print("You will find suceess in work.")
    if fortune == 3:
        print("Life will become fulfilling.")
    if fortune == 4:
        print("A new hobby will find you.")
print("Now, go spread positive vibes!")