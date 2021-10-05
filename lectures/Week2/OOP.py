class Car: # Model names should start with a capital (upper-case) letter, and be singular (not plural)
    # Class variables
    all_cars = [] # List of all cars created
    average_speed = 0 # Average speed of all cars

    # Constructor - build instances of Cars through the __init__ method
    def __init__(self, name, car_color, gas_tank, fuel_efficiency, top_speed):
        # Color, name, type, top speed, engine, traction, transmission, gas_tank_size, fuel type, fuel efficiency
        self.color = car_color
        self.name = name
        self.gas_tank_size = gas_tank
        self.fuel_efficiency = fuel_efficiency
        self.max_speed = top_speed
        self.current_fuel = 0 # Hold amount of fuel CURRENTLY in the tank
        Car.all_cars.append(self) # To access a class variable, you type Class_name.class_variable
    
    # Method to fill the tank of the car
    def fill_tank(self,num_gallons_to_add):
        self.current_fuel += num_gallons_to_add
        return self

    @classmethod
    def get_biggest_tank(cls):
        # print(cls.all_cars[1].gas_tank_size)
        max_tank = cls.all_cars[0].gas_tank_size
        # self.color # ILLEGAL - cannot directly access an individual car's attributes, like color, name, etc.
        for this_car in cls.all_cars[1:]: # Loop through cars, starting with the 2nd car
            if this_car.gas_tank_size > max_tank:
                max_tank = this_car.gas_tank_size
        return max_tank
    
    # Static methods do NOT grant access to class OR instance (those with self) variables
    @staticmethod
    def is_tank_empty(current_fuel):
        if current_fuel == 0:
            return True
        else:
            return False

class Manufacturer:
    all_cars_made = [] # List of all cars from all manufacturers

    def __init__(self,name):
        self.name = name # Name of manufacturer
        self.cars_made = [] # List of all cars for this manufacturer
        # self.top_seller = Car()

    # Add a car to a manufacturer - provided it's not a duplicate
    def add_car(self,car_model):
        # If car was not already added, add it
        if Manufacturer.duplicate_car_validation(car_model) == True: # Can omit the "== True" part
            print("Not a duplicate")
            self.cars_made.append(car_model)
            Manufacturer.all_cars_made.append(car_model)
        else:
            print("is a duplicate")
        return self # To allow for chaining

    # Class method where we check to see if a car has already been added among all manufacturers
    @classmethod
    def duplicate_car_validation(cls, some_car):
        for this_car in cls.all_cars_made: # Loop through all cars made
            if this_car == some_car: # If car is same, it's a duplicate, so return False
                return False
        return True # Not a duplicate

# Instances of cars
corvette = Car("Corvette","black",50,20,200)
prius = Car("Prius","blue",9,60,120)
golden_hawk = Car("Golden Hawk","gold",300,10,220)
malibu = Car("Malibu","white",30,20,150)

# Instance of a manufacturer
chevrolet = Manufacturer("Chevrolet")
chevrolet.add_car(corvette)
chevrolet.add_car(malibu)
chevrolet.add_car(corvette) # Won't add since it's a duplicate

# print(corvette.fuel_efficiency)
# print(corvette)
corvette.fill_tank(10).fill_tank(5)
# print(corvette.current_fuel)

# Demonstrating accessing class methods and variables - notice it's Class_name.variable_or_method
# print(Car.fuel_efficiency) # doesn't work since fuel_efficiency is NOT a class variable
print(Car.average_speed) # OK
print(Car.get_biggest_tank())

# Demonstrating a static method
print(Car.is_tank_empty(prius.current_fuel))
print(prius.is_tank_empty(prius.current_fuel))