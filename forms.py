from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, StringField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    first_name = StringField("First Name",  [validators.DataRequired("Please enter your first name."), validators.Length(min=5, max=20)])
    last_name = StringField("Last Name",  [validators.DataRequired("Please enter your last name."), validators.Length(min=5, max=20)])
    email = StringField("Email",  [validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    message = TextAreaField("Message",  [validators.DataRequired("Please enter a message."), validators.Length(min=10, max=200)])
    submit = SubmitField("Send")


