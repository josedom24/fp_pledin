---
title: "Ejecución de script Python"
permalink: /serviciosgs/u05/script_python.html
---

## Apache2 y módulo wsgi

Instalamos el módulo de apache2 que nos permite ejecutar código python: `libapache2-mod-wsgi-py3`.

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

Aunque podemos instalarlo desde repositorios, nosotros vamos a instalarlo en el entorno virtual:

    (env)$ pip install gunicorn

**Despliegue de una aplicación django con gunicorn**

Hemos creado una aplicación django en el directorio: `/home/debian/myapp` para desplegarla con gunicorn ejecutamos:

    /home/debian/myapp# ~/env/bin/gunicorn -w 2 -b :8080 myapp.wsgi:application
    [2020-01-07 18:55:34 +0000] [14329] [INFO] Starting gunicorn 20.0.4
    [2020-01-07 18:55:34 +0000] [14329] [INFO] Listening at: http://0.0.0.0:8080 (14329)
    [2020-01-07 18:55:34 +0000] [14329] [INFO] Using worker: sync
    [2020-01-07 18:55:34 +0000] [14333] [INFO] Booting worker with pid: 14333
    [2020-01-07 18:55:34 +0000] [14334] [INFO] Booting worker with pid: 14334
    ...
   

Con la opción `-w` indico el número de procesos que van a servir las peticiones, y con la opción `-b` indico la dirección y el puerto de escucha. Para más información: [How to Deploy Python WSGI Apps Using Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx).

Podemos configurar systemd para gunicorn se pueda utilizar con `systemctl`, esto lo puedes ver en el documento: [Deploying Gunicorn](http://docs.gunicorn.org/en/stable/deploy.html#systemd).

Finalmente podemos configurar apache2 o nginx como proxy inversos para enviar todas las peticiones python a gunicorn (podemos hacer que el servidor web sirva el contenido estático).

### uwsgi

También lo podemos instalar desde repositorio, pero lo vamos a instalar en el entorno virtual:

    (env)$ pip install uwsgi

**Despliegue de una aplicación django con uwsgi**

Hemos creado una aplicación django en el directorio: `/home/debian/myapp` para desplegarla con uwsgi ejecutamos:

    ~/env/bin/uwsgi --http :8080 --plugin python35 --chdir /home/debian/myapp --wsgi-file myapp/wsgi.py --process 4 --threads 2 --master 

Otra alternativa es crear un fichero `.ini` de configuración, `ejemplo.ini` de la siguiente manera:

    [uwsgi]
    http = :8080
    chdir = /home/debian/myapp 
    wsgi-file = myapp/wsgi.py
    processes = 4
    threads = 2

Y para ejecutar el servidor, simplemente:

    ~/env/bin/uwsgi ejemplo.ini

De esta forma puedo tener varios ficheros de configuración del servidor uwsgi para las distintas aplicaciones python que sirva el servidor.

En el ejemplo anterior hemos usado la opción `http` para indicar que se va a devolver una respuesta HTTP, podemos usar varias opciones:

* `http`: Se comporta como un servidor http. Por ejemplo en nginx usaremos `proxy_pass` para hacer de proxy inverso.
* `socket`: La respuesta ofrecida por el servidor no es HTTP, es usando el prootocolo uwsgi. Por ejemplo en nginx usaremos `uwsgi_pass` para hacer de proxy inverso.

Existen muchas más opciones que puedes usar: [http://uwsgi-docs.readthedocs.io/en/latest/Options.html](http://uwsgi-docs.readthedocs.io/en/latest/Options.html).

* [Apache support](http://uwsgi-docs.readthedocs.io/en/latest/Apache.html)
* [Nginx support](http://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)

