from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/help')
def hello_world():
    return 'Hello from help1!'
