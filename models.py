from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    bio = db.Column(db.String(45),nullable=False)
    password = db.Column(db.String(),nullable=False)
    
    __tablename__ = "users"