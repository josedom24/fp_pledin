---
title: "Ejercicio: Almacenamiento persistente en los contenedores"
permalink: /iawgs/u06/docker4.html
---

Como hemos estudiado la información que se guarda en un contenedor no es persistente. En el siguiente ejercicio vamos a ver un ejemplo de un contenedor con almacenamiento persistente.

## Contenedor mariadb con almacenamiento persistente

Contenedor con mariadb. Guardamos la información de la base de datos en un volumen persistente:

    $ docker run --name some-mysql -v /opt/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=asdasd -d mariadb

Comprobamos que se ha guardado la BD en el host:

    /opt/mysql$ ls
    ibdata1  ib_logfile0  ib_logfile1  ibtmp1  #innodb_temp  mysql  mysql.ibd  undo_001  undo_002
 
Ahora podemos crear una base de datos:

    $ docker exec -it some-mysql bash
    root@75544a024f9b:/# mysql -u root -p -h localhost
    ...
    create database dbtest;
    Query OK, 1 row affected (0.07 sec)

{% capture notice-text %}
Podemos conectarnos de una forma más "elegante" al servidor de base de datos con un contenedor temporal (opción `-.rm`):

    docker run -it --rm --link some-mysql:mysql mariadb mysql -hmysql -uroot -p

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

Si simulamos que nuestro contenedor ha fallado: 

    $ docker rm -f some-mysql 

Podemos crear otro contenedor y comprobar como sigue existiendo la BD:


    $ docker run --name some-mysql2 -v /opt/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=asdasd -d mariadb

    $ docker exec -it some-mysql2 bash
    root@878f77d80fcf:/# mysql -u root -p -h localhost
    ...
    show databases;
    ...
    | dbtest             |
    ...
  
{% capture notice-text %}
### ¿Qué debemos guardar en un volumen persistente?

* Los datos de la aplicación
* Los logs del servicio
* La configuración del servicio: En este caso podemos añadirla a la imagen, pero será necesaria la creación de una nueva imagen si cambiamos la configuración. Si la guardamos en un volumen hay que tener en cuanta que ese fichero lo tenemos que tener en el entorno de producción (puede ser bueno, porque las configuraciones de los distintos entornos puede variar).
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Instalación de wordpress de forma persistente

Al instalar el wordpress en el ejercicio anterior, si eliminamos el contenedor todos los datos del wordpress se perdían (directorio `wp-content`). Por lo tanto vamos a crear el contenedor de wordpress con un volumen asociado:

    docker run -d --name servidor_mysql -v /opt/mysql_wp:/var/lib/mysql -e MYSQL_DATABASE=bd_wp -e MYSQL_USER=user_wp -e MYSQL_PASSWORD=asdasd -e MYSQL_ROOT_PASSWORD=asdasd mariadb

    docker run --name servidor_wp -v /opt/wordpress:/var/www/html/wp-content -p 80:80 --link servidor_mysql:mysql -d wordpress

## Creación de imágenes con volúmenes desde Dockerfile

Cuando creamos una imagen desde Dockerfile podemos indicar la creación de volumenes: [Gestionando el almacenamiento docker con Dockerfile](https://www.josedomingo.org/pledin/2016/11/gestionando-el-almacenamiento-docker-con-dockerfile/).