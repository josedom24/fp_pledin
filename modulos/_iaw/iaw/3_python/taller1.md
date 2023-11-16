---
title: "Taller 1: Desplegando aplicaciones flask con apache2 + mod_wsgi"
---

## ¿Qué vas a aprender en este taller?

* A instalar un servidor apache con el módulo wsgi para servir una aplicación python flask.

## ¿Qué tienes que hacer?

Podemos seguir trabajando en la máquina de OpenStack del ejercicio anterior. Suponemos que ya tienes clonado el repositorio de la aplicación guestbook, y que has creado un entorno virtual donde has instalado las librería para que la aplicación funcione.

### Configuración de apache2 para servir una aplicación web flask

Lo primero que tenemos que hacer es instalar el módulo de apache2 wsgi:

    apt install libapache2-mod-wsgi-py3

* Suponemos que tenemos un servidor web apache2 con el módulo wsgi activado.
* Suponemos que nuestra aplicación se encuentra en `/home/debian/guestbook`.
* Suponemos que hemos creado un entorno virtual con los paquetes instalados en `/home/debian/venv/flask`.

### Creación del fichero wsgi

Lo primero que vamos a hacer es crear el fichero WSGI, que vamos a llamar `wsgi.py` estará en `/home/debian/guestbook/` y tendrá el siguiente contenido:

    from app import prog as application

Veamos:

* El `app` corresponde con el nombre del módulo, es decir, el fichero del programa, en nuestro caso se llama `app.py`.
* El `prog` corresponde a la aplicación flask creada en `app.py`:  `prog = Flask(__name__)`.
* Importamos la aplicación flask, pero la llamamos `application` necesario para que el servidor web pueda enviarle peticiones.

### Configuración de apache2

Crea un virtualhost que se acceda con el nombre `flask.tunombre.org`, esta configuración irá en el fichero correspondiente:

	DocumentRoot /home/debian/guestbook
    WSGIDaemonProcess flask_guestbook python-path=/home/debian/guestbook:/home/debian/venv/flask/lib/pythonX.X/site-packages
    WSGIProcessGroup flask_guestbook
    WSGIScriptAlias / /home/debian/guestbook/wsgi.py process-group=flask_guestbook
    <Directory /home/debian/guestbook>
            Require all granted
    </Directory>

**Nota: Tienes que mirar la versión de python3 para sustituir el nombre del directorio `pythonX.X`.**

Vamos a explicar la configuración:

* El `DocumentRoot`se indica el directorio donde está la aplicación. Realmente el servidor web siempre va a llamar al fichero WSGI `wsgi.py`, pero el DocumentRoot es necesario para servir el contenido estático.
* La directiva `WSGIDaemonProcess`: Se define un grupo de procesos que se van a encargar de ejecutar la aplicación (servidor de aplicaciones). A estos procesos se le ponen un nombre (`flask_guestbook`) y se indica los directorios donde se encuentran la aplicación y los paquetes necesarios (`python-path`), como puedes observar se pone el directorio donde esta la aplicación y el directorio donde se encuentran los paquetes en el entorno virtual, separados por dos puntos.
* `WSGIProcessGroup`: Nos permite agrupar procesos. Se pone el mismo nombre que hemos definido en la directiva anterior.
* La directiva `WSGIScriptAlias` nos permite indicar que programa se va a ejecutar (el fichero WSGI: `/home/debian/guestbook/wsgi.py`) cuando se haga una petición a la url `/` y que proceso lo va a ejecutar.

Reinicia el servicio web y prueba el funcionamiento. Si te da algún error 500 puedes ver los errores, en `/var/log/apache2/error.log`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega la configuración del virtualhost.
2. Entrega una captura de pantalla accediendo a la aplicación web.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

