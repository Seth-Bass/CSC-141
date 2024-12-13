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

# Creating three instances of Restaurant
restaurant1 = Restaurant("The Gourmet Spot", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Taco Fiesta", "Mexican")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
print()  
restaurant2.describe_restaurant()
print()  
restaurant3.describe_restaurant()
