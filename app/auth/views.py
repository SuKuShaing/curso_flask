from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.forms import LoginForm
from . import auth
from app.firestore_service import get_user
from app.models import UserData, UserModel

@auth.route('/login', methods=['GET', 'POST']) # Indicamos la ruta de la página y los métodos permitidos
def login():
    if current_user.is_authenticated:
        flash('Ya estás logueado')
        return redirect(url_for('index'))

    else:
        # Si no está logeado
        login_form = LoginForm() 
        contexto = {
            'login_form': login_form
        }

        if login_form.validate_on_submit(): # Si el formulario es válido
            username = login_form.username.data # Obtenemos el nombre de usuario de la base de datos
            password = login_form.password.data

            user_doc = get_user(username) # Obtenemos el usuario de la base de datos

            if user_doc.to_dict() is not None: # Si el usuario existe
                password_from_db = user_doc.to_dict()['password'] # de los datos del usuario obtenemos la contraseña

                if password == password_from_db: # Si la contraseña es correcta
                    user_data = UserData(username, password) # se guarda la data del usuario
                    user = UserModel(user_data) # Se crea el modelo del usuario que creamos en models.py

                    login_user(user) # Ese usuario se loguea en nuestra aplicación

                    flash('Bienvenido de nuevo')

                    redirect(url_for('hello'))
                
                else:
                    flash('La información no coincide')
            else:
                flash('El usuario no existe')

            return redirect(url_for('index'))

        return render_template('login.html', **contexto)


# para cerrar sesión
@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))