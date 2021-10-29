from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.doctor import Doctor # Import each model needed here!
from flask_app.models.patient import Patient

# Page for adding a patient - HTML
@app.route("/new_patient")
def new_patient_page():
    all_doctors = Doctor.get_all()
    return render_template("new_patient.html", doctors = all_doctors)

# POST method to create the patient - POST
@app.route("/create_patient", methods=["GET","POST"])
def create_patient():
    if request.method == "GET":
        return redirect("/new_patient")
    # If we reach this point, this is a POST request
    data = {
        "name": request.form["name"],
        "date_of_birth": request.form["date_of_birth"],
        "doctor_id": request.form["doctor_id"],
    }
    # INSERT queries return a number if it runs
    new_patient_id = Patient.create_one(data)
    # Redirect to the new patient's page
    return redirect(f"/patients/{new_patient_id}")

# Show an individual patient's page - READ one - HTML
@app.route("/patients/<int:id>")
def show_patient_page(id):
    data = {
        "id": id,
    }
    patient_with_doctor = Patient.get_one_with_doctor(data)
    return render_template("individual_patient.html", patient = patient_with_doctor)

# Show all the patients together - READ all - HTML
@app.route("/patients")
def show_all_patients():
    all_patients = Patient.get_all_with_doctors() # Grab all the patients
    return render_template("all_patients.html", patients = all_patients)

# Page for editing a patient - HTML
@app.route("/patients/<int:id>/edit_page")
def edit_one_patient_page(id):
    data = {
        "id": id,
    }
    patient = Patient.get_one_with_doctor(data)
    all_doctors = Doctor.get_all() # NEED THIS to list all the doctors!
    return render_template("edit_patient.html", patient=patient, doctors = all_doctors)

# POST method to edit the patient  - POST
@app.route("/patients/<int:id>/edit", methods=["GET","POST"])
def edit_one_patient(id):
    if request.method == "GET":
        return redirect(f"/patients/{id}/edit_page")
    data = {
        "id": id,
        "name": request.form["name"],
        "date_of_birth": request.form["date_of_birth"],
        "doctor_id": request.form["doctor_id"],
    }
    Patient.edit_one(data)
    return redirect(f"/patients/{id}")

# Delete a patient - DELETE one - POST
@app.route("/patients/<int:id>/delete", methods=["GET","POST"])
def delete_patient(id):
    if request.method == "GET":
        return redirect("/patients")
    # Here we will do the actual deleting of the patient since if we reach this point, we have a POST request
    data = {
        "id": id,
    }
    Patient.delete_one(data)
    return redirect("/patients")