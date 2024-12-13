# Creating a dictionary with names as keys and their favorite places as values
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['London', 'Rome'],
    'Charlie': ['Berlin', 'Amsterdam', 'Barcelona']
}

# Looping through the dictionary and printing each person's name and their favorite places
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()  # Blank line between each person for better readability
    