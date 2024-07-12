# app/views.py

from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from flask import request, redirect, url_for, flash
from flask_login import current_user
from app import db
from app.models import User, Role, Paciente
from wtforms.validators import DataRequired, Length, Optional
from wtforms import PasswordField, SelectField
import bcrypt

class UserView(ModelView):
    column_exclude_list = ['password_hash']
    form_columns = ['username', 'email', 'first_name', 'last_name', 'document_type', 'document_number', 'role', 'professional_card_number']

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.name == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        flash('No tienes acceso a esta página.', 'warning')
        return redirect(url_for('login', next=request.url))

    form_create_rules = [
        rules.FieldSet(['username', 'email', 'password', 'first_name', 'last_name', 'document_type', 'document_number', 'role'], 'Detalles Personales'),
        rules.FieldSet(['professional_card_number'], 'Detalles Profesionales')
    ]
    
    form_edit_rules = [
        rules.FieldSet(['username', 'email', 'first_name', 'last_name', 'document_type', 'document_number', 'role'], 'Detalles Personales'),
        rules.FieldSet(['professional_card_number'], 'Detalles Profesionales')
    ]

    def create_form(self, obj=None):
        form = super(UserView, self).create_form(obj)
        self._populate_role_choices(form)
        self._handle_role_change(form)
        return form

    def edit_form(self, obj=None):
        form = super(UserView, self).edit_form(obj)
        self._populate_role_choices(form)
        self._handle_role_change(form)
        return form

    def _populate_role_choices(self, form):
        form.role.choices = [(role.id, role.name) for role in Role.query.all()]

    def _handle_role_change(self, form):
        if form.role.data == 'medico':
            form.professional_card_number.validators = [DataRequired(), Length(max=64)]
        else:
            form.professional_card_number.validators = [Optional(), Length(max=64)]

class PacienteView(ModelView):
    column_exclude_list = ['direccion', 'telefono', 'correo_electronico']
    form_columns = ['nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'ciudad', 'departamento', 'pais', 'direccion', 'telefono', 'correo_electronico', 'tiene_eps', 'nombre_eps']

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.role.name == 'admin' or current_user.role.name == 'medico')

    def inaccessible_callback(self, name, **kwargs):
        flash('No tienes acceso a esta página.', 'warning')
        return redirect(url_for('login', next=request.url))

    def can_delete(self, obj):
        return current_user.can_delete_patient

    form_create_rules = [
        rules.FieldSet(['nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'ciudad', 'departamento', 'pais', 'direccion', 'telefono', 'correo_electronico', 'tiene_eps', 'nombre_eps'], 'Detalles del Paciente')
    ]

    form_edit_rules = [
        rules.FieldSet(['nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'ciudad', 'departamento', 'pais', 'direccion', 'telefono', 'correo_electronico', 'tiene_eps', 'nombre_eps'], 'Detalles del Paciente')
    ]

    def create_form(self, obj=None):
        form = super(PacienteView, self).create_form(obj)
        return form

    def edit_form(self, obj=None):
        form = super(PacienteView, self).edit_form(obj)
        return form
