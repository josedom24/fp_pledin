---
title: "Ejecución de script Python con nginx/apache2 + gunicorn"
permalink: /iawgs/u03/script_python2.html
---

Otra forma de ejecutar código python es usar servidores de aplicación wsgi. Tenemos a nuestra disposición varios servidores: [A Comparison of Web Servers for Python Based Web Applications](https://www.digitalocean.com/community/tutorials/a-comparison-of-web-servers-for-python-based-web-applications). Si usamos el servidor web nginx está opción es la única disponible, pero en apache2 también la podemos usar. Realmente usamos los servidores web como proxies inversos que envían la petición python al servidor WSGI que estemos utilizando.

## gunicorn

[Gunicorn](http://gunicorn.org/), también conocido como Green Unicorn (Unicornio Verde), es un servidor WSGI HTTP para Python.

Para instalarlo en Debian 9 Stretch:

    apt install gunicorn

También lo podemos instalar con `pip` en un entorno virtual.

### Despliegue de una aplicación django con gunicorn

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