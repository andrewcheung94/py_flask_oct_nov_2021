# Define a class of animals
class Animal():
    # Class variables that can be accessed through class methods and also through instance methods (those with "self"
    # as a parameter)
    total_animals = 0 # Class variable
    all_animals = [] # Empty list of instances of animals to start

    # From Mel: A link on the init method
    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

    # Constructor that makes an instance of an animal
    def __init__(self, name, num_legs, spd, hgt, wgt, eye_col, fur_piece = None):
        self.name = name
        self.legs = num_legs
        self.speed = spd
        self.height = hgt
        self.weight = wgt
        self.eye_color = eye_col
        self.fur = fur_piece
        Animal.total_animals += 1
        Animal.all_animals.append(self) # Store the created animal in the list

    # growth_rate = amount of inches to increase the height of the animal by
    def heighten_animal(self, growth_rate): # Instance method because of the word "self"
        self.height += growth_rate
        # print(Animal.total_animals) # You can access class variables here as well!
        return self # Allows for chaining of commands

    @classmethod
    def count_animals(cls): # Notice the cls - cls.class_variable for class variables, akin to self.instance_variable
        return cls.total_animals

    @classmethod
    def average_weight(cls):
        total_weight = 0
        # Loop through all the created animals stored in the class variable all_animals
        for cur_animal in cls.all_animals:
            total_weight += cur_animal.weight
        return total_weight / cls.total_animals

    # Useful way to overwrite print(class_instance) with more "readable" output
    def __str__(self):
        return f"Animal named {self.name}"

cat = Animal("cat",4, 10, 3, 2, "brown") # Creating an instance of an animal
cat.heighten_animal(5).heighten_animal(3) # Chaining example here
print(cat.height)
print(cat.legs)

bear = Animal("bear",2, 20, 84, 250, "blue") # Another instance of an animal
print(bear.legs)

print(Animal.total_animals)
print(Animal.all_animals)

print(Animal.average_weight())

print(bear)