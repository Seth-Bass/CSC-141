# 1. My pizzas, your pizzas

# Original list of pizzas
my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# Copy of the original list
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append('Hawaiian')

# Add a different pizza to the friend's list
friend_pizzas.append('Vegetarian')

# Prove that we have two separate lists by printing each list
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 2. Odd numbers.

# Use range() with a step of 2 to generate odd numbers from 1 to 20
for number in range(1, 21, 2):
    print(number)

# 3. Buffet

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
