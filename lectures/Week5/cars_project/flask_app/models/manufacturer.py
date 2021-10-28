from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import car # IMPORT the FILE, NOT the class - to avoid circular imports

class Manufacturer:
    db_name = 'manufacturers_cars_schema' # Class variable that holds database we'll link to

    # Model for the manufacturer - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = [] # This list will eventually hold instances of Car objects linked to this individual manufacturer

    # Method to create a new manufacturer - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.  Don't use {} like I did!
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO manufacturers (name) VALUES (%(name)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    # Method to grab all the manufacturers - WITHOUT cars linked to them
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM manufacturers;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        manufacturers_from_db = connectToMySQL(cls.db_name).query_db(query)
        # print(manufacturers_from_db) # Show the list of dictionaries
        manufacturers = [] # List that will hold CLASS objects
        for manufacturer in manufacturers_from_db:
            manufacturers.append(cls(manufacturer)) # cls(data) makes an instance of a class
        return manufacturers

    # Method to grab all the manufacturers - WITH cars
    @classmethod
    def get_all_with_cars(cls):
        query = "SELECT * FROM manufacturers LEFT JOIN cars ON manufacturers.id = cars.manufacturer_id;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        manufacturers_from_db_with_cars = connectToMySQL(cls.db_name).query_db(query)
        # manufacturer_instance = cls(manufacturer_from_db_with_cars[0])
        print(manufacturers_from_db_with_cars) # Show the list of dictionaries
        # If no manufacturers found, return an empty list
        if len(manufacturers_from_db_with_cars) == 0:
            return []
        manufacturers = [] # List that will hold CLASS objects
        cur_manufacturer_instance = None # Starting variable with nothing to begin
        # Loop through each row in the grabbed data - each row either has a manufacturer only OR
        # a manufacturer with a car joined
        for k in range(len(manufacturers_from_db_with_cars)):
            cur_row_in_db = manufacturers_from_db_with_cars[k] # Grab current dictionary from list
            # If at beginning of loop OR current manufacturer's ID is different from manufacturer in previous row
            if k == 0 or cur_row_in_db["id"] != manufacturers_from_db_with_cars[k-1]["id"]:
                if cur_manufacturer_instance != None: # If previous instance of manufacturer is found, then add this to list since that one is done
                    manufacturers.append(cur_manufacturer_instance)
                # Grab data for new manufacturer
                cur_manufacturer_data = {
                    "id": cur_row_in_db['id'],
                    "name": cur_row_in_db['name'],
                    "created_at": cur_row_in_db['created_at'],
                    "updated_at": cur_row_in_db['updated_at'],
                }
                cur_manufacturer_instance = cls(cur_manufacturer_data) # Create instance of Manufacturer
            # Grab data for car - regardless of if new or old manufacturer
            cur_car_data = {
                "id": cur_row_in_db['cars.id'],
                "name": cur_row_in_db['cars.name'],
                "max_speed": cur_row_in_db['max_speed'],
                "fuel_efficiency": cur_row_in_db['fuel_efficiency'],
                "door_count": cur_row_in_db['door_count'],
                "gas_tank_size": cur_row_in_db['gas_tank_size'],
                "created_at": cur_row_in_db['cars.created_at'],
                "updated_at": cur_row_in_db['cars.updated_at'],
            }
            cur_car_instance = car.Car(cur_car_data) # Create instance of Car class
            cur_manufacturer_instance.cars.append(cur_car_instance) # Add this car to this manufacturer
            if k == len(manufacturers_from_db_with_cars)-1: # If at end of the list, add manufacturer since the loop will end
                manufacturers.append(cur_manufacturer_instance)
        return manufacturers # Return list of Manufacturers

    # Method to grab just one manufacturer from the datbase - with NO cars attached
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM manufacturers WHERE id = %(id)s;"
        manufacturer_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        # print(manufacturer_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since manufacturer_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(manufacturer_from_db[0]) # Convert this item into a class instance, and return it

    # Grab a manufacturer WITH cars attached
    @classmethod
    def get_one_with_cars(cls, data):
        # Notice the LEFT JOIN - we need to grab the manufacturer, even if they haven't had a car linked
        query = "SELECT * FROM manufacturers LEFT JOIN cars ON manufacturers.id = cars.manufacturer_id WHERE manufacturers.id = %(id)s;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        manufacturer_from_db_with_cars = connectToMySQL(cls.db_name).query_db(query, data)
        manufacturer_instance = cls(manufacturer_from_db_with_cars[0])
        print(manufacturer_from_db_with_cars) # Show the list of dictionaries
        # Loop through all the cars for this manufacturer
        for this_car in manufacturer_from_db_with_cars:
            # Grab car data - notice the table names added where column names are shared between tables!
            car_data = {
                "id": this_car['cars.id'],
                "name": this_car['cars.name'],
                "max_speed": this_car['max_speed'],
                "fuel_efficiency": this_car['fuel_efficiency'],
                "door_count": this_car['door_count'],
                "gas_tank_size": this_car['gas_tank_size'],
                "created_at": this_car['cars.created_at'],
                "updated_at": this_car['cars.updated_at'],
            }
            manufacturer_instance.cars.append(car.Car(car_data)) # cls(data) makes an instance of a class
        return manufacturer_instance # Return manufacturer with cars

    # Edit method
    @classmethod
    def edit_one(cls, data):
        query = "UPDATE manufacturers SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM manufacturers WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)