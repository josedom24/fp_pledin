---
title: "Ejercicio 3: Almacenamiento y redes en Docker"
---

## Almacenamiento

Vamos a trabajar con volúmenes docker:
1. Crea un volumen docker que se llame `miweb`.
2. Crea un contenedor desde la imagen `php:7.4-apache` donde montes en el directorio `/var/www/html` (que sabemos que es el *DocuemntRoot* del servidor que nos ofrece esa imagen) el volumen docker que has creado.
3. Utiliza el comando `docker cp` para copiar un fichero `index.html` en el directorio `/var/www/html`.
4. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`.
5. Borra el contenedor
6. Crea un nuevo contenedor y monta el mismo volumen como en el ejercicio anterior.
7. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`. ¿Seguía existiendo ese fichero?

Vamos a trabajar con bind mount:
1. Crea un directorio en tu host y dentro crea un fichero `index.html`.
2. Crea un contenedor desde la imagen `php:7.4-apache` donde montes en el directorio `/var/www/html` el directorio que has creado por medio de `bind mount`.
3. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`.
4. Modifica el contenido del fichero `index.html` en tu host y comprueba que al refrescar la página ofrecida por el contenedor, el contenido ha cambiado.
5. Borra el contenedor
6. Crea un nuevo contenedor y monta el mismo directorio como en el ejercicio anterior.
7. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`. ¿Se sigue viendo el mismo contenido?

## Redes

Despliegue de Nextcloud + mariadb/postgreSQL

Vamos a desplegar la aplicación nextcloud con una base de datos (puedes elegir mariadb o PostgreSQL) (**NOTA: Para que no te de errores utiliza la imagen `mariadb:10.5`**). Te puede servir el ejercicio que hemos realizado para desplegar [Wordpress](wordpress.html). Para ello sigue los siguientes pasos:

1. Crea una red de tipo bridge.
2. Crea el contenedor de la base de datos conectado a la red que has creado. La base de datos se debe configurar para crear una base de dato y un usuario. Además el contenedor debe utilizar almacenamiento (volúmenes o bind mount) para guardar la información. Puedes seguir la documentación de [mariadb](https://hub.docker.com/_/mariadb) o la de [PostgreSQL](https://hub.docker.com/_/postgres).
3. A continuación, siguiendo la documentación de la imagen [nextcloud](https://hub.docker.com/_/nextcloud), crea un contenedor conectado a la misma red, e indica las variables adecuadas para que se configure de forma adecuada y realice la conexión a la base de datos. El contenedor también debe ser persistente usando almacenamiento.
4. Accede a la aplicación usando un navegador web.
