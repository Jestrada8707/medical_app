from app import db
from flask_login import UserMixin

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    tipo_documento = db.Column(db.String(50), nullable=False)
    numero_documento = db.Column(db.String(20), nullable=False)
    ciudad = db.Column(db.String(100))
    departamento = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    direccion = db.Column(db.Text)
    telefono = db.Column(db.String(20))
    correo_electronico = db.Column(db.String(100))
    tiene_eps = db.Column(db.Boolean, nullable=False)
    nombre_eps = db.Column(db.String(100))

    def __repr__(self):
        return f'<Paciente {self.nombres} {self.apellidos}>'


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))