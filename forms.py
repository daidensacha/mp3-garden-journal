from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, validators
from wtforms.validators import InputRequired, Length, Email


class ContactForm(FlaskForm):
    firstname = StringField("First Name",  [validators.InputRequired(
        "Please enter your first name."), validators.Length(min=5, max=20)])
    lastname = StringField("Last Name",  [validators.InputRequired(
        "Please enter your last name."), validators.Length(min=5, max=20)])
    email = StringField("Email",  [validators.InputRequired(
        "Please enter your email address."), validators.Email(
            "Please enter a valid email address.")])
    message = TextAreaField("Message",  [validators.InputRequired(
        "Please enter a message."), validators.Length(min=10, max=200)])
    submit = SubmitField("Send")
