from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional, Length
from app.models import Role

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    document_type = SelectField('Document Type', choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad')], validators=[DataRequired()])
    document_number = StringField('Document Number', validators=[DataRequired(), Length(max=64)])
    role = SelectField('Role', choices=[], validators=[DataRequired()])
    professional_card_number = StringField('Professional Card Number', validators=[Optional(), Length(max=64)])

    def validate_professional_card_number(form, field):
        if form.role.data == 'medico' and not field.data:
            raise ValidationError('El número de tarjeta profesional es obligatorio para el rol médico.')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.all()]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


