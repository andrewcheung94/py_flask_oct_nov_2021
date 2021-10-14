from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "89vfjn3489bmj8943klfd" # Whenever you use session, you MUST use a secret key

@app.route("/")
def index(): # Displays the form for entering data
    return render_template("my_form.html")

@app.route("/send_data", methods=["POST"]) # REMEMBER the "methods=["POST"]" part when handling POST data!
def handle_data():
    # print(request.form)
    # Grab the data from the form and save in session
    session["name"] = request.form['name']
    session["email"] = request.form['email']
    session["anniversary"] = request.form['important_date']
    # print(session)
    # ALWAYS REDIRECT WHEN YOU HANDLE POST DATA!!!!
    return redirect("/results") # ALWAYS the name of a path - NOT the name of an html file

@app.route("/results")
def show_results(): # Displays the RESULTS of the form
    return render_template("entered_data.html")

if __name__=="__main__":
    app.run(debug=True)