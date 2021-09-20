from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import Length, Email, EqualTo, ValidationError
from BibotApp.models import User


class RegistrationForm(FlaskForm): 
    username= StringField('Username',
                            validators=[Length(min=5, max=20)])
    email = StringField('Email',
                        validators=[Email()])

    password = PasswordField('Password', validators=[Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: 
            raise ValidationError('That username is taken. Please choose another one')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email: 
            raise ValidationError('That email is taken. Please choose another one')


class LoginForm(FlaskForm): 
    email = StringField('Email',
                        validators=[ Email()])

    password = PasswordField('Password', validators=[Length(min=5, max=20)])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign Up')