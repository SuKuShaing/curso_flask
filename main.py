from flask import Flask, request, make_response, redirect, render_template, abort, session, url_for, flash
from markupsafe import escape # Para reemplazar caracteres de <script> a &lt;script&gt; para evitar la inyección de código por parte de los usuarios
from flask_bootstrap import Bootstrap # Para usar Bootstrap en Flask
import unittest # Para ejecutar las pruebas unitarias
from flask_login import login_required, current_user
# Flask, para crear el servidor
# request, para obtener cosas del usuario, entre ellos la IP
# make_response, para crear una respuesta al usuario
# redirect, para redireccionar al usuario a otra página
# render_template, para renderizar un template HTML
# abort, para forzar un error 500
# session, para crear una sesión de usuario
# url_for, para crear una URL de una ruta
# flash, para mostrar mensajes al usuario

from app import create_app # Importamos la función create_app del archivo __init__.py de la carpeta app
from app.forms import LoginForm # Importamos la clase LoginForm del archivo forms.py de la carpeta app
from app.firestore_service import get_users, get_todos



#Creamos la instancia del objeto Flask
app = create_app() # Creamos la instancia de la aplicación Flask

#############################################
################ Testing ####################
#############################################

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests') # Cargamos las pruebas unitarias de la carpeta tests
    unittest.TextTestRunner().run(tests)


#############################################
############# Manejo de errores #############
#############################################

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error) # Renderizamos el template HTML y le enviamos el error como parámetro

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/debug-errors/500')
def debug_500():
    abort(500) # Forzamos un error 500


#############################################
################## Rutas ####################
#############################################

@app.route('/') # Indicamos la ruta de la página
def index():
    # raise(500) # Forzamos un error 500
    user_ip = escape(request.remote_addr) # Obtenemos la IP del usuario y con escape de manera segura sin inyección de código

    response = make_response(redirect('/hello')) # Creamos una respuesta al usuario, redireccionándolo a la página /hello
    session['user_ip'] = user_ip # Creamos una sesión de usuario con la IP del usuario, de manera segura, encriptada
    # response.set_cookie('user_ip', user_ip) # Creamos una cookie con la IP del usuario, user_ip es el nombre de la cookie y user_ip es el valor de la cookie

    return response


# Este es un decorador
@app.route('/hello', methods=['GET']) # por defecto es GET (obtener) es permitido, POST hay que especificarlo, methods=['GET', 'POST']
@login_required
def hello():
    user_ip = session.get('user_ip') # Obtenemos la IP del usuario guardada en la cookie
    username = current_user.id
    # username = session.get('username')
    # user_ip = request.cookies.get('user_ip') # Obtenemos la IP del usuario guardada en la cookie
    # login_form = LoginForm() # Instanciamos el formulario de login, después de esto se puede agregar al contexto

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        # 'login_form': login_form,
        'username': username
    }

    users = get_users()

    return render_template('hello.html', **context) # Renderizamos el template HTML y le enviamos la ip del usuario como parámetro
    # expandir un diccionario (**Kwargs), al colocar "**" a la variable context, le estamos indicando que en vez de pasarle un diccionario, le pasamos los elementos del diccionario como parámetros, como lo de arriba
    # expandir una lista, tupla o sets (*arg), al colocar "*" a la variable context, le estamos indicando que en vez de pasarle una lista, le pasamos los elementos de la lista como parámetros
    # return render_template('hello.html', user_ip=user_ip, todos=todos) # así le pasamos parámetros al template



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port = 1313, debug=False, host="0.0.0.0")