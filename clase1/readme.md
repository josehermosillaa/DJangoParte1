# Pasos clase 1 de Django

### Creacion entorno virtual

python -m venv django1

donde django1 es el nombre que queremos colocar al entorno virtual que estammos creando

para la activacion del entorno virtual

source django/Scripts/Activate

para desactivar cualquier entorno virtual

deactivate

nota : para saber la version de pip --> pip --version
pip es el gestor de paquetes de python

para ver todos los paquetes instalados de python
pip list

Para instalar Django 

pip install django    
* esto instala la ultima version disponible
(para concocer las versiones de librerias usamos pip list)

creacion del primer proyecto de prueba

django-admin startproject prueba1

contiene archivos como 
prueba1/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
manage.py -> comandos para trabajar con Django


comando para probar que django funcione
python manage.py runserver

en la carpeta del proyecto django (para cambiar de directorio cd prueba1)

creacion de la primera aplicacion

python manage.py startapp hola

una vez creada la app lo que debe hacer es agregarla a las aplicaciones instaladas

en el archivo settings.py
buscamos INSTALLED_APPS


## comandos que veremos igual mas adelante

### migraciones

``` python manage.py makemigrations``` 

va a buscar todos los cambios existentes en los modelos de datos para prepararlos para su modificacion

### aplicar los cambios o migrate

``` python manage.py migrate```

aplicar todos los cambios existentes en la base de datos



una vez que nosotros creamos la primera migracion podemos crear el superuser
### creacion de un superusuario

```python manage.py createsuperuser```



# NOTA USAR COMILLAS SIMPLES EN LOS NOMBRES DE TEMPLATE

