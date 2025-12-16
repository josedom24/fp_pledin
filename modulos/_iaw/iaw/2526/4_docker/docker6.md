---
title: "Ejemplo 5: Construcción de imágenes configurables con variables de entorno (Python)"
---

En este documento se explica cómo crear una **imagen Docker sencilla** de una aplicación Django (*Guestbook*) [https://github.com/josedom24/guestbook_django](https://github.com/josedom24/guestbook_django) que utiliza **MariaDB** como base de datos. En el fichero `requirements.txt` tenemos definido la librería `mysqlclient` para que la aplicación pueda acceder a la base de datos.
La aplicación se ejecuta con el **servidor de desarrollo de Django** (`python manage.py runserver`) y crea automáticamente un **superusuario** para acceder a la zona de administración.

Tenemos que tener en cuenta:

* La base de datos se ejecuta en un contenedor independiente
* La configuración se realiza mediante **variables de entorno**
* `mysqlclient` ya está incluido en `requirements.txt`
* El superusuario se crea **sin interacción**

## Configuración de la base de datos en Django

En `settings.py`:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}
```

* `os.getenv()` nos devuelve el valor de la variable de entorno que recibe como parámetro.


## Creación automática del superusuario

Django permite crear un superusuario **sin interacción** usando variables de entorno:

* `DJANGO_SUPERUSER_USERNAME`
* `DJANGO_SUPERUSER_EMAIL`
* `DJANGO_SUPERUSER_PASSWORD`

Estas variables se definirán en `docker-compose.yaml`.

## Script de arranque (`entrypoint.sh`)

El script realiza tres pasos:

1. Aplicar migraciones
2. Crear el superusuario (si no existe)
3. Arrancar el servidor Django

### `entrypoint.sh`

```bash
#!/bin/bash
set -e

echo "Starting Django Guestbook"

# Migraciones
python3 manage.py migrate --noinput

# Crear superusuario (no falla si ya existe)
python3 manage.py createsuperuser --noinput || true

# Servidor de desarrollo
exec python3 manage.py runserver 0.0.0.0:8000
```

* El uso de `|| true` evita errores si el superusuario ya está creado.


## Dockerfile de la aplicación

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN chmod +x entrypoint.sh \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["./entrypoint.sh"]
```

* Es necesario instalar los paquetes con apt, ya que porque `mysqlclient` no es una librería Python pura y necesita las librerías y cabeceras del sistema para poder compilarse correctamente.


## Construcción de la imagen

Desde el directorio del proyecto:

```bash
docker build -t guestbook_django .
```


## Despliegue con docker-compose

```yaml
version: '3.9'

services:
  web:
    image: guestbook_django
    restart: always
    environment:
      DB_HOST: db
      DB_NAME: guestbook
      DB_USER: guestbook
      DB_PASSWORD: secret

      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_EMAIL: admin@example.com
      DJANGO_SUPERUSER_PASSWORD: admin123
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: mariadb
    restart: always
    environment:
      MYSQL_DATABASE: guestbook
      MYSQL_USER: guestbook
      MYSQL_PASSWORD: secret
      MYSQL_ROOT_PASSWORD: rootpass
    volumes:
      - mariadb_data:/var/lib/mysql

volumes:
  mariadb_data:
```


