---
title: "Introducción al despliegue de aplicaciones Django con Apache2 y el módulo WSGI"
---

## Contexto: del entorno de desarrollo al entorno de producción

Hasta ahora hemos trabajado con Django usando el servidor de desarrollo que se ejecuta con el comando:

```bash
python manage.py runserver
```

Este servidor es muy útil para pruebas locales, pero **no está diseñado para entornos de producción**, ya que no ofrece:

* Rendimiento suficiente para múltiples clientes.
* Seguridad y aislamiento adecuados.
* Gestión eficiente de procesos.

En producción, normalmente usamos un **servidor web real** como **Apache2** o **Nginx**, que se encarga de:

* Atender las peticiones HTTP de los clientes.
* Servir directamente el contenido estático (imágenes, CSS, JavaScript).
* Delegar la ejecución de la aplicación Django a un **módulo intermedio**, en este caso **`mod_wsgi`**, que permite ejecutar aplicaciones Python dentro de Apache.

## El protocolo WSGI

**WSGI (Web Server Gateway Interface)** es una especificación que define cómo un **servidor web** (como Apache o Nginx) comunica peticiones HTTP a una **aplicación Python**.

En pocas palabras:

* Apache recibe una petición HTTP.
* A través del módulo **mod_wsgi**, la envía a la aplicación Django.
* Django procesa la petición (por ejemplo, consultando la base de datos y renderizando una plantilla HTML).
* El resultado se devuelve a Apache, que responde al cliente.

Este mecanismo permite integrar aplicaciones Python con servidores web de propósito general de forma estándar y eficiente.

## El archivo `wsgi.py` en Django

Cada proyecto Django incluye un archivo llamado **`wsgi.py`**, normalmente ubicado en el directorio del proyecto (por ejemplo, `guestbook_project/guestbook_project/wsgi.py`).

Este archivo define un objeto llamado **`application`**, que es el punto de entrada que el servidor Apache (a través de mod_wsgi) utilizará para comunicarse con Django.

Ejemplo simplificado del contenido del archivo:

```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guestbook_project.settings')
application = get_wsgi_application()
```
En resumen:
`wsgi.py` es el **enlace entre Apache y Django**, y su correcta configuración es imprescindible para que la aplicación funcione en producción.

## Módulos necesarios en Apache2

Para que Apache2 pueda ejecutar aplicaciones Python, debe tener instalado el módulo **mod_wsgi**.

En sistemas basados en Debian/Ubuntu, se instala con:

```bash
sudo apt install libapache2-mod-wsgi-py3
```

Una vez instalado, el módulo se activa automáticamente. Si no es así, puede activarse manualmente con:

```bash
sudo a2enmod wsgi
sudo systemctl reload apache2
```

## Configuración del VirtualHost

A continuación se muestra una configuración típica para desplegar un proyecto Django llamado `guestbook_project`, ubicado en `/home/debian/guestbook_project`, con un entorno virtual en `/home/debian/venv/django/`.

Archivo: `/etc/apache2/sites-available/guestbook.conf`

```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName guestbook.local
    DocumentRoot /home/debian/guestbook_project

    # === Configuración del proceso WSGI ===
    WSGIDaemonProcess django_guestbook python-path=/home/debian/guestbook_project:/home/debian/venv/django/lib/python3.X/site-packages
    WSGIProcessGroup django_guestbook
    WSGIScriptAlias / /home/debian/guestbook_project/guestbook_project/wsgi.py process-group=django_guestbook

    <Directory /home/debian/guestbook_project/guestbook_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    # === Archivos estáticos (CSS, imágenes, JS) ===
    Alias /static/ /home/debian/guestbook_project/static/
    <Directory /home/debian/guestbook_project/static>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/guestbook_error.log
    CustomLog ${APACHE_LOG_DIR}/guestbook_access.log combined
</VirtualHost>
```

### Explicación de los parámetros principales

| Parámetro                | Descripción                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `ServerName`             | Nombre de dominio o dirección del sitio.                                                                          |
| `DocumentRoot`           | Carpeta principal del proyecto.                                                                                   |
| `WSGIDaemonProcess`      | Define un proceso aislado para ejecutar la aplicación Django; incluye la ruta del proyecto y del entorno virtual. |
| `WSGIProcessGroup`       | Asocia el grupo de procesos definido anteriormente.                                                               |
| `WSGIScriptAlias`        | Indica a Apache dónde está el archivo `wsgi.py` que sirve de punto de entrada a Django.                           |
| `<Directory>`            | Concede permisos de acceso al directorio donde está `wsgi.py`.                                                    |
| `Alias /static/`         | Permite servir archivos estáticos desde un directorio determinado.                                                |
| `ErrorLog` / `CustomLog` | Rutas donde se guardan los registros de errores y accesos.                                                        |

## El problema del contenido estático

En Django, muchos recursos estáticos (CSS, imágenes, JavaScript) no están ubicados en la carpeta del proyecto, sino distribuidos dentro de las aplicaciones del framework.
Por ejemplo:

* Los estilos del **panel de administración** (`/admin/`) se encuentran en los paquetes internos de Django.
* Nuestros propios archivos estáticos pueden estar en `static/`.

En un entorno de desarrollo, Django los sirve automáticamente.
Pero **en producción, Apache no los conoce** si no los copiamos a un único lugar accesible.

## Solución: `collectstatic`

Django proporciona el comando **`collectstatic`**, que recopila todos los archivos estáticos (de las apps y del proyecto) en una única carpeta, normalmente `/static/`.

```bash
source /home/debian/venv/django/bin/activate
cd /home/debian/guestbook_project
python manage.py collectstatic
```

Este comando crea o actualiza la carpeta `/home/debian/guestbook_project/static/` con todos los archivos necesarios.

El bloque `Alias /static/` del VirtualHost permite que Apache los sirva directamente a los clientes, sin pasar por Django.

## La base de datos y las migraciones

Si desplegamos el proyecto en un servidor limpio, probablemente **no exista aún la base de datos SQLite**.
En ese caso, debemos inicializarla con las migraciones, igual que hicimos en desarrollo:

```bash
source /home/debian/venv/django/bin/activate
cd /home/debian/guestbook_project
python manage.py makemirations
python manage.py migrate
```

Esto creará el fichero `db.sqlite3` y todas las tablas necesarias según los modelos definidos.

## Permisos y usuario de Apache

El servidor Apache suele ejecutarse con el usuario **`www-data`** (en Debian/Ubuntu).
Por ello:

* Los archivos del proyecto deben ser legibles por ese usuario.
* La carpeta del entorno virtual debe tener permisos adecuados.
* Si se usa SQLite, el fichero `db.sqlite3` debe permitir escritura para `www-data`.

Por ejemplo:

```bash
sudo chown -R www-data:www-data /home/debian/guestbook_project
sudo chmod -R 755 /home/debian/guestbook_project
```

