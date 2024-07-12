from app import db
from app.models import User, Role
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_admin_user():
    # Verificar si el usuario admin ya existe
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        # Verificar si el rol de admin existe, si no, crearlo
        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(name='admin', description='Administrator role')
            db.session.add(admin_role)
            db.session.commit()

        # Generar hash de la contraseña
        hashed_password = bcrypt.generate_password_hash('admin12345').decode('utf-8')

        # Crear el usuario admin
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

    # Crear otros roles si no existen
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

# Llamar a la función para asegurarse de que se cree el usuario admin y otros roles
create_admin_user()
