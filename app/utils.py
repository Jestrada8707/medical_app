from app import db
from app.models import User, Role
from flask_bcrypt import Bcrypt

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
        admin = User(username='admin', password_hash=hashed_password, role=admin_role)
        db.session.add(admin)
        db.session.commit()
        print('Usuario admin creado exitosamente.')
