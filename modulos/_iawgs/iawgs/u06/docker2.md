---
title: "Ejercicio: Almacenamiento persistente en los contenedores"
permalink: /iawgs/u06/docker2.html
---

Como hemos estudiado la información que se guarda en un contenedor no es persistente. En el siguiente ejercicio vamos a ver un ejemplo de un contenedor con almacenamiento persistente.

## Contenedor mysql con almacenamiento persistente

Contenedor con mysql. guardamos la información de la base de datos en un volumen persistente:


    $ docker run --name some-mysql \ 
                 -v /opt/mysql:/var/lib/mysql \
                 -e MYSQL_ROOT_PASSWORD=asdasd \
                 -d mysql
  

Comprobamos que se ha guardado la BD en el host:

    /opt/mysql$ ls
    ibdata1  ib_logfile0  ib_logfile1  ibtmp1  #innodb_temp  mysql  mysql.ibd  undo_001  undo_002
 
Ahora podemos crear una base de datos:

    $ docker exec -it some-mysql bash
    root@75544a024f9b:/# mysql -u root -p -h localhost
    ...
    create database dbtest;
    Query OK, 1 row affected (0.07 sec)
  

Si simulamos que nuestro contenedor ha fallado: 

    $ docker container rm -f some-mysql 

Podemos crear otro contenedor y comprobar como sigue existiendo la BD:


    $ docker run --name some-mysql2 \
                -v /opt/mysql:/var/lib/mysql \
                -e MYSQL_ROOT_PASSWORD=asdasd \
                -d mysql
    
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
