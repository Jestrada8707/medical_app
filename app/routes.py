from flask import render_template, request, jsonify, flash, redirect, url_for
from flask_login import current_user
from app import app, db
from app.models import Paciente
from app.forms import PacienteForm
from app.utils import admin_required

@app.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('index.html', pacientes=pacientes)

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/agregar_paciente', methods=['GET', 'POST'])
def agregar_paciente():
    form = PacienteForm()

    if form.validate_on_submit():
        nuevo_paciente = Paciente(
            nombres=form.nombres.data,
            apellidos=form.apellidos.data,
            tipo_documento=form.tipo_documento.data,
            numero_documento=form.numero_documento.data,
            ciudad=form.ciudad.data,
            departamento=form.departamento.data,
            pais=form.pais.data,
            direccion=form.direccion.data,
            telefono=form.telefono.data,
            correo_electronico=form.correo_electronico.data,
            tiene_eps=form.tiene_eps.data,
            nombre_eps=form.nombre_eps.data if form.tiene_eps.data else None
        )

        db.session.add(nuevo_paciente)
        db.session.commit()

        flash('Paciente agregado correctamente', 'success')  # Mensaje flash para el usuario
        return redirect(url_for('index'))

    return render_template('agregar_paciente.html', form=form)

