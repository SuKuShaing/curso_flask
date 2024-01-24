from flask import Flask
from flask_bootstrap import Bootstrap

from flask_login import LoginManager

from .config import Config # el punto al inicio indica que el archivo config.py está en la misma carpeta que __init__.py
from .auth import auth # Importamos el blueprint auth

from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login' # vista a la que los usuarios deben ser redirigidos si intentan acceder a una página protegida sin estar autenticados. En este caso, se redirigirán a la vista 'auth.login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

# @login_manager.user_loader
# def load_user(user_id=''):
#     return None


# retorna la app
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')  # __name__ es el nombre del módulo, en este caso main, template_folder es la carpeta donde se encuentran los templates HTML, static_folder es la carpeta donde se encuentran los archivos estáticos como CSS, JS, imágenes, etc.
    bootstrap = Bootstrap(app) # Instanciamos Bootstrap con la instancia de Flask

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth) # Registramos el blueprint auth

    return app

# app.config.update( # Supuestamente esto es para cambiar los entorno de desarrollo, pero al parecer no funciona
#     DEBUG=False, # Para que no se muestren los errores en el navegador
#     ENV='development'
# )
