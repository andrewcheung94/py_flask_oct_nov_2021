from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.car import Car # Import each model needed here!

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# Showing all the cars
@app.route("/cars")
def all_cars():
    # Grab all the cars from the database
    cars = Car.get_all()
    # Show them all on one page
    return render_template("all_cars.html", cars = cars)

# Showing just one car - NO EDITING
@app.route("/cars/<int:id>")
def show_car(id):
    # When sending data through a query, you MUST pass in a dictionary!!
    data = {
        "id": id,
    }
    # Grab just this car from the database - remember to put the data in!
    car = Car.get_one(data)
    # Send the data to the HTML
    return render_template("show_one_car.html", car = car)

# Editing a car - SHOWING THE FORM
@app.route("/cars/<int:id>/edit_page")
def edit_car_page(id):
    data = {
        "id": id,
    }
    # Grab just this car from the database
    car = Car.get_one(data)
    # Show edit page for this car
    return render_template("edit_car.html", car = car)

# Editing a car - ACTUALLY SAVING THE CHANGES
@app.route("/cars/<int:id>/edit", methods=["POST"])
def edit_car(id):
    data = {
        "id": id, # Notice the id is a path variable, NOT from the form
        "fuel_efficiency": request.form["fuel_efficiency"],
        "door_count": request.form["door_count"],
        "gas_tank_size": request.form["gas_tank_size"],
        "name": request.form["name"],
        "max_speed": request.form["max_speed"],
    }
    Car.edit_one(data) # Save the changes for this car
    return redirect("/")

# Creating a new car - SHOWING THE FORM
@app.route("/cars/new_page")
def new_car_page():
    return render_template("new_car.html")

# Creating a new car - ACTUALLY CREATES IT IN THE DATABASE
@app.route("/cars/new", methods=["POST"])
def new_car():
    data = {
        "fuel_efficiency": request.form["fuel_efficiency"],
        "door_count": request.form["door_count"],
        "gas_tank_size": request.form["gas_tank_size"],
        "name": request.form["name"],
        "max_speed": request.form["max_speed"],
    }
    # print(data)
    Car.create_one(data)
    # print("Created successfully")
    return redirect("/")

# Deleting a car - it's HIGHLY recommended to put this is a POST request so that
# random clicks or links won't delete from the database!
@app.route("/cars/<int:id>/delete", methods=["POST"])
def delete_car(id):
    data = {
        "id": id
    }
    Car.delete_one(data)
    return redirect("/")
