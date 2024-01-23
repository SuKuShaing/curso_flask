from flask import render_template, session, redirect, flash, url_for
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST']) # Indicamos la ruta de la página y los métodos permitidos
def login():
    login_form = LoginForm() 
    contexto = {
        'login_form': login_form
    }

    if login_form.validate_on_submit(): # Si el formulario es válido
        username = login_form.username.data # Obtenemos el nombre de usuario del formulario
        session['username'] = username # el nombre de usuario se guarda en la sesión de manera segura

        flash(f'Nombre de usuario {username} registrado con éxito') # Mostramos un mensaje al usuario

        return redirect(url_for('index'))

    return render_template('login.html', **contexto)