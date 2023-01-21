from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms import validators 


# Fake login form
class FakeLoginForm(FlaskForm):
    email = EmailField("Email address", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.data_required()]) # Add length params of target phsiing deploy site