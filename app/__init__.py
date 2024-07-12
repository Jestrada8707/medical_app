from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from config import DevelopmentConfig
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

login_manager.login_view = 'login'

# Configuración de Flask-Admin
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

# Importar los modelos y vistas necesarios para Flask-Admin
from app.models import User, Role, Paciente
from app.views import UserView

# Añadir las vistas al panel de administración
admin.add_view(UserView(User, db.session, endpoint='userview'))
admin.add_view(ModelView(Role, db.session, endpoint='roleview'))
admin.add_view(ModelView(Paciente, db.session, endpoint='pacienteview'))

# No ejecutar la creación del usuario admin automáticamente aquí

if __name__ == '__main__':
    # Ejecutar la creación del usuario admin manualmente
    with app.app_context():
        from app.utils import create_admin_user
        create_admin_user()
    
    # Iniciar la aplicación Flask
    app.run()
