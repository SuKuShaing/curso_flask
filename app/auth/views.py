from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm
from . import auth
from app.firestore_service import get_user, user_put
from app.models import UserData, UserModel

@auth.route('/login', methods=['GET', 'POST']) # Indicamos la ruta de la página y los métodos permitidos
def login():
    if current_user.is_authenticated:
        flash('Ya estás logueado')
        return redirect(url_for('index'))

    # Si no está logeado
    login_form = LoginForm() 
    contexto = {
        'login_form': login_form
    }

    if login_form.validate_on_submit(): # Si el formulario es válido
        username = login_form.username.data # Obtenemos el nombre de usuario de la base de datos
        password = login_form.password.data

        user_doc = get_user(username) # Obtenemos el usuario de la base de datos

        if user_doc.to_dict() is not None: # Si el usuario existe, validamos sus datos
            password_from_db = user_doc.to_dict()['password'] # Obtenemos la contraseña de la base de datos

            # if password == password_from_db: # Si la contraseña es correcta # si los usuarios no tuvieran la contraseña encriptada
            # if check_password_hash(user_doc.to_dict()['password'], password): # si todos los usuarios tuvieran la contraseña encriptada
            if check_password_hash(user_doc.to_dict()['password'], password) or (password == password_from_db): #Verifica ambas opciones
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Bienvenido de nuevo')

                return redirect(url_for('hello'))
            else:
                flash('La información no coincide')
        else:
            flash('El usuario no existe')

        return redirect(url_for('index'))

    return render_template('login.html', **contexto)


# Ruta para registrarse
@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    contexto = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        # Primero debemos verificar que el usuario no exista
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None: # Si el usuario no existe
            password_hash = generate_password_hash(password) # Generamos el hash de la contraseña
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user) # apenas esté registrado pasa de inmediato a la página de hello, con sus datos de logeado

            flash('Bienvenido')

            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')

    return render_template('signup.html', **contexto)



# para cerrar sesión
@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))