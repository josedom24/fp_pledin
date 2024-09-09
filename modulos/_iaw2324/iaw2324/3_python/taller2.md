---
title: "Taller 2: Desplegando aplicaciones flask con apache2/nginx + uwsgi"
---

## ¿Qué vas a aprender en este taller?

* A instalar un servidor de aplicaciones uwsgi para servir una aplicación python flask.
* Configurar un servidor web apache2 como proxy inverso para acceder a la aplicación.
* Configurar un servidor web nginx como proxy inverso para acceder a la aplicación.

## ¿Qué tienes que hacer?

[uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) es un servidor de aplicaciones WSGI HTTP para Python.

Debemos tener instalado el paquete `python3-dev` que es una dependencia necesaria. También es posible que necesites las herramientas para compilar, instala el paquete `build-essential` Podríamos instalar el paquete `uwsgi` desde los repositorios, pero lo vamos a instalar en el entorno virtual:

    (flask)$ pip install uwsgi

## Despliegue de una aplicación flask con uwsgi

* Suponemos que nuestra aplicación se encuentra en `/home/debian/guestbook`.
* Suponemos que hemos creado un entorno virtual con los paquetes instalados en `/home/debian/venv/flask`.

Para probar el servidor uwsgi podemos ejecutar en la línea de comandos:

    (flask)$ uwsgi --http :8080 --chdir /home/debian/guestbook --wsgi-file wsgi.py --process 4 --threads 2 --master 

Otra alternativa es crear un fichero `.ini` de configuración, `ejemplo.ini` de la siguiente manera:

    [uwsgi]
    http = :8080
    chdir = /home/debian/guestbook 
    wsgi-file = wsgi.py
    processes = 4
    threads = 2

Y para ejecutar el servidor, simplemente:

    (flask)$ uwsgi ejemplo.ini

De esta forma puedo tener varios ficheros de configuración del servidor uwsgi para las distintas aplicaciones python que sirve el servidor.

La instalación se está sirviendo por el servidor uwsgi en `localhost:8080`.

## Creación de una unidad systemd

Evidentemente no vamos a ejecutar "a mano" el programa uwsgi, vamos a crear una unidad systemd, para controlarla con `systemctl`, para ello, vamos a crear el fichero `/etc/systemd/system/uwsgi-guestbook.service` con el siguiente contenido:

```
[Unit]
Description=uwsgi-guestbook
After=network.target

[Install]
WantedBy=multi-user.target

[Service]
User=www-data
Group=www-data
Restart=always

ExecStart=/home/debian/venv/flask/bin/uwsgi /home/debian/venv/flask/ejemplo.ini
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

WorkingDirectory=/home/debian/guestbook
Environment=PYTHONPATH='/home/debian/guestbook:/home/debian/venv/flask/lib/pythonX.X/site-packages'

PrivateTmp=true
```

**Nota: Tienes que mirar la versión de python3 para sustituir el nombre del directorio `pythonX.X`.**

Activamos la unidad de systemd, y la iniciamos:

```
systemctl enable uwsgi-guestbook.service
systemctl start uwsgi-guestbook.service
```

Si cambias el contenido de la unidad tendrás que hacer la recarga:

```
systemctl daemon-reload
```

## Proxy inversos para uwsgi

### Apache2 como proxy inverso de uwsgi

Activamos el módulo `proxy_http` y en la configuración de algún virtualhost:

```
DocumentRoot /home/debian/flask_temperaturas
ProxyPass / http://127.0.0.1:8080/
ProxyPassReverse / http://127.0.0.1:8080/
<Directory /home/debian/flask_temperaturas>
        Require all granted
</Directory>
```

## nginx como proxy inverso de uwsgi

En la configuración de un virtualhost:

```
location / {
    proxy_pass http://localhost:8080;
    include proxy_params;
}
```

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega la el contenido del fichero de configuración de la unidad systemctl.
2. Entrega la salida del comando `systemctl status uwsgi-guestbook.service`.
3. Configura apache2 como proxy inverso. Entrega la configuración del virtualhost (el mismo que el del taller anterior) y una captura accediendo a la aplicación web.
4. Instala nginx. Configura nginx como proxy inverso. Entrega la configuración del virtualhost y una captura accediendo a la aplicación web.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
