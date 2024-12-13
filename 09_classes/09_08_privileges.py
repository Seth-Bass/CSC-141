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


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        # Initialize the privileges list
        self.privileges = privileges

    def show_privileges(self):
        # Method to display the privileges
        print("The following privileges are granted:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges):
        # Initialize the parent class
        super().__init__(first_name, last_name, age, email, location)
        # Initialize Privileges as an attribute
        self.privileges = Privileges(privileges)


# Creating an instance of Admin with a list of privileges
admin = Admin(
    "John", "Doe", 40, "john.doe@example.com", "New York", 
    ["can add post", "can delete post", "can ban user", "can manage users"]
)

# Calling the show_privileges() method through the Privileges instance
admin.privileges.show_privileges()
