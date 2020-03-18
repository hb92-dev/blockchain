## Instructions

To get this working, first we should start a blockchain server, by running the following commands:

`$ export FLASK_APP=node_server.py`</br>
`$ flask run --port 8000`

One instance of our blockchain node is now up and running at port 8000

Now, we have to run the application (use different terminal session) </br>
`$ python run_app.py`

The application should be up and running at * http://127.0.0.1:5000/ *

Once you do all this, you can run the application, create transactions (post messages via the web inteface), and once you mine the transactions, all the nodes in the network will update the chain.

