from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

# retorna la app
def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')  # __name__ es el nombre del módulo, en este caso main, template_folder es la carpeta donde se encuentran los templates HTML, static_folder es la carpeta donde se encuentran los archivos estáticos como CSS, JS, imágenes, etc.
    bootstrap = Bootstrap(app) # Instanciamos Bootstrap con la instancia de Flask

    app.config.from_object(Config)

    return app

# app.config.update( # Supuestamente esto es para cambiar los entorno de desarrollo, pero al parecer no funciona
#     DEBUG=False, # Para que no se muestren los errores en el navegador
#     ENV='development'
# )
