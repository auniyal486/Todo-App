from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,validators
class Signupform(FlaskForm):
    first_name=StringField('First Name ',validators=[validators.input_required(),validators.Length(max=15)],id="first_name")
    last_name=StringField('Last Name ',validators=[validators.Optional(),validators.Length(max=15)],id="last_name")
    email=StringField('Email Address',validators=[validators.input_required(),validators.Email(),validators.Length(max=40)],id="email")
    password=PasswordField('Password',validators=[validators.input_required(),validators.Length(max=20)],id="password")
    confirm_password=PasswordField('Confirm Password',validators=[validators.input_required(),validators.EqualTo('password'),validators.Length(max=30)],id="conpassword")
    remember = BooleanField('Remember Me')
    submit=SubmitField('Sign Up',id='signup_btn')
class LoginForm(FlaskForm):
    email = StringField('Email Address',validators=[validators.input_required(),validators.Email(),validators.Length(max=40)],id="log_email")
    password = PasswordField('Password', validators=[validators.input_required(),validators.Length(max=20)],id="log_password")
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login' ,id="login_btn")