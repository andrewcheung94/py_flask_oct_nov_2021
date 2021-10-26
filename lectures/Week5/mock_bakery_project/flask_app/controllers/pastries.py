from flask_app import app # NEED this line
from flask import render_template,redirect,request
from flask_app.models.pastry import Pastry # Import each model needed here!

# Controllers contan all the logic for all your routes.  They call on the models, which
# will handle all the interactions with the database.

# Showing all the pastries
@app.route("/")
def all_pastries():
    # Grab all the pastries from the database
    pastries = Pastry.get_all()
    # Show them all on one page
    return render_template("all_pastries.html", pastries = pastries)

# Showing just one pastry - NO EDITING
@app.route("/pastries/<int:id>")
def show_pastry(id):
    # When sending data through a query, you MUST pass in a dictionary!!
    data = {
        "id": id,
    }
    # Grab just this pastry from the database - remember to put the data in!
    pastry = Pastry.get_one(data)
    # Send the data to the HTML
    return render_template("show_one_pastry.html", pastry = pastry)

# Editing a pastry - SHOWING THE FORM
@app.route("/pastries/<int:id>/edit_page")
def edit_pastry_page(id):
    data = {
        "id": id,
    }
    # Grab just this pastry from the database
    pastry = Pastry.get_one(data)
    # Show edit page for this pastry
    return render_template("edit_pastry.html", pastry = pastry)

# Editing a pastry - ACTUALLY SAVING THE CHANGES
@app.route("/pastries/<int:id>/edit", methods=["POST"])
def edit_pastry(id):
    data = {
        "id": id, # Notice the id is a path variable, NOT from the form
        "flavor": request.form["flavor"],
        "name": request.form["name"],
        "size": request.form["size"],
        "price": request.form["price"],
    }
    Pastry.edit_one(data) # Save the changes for this pastry
    return redirect("/")

# Creating a new pastry - SHOWING THE FORM
@app.route("/pastries/new_page")
def new_pastry_page():
    return render_template("new_pastry.html")

# Creating a new pastry - ACTUALLY CREATES IT IN THE DATABASE
@app.route("/pastries/new", methods=["POST"])
def new_pastry():
    data = {
        "flavor": request.form["flavor"],
        "name": request.form["name"],
        "size": request.form["size"],
        "price": request.form["price"],
    }
    # print(data)
    Pastry.create_one(data)
    # print("Created successfully")
    return redirect("/")

# Deleting a pastry - it's HIGHLY recommended to put this is a POST request so that
# random clicks or links won't delete from the database!
@app.route("/pastries/<int:id>/delete", methods=["POST"])
def delete_pastry(id):
    data = {
        "id": id
    }
    Pastry.delete_one(data)
    return redirect("/")
