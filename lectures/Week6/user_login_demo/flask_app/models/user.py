from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # Need this to display flash messages
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app import app # NEEDED FOR BCRYPT!!
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

class User:
    db_name = 'user_lecture_schema' # Make use of class variable to hold schema name

    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create a new user
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (username, password, email) VALUES (%(username)s, %(password)s, %(email)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    # Method to grab just one user
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        # Returns a single one - notice the [0] since user_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(user_from_db[0]) # Convert this item into a class instance, and return it

    # Validating a new user
    @staticmethod
    def validate_registration(form_data):
        is_valid = True # Start with True always!
        # Make sure the user name is at least 4 characters
        if len(form_data['username']) < 4:
            is_valid = False
            flash("User name must be at least 4 characters.")
        # CHALLENGE: How do you check to see if the user name is unique?  HINT: think about queries.

        # Check email
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False
            flash("Email is invalid.")
        # Confirm that the passwords match
        if form_data['password'] != form_data['confirm_password']:
            is_valid = False
            flash("Passwords do not agree.")
        # Password is at least 10 characters
        if len(form_data['password']) < 10:
            is_valid = False
            flash("Password is not long enough.  Must be 10 or more characters.")
        return is_valid

    # Validating logging in
    @staticmethod
    def validate_login(form_data, data_dictionary):
        is_valid = True
        # Check to see if the username exists in the database
        query = "SELECT * FROM users WHERE username = %(username)s;"
        list_of_users = connectToMySQL(User.db_name).query_db(query, data_dictionary) # Returns an integer
        if len(list_of_users) < 1: # If nobody found
            is_valid = False
            flash("Invalid login credentials.")
            return is_valid # Stop running function - no need to check password
        # Now check password
        this_user = list_of_users[0] # Because this is a list, just grab the one at index 0
        user_instance = User(this_user) # Creates an instance of a User
        if not bcrypt.check_password_hash(user_instance.password, form_data['password']):
            is_valid = False
            # if we get False after checking the password
            flash("Invalid login credentials.")
        # Return ID if the credentials are right
        if is_valid:
            is_valid = user_instance.id
        return is_valid # Return False - invalid credentials OR the id of the user