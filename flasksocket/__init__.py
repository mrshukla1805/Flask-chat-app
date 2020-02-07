from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = ""

app.config['SQLALCHEMY_DATABASE_URI']= ''
db = SQLAlchemy(app)

login_m = LoginManager(app)
login_m.init_app(app)

socketio = SocketIO(app)


from flasksocket import routes
