# Define some variables to test
car = 'subaru'
color = 'blue'
age = 25
height = 5.9
foods = ['pizza', 'burger', 'salad', 'pasta']
is_sunny = True
is_weekend = False

# --- Equality and Inequality with Strings ---
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

# --- Tests using the lower() method ---
print("\nIs color == 'blue'? I predict True.")
print(color.lower() == 'blue')  # True

print("\nIs color == 'BLUE'? I predict True.")
print(color.lower() == 'blue')  # True

print("\nIs color.lower() == 'red'? I predict False.")
print(color.lower() == 'red')  # False

# --- Numerical Tests ---
print("\nIs age == 25? I predict True.")
print(age == 25)  # True

print("\nIs age != 30? I predict True.")
print(age != 30)  # True

print("\nIs height > 6? I predict False.")
print(height > 6)  # False

print("\nIs height >= 5.9? I predict True.")
print(height >= 5.9)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age <= 25? I predict True.")
print(age <= 25)  # True

# --- Tests using the and and or keywords ---
print("\nIs it sunny and is it weekend? I predict False.")
print(is_sunny and is_weekend)  # False

print("\nIs it sunny or is it weekend? I predict True.")
print(is_sunny or is_weekend)  # True

print("\nIs age >= 18 and height > 5? I predict True.")
print(age >= 18 and height > 5)  # True

# --- Test whether an item is in a list ---
print("\nIs 'pizza' in foods? I predict True.")
print('pizza' in foods)  # True

print("\nIs 'tacos' in foods? I predict False.")
print('tacos' in foods)  # False

# --- Test whether an item is not in a list ---
print("\nIs 'burger' not in foods? I predict False.")
print('burger' not in foods)  # False

print("\nIs 'sushi' not in foods? I predict True.")
print('sushi' not in foods)  # True
