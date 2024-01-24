import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id = 'flask-curso-platzi'
credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials, {
    'projectId': project_id,
})

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

# Esta es la estructura de la base de datos, se va a la colección "users", al documento del "usuario" y a la colección "todos" de cada usuario
def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()