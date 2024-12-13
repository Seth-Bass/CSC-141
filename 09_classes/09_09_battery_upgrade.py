class Battery:
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def get_range(self):
        # Return the range based on battery size
        if self.battery_size == 50:
            range = 200  # Assume the range is 200 miles for a 50 kWh battery
        elif self.battery_size == 65:
            range = 250  # Assume the range is 250 miles for a 65 kWh battery
        else:
            range = 0  # Just in case there are unexpected battery sizes
        return range

    def upgrade_battery(self):
        # If the battery size is less than 65, upgrade it
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at the maximum size of 65 kWh.")


class ElectricCar:
    def __init__(self, make, model, year, battery_size=50):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery(battery_size)  # Each car has a battery

    def get_car_info(self):
        # Return a summary of the car's information
        return f"{self.year} {self.make} {self.model}"

    def get_range(self):
        # Call the get_range method of the Battery class to get the range of the car
        return self.battery.get_range()


# Create an electric car with the default battery size of 50 kWh
my_car = ElectricCar("Tesla", "Model S", 2022)

# Print the car info and the range before upgrading the battery
print(f"Car info: {my_car.get_car_info()}")
print(f"Range before upgrade: {my_car.get_range()} miles")

# Upgrade the battery
my_car.battery.upgrade_battery()

# Print the range after upgrading the battery
print(f"Range after upgrade: {my_car.get_range()} miles")
