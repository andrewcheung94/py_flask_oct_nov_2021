from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.doctor import Doctor # Import each model needed here!
from flask_app.models.patient import Patient

# Empty route (localhost:5000)
@app.route("/")
def index():
    return redirect("/doctors")

# Page for adding a doctor - HTML
@app.route("/new_doctor")
def new_doctor_page():
    return render_template("new_doctor.html")

# POST method to create the doctor - POST
@app.route("/create_doctor", methods=["GET","POST"])
def create_doctor():
    if request.method == "GET":
        return redirect("/new_doctor")
    # If we reach this point, this is a POST request
    data = {
        "name": request.form["name"],
    }
    # INSERT queries return a number if it runs
    new_doctor_id = Doctor.create_one(data)
    # Redirect to the new doctor's page
    return redirect(f"/doctors/{new_doctor_id}")

# Show an individual doctor's page - READ one - HTML
@app.route("/doctors/<int:id>")
def show_doctor_page(id):
    data = {
        "id": id,
    }
    doctor_with_patients = Doctor.get_one_with_patients(data)
    return render_template("individual_doctor.html", doctor = doctor_with_patients)

# Show all the doctors together - READ all - HTML
@app.route("/doctors")
def show_all_doctors():
    all_doctors = Doctor.get_all() # Grab all the doctors
    return render_template("all_doctors.html", doctors = all_doctors)

# Page for editing a doctor - HTML
@app.route("/doctors/<int:id>/edit_page")
def edit_one_doctor_page(id):
    data = {
        "id": id,
    }
    doctor = Doctor.get_one(data)
    return render_template("edit_doctor.html", doctor=doctor)

# POST method to edit the doctor  - POST
@app.route("/doctors/<int:id>/edit", methods=["GET","POST"])
def edit_one_doctor(id):
    if request.method == "GET":
        return redirect(f"/doctors/{id}/edit_page")
    data = {
        "id": id,
        "name": request.form["name"]
    }
    Doctor.edit_one(data)
    return redirect(f"/doctors/{id}")

# Delete a doctor - DELETE one - POST
@app.route("/doctors/<int:id>/delete", methods=["GET","POST"])
def delete_doctor(id):
    if request.method == "GET":
        return redirect("/doctors")
    # Here we will do the actual deleting of the doctor since if we reach this point, we have a POST request
    data = {
        "id": id,
    }
    Doctor.delete_one(data)
    return redirect("/doctors")