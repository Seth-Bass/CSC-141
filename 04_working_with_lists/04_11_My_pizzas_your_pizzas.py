# Original list of pizzas
my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# Copy of the original list
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append('Hawaiian')

# Add a different pizza to the friend's list
friend_pizzas.append('Vegetarian')

# Prove that we have two separate lists by printing each list

# Printing the original list of pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

# Printing the friend's list of pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
