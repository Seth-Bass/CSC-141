# admin.py

from user import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        # Method to display the privileges
        print("The following privileges are granted:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges):
        # Initialize the parent class (User)
        super().__init__(first_name, last_name, age, email, location)
        # Initialize Privileges as an attribute
        self.privileges = Privileges(privileges)
