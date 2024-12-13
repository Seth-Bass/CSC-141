# user.py

class User:
    def __init__(self, first_name, last_name, age, email, location):
        # Initializing user attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        # Method to describe the user
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        # Method to greet the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
