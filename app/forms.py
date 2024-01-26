from flask_wtf import FlaskForm # Para crear formularios en Flask
from wtforms.fields import StringField, PasswordField, SubmitField # Para crear los campos de los formularios
from wtforms.validators import DataRequired # Para validar los campos de los formularios


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')