from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField(
        "username",
        validators = [
            DataRequired("need username"),
            Length(1, 30, "under 30")
        ]
    )
    
    email = StringField(
        "mail",
        validators = [
            DataRequired("need mail"),
            Email("xxx@yyy.zzz")
        ]
    )
    
    password = PasswordField(
        "password",
        validators = [
            DataRequired("need password")
        ]
    )
    
    submit = SubmitField("register new")
    
class LoginForm(FlaskForm):
    email = StringField(
        "mail",
        validators = [
            DataRequired("need mail"),
            Email("xxx@yyy.zzz")
        ]
    )
    
    password = PasswordField(
        "password",
        validators = [
            DataRequired("need password")
        ]
    )
    
    submit = SubmitField("login")