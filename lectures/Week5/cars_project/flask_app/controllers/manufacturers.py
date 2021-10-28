from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.manufacturer import Manufacturer # Import each model needed here!

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# Have root rout show all manufacturers
@app.route("/")
def index():
    return redirect("/manufacturers")

# Showing all the manufacturers
@app.route("/manufacturers")
def all_manufacturers():
    # Grab all the manufacturers from the database
    manufacturers = Manufacturer.get_all_with_cars() # Now with cars attached
    # Show them all on one page
    return render_template("all_manufacturers.html", manufacturers = manufacturers)

# Showing just one manufacturer - NO EDITING
@app.route("/manufacturers/<int:id>")
def show_manufacturer(id):
    # When sending data through a query, you MUST pass in a dictionary!!
    data = {
        "id": id,
    }
    # Grab just this manufacturer from the database - remember to put the data in!
    manufacturer = Manufacturer.get_one_with_cars(data)
    # Send the data to the HTML
    return render_template("show_one_manufacturer.html", manufacturer = manufacturer)

# Editing a manufacturer - SHOWING THE FORM
@app.route("/manufacturers/<int:id>/edit_page")
def edit_manufacturer_page(id):
    data = {
        "id": id,
    }
    # Grab just this manufacturer from the database
    manufacturer = Manufacturer.get_one(data)
    # Show edit page for this manufacturer
    return render_template("edit_manufacturer.html", manufacturer = manufacturer)

# Editing a manufacturer - ACTUALLY SAVING THE CHANGES
@app.route("/manufacturers/<int:id>/edit", methods=["POST"])
def edit_manufacturer(id):
    data = {
        "id": id, # Notice the id is a path variable, NOT from the form
        "name": request.form["name"],
    }
    Manufacturer.edit_one(data) # Save the changes for this manufacturer
    return redirect("/manufacturers")

# Creating a new manufacturer - SHOWING THE FORM
@app.route("/manufacturers/new_page")
def new_manufacturer_page():
    return render_template("new_manufacturer.html")

# Creating a new manufacturer - ACTUALLY CREATES IT IN THE DATABASE
@app.route("/manufacturers/new", methods=["POST"])
def new_manufacturer():
    data = {
        "name": request.form["name"],
    }
    # print(data)
    Manufacturer.create_one(data)
    # print("Created successfully")
    return redirect("/manufacturers")

# Deleting a manufacturer - it's HIGHLY recommended to put this is a POST request so that
# random clicks or links won't delete from the database!
@app.route("/manufacturers/<int:id>/delete", methods=["POST"])
def delete_manufacturer(id):
    data = {
        "id": id
    }
    Manufacturer.delete_one(data)
    return redirect("/manufacturers")
