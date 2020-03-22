from flask import Flask
from app.block import Block
from flask_bcrypt import Bcrypt
from hashlib import sha256
from app import app

app = Flask(__name__)
bcrypt = Bcrypt(app)


class User(Block):

    def __init__(self):
        Block.__init__(self, 0, [], 0, '0')

    def generatePasswordHash(self, password):
        return bcrypt.generate_password_hash(password)

    def _compute_hash(self):
        string = "encryptionkey"
        return sha256(string.encode()).hexdigest()