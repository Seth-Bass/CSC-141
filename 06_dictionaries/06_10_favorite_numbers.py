# Creating a dictionary with people's names as keys and a list of their favorite numbers as values
favorite_numbers = {
    'Alice': [7, 22, 33],
    'Bob': [5, 19],
    'Charlie': [12, 8, 21],
    'David': [3, 25],
    'Eve': [11, 4]
}

# Looping through the dictionary and printing each person's name and their favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print()  # Blank line between each person for better readability
