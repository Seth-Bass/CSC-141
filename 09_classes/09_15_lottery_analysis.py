import random

# Create a list with 10 numbers and 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define my_ticket (the ticket we're trying to match)
my_ticket = [3, 'B', 7, 'E']

# Initialize the number of draws
draw_count = 0

# Loop until the randomly selected combination matches my_ticket
while True:
    draw_count += 1
    winning_combination = random.sample(lottery_items, 4)
    if winning_combination == my_ticket:
        break

# Print the result
print(f"It took {draw_count} draws to win with ticket: {my_ticket}")
