from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import patient

class Doctor:
    db_name = "doctors_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.patients = [] # Placeholder list that will hold all the patients linked to the doctor

    # Method to create a new doctor
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO doctors (name) VALUES (%(name)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer
    
    # Method to grab a single doctor - WITHOUT patients
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM doctors WHERE id = %(id)s;"
        doctor_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        # print(doctor_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since doctor_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(doctor_from_db[0]) # Convert this item into a class instance, and return it

    # Grabs one doctor with ALL their patients
    @classmethod
    def get_one_with_patients(cls, data):
        # Notice the LEFT JOIN - we need to grab the doctor, even if they haven't had a patient linked
        query = "SELECT * FROM doctors LEFT JOIN patients ON doctors.id = patients.doctor_id WHERE doctors.id = %(id)s;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        doctor_from_db_with_patients = connectToMySQL(cls.db_name).query_db(query, data)
        doctor_instance = cls(doctor_from_db_with_patients[0])
        print(doctor_from_db_with_patients) # Show the list of dictionaries
        # Loop through all the patients for this doctor
        for this_patient in doctor_from_db_with_patients:
            # Grab patient data - notice the table names added where column names are shared between tables!
            patient_data = {
                "id": this_patient['patients.id'],
                "name": this_patient['patients.name'],
                "date_of_birth": this_patient['date_of_birth'],
                "created_at": this_patient['patients.created_at'],
                "updated_at": this_patient['patients.updated_at'],
            }
            doctor_instance.patients.append(patient.Patient(patient_data)) # cls(data) makes an instance of a class
        return doctor_instance # Return manufacturer with cars
    
    # Get all the doctors - NO patients linked
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM doctors;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        doctors_from_db = connectToMySQL(cls.db_name).query_db(query)
        # print(doctors_from_db) # Show the list of dictionaries
        doctors = [] # List that will hold CLASS objects
        for doctor in doctors_from_db:
            doctors.append(cls(doctor)) # cls(data) makes an instance of a class
        return doctors

    # Update a doctor
    @classmethod
    def edit_one(cls, data):
        query = "UPDATE doctors SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Delete a doctor
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM doctors WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)