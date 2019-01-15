---
title: "Ejecución de script Python"
permalink: /serviciosgs/u06/script_python.html
---

## Apache2 y módulo wsgi

Instalamos el módulo de apache2 que nos permite ejecutar código python: `libapache2-mod-wsgi`.

Veamos un ejemplo de configuración para una aplicación django. Suponemos que el fichero wsgi se encuentra en el directorio: ``/var/www/html/mysite/mysite/wsgi.py`` y configuramos apache2 de la siguiente manera::

    <VirtualHost *>
        ServerName www.example.com
        DocumentRoot /var/www/html/mysite
        WSGIDaemonProcess mysite user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/mysite
        WSGIScriptAlias / /var/www/html/mysite/mysite/wsgi.py

        <Directory /var/www/html/mysite>
                WSGIProcessGroup mysite
                WSGIApplicationGroup %{GLOBAL}
                Require all granted
        </Directory>
    </VirtualHost>

Si hemos usado un entorno virtual creado en el directorio ``/home/debian/python``, la siguiente línea de configuración quedaría de la siguiente manera:

    ...
    WSGIDaemonProcess mysite user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/mysite:/home/debian/python/lib/python2.7/site-packages
    ...

## Usando servidores wsgi

Otra forma de ejecutar código python es usar servidores de aplicación wsgi. Tenemos a nuestra disposición varios servidores: [A Comparison of Web Servers for Python Based Web Applications](https://www.digitalocean.com/community/tutorials/a-comparison-of-web-servers-for-python-based-web-applications). Si usamos el servidor web nginx está opción es la úmica disponible, pero en apache2 también la podemos usar. Realmente usamos los servidores web como proxies inversos que envían la petición python al servidor WSGI que estemos utilizando.

### gunicorn

[Gunicorn](http://gunicorn.org/), también conocido como Green Unicorn (Unicornio Verde), es un servidor WSGI HTTP para Python.

Para instalarlo en Debian 9 Stretch:

    apt install gunicorn

También lo podemos instalar con `pip` en un entorno virtual.

**Despliegue de una aplicación django con gunicorn**

Hemos creado una aplicación django en el directorio: `/home/debian/myapp` para desplegarla con gunicorn ejecutamos:

    /home/debian/myapp# gunicorn -w 2 -b :8080 myapp.wsgi:application
    [2018-01-07 18:55:34 +0000] [14329] [INFO] Starting gunicorn 19.6.0
    [2018-01-07 18:55:34 +0000] [14329] [INFO] Listening at: http://0.0.0.0:8080 (14329)
    [2018-01-07 18:55:34 +0000] [14329] [INFO] Using worker: sync
    [2018-01-07 18:55:34 +0000] [14333] [INFO] Booting worker with pid: 14333
    [2018-01-07 18:55:34 +0000] [14334] [INFO] Booting worker with pid: 14334
    ...
   

Con la opción `-w` indico el número de procesos que van a servir las peticiones, y con la opción `-b` indico la dirección y el puerto de escucha. Para más información: [How to Deploy Python WSGI Apps Using Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx).

Podemos configurar systemd para gunicorn se pueda utilizar con `systemctl`, esto lo puedes ver en el documento: [Deploying Gunicorn](http://docs.gunicorn.org/en/stable/deploy.html#systemd).

Finalmente podemos configurar apache2 o nginx como proxy inversos para enviar todas las peticiones python a gunicorn (podemos hacer que el servidor web sirva el contenido estático).

### uwsgi

Para instalarlo en Debian 9 Stretch:

    apt install uwsgi
    apt install uwsgi-plugin-python

También lo podemos instalar con `pip` en un entorno virtual.  

**Despliegue de una aplicación django con uwsgi**

Hemos creado una aplicación django en el directorio: `/home/debian/myapp` para desplegarla con uwsgi ejecutamos:

    uwsgi --http :8080 --plugin python --chdir /home/debian/myapp --wsgi-file myapp/wsgi.py --process 4 --threads 2 --master 

Otra alternativa es crear un fichero `.ini` de configuración, `ejemplo.ini` de la siguiente manera:

    [uwsgi]
    http = :8080
    chdir = /home/debian/myapp 
    wsgi-file = myapp/wsgi.py
    processes = 4
    threads = 2

Y para ejecutar el servidor, simplemente:

    uwsgi ejemplo.ini

De esta forma puedo tener varios ficheros de configuración del servidor uwsgi para las distintas aplicaciones python que sirva el servidor.

Podemos tener los ficheros de configuración en `/etc/uwsgi/apps-available` y para habiliatar podemos crear un enlace simbólico a estos ficheros en `/etc/uwsgi/apps-enabled`.

En el ejemplo anterior hemos usado la opción `http` para indicar que se va a devolver una respuesta HTTP, podemos usar varias opciones:

* `http`: Se comporta como un servidor http.
* `http-socket`: Si vamos a utilizar un proxy inverso usando el servidor uwsgi.
* `socket`: La respuesta ofrecida por el servidor no es HTTP, es usando el protocolo uwsgi.

Existen muchas más opciones que puedes usar: [http://uwsgi-docs.readthedocs.io/en/latest/Options.html](http://uwsgi-docs.readthedocs.io/en/latest/Options.html).

* [Apache support](http://uwsgi-docs.readthedocs.io/en/latest/Apache.html)
* [Nginx support](http://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)

