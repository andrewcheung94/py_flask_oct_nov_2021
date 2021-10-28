from flask_app.config.mysqlconnection import connectToMySQL

class Pastry:
    db = 'bakery_schema' # Name of the database/schema you'll use - class variable
    # Model for the pastry - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.flavor = data['flavor']
        self.size = data['size']
        self.name = data['name']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Method to create a new pastry - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.  Don't use {} like I did!
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO baked_goods (flavor, price, size, name) VALUES (%(flavor)s, %(price)s, %(size)s, %(name)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db).query_db(query, data) # Returns an integer

    # Method to grab all the pastries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM baked_goods;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        pastries_from_db = connectToMySQL(cls.db).query_db(query)
        # print(pastries_from_db) # Show the list of dictionaries
        pastries = [] # List that will hold CLASS objects
        for pastry in pastries_from_db:
            pastries.append(cls(pastry)) # cls(data) makes an instance of a class
        return pastries

    # Method to grab just one pastry from the datbase
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM baked_goods WHERE id = %(id)s;"
        pastry_from_db = connectToMySQL(cls.db).query_db(query, data)
        # print(pastry_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since pastry_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(pastry_from_db[0]) # Convert this item into a class instance, and return it

    @classmethod
    def edit_one(cls, data):
        query = "UPDATE baked_goods SET flavor = %(flavor)s, price = %(price)s, size = %(size)s, name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM baked_goods WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)