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


# IceCreamStand class inherits from Restaurant class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # Initialize the parent class
        super().__init__(restaurant_name, cuisine_type)
        # Initialize IceCreamStand specific attribute
        self.flavors = flavors

    def display_flavors(self):
        # Method to display the ice cream flavors
        print(f"Available Ice Cream Flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"])

# Calling the display_flavors() method
ice_cream_stand.display_flavors()
