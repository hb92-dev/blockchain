import datetime
import json


import requests
from flask import render_template, redirect, request
import pymysql
from app import app
from app.user import User


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []
db=pymysql.connect('localhost', 'root', '', 'blockchain_db')



def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)

    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


# fetch part of nodes
@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    # get value from request
    post_content = request.form["content"]
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
    }

    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    # Submit a transaction
    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')


@app.route('/login', methods=['GET'])
def loginForm():
    return render_template('login.html',
                           title='Login:',
                           node_address=CONNECTED_NODE_ADDRESS)


@app.route('/register', methods=['GET'])
def registerForm():
    return render_template('registerForm.html',
                           title='Register:',
                           node_address=CONNECTED_NODE_ADDRESS)


@app.route('/register', methods=['POST'])
def registerSubmit():
    user = User()
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    cursor = db.cursor()
    #generate password hash
    password = user.generatePasswordHash(password)
    cursor.execute("INSERT INTO users(first_name, last_name, email, password) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, password))
    db.commit()
    return redirect("/login")

@app.route('/login', methods=['POST'])
def loginSubmit():
    user = User()
    email = request.form["email"]
    password = request.form["password"]
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s', (email))
    result = cursor.fetchone()
    if result:
        password_hash = result[4]
        check_hash = user.checkPasswordHash(password_hash, password)
        if check_hash:
            return redirect("/")

        else:
            return "Incorrect password"

    else:
        return "Incorrect email or password", 400

