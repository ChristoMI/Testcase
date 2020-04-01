import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from auth import auth as auth_blueprint
from main import main as main_blueprint

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)



if __name__ == '__main__':
    app.run()

