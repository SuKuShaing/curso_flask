from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config # el punto al inicio indica que el archivo config.py está en la misma carpeta que __init__.py
from .auth import auth # Importamos el blueprint auth

# retorna la app
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')  # __name__ es el nombre del módulo, en este caso main, template_folder es la carpeta donde se encuentran los templates HTML, static_folder es la carpeta donde se encuentran los archivos estáticos como CSS, JS, imágenes, etc.
    bootstrap = Bootstrap(app) # Instanciamos Bootstrap con la instancia de Flask

    app.config.from_object(Config)

    app.register_blueprint(auth) # Registramos el blueprint auth

    return app

# app.config.update( # Supuestamente esto es para cambiar los entorno de desarrollo, pero al parecer no funciona
#     DEBUG=False, # Para que no se muestren los errores en el navegador
#     ENV='development'
# )
