from flask_app.config.mysqlconnection import connectToMySQL

class Car:
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

    # Method to create a new car - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.  Don't use {} like I did!
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO cars (name, max_speed, fuel_efficiency, door_count, gas_tank_size) VALUES (%(name)s, %(max_speed)s, %(fuel_efficiency)s, %(door_count)s, %(gas_tank_size)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data) # Returns an integer

    # Method to grab all the cars
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        cars_from_db = connectToMySQL('manufacturers_cars_schema').query_db(query)
        # print(cars_from_db) # Show the list of dictionaries
        cars = [] # List that will hold CLASS objects
        for car in cars_from_db:
            cars.append(cls(car)) # cls(data) makes an instance of a class
        return cars

    # Method to grab just one car from the datbase
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        car_from_db = connectToMySQL('manufacturers_cars_schema').query_db(query, data)
        # print(car_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since car_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(car_from_db[0]) # Convert this item into a class instance, and return it

    @classmethod
    def edit_one(cls, data):
        query = "UPDATE cars SET name = %(name)s, max_speed = %(max_speed)s, fuel_efficiency = %(fuel_efficiency)s, door_count = %(door_count)s, gas_tank_size = %(gas_tank_size)s, WHERE id = %(id)s;"
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data)