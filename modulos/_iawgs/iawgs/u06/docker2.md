---
title: "Ejercicio: Configuración de contenedores docker con variables de entorno"
permalink: /iawgs/u06/docker2.html
---

En este ejercicio vamos a configurar una imagen docker al crear el contenedor por medio de variables de entorno.

## Configuración de apache2 en un contenedor docker

Imáginamos que creamos una imagen docker que ofrece un servidor web apache2 pero a la hora de crear el contenedor queremos modificar la configuración de este servicio. En nuestro ejemplo vamos a modificar el valor del parámetro `ServerName` de la configuración del virtualhost por defecto.

Para ello crea un entorno donde vamos a tener un fichero `index.html` y un fichero Dockerfile con el siguiente contenido:

    FROM debian
    MAINTAINER José Domingo Muñoz "josedom24@gmail.com"

    RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*

    ENV APACHE_SERVER_NAME www.example.com

    EXPOSE 80
    ADD ["index.html","/var/www/html/"]

    ADD script.sh /usr/local/bin/script.sh
    RUN chmod +x /usr/local/bin/script.sh

    CMD ["/usr/local/bin/script.sh"]

Algunas cosas importantes de esta configuración:

* `ENV APACHE_SERVER_NAME www.example.com`: Hemos creado una variable de entorno que va a existir en el contenedor que creemos a partir de esta imagen. Le damos un valor por defecto.
* `CMD ["/usr/local/bin/script.sh"]`: Como podemos apreciar el comando (puedes ver la diferencia entre `CMD` y `ENTRYPOINT` en el siguiente [artículo](https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/)) que se ejecuta al crear el contenedor será un script `/usr/local/bin/script.sh`. Este script se añade a la imagen (Puedes ver la diferencia entre `ADD` y `COPY` en la siguiente [entrada](https://stackoverflow.com/questions/24958140/what-is-the-difference-between-the-copy-and-add-commands-in-a-dockerfile)) y se le da permisos de ejecución.

Por lo tanto en el contexto también tenemos que crear el fichero `script.sh` que tendrá el siguiente contenido:

    #!/bin/bash
    sed -i "s/#ServerName www.example.com/ServerName ${APACHE_SERVER_NAME}/g" /etc/apache2/sites-available/000-default.conf
    apache2ctl -D FOREGROUND

Es decir, reemplaza de forma adecuada la configuración de apache2 con el valor de la variable de entorno y ejecuta apache2.

## Prueba de funcionamiento

Vamos a probar el funcionamiento teniendo en cuenta que por defecto el valor de la variable de entorno es `www.example.com`

Construimos la imagen:

    docker build -t josedom24/myapache2:v1 .

Creamos un contenedor:

    docker run -d --name prueba -p 8081:80 josedom24/myapache2:v1

Comprobamos que en el contenedor existe la variable de entorno:

    docker exec prueba env
    ...
    APACHE_SERVER_NAME=www.example.com
    ...

Y que efectivamente hemos modificado la configuración del servidor web:

    docker exec prueba cat /etc/apache2/sites-available/000-default.conf
    ...
    	ServerName www.example.com
	...

## Configurando nuestro contenedor con variables de entorno

A la hora de crear un contenedor con nuestra imagen, podemos dar cualquier valor a las variables que hayamos creado, de esta manera puedo crear un segundo contenedor de esta manera:

    docker run -d --name prueba2 -e APACHE_SERVER_NAME=www.prueba.com -p 8082:80 josedom24/myapache2:v1

Y ahora comprobamos la configuración que hemos cambiado:

    docker exec prueba2 cat /etc/apache2/sites-available/000-default.conf
    ...
    	ServerName www.prueba.com
	...

## Configuración de contenedores docker desde imágenes de Docker Hub

La mayoría de las imágenes que encontramos en Docker Hub se pueden configurar en el momento de crear el contenedor por medio de variables de entorno. 

{% capture notice-text %}
1. Accede a la documentación de la imagen de mariadb en Docker Hub y comprueba las variables de entorno que podemos cambiar para configurar el contenedor.
2. Crea un contenedor desde la imagen de mariadb, que tenga un usuario que se llame `usuario`, una contraseña que sea `asdasd` y una base de datos que sea `mibasededatos`.
3. Accede al puerto 3306 del contenedor y comprueba que efectivamente se ha creado de forma adecuada. Para ello ejecuta:

        mysql -u usuario -p -h 10.0.0.6

    Cambiando la ip por la tuya.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

