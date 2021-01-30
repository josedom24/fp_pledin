---
title: "Almacenamiento en docker"
permalink: /iawgs/u06/curso/almacenamiento.html
---

## Los contenedores son efímeros

**Los contenedores son efímeros**, es decir, los ficheros, datos y configuraciones que creemos en los contenedores sobreviven a las paradas de los mismos pero, sin embargo, son destruidos si el contenedor es destruido. 

Veamos un ejemplo:

    $ docker run -d --name my-apache-app -p 8080:80 httpd:2.4
    ac50cc24ef71ae0263be7794278600d5cc4f085b88cebbf97b7b268212f2a82f
    
    $ docker exec my-apache-app bash -c 'echo "<h1>Hola</h1>" > htdocs/index.html'
    
    $ curl http://localhost:8080
    <h1>Hola</h1>
    
    $ docker rm -f my-apache-app
    my-apache-app
    
    $ docker run -d --name my-apache-app -p 8080:80 httpd:2.4
    bb94716205c780ec4a3a2695722fb35ac616ae4cea573308d9446208afb164dc
    
    $ curl http://localhost:8080
    <html><body><h1>It works!</h1></body></html>

Vemos como al eliminar el contenedor, la información que habíamos guardado en el fichero `index.html` se pierde, y al crear un nuevo contenedor ese fichero tendrá el contenido original.

> NOTA: En la instrucción `docker exec` hemos ejecutado el comando con `bash -c` qie nos permite ejecutar uno o mas comandos en el contenedor de forma más compleja (por ejemplo, indicando ficheros dentro del contenedor).

## Los datos en los contenedores

![docker](img/types-of-mounts.png)

Ante la situación anteriormente descrita Docker nos proporciona varias soluciones para persistir los datos de los contenedores. En este curso nos vamos a centrar en las dos que considero que son más importantes:

* Los **volumenes docker**.
* Los **bind mount**
* Loa **tmpfs mounts**: Almacenan en memoria la información. (No lo vamos a ver ene este curso)

## Volúmenes docker y bind mount

* **Volúmenes docker**: Si elegimos conseguir la persistencia usando volúmenes estamos haciendo que los datos de los contenedores que nosotros decidamos se almacenen en una parte del sistema de ficheros que es gestionada por docker y a la que, debido a sus permisos, sólo docker tendrá acceso. En linux se guardan en `/var/lib/docker/volumes`. Este tipo de volúmenes se suele usar en los siguiente casos:

    * Para compartir datos entre contenedores. Simplemente tendrán que usar el mismo volumen.
    * Para copias de seguridad ya sea para que sean usadas posteriormente por otros contenedores o para mover esos volúmenes a otros hosts.
    * Cuando quiero almacenar los datos de mi contenedor no localmente si no en un proveedor cloud.

* **Bind mounts**: Si elegimos conseguir la persistencia de los datos de los contenedores usando bind mount lo que estamos haciendo es "mapear" (montar) una parte de mi sistema de ficheros, de la que yo normalmente tengo el control, con una parte del sistema de ficheros del contenedor. De esta manera conseguimos:
    * Compartir ficheros entre el host y los containers.
    * Que otras aplicaciones que no sean docker tengan acceso a esos ficheros, ya sean código, ficheros etc...

## Gestionando volúmenes

Algunos comando útiles para trabajar con volúmenes docker:

* **docker volumen create**: Crea un volumen con el nombre indicado.
* **docker volume rm**: Elimina el volumen indicado.
* **docker volumen prune**: Para eliminar los volúmenes que no están siendo usados por ningún contenedor.
* **docker volume ls**: Nos proporciona una lista de los volúmenes creados y algo de información adicional.
* **docker volume inspect**: Nos dará una información mucho más detallada de el volumen que hayamos elegido.

## Asociando almacenamiento a los contenedores

Veamos como puedo usar los volúmenes y los bind mounts en los contenedores. Para cualquiera de los dos casos lo haremos mediante el uso de dos flags de la orden `docker run`:

* El flag `--volume` o `-v`, lo utilizaremos para establecer bind mounts.
* El flag `--mount`, nos servirá para establecer bind mounts y para usar volúmenes previamente definidos.

Es importante que tengamos en cuenta dos cosas importantes a la hora de realizar estas operaciones:

* Al usar tanto volúmenes como bind mount, el contenido de lo que tenemos sobreescribirá la carpeta destino en el sistema de ficheros del contenedor en caso de que exista.
* Si nuestra carpeta origen no existe y hacemos un bind mount esa carpeta se creará pero lo que tendremos en el contenedor es una carpeta vacía. 
* Si usamos imágenes de DockerHub, debemos leer la información que cada imagen nos proporciona en su página ya que esa información suele indicar cómo persistir los datos de esa imagen, ya sea con volúmenes o bind mounts, y cuáles son las carpetas importantes en caso de ser imágenes que contengan ciertos servicios (web, base de datos etc...)

### Ejemplo usando volúmenes docker

    $ docker volume create miweb
    miweb

    $ docker run -d --name my-apache-app --mount type=volume,src=miweb,dst=/usr/local/apache2/htdocs -p 8080:80 httpd:2.4
    b51f89eb21701362279489c5b52a06b1a44c10194c00291de895b404ab347b80

    $ docker exec my-apache-app bash -c 'echo "<h1>Hola</h1>" > htdocs/index.html'

    $ curl http://localhost:8080
    <h1>Hola</h1>

    $ docker rm -f my-apache-app 
    my-apache-app

    $ docker run -d --name my-apache-app --mount type=volume,src=miweb,dst=/usr/local/apache2/htdocs -p 8080:80 httpd:2.4
    baa3511ca2227e30d90fa2b4b225e209889be4badff583ce58ac1feaa73d5d77

    $ curl http://localhost:8080
    <h1>Hola</h1>

Una aclaración, si hubiéramos ejecutado:

    $ docker run -d --name my-apache-app --mount type=volume,dst=/usr/local/apache2/htdocs -p 8080:80 httpd:2.4

Al no indicar el volumen, se creará un nuevo volumen.

### Ejemplo usando bind mount

En este caso vamos a crear un directorio en el sistema de archivo del host, donde vamos a crear un fichero `index.html`:

    $ mkdir web
    $ cd web
    /web$ echo "<h1>Hola</h1>" > index.html

    $ docker run -d --name my-apache-app -v /home/usuario/web:/usr/local/apache2/htdocs -p 8080:80 httpd:2.4
    8de025f6ff4d4b8a5a57d10a9cbb283b103209f358c43148a4716a33a404e208

    $ curl http://localhost:8080
    <h1>Hola</h1>

    $ docker rm -f my-apache-app 
    my-apache-app

    $ docker run -d --name my-apache-app --mount type=bind,src=/home/usuario/web,dst=/usr/local/apache2/htdocs -p 8080:80 httpd:2.4
    1751b04b0548217d7faa628fd69c10e84c695b0e5cc33b482df2c04a6af83292

    $ curl http://localhost:8080
    <h1>Hola</h1>

Además podemos comprobar que podemos modificar el contenido del fichero aunque este montado en el contenedor:

    $ echo "<h1>Adios</h1>" > web/index.html 
    $ curl http://localhost:8080
    <h1>Adios</h1>

## Ejercicio: Contenedor mariadb con almacenamiento persistente

Si estudiamos la documentación de la [imagen mariadb]() en Docker Hub, nos indica que podemos crear un contenedor con información persistente de maridb, de la siguiente forma:

    $ docker run --name some-mariadb -v /home/usuario/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb

Es decir se va a crear un directorio `/home/usuario/datadir` en el host, donde se va a guardar la información de la base de datos. Si tenemos que crear de nuevo el contenedor indicaremos ese directorio como bind mount y volveremos a tener accesible la información.

    $ cd datadir/
    ~/datadir$ ls
    aria_log.00000001  aria_log_control  ib_buffer_pool  ib_logfile0  ibdata1  ibtmp1  multi-master.info  mysql  performance_schema

    $ docker exec -it some-mariadb bash -c 'mysql -uroot -p$MYSQL_ROOT_PASSWORD'
    ...
    MariaDB [(none)]> create database prueba;
    MariaDB [(none)]> quit


    $ docker rm -f some-mariadb 
    some-mariadb

    $ docker run --name some-mariadb -v /home/vagrant/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb
    f36589090dd33b116da87e599850b1f25c9ae40e4b28c036c23e602d7bde4cc5

    $ docker exec -it some-mariadb bash -c 'mysql -uroot -p$MYSQL_ROOT_PASSWORD'
    ...
    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | prueba             |
    +--------------------+
    4 rows in set (0.003 sec)


Para terminar: ¿Qué debemos guardar de forma persistente en un contenedor?

* Los datos de la aplicación
* Los logs del servicio
* La configuración del servicio: En este caso podemos añadirla a la imagen, pero será necesaria la creación de una nueva imagen si cambiamos la configuración. Si la guardamos en un volumen hay que tener en cuanta que ese fichero lo tenemos que tener en el entorno de producción (puede ser bueno, porque las configuraciones de los distintos entornos puede variar).

