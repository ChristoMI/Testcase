from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signin')
def signin():
    return "Sign in"


@auth.route('/signup')
def signup():
    return "Sign up"


@auth.route('/logout')
def logout():
    return "Log out"