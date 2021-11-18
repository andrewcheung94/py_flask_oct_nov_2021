from flask import Flask
# Two lines below are from this article (thanks to Mel!): https://dev.to/sasidharan/flask-and-env-22am
from dotenv import load_dotenv # Still need to install python-dotenv in virtual environment
load_dotenv() # Load environmental variables
import os # New package that we'll use to read in values from the .env file

app = Flask(__name__) # Creates instance of Flask class here
app.secret_key = os.getenv("FLASK_SECRET_KEY")
api_key = os.getenv("NASA_API_KEY")

# print(os.getenv("FLASK_SECRET_KEY"))
# print(os.getenv("NASA_API_KEY"))

# Original code does NOT work:
# app.secret_key = os.environ.get("FLASK_SECRET_KEY") # Secret key goes here
# print(app.secret_key)
# print("App's secret key from init = " + app.secret_key)
# api_key = os.environ.get("NASA_API_KEY")
# print("App's api key from init = " + api_key)