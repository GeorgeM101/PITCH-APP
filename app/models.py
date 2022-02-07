from ensurepip import bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Email,Length
from wtforms import StringField, PasswordField, BooleanField

app=Flask(__name__)
bootstrap(app)