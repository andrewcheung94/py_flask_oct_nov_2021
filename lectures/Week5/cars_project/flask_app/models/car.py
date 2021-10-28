from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import manufacturer # IMPORT the FILE, NOT the class - to avoid circular imports

class Car:
    db_name = 'manufacturers_cars_schema' # Make use of class variable to hold schema name
    
    # Model for the car - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.max_speed = data['max_speed']
        self.fuel_efficiency = data['fuel_efficiency']
        self.door_count = data['door_count']
        self.gas_tank_size = data['gas_tank_size']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.manufacturer = None # Placeholder that will hold an instance of a Manufacturer

    # Method to create a new car - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.  Don't use {} like I did!
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        # Also notice the manufacturer_id - the foreign key!
        query = "INSERT INTO cars (name, max_speed, fuel_efficiency, door_count, gas_tank_size, manufacturer_id) VALUES (%(name)s, %(max_speed)s, %(fuel_efficiency)s, %(door_count)s, %(gas_tank_size)s, %(manufacturer_id)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    # Method to grab all the cars
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        cars_from_db = connectToMySQL(cls.db_name).query_db(query)
        # print(cars_from_db) # Show the list of dictionaries
        cars = [] # List that will hold CLASS objects
        for car in cars_from_db:
            cars.append(cls(car)) # cls(data) makes an instance of a class
        return cars

    # Method to grab just one car from the datbase - without the manufacturer
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        car_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        # print(car_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since car_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(car_from_db[0]) # Convert this item into a class instance, and return it
    
    @classmethod
    def get_one_with_manufacturer(cls,data):
        # Grab a list - even though there's only one car, SELECT queries return a LIST
        query = "SELECT * FROM cars JOIN manufacturers ON cars.manufacturer_id = manufacturers.id WHERE cars.id = %(id)s;"
        car_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        print(car_from_db) # Show the list of dictionaries
        car_instance = cls(car_from_db[0]) # Create instance of Car - note the index 0 here since the data is a list!
        manufacturer_data = {
            "id": car_from_db[0]['manufacturers.id'],
            "name": car_from_db[0]['manufacturers.name'],
            "created_at": car_from_db[0]['manufacturers.created_at'],
            "updated_at": car_from_db[0]['manufacturers.updated_at'],
        }
        this_manufacturer = manufacturer.Manufacturer(manufacturer_data) # Create an instance of the Manufacturer class
        car_instance.manufacturer = this_manufacturer # This links the manufacturer object to this specific car
        return car_instance # Return the car with the manufacturer
    
    @classmethod
    def get_all_with_manufacturers(cls):
        query = "SELECT * FROM cars JOIN manufacturers ON cars.manufacturer_id = manufacturers.id;"
        cars_from_db = connectToMySQL(cls.db_name).query_db(query)
        print(cars_from_db) # Show the list of dictionaries
        car_instances = [] # List of instances of the Car class
        for this_car in cars_from_db: # Loop through all cars
            this_car_instance = cls(this_car) # Create instance of Car class
            # Get manufacturer for this car
            manufacturer_data = {
                "id": this_car['manufacturers.id'],
                "name": this_car['manufacturers.name'],
                "created_at": this_car['manufacturers.created_at'],
                "updated_at": this_car['manufacturers.updated_at'],
            }
            this_manufacturer = manufacturer.Manufacturer(manufacturer_data) # Create an instance of the Manufacturer class
            this_car_instance.manufacturer = this_manufacturer # This links the manufacturer object to this specific car
            car_instances.append(this_car_instance) # Append the car with the manufacturer linked to it
        return car_instances # Return all the cars with the manufacturers linked accordingly

    @classmethod
    def edit_one(cls, data):
        # Note the added manufacturer_id here!
        query = "UPDATE cars SET name = %(name)s, max_speed = %(max_speed)s, fuel_efficiency = %(fuel_efficiency)s, door_count = %(door_count)s, gas_tank_size = %(gas_tank_size)s, manufacturer_id = %(manufacturer_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)