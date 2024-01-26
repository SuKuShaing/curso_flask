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

# Esta función nos permite crear un usuario en la base de datos
def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})

# Esta es la estructura de la base de datos, se va a la colección "users", al documento del "usuario" y a la colección "todos" de cada usuario
def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()

def put_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos') # Obtenemos la colección "todos" del usuario
    todos_collection_ref.add({'description': description, 'done': False}) # Agregamos un nuevo documento a la colección "todos" del usuario

def delete_todo(user_id, todo_id):
    todo_ref = db.document(f'users/{user_id}/todos/{todo_id}'.format(user_id, todo_id)) # Obtenemos el documento "todo" del usuario
    todo_ref.delete() # Borramos el documento "todo" del usuario
    # todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id) # Obtenemos el documento "todo" del usuario