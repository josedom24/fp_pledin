---
title: "Ejemplo 3: Construcción de imágenes con una una aplicación Python"
---

En este ejemplo vamos a construir una imagen Docker para servir una aplicación escrita en **Python utilizando el framework Django**.
La aplicación será servida en el **puerto 8000/tcp**, que es el puerto por defecto del servidor de desarrollo de Django.

Puedes encontrar el código de la aplicación en el siguiente repositorio: [https://github.com/josedom24/guestbook_django](https://github.com/josedom24/guestbook_django)

### Estructura del contexto de construcción

En el contexto de construcción tendremos:

* Un fichero `Dockerfile`
* Un directorio `app` que contendrá el código de la aplicación Django

## Versión 1: Imagen basada en un sistema operativo mínimo

En este primer caso utilizaremos una imagen base de **Debian**, sin Python instalado previamente. Seremos nosotros los que instalemos los paquetes necesarios.

El fichero `Dockerfile` será el siguiente:

```Dockerfile
# syntax=docker/dockerfile:1
FROM debian:13

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/share/app

COPY app .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
```

### Consideraciones

* Partimos de una imagen base de **Debian 13**, que no incluye Python.
* Instalamos `python3` y `pip`, que utilizaremos para gestionar las dependencias.
* Copiamos el código de la aplicación Django al directorio `/usr/share/app`.
* Con `WORKDIR` establecemos el directorio de trabajo para las instrucciones posteriores.
* Instalamos las dependencias Python listadas en el fichero `requirements.txt`.
* Exponemos el puerto **8000/tcp**, que es el puerto en el que Django sirve la aplicación.
* El proceso por defecto que se ejecutará al iniciar el contenedor es:

  ```bash
  python3 manage.py runserver 0.0.0.0:8000
  ```

  Es importante indicar `0.0.0.0` para que el servidor sea accesible desde fuera del contenedor.



### Construcción de la imagen

Para crear la imagen ejecutamos:

```bash
$ docker build -t josedom24/guestbook_django:v1 .
```

Comprobamos que la imagen se ha creado correctamente:

```bash
$ docker images
REPOSITORY                    TAG      IMAGE ID       CREATED          SIZE
josedom24/guestbook_django    v1       a1b2c3d4e5f6   1 minute ago      240MB
```



### Creación y ejecución del contenedor

Creamos un contenedor a partir de la imagen, publicando el puerto 8000 del contenedor en el puerto 80 del sistema anfitrión:

```bash
$ docker run -d -p 80:8000 --name guestbook_django josedom24/guestbook_django:v1
```

Si accedemos desde el navegador a `http://localhost/` veremos la aplicación **Guestbook** desarrollada con Django funcionando correctamente.


## Versión 2: Usando una imagen base con Python instalado

En este segundo caso utilizaremos una imagen oficial de Python que ya incluye el intérprete y `pip`. Esto simplifica el `Dockerfile` y reduce la cantidad de pasos necesarios.

El fichero `Dockerfile` sería el siguiente:

```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.14.2-trixie

WORKDIR /usr/share/app

COPY app .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
```

### Ventajas de esta aproximación

* El `Dockerfile` es más sencillo y legible.
* No es necesario instalar Python ni pip manualmente.
* Se reduce la posibilidad de errores relacionados con versiones del intérprete.

El proceso de construcción y ejecución del contenedor es exactamente el mismo que en la versión anterior.
{% capture notice-text %}
## Ejercicio

1. Realiza las dos versiones de la imagen. 

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>