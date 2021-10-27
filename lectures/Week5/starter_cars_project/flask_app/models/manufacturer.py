from flask_app.config.mysqlconnection import connectToMySQL

class Manufacturer:
    # Model for the manufacturer - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Method to create a new manufacturer - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.  Don't use {} like I did!
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO manufacturers (name) VALUES (%(name)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data) # Returns an integer

    # Method to grab all the manufacturers
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM manufacturers;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        manufacturers_from_db = connectToMySQL('manufacturers_cars_schema').query_db(query)
        # print(manufacturers_from_db) # Show the list of dictionaries
        manufacturers = [] # List that will hold CLASS objects
        for manufacturer in manufacturers_from_db:
            manufacturers.append(cls(manufacturer)) # cls(data) makes an instance of a class
        return manufacturers

    # Method to grab just one manufacturer from the datbase
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM manufacturers WHERE id = %(id)s;"
        manufacturer_from_db = connectToMySQL('manufacturers_cars_schema').query_db(query, data)
        # print(manufacturer_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since manufacturer_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(manufacturer_from_db[0]) # Convert this item into a class instance, and return it

    @classmethod
    def edit_one(cls, data):
        query = "UPDATE manufacturers SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM manufacturers WHERE id = %(id)s;"
        return connectToMySQL('manufacturers_cars_schema').query_db(query, data)