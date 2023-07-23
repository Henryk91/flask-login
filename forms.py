from flask_wtf import Form
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    username = EmailField('Username', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])