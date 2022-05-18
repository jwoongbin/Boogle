from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, BooleanField


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    # email format에 대한 유효성 검사를 위해서는 추가적으로 email_validator package를 추가해야함
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Passwords must be matched'),
    ])
    password_confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.InputRequired()])