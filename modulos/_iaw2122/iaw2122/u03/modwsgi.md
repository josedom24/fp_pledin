---
title: "Ejercicio 1: Desplegando aplicaciones flask con apache2 + mod_wsgi"
---

## Despliegue en el entorno de desarrollo

Vamos a trabajar con la aplicación flask_temperaturas que puedes encontrar en el siguiente enlace: [https://github.com/josedom24/flask_temperaturas](https://github.com/josedom24/flask_temperaturas).

Clona el repositorio en tu equipo, mira las versiones de los paquetes necesarios para que la aplicación funcione en el fichero `requirements.txt` y responde las siguientes preguntas:

### Trabajamos con entornos virtuales

Crea un entorno virtual con el módulo `venv` e instala en él los paquetes necesarios para que el programa funcione. Una vez instalado, ejecuta la aplicación con el servidor de desarrollo y comprueba que funciona.

### Configuración de apache2 para servir una aplicación web flask

Lo primero que tenemos que hacer es instala el módulo de apache2 wsgi:

    apt install libapache2-mod-wsgi-py3

* Suponemos que tenemos un servidor web apache2 con el módulo wsgi activado.
* Suponemos que nuestra aplicación se encuentra en `/home/debian/flask_temperatura`.
* Suponemos que hemos creado un entorno virtual con los paquetes instalados en `/home/debian/venv/flask`.

### Creación del fichero wsgi

Lo primero que vamos a hacer es crear el fichero WSGI, que vamos a llamar `wsgi.py` estará en `/home/debian/flask_temperatura` y tendrá el siguiente contenido:

    from app import app as application

Veamos:

* El primer `app` corresponde con el nombre del módulo, es decir del fichero del programa, en nuestro caso se llama `app.py`.
* El segundo `app` corresponde a la aplicación flask creada en `app.py`:  `app = Flask(__name__)`.
* Importamos la aplicación flask, pero la llamamos `application` necesario para que el servidor web pueda enviarle peticiones.

### Configuración de apache2

Yo he utilizado el virtualhost por defecto, si usamos otro virtualhost esta configuración ira en el fichero correspondiente:

    WSGIDaemonProcess flask_temp python-path=/home/vagrant/flask_temperaturas:/home/vagrant/venv/flask/lib/python3.9/site-packages
    WSGIProcessGroup flask_temp
    WSGIScriptAlias / /home/vagrant/flask_temperaturas/wsgi.py process-group=flask_temp
    <Directory /home/vagrant/flask_temperaturas>
            Require all granted
    </Directory>


Vamos a explicar la configuración:

* El `DocumentRoot`se indica el directorio donde está la aplicación. Realmente el servidor web siempre va a llamar al fichero WSGI `wsgi.py`, pero el DocumentRoot es necesario por si hay contenido estático.
* La directiva `WSGIDaemonProcess`: Se define un grupo de procesos que se van a encargar de ejecutar la aplicación (servidor de aplicaciones). A estos procesos se le ponen un nombre (`flask_temp`) y se indica los directorios donde se encuentran la aplicación y los paquetes necesarios (`python-path`), como puedes observar se pone el directorio donde esta la aplicación y el directorio donde se encuentran los paquetes en el entorno virtual, separados por dos puntos.
* `WSGIProcessGroup`: Nos permite agrupar procesos. Se pone el misimo nombre que hemos definido en la directiva anterior.
* La directiva `WSGIScriptAlias` nos permite indicar que programa se va a ejecutar (el fichero WSGI: `/home/debian/flask_temperaturas/wsgi.py`) cuando se haga una petición a la url `/` y que proceso lo va a ejecutar.

Reinicia el servicio web y prueba el funcionamiento. Si te da algún erro 500 puedes ver los errores, en `/var/log/apache2/error.log`.

{% capture notice-text %}

* Configura la aplicación [guestbook](https://github.com/josedom24/guestbook) para que sea servida con apache2 + mod_wsgi. Explica los pasos más importante y entrega una prueba de funcionamiento.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

