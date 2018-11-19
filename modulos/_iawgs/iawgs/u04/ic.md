---
title: Introducción a la integración continua
permalink: /iawgs/u04/ic.html
---

Antes de comenzar date de alta en el servicio web [travis](https://travis-ci.org/) con tu cuenta de github. **Travis** nos permite hacer integración continúa en los proyectos que tenemos guardados en nuestros repositorios de GitHub.

## Tarea 1: Corrector ortográfico de documentos markdown (test)

Imaginemos que estamos escribiendo documentos markdown y lo guardamos en un repositorio de github. Queremos que cada vez que hagamos una modificación (commit - push) queremos probar (test) si tienes alguna falta de ortografía. Ese proceso lo vamos a hacer de forma automática y continua con travis. Si tenemos activada la IC en travis sobre nuestro repositorio, cada vez que hagamos un push, travis va a crear una máquina (entorno de pruebas), va a clonar nuestro repositorio y va a realizar la prueba (test) que indiquemos en el fichero `.travis.yml`. Cuando termine la prueba nos va mandar un correo informándonos si la prueba ha tenido éxito o no.

Por lo tanto realiza los siguientes pasos:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-travis-diccionario](https://github.com/josedom24/ic-travis-diccionario).
* Activa la IC en travis de tu repositorio.
* Comprueba la prueba que vamos a realizar estudiando el fichero `.travis.yml`.
* Realiza cambios en los ficheros que están en el directorio `doc` y comprueba en travis como se van ejecutando las pruebas.


{% capture notice-text %}
Entrega varias capturas de pantalla donde se vea una prueba que termina en éxito (sin faltas de ortografía) y otra que no termine en éxito (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Comprobación de html5 válido y despliegue en surge.sh (test y deploy)

En esta tarea queremos desplegar una página html5 en el servicio surge.sh, además queremos comprobar si el código html5 es válido. Estas dos operaciones: comprobar si el html5 es válido (test) y el despliegue en surge.sh (deploy) lo vamos a hacer con travis de forma automática (IC y DC).

Antes de empezar vamos a aprender a trabajar con [surge.sh](http://surge.sh/):

* Siguiendo las instrucciones de esta [página](https://linuxconfig.org/how-to-install-nodejs-on-debian-9-stretch-linux) instala NodeJS y npm.
* Instala surge.sh
* Despliega una pequeña página web en el dominio `tunombre.surge.sh`.

{% capture notice-text %}
Entrega una descripción con los pasos fundamentales para la instalación y una captura de la página web que has realizado. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Vamos a añadir la funcionalidad de IC y DC con travis, para ello:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-travis-html5](https://github.com/josedom24/ic-travis-html5)
* Activa la IC en travis de tu repositorio.
* Comprueba la prueba y el despliegue que vamos a realizar estudiando el fichero `.travis.yml`.
* Modifica el fichero `.travis.yml` para poner el nombre de dominio que vas a utilziar.
* Para que travis pueda hacer el despliegue en surge le tenemos que indicar un TOKEN. Genera el token:
	
		surge token

* Crea dos variables de entorno en *settings* del proyecto travis:
	
    * `SURGE_LOGIN`: Indica el correo electrónico que has utilizado como lógin en surge
    * `SURGE_TOKEN`: Indica el TOKEN que has obtenido en el paso anterior.

* Realiza cambios en el fichero index.html del directorio `_build` y comprueba, que si el código html5 es válido se despliega y puedes aceder a la página web. Si el código html5 no es válido no se realiza el despliegue y te mandan un correo informando de la incidencia.

{% capture notice-text %}
Entrega una descripción con los pasos fundamentales que has realizado. Entrega varias capturas de pantalla donde se vea una prueba que termina en éxito (HTML5 válido) y otra que no termine en éxito (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Despliegue de un blog desarrollado con Pelican en GitHub Page (build, deploy)

En esta última tarea vamos a construir una página web (blog) con una herramienta escrita en python que se llama Pelican, y la vamos a desplegar en GitHub Page. Todo esto lo vamos a realizar co IC con Travis. Sigue los siguientes pasos:

* Crea un repositorio en GitHub con un README.md, crea también una rama `gh-pages` donde vamos  a publicar el blog.
* Crea un entorno virtual e instala Pelican (Puedes seguir las instrucciones que encenstras en esta página: [https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html)). (En el artículo se explica como crear un entrono virtual con python3, pero también funciona con un virtualenv de python2).
* Crea un proyecto, en tu repositorio local de github, con `pelican-quickstart`, aquí es muy importante que pongas la URL base (si suponemos que he creado un repositorio llamado `ic-blog` la URL base sería: `https://josedom24.github.io/ic-blog`).
* Con `make html` se genera el contenido estático, comprueba el resultado en el directorio `output`.
* Con `make devserver` se ejecuta un servidor web para desarrollo, con `make stopserver` se detiene dicho servidor.
* Siguiendo las instrucciones de la página anterior, crea un post en el blog.

{% capture notice-text %}
Entrega una captura de pantalla donde se vea el blog con la nueva entrada en el servidor web de desarrollo. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Ahora queremos que este proceso de "build" se haga de manera automática con travis. Además tenemos la opción `make publish github` que realiza el despliegue en Github Page, esto también queremos hacerlos de forma automática. Vamos por pasos:

* Activa tu repositorio en Travis.
* Crea el fichero `.travis.yml` con el siguiente contenido:

		language: python
		branches:
		  only:
		  - master
		install:
		- pip install pelican ghp-import markdown
		script:
		- make publish github

* Sigue las instrucciones de este artículo: [Publish your Pelican blog on Github pages via Travis-CI](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html) para crear un TOKEN en github, encriptarlo y añadirlo en el fichero `.travis.yml`.
* Por último, cómo indica en el artículo, modifica el fichero `Makefile` para poder desplegar en github usando tu TOKEN. (Sustituye la variable `$(`TRAVIS_REPO_SLUG`)` pon el nombre de tu repositorio.)

{% capture notice-text %}
Describe los pasos más importantes para realzar dicha práctica, y entrega una captura de pantalla donde se vea el blog con la nueva entrada en el GitHub Page. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Integración continúa de aplicación django (Test + Deploy)

Vamos a trabajar con el repositorio de la aplicación `django_tutorial`. Esta aplicación tiene definidas una serie de test, que podemos estudiar en el fichero `tests.py` del directorio `polls`.

Para ejecutar las pruebas unitarias, ejecutamos la instrucción `python manage.py test`.

{% capture notice-text %}
Estudia las distintas pruebas que se han realizado, y modifica el código de la aplicación para que al menos una de ella no se ejecute de manera exitosa. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

A continuación vamos a configurar la integración continúa para que cada vez que hagamos un commit se haga la ejecución de test en travis.

{% capture notice-text %}
Crea un fichero ``.travis.yml`` para realizar de los tests en travis. Entrega el fichero ``.travis.yml``, una captura de pantalla con un resltado exitoso de la IC y otro con un error.(1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Siguiendo la guía de esta página: [Continuous delivery of a Django app from Travis CI to PythonAnywhere](https://flowfx.de/blog/continuous-delivery-of-a-django-app-from-travis-ci-to-pythonanywhere/). Para además de realizar los tests, se haga un despliegue al servicio **pythonanyhere**.

{% capture notice-text %}
Entrega un breve descripción de los pasos más importantes para realizar el despliegue desde travis. (3 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

