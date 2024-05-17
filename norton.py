class Bike:
    def __init__(self, brand, model, color, gear_count):
        self.brand = brand
        self.model = model
        self.color = color
        self.gear_count = gear_count
    
    def bike_info(self):
        return f"{self.color} {self.brand} {self.model} with {self.gear_count} gears"
    
    def change_gear(self, new_gear_count):
        self.gear_count = new_gear_count
        return f"Gears changed to {self.gear_count}"

# Create instances of Bike
bike1 = Bike("Trek", "Domane", "red", 22)
bike2 = Bike("Giant", "Defy", "blue", 18)

# Display bike information
print(bike1.bike_info())
print(bike2.bike_info())

# Change gear count for bike1
print(bike1.change_gear(24))
