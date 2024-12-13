import random

# Create a list with 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items (numbers or letters) from the list
winning_combination = random.sample(lottery_items, 4)

# Print the message with the winning combination
print(f"Winning combination: {winning_combination}")
print("Any ticket matching these 4 numbers or letters wins a prize!")
