---
title: "Desplegando aplicaciones flask con uwsgi"
---

## uwsgi

[uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) es otro servidor WSGI HTTP para Python.

También lo podemos instalar desde repositorio, pero lo vamos a instalar en el entorno virtual:

    (flask)$ pip install uwsgi

## Despliegue de una aplicación flask con uwsgi

Hemos creado una aplicación django en el directorio: `/home/debian/flask_temperaturas` para desplegarla con uwsgi ejecutamos:

    (flask)$ uwsgi --http :8080 --chdir /home/debian/flask_temperaturas --wsgi-file    wsgi.py --process 4 --threads 2 --master 

Otra alternativa es crear un fichero `.ini` de configuración, `ejemplo.ini` de la siguiente manera:

    [uwsgi]
    http = :8080
    chdir = /home/debian/flask_temperaturas 
    wsgi-file = wsgi.py
    processes = 4
    threads = 2

Y para ejecutar el servidor, simplemente:

    (flask)$ uwsgi ejemplo.ini

De esta forma puedo tener varios ficheros de configuración del servidor uwsgi para las distintas aplicaciones python que sirva el servidor.

## Creación de una unidad systemd

Evidentemente no vamos a ejecutar "a mano" el programa uwsgi, vamos a crear una unidad systemd, para controlarla con `systemctl`, para ello, vamos a crear el fichero `/etc/systemd/system/uwsgi-temperaturas.service` con el siguiente contenido:

```
[Unit]
Description=uwsgi-temperaturas
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

WorkingDirectory=/home/debian/flask_temperaturas
Environment=PYTHONPATH='/home/debian/flask_temperaturas:/home/debian/venv/flask/lib/python3.9/site-packages'

PrivateTmp=true
```

Activamos la unidad de systemd, y la iniciamos:

```
systemctl enable gunicorn-temperaturas.service
systemctl start gunicorn-temperaturas.service
```

Si cambias el contenido de la unidad tendrás que hacer la recarga:

```
systemctl daemon-reload
```

## Proxy inversos para uwsgi

LÑa configuración será similar a la estudiada en gunicorn.