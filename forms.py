from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , TextAreaField , SubmitField
from wtforms.validators import InputRequired, EqualTo


class Register(FlaskForm):
    

    username = StringField('username',validators=[InputRequired()])
    bio = TextAreaField('bio',validators=[InputRequired()])
    password = PasswordField('password',validators=[InputRequired()])
    confirm_password = PasswordField('confirm_password',
        validators=[InputRequired(), EqualTo('password',
        message="Both passwords should match")])
    #submit_button = SubmitField('Register')