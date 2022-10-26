
from cProfile import run
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
export FLASK_APP=app.py
set FLASK_APP=app.py
flask run