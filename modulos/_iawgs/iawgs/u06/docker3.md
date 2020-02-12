---
title: "Ejercicio: Redes en docker. Enlazando contenedores docker"
permalink: /iawgs/u06/docker3.html
---

Docker nos permite distintos mecanismos para enlazar contenedores, es decir que exista un mecanismo de resolución de nombres que permita acceder a los distintos contenedores por medio de su nombre.

## Introducción a las redes en docker

Cuando instalamos docker tenemos las siguientes redes predefinidas:

    # docker network ls
    NETWORK ID          NAME                DRIVER              SCOPE
    ec77cfd20583        bridge              bridge              local
    69bb21378df5        host                host                local
    089cc966eaeb        none                null                local

* Por defecto los contenedores que creamos se conectan a la red de tipo bridge llamada `bridge` (por defecto el direccionamiento de esta red es `172.17.0.0/16`). Los contenedores conectados a esta red que quieren exponer algún puerto al exterior tienen que usar la opción `-p` para mapear puertos.
* Si conecto un contenedor a la red host, el contenedor estaría en la misma red que el host (por lo tanto toma direccionamiento del servidor DHCP de nuestra red). Además los puerto son accesibles directamente desde el host. Por ejemplo:

        # docker run -d --name mi_servidor --network host josedom24/aplicacionweb:v1
        
        # docker ps
        CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS               NAMES
        135c742af1ff        josedom24/aplicacionweb:v1   "/usr/sbin/apache2ct…"   3 seconds ago       Up 2 seconds                                  mi_servidor

    Prueba acceder directamente al puerto 80 del servidor para ver la página web.
* La red `none` no configurará ninguna IP para el contenedor y no tiene acceso a la red externa ni a otros contenedores. Tiene la dirección loopback y se puede usar para ejecutar trabajos por lotes.

Nosotros podemos crear nuevas redes (redes definidas por el usuario), por ejemplo para crear una red de tipo bridge:

    # docker network create mired

Y para ver las características de esta nueva red, podemos ejecutar:

    # docker network inspect mired

Para crear un contenedor en esta red, ejecutamos:

    # docker run -d --name mi_servidor --network mired -p 80:80 josedom24/aplicacionweb:v1

Dependiendo de la red que estemos usando (la red puente por defecto o una red definida por el usuario) el mecanismo de enlace entre contenedores será distinto.

## Enlazando contenedores conectados a la red bridge por defecto

Esta manera en enlazar contenedores no está recomendada y esta obsoleta. Además el uso de contenedores conectados a la red por defecto no está recomendado en entornos de producción. Para realizar este tipo de enlace vamos a usar el flag `--link`:

Veamos un ejemplo, primero creamos un contenedor de mariadb:

    # docker run -d --name servidor_mysql -e MYSQL_DATABASE=bd_wp -e MYSQL_USER=user_wp -e MYSQL_PASSWORD=asdasd -e MYSQL_ROOT_PASSWORD=asdasd mariadb

A continuación vamos a crear un nuevo contenedor, enlazado con el contenedor anterior:

    # docker run -d --name servidor --link servidor_mysql:mariadb josedom24/aplicacionweb:v1

Para realizar la asociación entre contenedores hemos utilizado el parámetro `--link`, donde se indica el nombre del contenedor enlazado y un alias por el que nos podemos referir a él.

En este tipo de enlace tenemos dos características:

* Se comparten las variables de entorno 

    Las variables de entorno del primer contenedor son accesibles desde el segundo contenedor:

        # docker exec servidor env

        ...
        MARIADB_PORT=tcp://172.17.0.2:3306
        MARIADB_PORT_3306_TCP=tcp://172.17.0.2:3306
        MARIADB_PORT_3306_TCP_ADDR=172.17.0.2
        MARIADB_PORT_3306_TCP_PORT=3306
        MARIADB_PORT_3306_TCP_PROTO=tcp
        MARIADB_NAME=/servidor/mariadb
        MARIADB_ENV_MYSQL_USER=user_wp
        MARIADB_ENV_MYSQL_PASSWORD=asdasd
        MARIADB_ENV_MYSQL_ROOT_PASSWORD=asdasd
        MARIADB_ENV_MYSQL_DATABASE=bd_wp
        MARIADB_ENV_GOSU_VERSION=1.10
        MARIADB_ENV_GPG_KEYS=177F4010FE56CA3336300305F1656F24C74CD1D8
        MARIADB_ENV_MARIADB_MAJOR=10.4
        MARIADB_ENV_MARIADB_VERSION=1:10.4.11+maria~bionic
        ...

* Los contenedores son conocido por resolución estática

    Otro mecanismo que se realiza para permitir la comunicación entre contenedores asociados es modificar el fichero `/etc/hosts` para que tengamos resolución estática entre ellos. Podemos comprobarlo:

        # docker exec servidor cat /etc/hosts
        ...
        172.17.0.2	mariadb c76089892798 servidor_mysql

## Enlazando contenedores conectados a una red definida por el usuario

En este caso vamos a definir una red de tipo bridge:

    # docker network create mired

Y creamos los contenedores conectados a dicha red:

    #  docker run -d --name servidor_mysql --network mired -e MYSQL_DATABASE=bd_wp -e MYSQL_USER=user_wp -e MYSQL_PASSWORD=asdasd -e MYSQL_ROOT_PASSWORD=asdasd mariadb

    # docker run -d --name servidor --network mired josedom24/aplicacionweb:v1

En este caso no se comparten las variables de entorno, y la resolución de nombres de los contenedores se hace mediante un servidor dns que se ha creado en el gateway de la red que hemos creado:

    # docker  exec -it servidor bash
    root@a86f6d758eba:/# apt update && apt install dnsutils -y
    ...
    root@a86f6d758eba:/# dig servidor_mysql
    ...
    ; ANSWER SECTION:
    servidor_mysql.		600	IN	A	172.20.0.2
    ...
    ;; SERVER: 127.0.0.11#53(127.0.0.11)

    root@a86f6d758eba:/# dig servidor_mysql.mired
    ...
    ; ANSWER SECTION:
    servidor_mysql.mired.		600	IN	A	172.20.0.2

    root@a86f6d758eba:/# dig servidor
    ...
    ; ANSWER SECTION:
    servidor.	    	600	IN	A	172.20.0.3

Como vemos desde un contenedor se pueden resolver tanto los nombres de los servidores, como el FHQN formado por el nombre del contenedor y como nombre de dominio el nombre de la red a la que están conectados.

## Instalación de wordpress en docker

Creamos una red de tipo bridge:

    # docker network create red_wp

Creamos un contenedor desde la imagen mariadb con el nombre `servidor_mysql`, conectada a la red creada:

    docker run -d --name servidor_mysql --network red_wp -e MYSQL_DATABASE=bd_wp -e MYSQL_USER=user_wp -e MYSQL_PASSWORD=asdasd -e MYSQL_ROOT_PASSWORD=asdasd mariadb

A continuación vamos a crear un nuevo contenedor, con el nombre `servidor_wp`, con el servidor web a partir de la imagen wordpress, conectada a la misma red y con las variables de entorno necesarias:

    docker run -d --name servidor_wp --network red_wp -e WORDPRESS_DB_HOST=servidor_mysql -e WORDPRESS_DB_USER=user_wp -e WORDPRESS_DB_PASSWORD=asdasd -e WORDPRESS_DB_NAME=bd_wp -p 80:80  wordpress
    
Accede a la ip del servidor docker y comprueba la instalación de wordpress.