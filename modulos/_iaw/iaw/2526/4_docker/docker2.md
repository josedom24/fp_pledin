---
title: "Ejemplo 1: Construcción de imágenes con una página estática"
---

En este ejemplo vamos a crear una imagen con una página estática. Vamos a crear tres versiones de la imagen.

## Versión 1: Desde una imagen base

Tenemos un directorio, que en Docker se denomina contexto, donde tenemos el fichero `Dockerfile` y un directorio, llamado `public_html` con nuestra página web:

```bash
$ ls
Dockerfile  public_html
```

En este caso vamos a usar una imagen base de un sistema operativo sin ningún servicio. El fichero `Dockerfile` será el siguiente:

```Dockerfile
# syntax=docker/dockerfile:1
FROM debian:stable-slim
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/html/
COPY public_html .
EXPOSE 80
CMD apache2ctl -D FOREGROUND
```

Al usar una imagen base `debian:stable-slim` tenemos que instalar los paquetes necesarios para tener el servidor web, en este acaso apache2. A continuación añadiremos el contenido del directorio `public_html` al directorio `/var/www/html/` del contenedor y finalmente indicamos el comando que se deberá ejecutar al crear un contenedor a partir de esta imagen: iniciamos el servidor web en segundo plano.

Para crear la imagen ejecutamos:

```bash
$ docker build -t josedom24/ejemplo1:v1 .
```

Comprobamos que la imagen se ha creado:

```bash
$ docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
josedom24/ejemplo1     v1                  8c3275799063        1 minute ago      226MB
```

Y podemos crear un contenedor:

```bash
$ docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v1
```

Y acceder con el navegador a nuestra página:

![ejemplo1](img/ejemplo1.png)


## Versión 2: Desde una imagen con apache2

En este caso el fichero `Dockerfile` sería el siguiente:

```Dockerfile
# syntax=docker/dockerfile:1
FROM httpd:2.4
COPY public_html /usr/local/apache2/htdocs/
EXPOSE 80
```

En este caso no necesitamos instalar nada, ya que la imagen tiene instalado el servidor web. En este caso y siguiendo la documentación de la imagen el *DocumentRoot* es `/usr/local/apache2/htdocs/`. No es necesario indicar el `CMD` ya que por defecto el contenedor creado a partir de esta imagen ejecutará el mismo proceso que la imagen base, es decir, la ejecución del servidor web.

De forma similar, crearíamos una imagen y un contenedor:

```bash
$ docker build -t josedom24/ejemplo1:v2 .
$ docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v2
```

## Versión 3: Desde una imagen con nginx

En este caso el fichero `Dockerfile` sería:

```Dockerfile
# syntax=docker/dockerfile:1
FROM nginx:1.24
COPY public_html /usr/share/nginx/html
EXPOSE 80
```

De forma similar, crearíamos una imagen y un contenedor:

```bash
$ docker build -t josedom24/ejemplo1:v3 .
$ docker run -d -p 80:80 --name ejemplo1 josedom24/ejemplo1:v3
```

{% capture notice-text %}
## Ejercicio

1. Crea una página web estática (por ejemplo busca una plantilla HTML5). O simplemente crea un `index.html`.
2. Crea un fichero `Dockerfile` que permita crear una imagen con un servidor web sirviendo la página. Puedes usar una imagen base debian o ubuntu, o una imagen que tenga ya un servicio web.
3. Ejecuta el comando docker que crea la nueva imagen. La imagen se debe llamar `<tu_usuario_docker_hub>/mi_servidor_web:v1`.
4. Conéctate a Docker Hub y sube la imagen que acabas de crear.
5. Descarga la imagen en otro ordenador donde tengas docker instalado, y crea un contenedor a partir de ella. (Si no tienes otro ordenador con docker instalado, borra la imagen en tu ordenador y bájala de Docker Hub).
6. Vamos a hacer una modificación de la página web: haz una modificación al fichero `index.html`.
7. Vuelve a crear una nueva imagen, en esta caso pon ta etiqueta `v2`. Súbela a Docker Hub.
8. Por último, baja la nueva imagen en el ordenador donde está corriendo el contenedor. Para hacer la implantación de la nueva versión debes borrar el contenedor y crear uno nuevo desde la nueva versión de la imagen.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>