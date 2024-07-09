from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Email, Length, Optional

class PacienteForm(FlaskForm):
    nombres = StringField('Nombres', validators=[InputRequired(), Length(max=100)])
    apellidos = StringField('Apellidos', validators=[InputRequired(), Length(max=100)])
    tipo_documento = SelectField('Tipo de Documento', choices=[('cedula', 'Cédula'), ('pasaporte', 'Pasaporte'), ('cedula_extranjeria', 'Cédula de Extranjería')], validators=[InputRequired()])
    numero_documento = StringField('Número de Documento', validators=[InputRequired(), Length(max=20)])
    ciudad = StringField('Ciudad', validators=[Optional(), Length(max=100)])
    departamento = StringField('Departamento', validators=[Optional(), Length(max=100)])
    pais = StringField('País', validators=[Optional(), Length(max=100)])
    direccion = StringField('Dirección', validators=[Optional(), Length(max=255)])
    telefono = StringField('Teléfono', validators=[Optional(), Length(max=20)])
    correo_electronico = StringField('Correo Electrónico', validators=[Optional(), Email(), Length(max=100)])
    tiene_eps = BooleanField('Tiene EPS')
    nombre_eps = StringField('Nombre de EPS', validators=[Optional(), Length(max=100)])
