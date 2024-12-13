import random

class Die:
    def __init__(self, sides=6):
        # Initialize the die with a default number of sides (6 by default)
        self.sides = sides

    def roll_die(self):
        # Roll the die and print a random number between 1 and the number of sides
        return random.randint(1, self.sides)

# Create a 6-sided die
six_sided_die = Die()

# Roll the die 10 times and print the result of each roll
for _ in range(10):
    print(six_sided_die.roll_die())
