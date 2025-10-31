---
title: "Introducción a Django"
---

## ¿Qué es Django?

**Django** es un *framework* de desarrollo web para el lenguaje **Python**.
Permite crear aplicaciones web completas de manera rápida, segura y estructurada, siguiendo el patrón de diseño **Modelo–Vista–Controlador (MVC)**, que en Django se denomina **Modelo–Vista–Template (MVT)**.

Algunas características destacadas:

* Incluye un **servidor de desarrollo** integrado.
* Proporciona un **sistema de plantillas** para generar páginas HTML dinámicas.
* Permite interactuar con bases de datos mediante un **ORM (Object Relational Mapper)**.
* Dispone de un **panel de administración web** listo para usar.
* Incluye herramientas de seguridad (autenticación, CSRF, inyección SQL, etc.).

## Entorno virtual y dependencias

Cada proyecto Django necesita un **entorno virtual** que aísle sus librerías del resto del sistema.
Esto evita conflictos entre versiones de dependencias y permite que cada aplicación tenga su propio conjunto de paquetes.

## Estructura básica de un proyecto Django

Supondremos que ya tenemos clonado desde GitHub el repositorio de nuestra aplicación (por ejemplo, el proyecto **Guestbook** que usaremos como ejemplo).

La estructura típica es la siguiente:

```
guestbook_project/
├── manage.py
├── guestbook_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── guestbook/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── inicio.html
├── static/
│   └── style.css
└── requirements.txt
```

### Archivos más importantes

#### `manage.py`

Es una herramienta de línea de comandos que centraliza las operaciones administrativas del proyecto:
crear usuarios, ejecutar el servidor, aplicar migraciones, etc.

Ejemplos de uso:

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
```

#### `settings.py`

Archivo principal de configuración del proyecto.
Define:

* la base de datos (`DATABASES`),
* la variable `ALLOWED_HOSTS` define qué nombres de dominio o direcciones IP tienen permiso para acceder a la aplicación Django,
* el idioma y zona horaria,
* las aplicaciones instaladas (`INSTALLED_APPS`),
* la configuración de plantillas y archivos estáticos.

#### `urls.py`

Define las **rutas** del proyecto.
En Django, las rutas **no corresponden a archivos reales** en un directorio público (como ocurre en servidores Apache tradicionales).
Son **rutas virtuales** que el framework interpreta para decidir qué función o vista debe ejecutarse.

Ejemplo:

```python
from django.urls import path
from guestbook import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('add/', views.add, name='add'),
]
```

#### `views.py`

Contiene las **funciones (o clases)** que se ejecutan cuando se accede a una ruta.
Cada vista recibe una petición (`request`) y devuelve una **respuesta HTTP**: normalmente una página HTML generada a partir de una plantilla, o bien una redirección o un mensaje.

Ejemplo:

```python
from django.shortcuts import render, redirect

def inicio(request):
    return render(request, "inicio.html")

def add(request):
    # Procesar formulario y redirigir
    return redirect("inicio")
```

#### `templates/`

Carpeta donde se guardan las **plantillas HTML** que se envían al navegador.
Pueden contener variables y estructuras de control usando el lenguaje de plantillas de Django:

```html
<h1>Entradas del Guestbook</h1>
{% for entrada in lista %}
  <p>{{ entrada }}</p>
{% endfor %}
```

#### `static/`

Directorio donde se ubican los **recursos estáticos** como hojas de estilo (`.css`), imágenes o archivos JavaScript.


## Rutas virtuales y vistas

En Django **no se accede directamente a archivos HTML**.
Cuando el usuario visita una URL, por ejemplo `/add/`, el servidor no busca un archivo físico `add.html`, sino que busca una **ruta virtual** definida en `urls.py`.

El sistema de enrutamiento de Django decide qué función (vista) debe ejecutarse.
Esa función genera la **respuesta HTTP**, normalmente renderizando una plantilla HTML o redirigiendo a otra vista.

> Esta separación entre rutas y archivos es una de las diferencias fundamentales entre un servidor web tradicional y un framework como Django.

## Introducción al ORM y la base de datos

Django incluye un **ORM (Object Relational Mapper)**, un sistema que permite trabajar con la base de datos usando objetos Python en lugar de sentencias SQL.

Cada **modelo** (definido en `models.py`) representa una tabla en la base de datos.

Ejemplo:

```python
from django.db import models

class Entry(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
```

Esto crea una tabla `guestbook_entry` con dos columnas: `content` y `created_at`.

### Base de datos SQLite

Por defecto, Django usa **SQLite**, una base de datos ligera que guarda la información en un único fichero (`db.sqlite3`).
Es perfecta para desarrollo y pruebas, y no requiere instalación adicional.

## Migraciones

Las **migraciones** son el mecanismo mediante el cual Django traduce los modelos Python a tablas reales en la base de datos.

### Comandos principales

* Crear migraciones (a partir de los modelos):

  ```bash
  python manage.py makemigrations
  ```

* Aplicar las migraciones a la base de datos:

  ```bash
  python manage.py migrate
  ```

* Ver migraciones pendientes:

  ```bash
  python manage.py showmigrations
  ```

Cada vez que modificamos un modelo, debemos generar una nueva migración y aplicarla.

> Si intentamos usar la base de datos sin haber hecho las migraciones, obtendremos errores como *“no such table…”*.

## Servidor de desarrollo

Para probar la aplicación, Django ofrece un **servidor de desarrollo** que permite ejecutar el proyecto localmente.

Se arranca con:

```bash
python manage.py runserver
```

y, por defecto, estará disponible en [http://localhost:8000](http://localhost:8000).

Este servidor detecta cambios automáticamente y se reinicia, por lo que resulta ideal para fase de desarrollo.
No debe usarse en producción.

## Panel de administración de Django

Una de las grandes ventajas del framework es el **panel de administración** que incluye por defecto.
Permite **gestionar el contenido de la base de datos desde una interfaz web**, sin escribir código HTML ni SQL.

### Acceso

La ruta `/admin/` está disponible automáticamente.
Primero, debemos crear un **superusuario** para acceder:

```bash
python manage.py createsuperuser
```

Tras introducir nombre de usuario, correo y contraseña, el nuevo usuario podrá iniciar sesión en [http://localhost:8000/admin/](http://localhost:8000/admin/).


