---
title: "Ejecución de script Python con Apache2 + módulo wsgi"
permalink: /iawgs/u03/script_python.html
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
    WSGIDaemonProcess mysite user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/mysite:/home/debian/python/lib/python3.7/site-packages
    ...
