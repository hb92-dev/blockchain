from flask import Flask
from flask_bcrypt import Bcrypt
from app import app

app = Flask(__name__)
bcrypt = Bcrypt(app)

class User():
    def generatePasswordHash(self, password):
        return bcrypt.generate_password_hash(password)
