from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if
qw=10

@app.route('/help')
def hello_help():
    return 'Hello from help1!'
