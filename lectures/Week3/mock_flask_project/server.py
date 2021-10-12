from flask import Flask, render_template # Import Flask and methods here!
app = Flask(__name__)

# Demonstration of routes - note that each route must have different function definitions!
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random")
def random_path():
    return render_template("random.html")

# Demonstration with path variables
@app.route("/random/<number>")
def random_path_with_number(number): # MUST pass in path variables as parameters!!
    print(type(number)) # The parameter "umber" is a string - so we have to convert it
    number = int(number) # Use the function int() to convert
    another_number = 50
    my_list = [88, 'hello', True]
    # Pass values to HTML file
    return render_template("random_with_number.html", number = number, my_name = "Adrian", 
    this_number = another_number, my_list = my_list)

# DON'T FORGET!!!
if __name__=="__main__":
    app.run(debug=True)