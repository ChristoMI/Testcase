from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to main page!"


@main.route('/hello')
def hello_name():
    return "Hello world"