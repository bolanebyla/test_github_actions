from flask import Flask
import os


app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/help')
def hello_help():
    return f'TOKEN: {TOKEN}'
