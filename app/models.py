from ensurepip import bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Email,Length
from wtforms import StringField, PasswordField, BooleanField

class loginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    remember = BooleanField('remember me')