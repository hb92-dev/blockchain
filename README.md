## Instructions

To get this working, first we should start a blockchain server, by running the following commands:

`export FLASK_APP=node_server.py`</br>
`flask run --port 8000`

One instance of our blockchain node is now up and running at port 8000

Now, we have to run the application (use different terminal session) </br>
`python run_app.py`

The application should be up and running at *localhost:5000*

To play around by spinning off multiple custom nodes, use the `register_with/` endpoint to register a new node. 
```
Here's a sample scenario that you might wanna try,

```sh
# already running
$ flask run --port 8000 &
# spinning up new nodes
$ flask run --port 8001 &
$ flask run --port 8002 &
```
You can use the following cURL requests to register the nodes at port `8001` and `8002` with the already running `8000`.

```sh
curl -X POST \
  http://127.0.0.1:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

```sh
curl -X POST \
  http://127.0.0.1:8002/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

This will make the node at port 8000 aware of the nodes at port 8001 and 8002, and make the newer nodes sync the chain with the node 8000, so that they are able to actively participate in the mining process post registration.
