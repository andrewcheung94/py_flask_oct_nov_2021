from flask import Flask
import os
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") # Whenever you use session, you MUST use a secret key
print(app.secret_key)