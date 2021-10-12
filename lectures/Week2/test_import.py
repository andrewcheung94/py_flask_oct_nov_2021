# from test_package import my_math_functions # my_math_functions is the name of the module (file) you're bringing in
# # from OOP import Car # Method A
import OOP # Method B

# import random # Method A
from random import randint # Method B

# # NOT ADVISED
# # from test_package import * # Import everything - not recommended

# print(my_math_functions.add(8,10))

# # Method A
# my_car = Car("Sentra","gray",25,40,140)
# print(my_car.gas_tank_size)

# Method B
my_car = OOP.Car("Sentra","gray",25,40,140)
print(my_car.gas_tank_size)

# Two ways to import a random function

# Method A
# for i in range(50):
#     print(random.randint(1,10))

# Method B
for i in range(50):
    print(randint(1,10))