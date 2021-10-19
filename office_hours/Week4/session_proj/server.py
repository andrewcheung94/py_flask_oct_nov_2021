from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = "itsasecrettoeverybody"
random_number = 0
@app.route("/")
def main():
    global random_number
    random_number += 1
    session["number"] = random_number
    print(session)
    return render_template("random.html")

@app.route('/reset')
def reset_count():
    global random_number
    random_number = 0
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)