---
title: "Ejercicio 2: Desplegando aplicaciones flask con apache2 + gunicorn"
---

## Servidores wsgi

Otra forma de ejecutar código python es usar servidores de aplicación wsgi. Tenemos a nuestra disposición varios servidores: [A Comparison of Web Servers for Python Based Web Applications](https://www.digitalocean.com/community/tutorials/a-comparison-of-web-servers-for-python-based-web-applications). Si usamos el servidor web nginx está opción es la única disponible, pero en apache2 también la podemos usar. Realmente usamos los servidores web como proxies inversos que envían la petición python al servidor WSGI que estemos utilizando.

## gunicorn

[Gunicorn](http://gunicorn.org/), también conocido como Green Unicorn (Unicornio Verde), es un servidor WSGI HTTP para Python.

Aunque podemos instalarlo desde repositorios, nosotros vamos a instalarlo en el entorno virtual:

    (flask)$ pip install gunicorn

## Despliegue de una aplicación flask con gunicorn

Tenemos nuestra aplicación en: `/home/debian/flask_temperaturas` para desplegarla con gunicorn ejecutamos:

    (flask) /home/debian/flask_temperaturas# gunicorn -w 2 -b :8080 wsgi:application
    [2021-10-28 12:13:03 +0000] [4706] [INFO] Starting gunicorn 20.1.0
    [2021-10-28 12:13:03 +0000] [4706] [INFO] Listening at: http://0.0.0.0:8081 (4706)
    [2021-10-28 12:13:03 +0000] [4706] [INFO] Using worker: sync
    [2021-10-28 12:13:03 +0000] [4707] [INFO] Booting worker with pid: 4707
    [2021-10-28 12:13:03 +0000] [4708] [INFO] Booting worker with pid: 4708

    ...
   

Con la opción `-w` indico el número de procesos que van a servir las peticiones, y con la opción `-b` indico la dirección y el puerto de escucha. Para más información: [How to Deploy Python WSGI Apps Using Gunicorn](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx)

## Creación de una unidad systemd

Evidentemente no vamos a ejecutar "a mano" el programa gunicorn, vamos a crear una unidad systemd, para controlarla con `systemctl`, para ello, vamos a crear el fichero `/etc/systemd/system/gunicorn-temperaturas.service` con el siguiente contenido:

```
[Unit]
Description=gunicorn-temperaturas
After=network.target

[Install]
WantedBy=multi-user.target

[Service]
User=www-data
Group=www-data
Restart=always

ExecStart=/home/debian/venv/flask/bin/gunicorn -w 2 -b :8080 wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

WorkingDirectory=/home/debian/flask_temperaturas
Environment=PYTHONPATH='/home/debian/flask_temperaturas:/home/debian/venv/flask/lib/python3.9/site-packages'

PrivateTmp=true
```

Activamos la unidad de systemd, y la inciamos:

```
systemctl enable gunicorn-temperaturas.service
systemctl start gunicorn-temperaturas.service
```

Si cambias el contenido de la unidad tendrás que hacer la recarga:

```
systemctl daemon-reload
```

## Apache2 como proxy inverso de gunicorn

Activamos el módulo `proxy_http` y en la configuración de algún virtualhost:

```
DocumentRoot /home/debian/flask_temperaturas
ProxyPass / http://127.0.0.1:8080/
ProxyPassReverse / http://127.0.0.1:8080/
<Directory /home/debian/flask_temperaturas>
        Require all granted
</Directory>
```

## nginx como proxy inverso de gunicorn

En la configuración de un virtualhost:

```
location / {
    proxy_pass http://localhost:8080;
    proxy_set_header X-Forwarded-Host $host:$server_port;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

{% capture notice-text %}

* Configura la aplicación [guestbook](https://github.com/josedom24/guestbook) para que sea servida con apache2 + mod_wsgi. Explica los pasos más importante y entrega una prueba de funcionamiento.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>