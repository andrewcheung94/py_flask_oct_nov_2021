from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import doctor

class Patient:
    db_name = "doctors_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.date_of_birth = data['date_of_birth']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.doctor = None # Placeholder that holds an instance of the Doctor class

    # Method to create a new patient
    @classmethod
    def create_one(cls, data):
        # NEED the foreign key doctor_id as well!
        query = "INSERT INTO patients (name, date_of_birth, doctor_id) VALUES (%(name)s, %(date_of_birth)s, %(doctor_id)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer
    
    # Method to grab a single patient - WITHOUT the doctor
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM patients WHERE id = %(id)s;"
        patient_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        # print(patient_from_db) # Show the list of dictionaries
        # Returns a single one - notice the [0] since patient_from_db is a LIST, even though
        # only one item is in the list - SELECT quries return a LIST of dictionaries
        return cls(patient_from_db[0]) # Convert this item into a class instance, and return it

    # Grabs one patient WITH the doctor included
    @classmethod
    def get_one_with_doctor(cls, data):
        query = "SELECT * FROM patients JOIN doctors ON doctors.id = patients.doctor_id WHERE patients.id = %(id)s;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        patient_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        patient_instance = cls(patient_from_db[0])
        print(patient_from_db) # Show the list of dictionaries
        # Loop through all the patients for this patient
            # Grab patient data - notice the table names added where column names are shared between tables!
        doctor_data = {
            "id": patient_from_db[0]['doctors.id'],
            "name": patient_from_db[0]['doctors.name'],
            "created_at": patient_from_db[0]['doctors.created_at'],
            "updated_at": patient_from_db[0]['doctors.updated_at'],
        }
        patient_instance.doctor = doctor.Doctor(doctor_data) # cls(data) makes an instance of a class
        return patient_instance # Return patient with the doctor
    
    # Get all the patients - NO doctors linked
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM patients;"
        # Grab a list of dictionaries, where each dictionary is a row from the DB
        patients_from_db = connectToMySQL(cls.db_name).query_db(query)
        # print(patients_from_db) # Show the list of dictionaries
        patients = [] # List that will hold CLASS objects
        for patient in patients_from_db:
            patients.append(cls(patient)) # cls(data) makes an instance of a class
        return patients

    # Get all the patients - WITH their doctors
    @classmethod
    def get_all_with_doctors(cls):
        query = "SELECT * FROM patients JOIN doctors ON doctors.id = patients.doctor_id;"
        patients_from_db = connectToMySQL(cls.db_name).query_db(query)
        print(patients_from_db) # Show the list of dictionaries
        patient_instances = [] # List of instances of the Car class
        for this_patient in patients_from_db: # Loop through all patients
            this_patient_instance = cls(this_patient) # Create instance of Car class
            # Get doctor for this patient
            doctor_data = {
                "id": this_patient['doctors.id'],
                "name": this_patient['doctors.name'],
                "created_at": this_patient['doctors.created_at'],
                "updated_at": this_patient['doctors.updated_at'],
            }
            this_doctor = doctor.Doctor(doctor_data) # Create an instance of the Doctor class
            this_patient_instance.doctor = this_doctor # This links the doctor object to this specific patient
            patient_instances.append(this_patient_instance) # Append the patient with the doctor linked to it
        return patient_instances # Return all the patients with the doctors linked accordingly

    # Update a patient
    @classmethod
    def edit_one(cls, data):
        # NEED FOREIGN KEY doctor_id!
        query = "UPDATE patients SET name = %(name)s, date_of_birth = %(date_of_birth)s, doctor_id = %(doctor_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Delete a patient
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM patients WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)