from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Paciente, User, Role
from app.views import UserView

admin = Admin(app, name='Admin', template_mode='bootstrap3')

admin.add_view(ModelView(Paciente, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(UserView(User, db.session))

if __name__ == '__main__':
    app.run()
