class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initializing attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Method to describe the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Method to indicate the restaurant is open
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of Restaurant
restaurant = Restaurant("The Gourmet Spot", "Italian")

# Printing the attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
