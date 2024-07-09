from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Paciente, User, Role

# Inicializar Flask-Admin
admin = Admin(app, name='Admin', template_mode='bootstrap3')

# Agregar vistas para los modelos
admin.add_view(ModelView(Paciente, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
