---
title: Entorno de desarrollo y producción con aplicaciones web python
permalink: /iawgs/u03/python2.html
---

## Tarea 1: Entorno de desarrollo 

Formas parte del equipo de desarrollo de la aplicación "Gestión IESGN", aplicación web desarrollada con python, con el framework django. Vamos a configurar tu equipo como entorno de desarrollo para trabajar con la aplicación, para ello:

* Realiza un fork del repositorio de GitHub: [https://github.com/jd-iesgn/iaw_gestionGN](https://github.com/jd-iesgn/iaw_gestionGN).
* Clona el repositorio en tu equipo.
* Crea un entorno virtual python2 e instala las dependencias necesarias para que funcione el proyecto (fichero `requierements.txt`).
* Comprueba que vamos a trabajar con una base de datos sqlite (`gestion\settings.py`). ¿Cómo se llama la base de datos que vamos a crear?
* Crea la base de datos: `python manage.py migrate`. A partir del modelo de datos se crean las tablas de la base de datos.
* Añade los datos de prueba a la base de datos. Para más información: [https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata). Utiliza el fichero `datos.json`.
* Entra en la zona de administración para comprobar que los datos se han añadido correctamente. Usuario: `admin` ontraseña: `asdasd1234`).
* Ejecuta el servidor web de desarrollo y comprueba en el navegador que la aplicación está funcionando. Accede con el usuario `usuario` (contraseña: `asdasd1234`).

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando. Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (3 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Desarrollando nuestra aplicación

Vamos a realizar un cambio en la aplicación y comprobar que los cambios se realizan correctamente.

* Modifica la página inicial de la aplicación para que aparezca tu nombre.
* Sube los cambios al repositorio

{% capture notice-text %}
Muestra una captura de pantalla donde sea la modificación realizada. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Entorno de producción

Vamos a realizar el despliegue de nuestra aplicación en un entorno de producción, para ello vamos a utilizar una instancia del cloud, para ello:

* Instala en el servidor los servicios necesarios (apache2, mysql, ...). Instala el módulo de apache2 para ejecutar código python.
* Clona tu repositorio en el `DocumentRoot` de tu virtualhost.
* Crea un entorno virtual e instala las dependencias de tu aplicación.
* Instala el módulo que permite que python trabaje con mysql: 

		$ apt-get install python-mysqldb

	Y en el entorno virtual:

		(env)$ pip install mysql-python

* Configura un virtualhost en apache2 con la configuración adecuada para que funcione la aplicación. El punto de entrada de nuestro servidor será `iaw_gestionGN/gestion/wsgi.py`.
* Crea una base de datos y un usuario en mysql.
* Configura la aplicación para trabajar con mysql, para ello modifica la configuración de la base de datos en el archivo `settings.py`:

		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.mysql',
		        'NAME': 'myproject',
		        'USER': 'myprojectuser',
		        'PASSWORD': 'password',
		        'HOST': 'localhost',
		        'PORT': '',
		    }
		}

* Crea las tablas de la base de datos y carga los datos de pruebas. Accede a mysql y comprueba que se han creado de forma adecuada.
* Desactiva en la configuración (fichero `settings.py`) el modo debug a False. Para que los errores de ejecución no den información sensible de la aplicación.
* Muestra la página funcionando.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando. Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Modificación de la aplicación en el entorno de producción

Vamos a realizar cambios en el entorno de desarrollo y posteriormente vamos a subirlas a producción.

* Modifica la página inicial para que muestre otra imagen. Despliega los cambios en el servidor de producción.
* Vamos a crear una nueva tabla en la base de datos, para ello sigue los siguientes pasos:
	
1. Añade un n uevo modelo al fichero `centro/models.py`:

		class Modulos(models.Model):	
			Abr = models.CharField(max_length=4)
			Nombre = models.CharField(max_length=50)
			Unidad = models.ForeignKey(Cursos,blank=True,null=True,on_delete=models.SET_NULL)
			
			def __unicode__(self):
				return self.Abr+" - "+self.Nombre 		

			class Meta:
				verbose_name="Modulo"
				verbose_name_plural="Modulos"

2. Crea una nueva migración: `python manage.py makemigrations`. 
3. Y realiza la migración: `python manage.py migrate`
4. Añade el nuevo modelo al sitio de administración de django:

Para ello cambia la siguiente línea en el fichero `centro/admin.py`:
	
	from centro.models import Cursos,Alumnos,Departamentos,Profesores,Areas

Por esta otra:

	from centro.models import Cursos,Alumnos,Departamentos,Profesores,Areas,Modulos

Y añade al final la siguiente línea:

	admin.site.register(Modulos)

* Despliega el cambio producido al crear la nueva tabla en el entorno de producción.

{% capture notice-text %}
Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
	En este momento, muestra al profesor la aplicación funcionando en el otro hosting. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Despliegue de nuestra aplicación en un hosting python: pythonanywhere

* Siguiendo la [documentación](https://help.pythonanywhere.com/pages/) despliega nuestra aplicación django en pythonanwhere. Utiliza git para desplegar los ficheros y crea una base de datos en tu proyecto. Si con la documentación no es suficiente puede seguir mi documento: [Despliegue de aplicación flask en hosting pythonanywhere](https://github.com/josedom24/curso_flask/tree/master/curso/u34).

{% capture notice-text %}
Entrega una breve documentación donde expliques los pasos más importantes para el despliegue en pythonanywhere (3 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

{% capture warning-text %}
* Identificación de problemas: si estamos desarrollando una aplicación es necesario probarla, realizar test.
* Identificación de problemas: además de lo anterior el equipo de desarrollo necesita ir haciendo otros procesos: analizando el código generado, generar documentación,...
* Identificación de problemas: Nuestro equipo de desarrollo las componen varios miembros: es fundamental utilizar un repositorio común (git)
* Identificación de problemas: Si seguimos una metodología ágil es deseable que todos los cambios que vayan realizando los programadores se vayan probando, analizando, ... de forma continúa
* Identificación de problemas: ¿Y si esas tareas las automatizamos? -> Integración continúa
{% endcapture %}<div class="notice--warning">{{ warning-text | markdownify }}</div>


