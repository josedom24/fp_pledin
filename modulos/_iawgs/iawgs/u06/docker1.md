---
title: "Ejercicio: Despliegue de páginas estáticas con docker"
permalink: /iawgs/u06/docker1.html
---

En este primer ejercicio vamos a desarrollar una página estática y la vamos a desplegar en un contenedor. Para ello seguimos los siguientes pasos:

## Desarrollo de nuestra página web estática

Lo primero que debemos hacer es desarrollar nuestra página web estática, podemos coger una que ya tengamos hecha, o simplemente:

    $ cd public_html
    echo "<h1>Prueba</h1>" > index.html

**Nota: El directorio `public_html` estará dentro del contexto para crear la imagen posteriormente.**

## Creación de la imagen con Dockerfile

Utilizando un fichero `Dockerfile` definimos como vamos a crear nuestra imagen:

* Qué imagen base vamos a utilizar.
* Qué paquetes vamos a instalar
* Donde copiamos nuestro código fuente (página web)
* Indicamos el servicio que va a ejecutar el contenedor (servidor apache)

Por lo tanto, lo primero que tenemos que responder sería que imagen base vamos a escoger, en este caso tenemos dos opciones:

1. Elegir una imagen base con un sistema operativo base, por lo tanto nosotros somos responsables en el fichero `Dockerfile` de instalar y configurar el servidor web.
2. Elegir una imagen que ya tenga instalado un servidor web (por ejemplo [Apache2](https://hub.docker.com/_/httpd)), en este caso tenemos que leer la documentación del contenedor en Docker Hub para saber como utilizarlo (por ejemplo, para saber donde tengo que copiar mi página estática).

Si elegimos la primera opción primera: utilizar una imagen base, el fichero `Dockerfile` sería el siguiente:

    FROM debian
    RUN apt-get update -y && apt-get install -y \
        apache2 \
        && apt-get clean && rm -rf /var/lib/apt/lists/*
    COPY ./public_html /var/www/html/
    ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

Si elegimos la segunda opción: utilizar una imagen base con apache2, el fichero `Dockerfile` quedaría:

    FROM httpd:2.4
    COPY ./public_html /usr/local/apache2/htdocs/

Creamos nuestra imagen, desde el directorio donde tenemos el `Dockerfile`, ejecutamos:

    $ docker build -t josedom24/aplicacionweb:v1 .


{% capture notice-text %}
1. Crea dos imágenes a partir de los `Dockerfile` anteriores (utiliza nombres distintos para diferenciarlo)
. Con las etiquetas podemos nombrar las distintas versiones de la aplicación, utiliza `v1`.
2. Modifica el `Dockerfile` para guardar la página estática en un directorio llamado web. Además queremos cambiar la configuración de apache2 para que al acceder se haga una redirección al directorio web. ¿Cómo cambiarías la configuración de apache2 en cada una de las opciones?
3. Crea un fichero `Dockerfile` y genera una imagen para que nuestra página web sea servida por el servidor web nginx (utiliza la imagen base oficial).
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Creación de un contenedor en el entorno de desarrollo

Vamos a crear un contenedor en nuestro entorno de desarrollo para ver si está funcionando de manera correcta.

{% capture notice-text %}
1. Prueba si funcionan las imágenes generadas en el apartado anterior creando un contenedor en tu entorno de desarrollo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Distribución de nuestra imagen (Docker Hub)

Para distribuir nuestras imágenes necesitamos un registro de imágenes docker. En este ejercicio vamos a usar un registro público llamado  [Docker Hub])(https://hub.docker.com/). Nos damos de alta en Docker Hub, y para subir nuestra imagen ejecutamos los siguientes comandos:

    $ docker login
    ...
    $ docker push josedom24/aplicacionweb:v1
    The push refers to repository [docker.io/josedom24/aplicacionweb]
    ac126159496f: Pushed 
    cc15ec5f0c43: Pushed 
    ...

Comprobamos que está subida al repositorio:

    $ docker search josedom24/aplicacionweb
    NAME                     DESCRIPTION...
    josedom24/aplicacionweb:v1   
    ...

### Generación automática de imágenes en Docker Hub

Podemos generar nuestras imágenes automáticamente desde Docker Hub, 

* Crea un repositorio en GitHub, y sube el contexto (`Dockerfile` y ficheros necesarios) para construir una imagen.
* Crea desde Docker Hub un repositorio conectado a tu repositorio de GitHub.
* Comprueba que se ha creado la nueva imagen.
* Descarga la nueva imagen en tu servidor Docker y crea un nuevo contenedor.
* Cada vez que hagas un commit en tu repositorio GitHub se creará de forma automática una nueva imagen.

Sigue este [enlace](https://docs.docker.com/docker-hub/builds/) para más información.

## Despliegue de la aplicación (página estática) en nuestro entorno de producción

En el el entorno de producción, bajamos la imagen de Docker Hub y creamos el contenedor:

    $ docker pull josedom24/aplicacionweb:v1
    v1: Pulling from josedom24/aplicacionweb
    9a029d5ca5bb: Pull complete 
    ...
    $ docker run --name aplweb_prod -d -p 80:80 josedom24/aplicacionweb:v1

## Modificación de la aplicación

* Al modificar el código de la aplicación tenemos que generar una nueva imagen (modificamos la etiqueta indicando que tenemos una nueva versión).
* Podemos probarla en el entorno de desarrollo, eliminando el contenedor anterior.
* Subimos la nueva versión de la aplicación. En el entorno de producción: bajamos la nueva versión, eliminamos el contenedor de la versión antigua y creamos un nuevo contenedor con la nueva imagen.

{% capture notice-text %}
1. Modifica la página web y realiza el proceso para desplegar en el entorno de producción la nueva versión de la página.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
