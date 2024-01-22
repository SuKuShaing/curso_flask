from flask_testing import TestCase
from main import app
from flask import current_app, url_for

class mainTest(TestCase):
    # Creamos el método create_app() para configurar lo aplicación para el modo testing
    def create_app(self):
        app.config['TESTING'] = True # Le decimos a Flask que estamos en modo testing
        app.config['WTF_CSRF_ENABLED'] = False # Deshabilitamos la protección CSRF para los formularios para poder hacer el testing, dado que no tenemos una sesión de usuario real

        return app

    # Primera prueba, verificamos que al app exista
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # Segunda prueba, verificamos que la app esté en modo testing
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # Tercera prueba, verificamos que index redireccione a hello
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    # Cuarta prueba, verificamos que hello retorne un código 200
    def test_hello_get_200(self):
        response = self.client.get(url_for('/hello'))
        self.assert200(response)

    # Quinta prueba, verificamos que hello post redireccione a index
    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('/hello'), data=fake_form)

        self.assertRedirects(response, url_for('/'))

    # Sexta prueba, verificamos que el blueprint auth exista
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    # Séptima prueba, verificamos que la ruta login retorne un código 200
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')