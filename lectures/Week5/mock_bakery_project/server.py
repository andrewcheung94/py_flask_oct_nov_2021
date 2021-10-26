from flask_app import app # Don't forget this line!
from flask_app.controllers import pastries # For each controller, import each file here!

if __name__ == "__main__":
    app.run(debug=True)