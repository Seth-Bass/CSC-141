class User:
    def __init__(self, first_name, last_name, age, email, location):
        # Initializing attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        # Method to describe the user's profile
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        # Method to print a personalized greeting
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

# Creating several instances of User
user1 = User("Alice", "Johnson", 28, "alice.johnson@example.com", "New York")
user2 = User("Bob", "Smith", 35, "bob.smith@example.com", "Los Angeles")
user3 = User("Charlie", "Brown", 22, "charlie.brown@example.com", "Chicago")

# Calling describe_user() and greet_user() for each user
user1.describe_user()
user1.greet_user()
print()  # Adding space between user profiles

user2.describe_user()
user2.greet_user()
print()  # Adding space between user profiles

user3.describe_user()
user3.greet_user()
