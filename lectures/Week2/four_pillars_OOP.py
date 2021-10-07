class Building:
    num_buildings = 0
    # Height, width, color,sq. ft., location, floors, rooms, address, price, windows
    def __init__(self,floors,rooms,color):
        self.num_floors = floors
        self.num_rooms = rooms
        self.color = color # Assume exterior color
        Building.num_buildings += 1

    def repaint(self,new_color):
        self.color = new_color
        return self # To allow for chaining
    
    def expand(self,num_new_rooms, num_new_floors = 0):
        self.num_floors += num_new_floors
        self.num_rooms += num_new_rooms
        print("Expanding this generic building")
        return self

    @classmethod
    def show_number_buildings(cls):
        return cls.num_buildings

# Inheritance - House is inheriting from the Building class
class House(Building):
    # Type of house (single-family, co-op, etc.), bedrooms, price
    def __init__(self,floors,rooms,color,num_of_TVs):
        super().__init__(floors,rooms,color)
        self.num_of_TVs = num_of_TVs
        self.hired_contractor = None

    # Our own expand method - we're overriding the Building's expand method
    def expand(self,num_new_rooms):
        self.num_rooms += num_new_rooms
        print("Expanding this house")
        return self

    # You can add your own methods here - they won't be available by the parent Building class
    def hire_contractor(self,new_contractor):
        self.hired_contractor = new_contractor
        return self

    def build_new_room(self):
        # Only add a room if a contractor was hired
        if self.hired_contractor != None:
            self.num_rooms += 1
            print("New room added")
        else:
            print("No room added - no contractor available")
        return self
    # self.hired_contractor.method_name_from_contractor_class
    # Class variables and methods are also inherited - not just the instance methods

boeing_plant = Building(2,5,"gray")

my_house = House(1,6,"yellow",3)

boeing_plant.expand(3,2)
my_house.expand(2)

boeing_plant.repaint("blue")
print(boeing_plant.color)
my_house.repaint("white")
print(my_house.color)

# New class for Contractor - no inheritance here; feel free to have the contractor do stuff!
class Contractor:
    def __init__(self,name):
        self.name = name


john_contractor = Contractor("John Contractor")
my_house.build_new_room() # Won't work
my_house.hire_contractor(john_contractor)

my_house.build_new_room() # Now will work