class User:
    def __init__(self, first_name, last_name, age, email, location):
        # Initializing attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Default value of login_attempts

    def describe_user(self):
        # Method to describe the user's profile
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        # Method to print a personalized greeting
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        # Method to increment login attempts
        self.login_attempts += 1

    def reset_login_attempts(self):
        # Method to reset login attempts to 0
        self.login_attempts = 0


# Admin class inherits from User class
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges):
        # Initialize the parent class
        super().__init__(first_name, last_name, age, email, location)
        # Initialize Admin specific attribute
        self.privileges = privileges

    def show_privileges(self):
        # Method to display the admin's privileges
        print(f"Administrator {self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Creating an instance of Admin
admin = Admin("John", "Doe", 40, "john.doe@example.com", "New York", 
              ["can add post", "can delete post", "can ban user", "can manage users"])

# Calling show_privileges() method to display the admin's privileges
admin.show_privileges()
