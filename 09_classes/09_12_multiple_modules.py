# main.py

from admin import Admin

# Creating an instance of Admin with a list of privileges
admin = Admin(
    "John", "Doe", 40, "john.doe@example.com", "New York",
    ["can add post", "can delete post", "can ban user", "can manage users"]
)

# Calling show_privileges() method to display the admin's privileges
admin.privileges.show_privileges()
