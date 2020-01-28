from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret"

app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://qtdkiadqujlwkt:32245eeb235f074e76f4f3e597b7686414ba09c9a8a1a4bbff95df560dc34544@ec2-174-129-32-240.compute-1.amazonaws.com:5432/d5f7lfpq6tn46o'
db = SQLAlchemy(app)

login_m = LoginManager(app)
login_m.init_app(app)

socketio = SocketIO(app)


from flasksocket import routes