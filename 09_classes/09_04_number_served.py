class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initializing attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of number_served

    def describe_restaurant(self):
        # Method to describe the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Method to indicate the restaurant is open
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        # Method to set the number of customers served
        self.number_served = number

    def increment_number_served(self, additional_served):
        # Method to increment the number of customers served
        self.number_served += additional_served

# Creating an instance of Restaurant
restaurant = Restaurant("The Gourmet Spot", "Italian")

# Printing the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Changing the number of customers served and printing it again
restaurant.number_served = 50
print(f"Number of customers served after change: {restaurant.number_served}")

# Setting a new number of customers served using set_number_served method
restaurant.set_number_served(120)
print(f"Number of customers served after using set_number_served: {restaurant.number_served}")

# Incrementing the number of customers served using increment_number_served method
restaurant.increment_number_served(30)
print(f"Number of customers served after increment: {restaurant.number_served}")
