from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , TextAreaField , SubmitField
from wtforms.validators import InputRequired, EqualTo , ValidationError
from flasksocket.models import User
from flasksocket import bcrypt

def data_check(form, field):

    u_entered = form.username.data
    p_entered = field.data

    user_obj = User.query.filter_by(username=u_entered).first()
    if user_obj is None:
        raise ValidationError("Error in data entered.")
    elif bcrypt.check_password_hash(user_obj.password, p_entered)!= True :
        raise ValidationError("Error in data entered")
    #elif p_entered != user_obj.password:
     #   raise ValidationError("Error in Data entered.")


class Register(FlaskForm):
    

    username = StringField('username',validators=[InputRequired()])
    bio = TextAreaField('bio',validators=[InputRequired()])
    password = PasswordField('password',validators=[InputRequired()])
    confirm_password = PasswordField('confirm_password',
        validators=[InputRequired(), EqualTo('password',
        message="Both passwords should match")])
    #submit_button = SubmitField('Register')


class Login(FlaskForm):

    username = StringField('username',validators=[InputRequired()])
    password = PasswordField('password',validators=[InputRequired(),data_check], 
        )
    #submit_button = SubmitField('Login')

    

