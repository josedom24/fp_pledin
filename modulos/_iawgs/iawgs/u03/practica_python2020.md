---
title: Despliegue de aplicaciones python
permalink: /iawgs/u03/practica_python2020.html
---

## Tarea 1: Entorno de desarrollo 

Vamos a desarrollar la aplicación del [tutorial de django 3.1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/). Vamos a configurar tu equipo como entorno de desarrollo para trabajar con la aplicación, para ello:

* Clona el repositorio de GitHub: [https://github.com/josedom24/django_tutorial](https://github.com/josedom24/django_tutorial).
* Crea un entorno virtual de python3 e instala las dependencias necesarias para que funcione el proyecto (fichero `requirements.txt`).
* Comprueba que vamos a trabajar con una base de datos sqlite (`django_tutorial/settings.py`). ¿Cómo se llama la base de datos que vamos a crear?
* Crea la base de datos: `python3 manage.py migrate`. A partir del modelo de datos se crean las tablas de la base de datos.
* Crea un usuario administrador: `python3 manage.py createsuperuser`.
* Ejecuta el servidor web de desarrollo y entra en la zona de administración (`\admin`) para comprobar que los datos se han añadido correctamente.
* Crea dos preguntas, con posibles respuestas.
* Comprueba en el navegador que la aplicación está funcionando, accede a la url `\polls`.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando. Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Entorno de producción

Vamos a realizar el despliegue de nuestra aplicación en un entorno de producción, para ello vamos a utilizar una instancia del cloud, sigue los siguientes pasos:

* Instala en el servidor los servicios necesarios (apache2). Instala el módulo de apache2 para ejecutar código python.
* Clona el repositorio en el `DocumentRoot` de tu virtualhost.
* Crea un entorno virtual e instala las dependencias de tu aplicación.
* Instala el módulo que permite que python trabaje con mysql: 

		$ apt-get install python3-mysqldb

	Y en el entorno virtual:

		(env)$ pip install mysql-connector-python

* Crea una base de datos y un usuario en mysql.
* Configura la aplicación para trabajar con mysql, para ello modifica la configuración de la base de datos en el archivo `settings.py`:

		DATABASES = {
		    'default': {
		        'ENGINE': 'mysql.connector.django',
		        'NAME': 'myproject',
		        'USER': 'myprojectuser',
		        'PASSWORD': 'password',
		        'HOST': 'localhost',
		        'PORT': '',
		    }
		}

* Como en la tarea 1, realiza la migración de la base de datos que creará la estructura de datos necesrias. comprueba en mariadb que la base de datos y las tablas se han creado.
* Crea un usuario administrador: `python3 manage.py createsuperuser`.
* Configura un virtualhost en apache2 con la configuración adecuada para que funcione la aplicación. El punto de entrada de nuestro servidor será `django_tutorial/django_tutorial/wsgi.py`. Puedes guiarte por el [Ejercicio: Desplegando aplicaciones flask](flask.html), por la documentación de django: [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/),...
* Debes asegurarte que el contenido estático se está sirviendo: ¿Se muestra la imagen de fondo de la aplicación? ¿Se ve de forma adecuada la hoja de estilo de la zona de administración?. Para arreglarlo puedes encontrar documentación en [How to use Django with Apache and mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/).
* Desactiva en la configuración (fichero `settings.py`) el modo debug a False. Para que los errores de ejecución no den información sensible de la aplicación.
* Muestra la página funcionando.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando. Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Modificación de nuestra aplicación

Vamos a realizar cambios en el entorno de desarrollo y posteriormente vamos a subirlas a producción. Vamos a realizar tres modificaciones (entrega una captura de pantalla donde se ven cada una de ellas). Recuerda que primero lo haces en el entrono de desarrollo, y luego tendrás que llevar los cambios a producción:

1. Modifica la página inicial donde se ven las encuestas para que aparezca tu nombre: Para ello modifica el archivo `django_tutorial/polls/templates/polls/index.html`.
2. Modifica la imagen de fondo que se ve la aplicación.
3. Vamos a crear una nueva tabla en la base de datos, para ello sigue los siguientes pasos:
	
    * Añade un nuevo modelo al fichero `polls/models.py`:

        ```python
		class Categoria(models.Model):	
        	Abr = models.CharField(max_length=4)
        	Nombre = models.CharField(max_length=50)

        	def __str__(self):
        		return self.Abr+" - "+self.Nombre 		
        ```

    * Crea una nueva migración: `python3 manage.py makemigrations`. 
    * Y realiza la migración: `python3 manage.py migrate`
    * Añade el nuevo modelo al sitio de administración de django:

        Para ello cambia la siguiente línea en el fichero `polls/admin.py`:
	
	        ```python
            from .models import Choice, Question
            ```

        Por esta otra:

            ```python
	        from .models import Choice, Question, Categoria
            ```

        Y añade al final la siguiente línea:

	        ```python
            admin.site.register(Categoria)
            ```

    * Despliega el cambio producido al crear la nueva tabla en el entorno de producción.

{% capture notice-text %}
Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
	En este momento, muestra al profesor la aplicación funcionando en el otro hosting. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>