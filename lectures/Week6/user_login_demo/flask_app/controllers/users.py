from flask_app import app # NEED this line
from flask import render_template, redirect, request, session
from flask_app.models.user import User # Import each model needed here!
from flask_bcrypt import Bcrypt # For login/registration
bcrypt = Bcrypt(app)

# Login/registration page with the forms
@app.route("/")
def login_registration_page():
    # If someone is logged in, send back to landing page
    if "user_id" in session:
        return redirect("/landing")
    # If not, show login/registration page
    return render_template("login_reg.html")

# Route for handling registration
@app.route("/register", methods=["POST"])
def register_new_user():
    if not User.validate_registration(request.form):
        return redirect("/") # Send back to login/registration page
    # At this point, registration passes
    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']), # Hashed passwaord - MUST be hashed before saving
    }
    # Save ID of new user - do NOT save instance of User class in session!
    session['user_id'] = User.create_user(data)
    return redirect("/landing")

# Route for handling logging in
@app.route("/login", methods=["POST"])
def process_login():
    # Check based on username
    data = {
        "username": request.form["username"],
    }
    # Returns False if credentials are invalid OR the id if found
    acceptable_id = User.validate_login(request.form, data)
    if acceptable_id == False:
        return redirect("/") # Send if not found or credentials
    session['user_id'] = acceptable_id
    return redirect("/landing")

# Show landing page
@app.route("/landing")
def landing_page():
    # If you're not logged in, you're sent back to the login/registration page
    if "user_id" not in session:
        return redirect("/")
    # Grab user from database
    data = {
        "id": session['user_id'],
    }
    this_user = User.get_one(data)
    return render_template("landing_page.html",user=this_user)

# Log out and redirect to login/reg pege
@app.route("/logout")
def log_out():
    session.clear() # Clear the sessoin
    return redirect("/")
