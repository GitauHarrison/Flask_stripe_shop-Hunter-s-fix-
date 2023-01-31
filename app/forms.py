from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add User')


class AddItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    per = SelectField(
        'How Many?',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3')
        ])
    submit = SubmitField('Add Item')
