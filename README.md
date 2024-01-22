# Curso de flask

Para ejecutar el servidor tienes que usar 

'''sh
$ python [nombre del archivo que tiene el servidor]
$ python main.py
'''

Otra forma es con 
'''sh
$ flask run
'''

pero primero tienes que crear una variables de entorno,
con esto se crea al variable de entorno para decir que cuando ejecutemos "flask run" queremos que corra el archivo main.py
'''sh
$ export FLASK_APP=main.py 
'''

Si desea verificar que está creada la variable, puedes usar
'''sh
$ echo $FLASK_APP 
'''
Después de esto puedes usar flask run

para activar el modo debug
'''sh
$ export FLASK_DEBUG=1
'''

para activar el modo development
'''sh
$ export FLASK_DEBUG=1
'''



## Notas

Flash por defecto está configurado para busca los archivos template HTML es la carpeta templates