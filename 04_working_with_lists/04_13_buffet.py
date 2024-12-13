# Step 1: Store five simple foods in a tuple
buffet_menu = ('Pizza', 'Pasta', 'Salad', 'Soup', 'Bread')

# Step 2: Use a for loop to print each food the restaurant offers
print("The restaurant offers the following foods:")
for food in buffet_menu:
    print(food)

# Step 3: Try to modify one of the items (this will raise an error)
try:
    buffet_menu[1] = 'Burger'  # This will cause an error because tuples are immutable
except TypeError as e:
    print(f"\nError: {e}")

# Step 4: The restaurant changes its menu, replacing two of the items
# Rewriting the tuple with new items
buffet_menu = ('Pizza', 'Burger', 'Steak', 'Soup', 'Fries')

# Step 5: Print the revised menu
print("\nThe revised menu includes:")
for food in buffet_menu:
    print(food)
