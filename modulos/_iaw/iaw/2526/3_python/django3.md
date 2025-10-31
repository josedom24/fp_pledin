---
title: "Despliegue de aplicaciones Django con uWSGI"
---

## Introducción

En los apartados anteriores desplegamos la aplicación Django usando **Apache2** con el módulo **mod_wsgi**, que ejecutaba la aplicación directamente dentro del servidor web.
En esta práctica vamos a hacerlo de otra forma: usaremos un **servidor de aplicaciones independiente**, **uWSGI**, encargado de ejecutar Django, y opcionalmente un **servidor web** (Apache2 o Nginx) que actuará como **proxy inverso**.

La arquitectura final será:

```
Cliente HTTP → Apache2 / Nginx (proxy inverso)
                        ↓
                  uWSGI (servidor de aplicaciones)
                        ↓
              Django (guestbook_project/wsgi.py)
```

Esta forma de despliegue es más modular y se utiliza ampliamente en producción, ya que separa el servidor web (que maneja HTTP, HTTPS y contenido estático) del proceso que ejecuta la lógica de Django.


## Instalación de uWSGI

Para mantener las dependencias aisladas, **uWSGI se instalará dentro del entorno virtual** del proyecto.

```bash
source /home/debian/venv/django/bin/activate
pip install uwsgi
```

Comprobamos la instalación:

```bash
uwsgi --version
```

## Configuración 1: uWSGI con modo HTTP

En lugar de exponer Django directamente a Internet, lo habitual es ejecutar **uWSGI escuchando en un puerto interno (por ejemplo, 8080)** y hacer que **Apache2 o Nginx actúen como proxy inverso**.
El proxy recibe las peticiones HTTP en el puerto 80 o 443 y las reenvía localmente a uWSGI.

De esta forma:

* uWSGI sigue siendo el **servidor de aplicaciones** que ejecuta Django.
* Apache o Nginx se encargan de la **gestión de clientes**, archivos estáticos, HTTPS, etc.
* El puerto 8080 no se expone al exterior, solo se usa para comunicación interna.


### Archivo de configuración de uWSGI

Creamos el archivo `/home/debian/guestbook_project/uwsgi.ini` con el siguiente contenido:

```ini
[uwsgi]
http = 127.0.0.1:8080
chdir = /home/debian/guestbook_project
wsgi-file = guestbook_project/wsgi.py
processes = 4
threads = 2
master = true
vacuum = true
```

#### Explicación

| Parámetro               | Descripción                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| `http = 127.0.0.1:8080` | uWSGI escucha conexiones HTTP **solo en localhost**, no accesibles desde fuera del servidor. |
| `chdir`                 | Directorio donde se encuentra el proyecto Django.                                            |
| `wsgi-file`             | Archivo `wsgi.py` del proyecto, punto de entrada de la aplicación.                           |
| `processes`             | Número de procesos de trabajo concurrentes.                                                  |
| `threads`               | Número de hilos por proceso.                                                                 |
| `master`                | Habilita el proceso maestro (gestiona los trabajadores).                                     |
| `vacuum`                | Limpia los sockets o ficheros temporales al detener el servicio.                             |


### Ejecución de prueba

Ejecutamos uWSGI con la configuración anterior:

```bash
uwsgi --ini /home/debian/guestbook_project/uwsgi.ini
```

uWSGI quedará escuchando localmente en el puerto 8080.
Si queremos comprobar que está funcionando, podemos hacer una petición desde el propio servidor:

```bash
curl http://127.0.0.1:8080
```

Esto debería devolver el contenido de la página principal de la aplicación Django.


## Confiuración 2: uWSGI con socket Unix

En un entorno real, no queremos que uWSGI atienda peticiones HTTP directamente.
En su lugar, un **servidor web (Apache2 o Nginx)** escuchará en el puerto 80 o 443 y reenviará las peticiones a uWSGI a través de un **socket interno** (exactamente igual que PHP-FPM).

Editamos el archivo `/home/debian/guestbook_project/uwsgi.ini` para dejarlo así:

```ini
[uwsgi]
socket = /run/uwsgi/guestbook.sock
chmod-socket = 660

chdir = /home/debian/guestbook_project
wsgi-file = guestbook_project/wsgi.py

processes = 4
threads = 2
master = true
vacuum = true
```

### Explicación

| Parámetro      | Descripción                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `socket`       | Crea un socket Unix en `/run/uwsgi/guestbook.sock`.                         |
| `chmod-socket` | Permite que otros procesos (por ejemplo, Apache o Nginx) accedan al socket. |
| `master`       | Activa el proceso maestro (gestiona subprocesos).                           |
| `vacuum`       | Limpia el socket al detener el servicio.                                    |

El resto de parámetros (`chdir`, `wsgi-file`, `processes`, `threads`) son los mismos que antes.


## Unidad de sistema (systemd)

Para que uWSGI se ejecute automáticamente y se integre con el sistema, creamos un servicio systemd.

Archivo: `/etc/systemd/system/guestbook_uwsgi.service`

```ini
[Unit]
Description=uWSGI service for Django Guestbook
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/debian/guestbook_project
Environment="PATH=/home/debian/venv/django/bin"
ExecStart=/home/debian/venv/django/bin/uwsgi --ini /home/debian/guestbook_project/uwsgi.ini

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Activamos el servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable guestbook_uwsgi
sudo systemctl start guestbook_uwsgi
sudo systemctl status guestbook_uwsgi
```

A partir de ahora, uWSGI se ejecutará automáticamente al arrancar el sistema y gestionará nuestra aplicación Django.

## Configuración del proxy inverso con Apache2

### Modo 1: uWSGI en modo HTTP (puerto 8080)

En esta configuración, Apache actúa como **proxy inverso HTTP**: recibe las peticiones en el puerto 80 y las reenvía a `127.0.0.1:8080`, donde uWSGI atiende las peticiones HTTP.

Instalamos y activamos los módulos necesarios:

```bash
sudo a2enmod proxy proxy_http
```

Creamos el archivo de configuración `/etc/apache2/sites-available/guestbook_http.conf`:

```apache
<VirtualHost *:80>
    ServerName guestbook.local
    ServerAdmin webmaster@localhost

    # Proxy inverso hacia uWSGI (modo HTTP)
    ProxyPass / http://127.0.0.1:8080/
    ProxyPassReverse / http://127.0.0.1:8080/

    # Archivos estáticos (CSS, JS, imágenes)
    Alias /static/ /home/debian/guestbook_project/static/
    <Directory /home/debian/guestbook_project/static>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/guestbook_error.log
    CustomLog ${APACHE_LOG_DIR}/guestbook_access.log combined
</VirtualHost>
```

Activamos el sitio y recargamos Apache:

```bash
sudo a2ensite guestbook_http.conf
sudo systemctl reload apache2
```

El flujo completo será:

```
Cliente → Apache2 (puerto 80) → uWSGI (127.0.0.1:8080) → Django
```

### Modo 2: uWSGI con socket Unix

En este caso, Apache2 no se comunica con uWSGI por HTTP, sino mediante el **protocolo nativo uwsgi** usando el módulo `mod_proxy_uwsgi`.

Instalamos y activamos el módulo correspondiente:

```bash
sudo apt install libapache2-mod-proxy-uwsgi
sudo a2enmod proxy proxy_uwsgi
```

Creamos el archivo `/etc/apache2/sites-available/guestbook_socket.conf`:

```apache
<VirtualHost *:80>
    ServerName guestbook.local
    ServerAdmin webmaster@localhost

    # Proxy inverso usando el socket Unix de uWSGI
    ProxyPassMatch ^/(.*)$ unix:/run/uwsgi/guestbook.sock|uwsgi://localhost/

    # Archivos estáticos
    Alias /static/ /home/debian/guestbook_project/static/
    <Directory /home/debian/guestbook_project/static>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/guestbook_error.log
    CustomLog ${APACHE_LOG_DIR}/guestbook_access.log combined
</VirtualHost>
```

Activamos el sitio y recargamos Apache:

```bash
sudo a2ensite guestbook_socket.conf
sudo systemctl reload apache2
```

El flujo será:

```
Cliente → Apache2 (puerto 80) → socket Unix /run/uwsgi/guestbook.sock → Django
```

## Configuración del proxy inverso con Nginx

Nginx también puede actuar como proxy inverso en ambos casos: HTTP o socket.
Solo cambia la directiva utilizada (`proxy_pass` o `uwsgi_pass`).


### Modo 1: uWSGI en modo HTTP (puerto 8080)

Instalamos Nginx:

```bash
sudo apt install nginx
```

Creamos el archivo `/etc/nginx/sites-available/guestbook_http`:

```nginx
server {
    listen 80;
    server_name guestbook.local;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /home/debian/guestbook_project/static/;
    }

    error_log /var/log/nginx/guestbook_error.log;
    access_log /var/log/nginx/guestbook_access.log;
}
```

Activamos el sitio y recargamos Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/guestbook_http /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Flujo:

```
Cliente → Nginx (puerto 80) → uWSGI (127.0.0.1:8080) → Django
```

### Modo 2: uWSGI con socket Unix

Creamos el archivo `/etc/nginx/sites-available/guestbook_socket`:

```nginx
server {
    listen 80;
    server_name guestbook.local;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/guestbook.sock;
    }

    location /static/ {
        alias /home/debian/guestbook_project/static/;
    }

    error_log /var/log/nginx/guestbook_error.log;
    access_log /var/log/nginx/guestbook_access.log;
}
```

Activamos el sitio:

```bash
sudo ln -s /etc/nginx/sites-available/guestbook_socket /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Flujo:

```
Cliente → Nginx (puerto 80) → socket Unix /run/uwsgi/guestbook.sock → Django
```
