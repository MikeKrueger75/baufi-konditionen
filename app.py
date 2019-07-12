from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Mike!'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye Mike'

