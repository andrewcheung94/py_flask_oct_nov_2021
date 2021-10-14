from flask import Flask, render_template
app = Flask(__name__)
# Link to shortcuts for typing HTML: https://docs.emmet.io/cheat-sheet/

@app.route("/")
def index():
    return render_template("random_page.html")

@app.route("/<int:count>")
def duplicate_messages(count):
    message = "Hello world!  I'm drinking raspberry tea!"
    return render_template("message.html", 
    my_message = message, count = count, number = 10)

if __name__=="__main__":
    app.run(debug=True)