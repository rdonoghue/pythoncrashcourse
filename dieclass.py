## Exercise 9-14
'''
“
“9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the range you provide. The following code returns a number between 1 and 6:
    from random import randint”
 Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.”

Excerpt From: Eric Matthes. “Python Crash Course.” iBooks.
'''

from random import randint

class Die():
    """ A Single Die """
    def __init__(self, diesize):
        self.diesize=6

    def roll_die(self):
        print(randint(1, self.diesize))

this_roll=Die(6)
print(this_roll.roll_die())
