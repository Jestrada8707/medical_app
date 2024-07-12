from app import db
from app.models import User, Role
from flask_bcrypt import Bcrypt
from functools import wraps
from flask import abort
from flask_login import current_user

bcrypt = Bcrypt()

def create_admin_user():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(name='admin', description='Administrator role')
            db.session.add(admin_role)
            db.session.commit()

        hashed_password = bcrypt.generate_password_hash('admin12345').decode('utf-8')
        admin = User(
            username='admin', 
            email='admin@example.com', 
            password_hash=hashed_password, 
            role=admin_role, 
            first_name='Admin', 
            last_name='User', 
            document_type='CC', 
            document_number='123456'
        )
        db.session.add(admin)
        db.session.commit()
        print('Usuario admin creado exitosamente.')

    roles = [
        {'name': 'medico', 'description': 'Medical role'},
        {'name': 'enfermero', 'description': 'Nursing role'},
        {'name': 'laboratorista', 'description': 'Lab technician role'},
        {'name': 'imagenologia', 'description': 'Radiology technician role'}
    ]

    for role in roles:
        role_obj = Role.query.filter_by(name=role['name']).first()
        if not role_obj:
            role_obj = Role(name=role['name'], description=role['description'])
            db.session.add(role_obj)
            db.session.commit()

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403) 
        return func(*args, **kwargs)
    return decorated_view
