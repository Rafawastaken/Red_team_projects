from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators, ValidationError
from .models import User

# Add User
class AddUserForm(FlaskForm):
    alias = StringField('Alias', [validators.length(min = 4, max = 24), validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(), 
        validators.EqualTo("password_2", message = "Passwords dont match")])
    password_2 = PasswordField("Repeat password", [validators.DataRequired()])

# Login User
class LoginUserForm(FlaskForm):
    alias = StringField('Alias', [validators.DataRequired()])
    password = PasswordField('Alias', [validators.DataRequired()])