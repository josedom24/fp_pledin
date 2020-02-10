---
title: "Ejercicio: Enlazando contenedores docker"
permalink: /iawgs/u06/docker3.html
---

Docker nos permite un mecanismo de enlace entre contenedores, posibilitando enviar información de forma segura entre ellos y pudiendo compartir información entre ellos, por ejemplo las variables de entorno. Para establecer la asociación entre contenedores es necesario usar el nombre con el que creamos el contenedor, el nombre sirve como punto de referencia para enlazarlo con otros contenedores.

## Instalación de wordpress en docker

Lo primero que vamos a hacer es crear un contenedor desde la imagen mysql con el nombre servidor_mysql, siguiendo las instrucción del repositorio de docker hub:

    docker run -d --name servidor_mysql -e MYSQL_DATABASE=bd_wp -e MYSQL_USER=user_wp -e MYSQL_PASSWORD=asdasd -e MYSQL_ROOT_PASSWORD=asdasd mariadb

A continuación vamos a crear un nuevo contenedor, con el nombre servidor_wp, con el servidor web a partir de la imagen wordpress, enlazado con el contenedor anterior.

    docker run --name servidor_wp -p 80:80 --link servidor_mysql:mysql -d wordpress

Para realizar la asociación entre contenedores hemos utilizado el parámetro `--link`, donde se indica el nombre del contenedor enlazado y un alias por el que nos podemos referir a él.

En esta situación el contenedor `servidor_web` puede acceder a información del contenedor `servidor_mysql`, para hacer esto docker construye un túnel seguro entre los contenedores y no es necesario exponer ningún puerto entre ellos (cuando hemos creado el contenedor `servidor_mysql` no hemos utilizado el parámetro -p), por lo tanto al `servidor_mysql` no se expone al exterior. Para facilitar la comunicación entre contenedores, docker utiliza las variables de entrono y modifica el fichero `/etc/hosts`.

### Variables de entorno en contenedores asociadosPermalink

Veamos las variables de entorno que se han creado en el contenedor `servidor_mysql`:

    docker exec servidor_mysql env
    ...
    MYSQL_PASSWORD=asdasd
    MYSQL_ROOT_PASSWORD=asdasd
    MYSQL_DATABASE=bd_wp
    MYSQL_USER=user_wp
    ...

Por cada asociación de contenedores, docker crea una serie de variables de entorno, en este caso, en el contenedor `servidor_wp`, se crearán las siguientes variables, donde se utiliza el nombre del alias indicada en el parámetro `--link`:

* `MYSQL_NAME`: Con el nombre del contenedor `servidor_mysql`.
* `MYSQL_PORT_3306_TCP_ADDR`: Por cada puerto que expone la imagen desde la que hemos creado el contenedor se crea una variable de entorno de este tipo. El contenido de esta variable es la dirección IP del contenedor.
* `MYSQL_PORT_3306_TCP_PORT`: De la misma manera se crea una por cada puerto expuesto por la imagen, en este caso guardamos el puerto expuesto.
* `MYSQL_PORT_3306_TCP_PROTOCOL`: Una vez más se crean tantas variables como puertos hayamos expuesto. En esta variable se guarda el protocolo del puerto.
* `MYSQL_PORT`: En esta variable se guarda la url del contenedor, con la ip del mismo y el puerto más bajo expuesto. Por ejemplo `MYSQL_PORT=tcp://172.17.0.4:3306`.

Finalmente por cada variable de entorno definido en el contenedor enlazado, en este caso `servidor_mysql`, se crea una en el contenedor principal, en este caso `servidor_web`. Si en el contenedor_mysql hay una variable `MYSQL_ROOT_PASSWORD`, en el servidor web se creará la variable `MYSQL_ENV_MYSQL_ROOT_PASSWORD`.

    docker exec servidor_wp env
    ...
    MYSQL_PORT=tcp://172.17.0.4:3306
    MYSQL_PORT_3306_TCP=tcp://172.17.0.4:3306
    MYSQL_PORT_3306_TCP_ADDR=172.17.0.4
    MYSQL_PORT_3306_TCP_PORT=3306
    MYSQL_PORT_3306_TCP_PROTO=tcp
    MYSQL_NAME=/servidor_wp/mysql
    MYSQL_ENV_MYSQL_PASSWORD=asdasd
    MYSQL_ENV_MYSQL_ROOT_PASSWORD=asdasd
    MYSQL_ENV_MYSQL_DATABASE=bd_wp
    MYSQL_ENV_MYSQL_USER=user_wp
    MYSQL_ENV_GOSU_VERSION=1.10
    MYSQL_ENV_GPG_KEYS=177F4010FE56CA3336300305F1656F24C74CD1D8
    MYSQL_ENV_MARIADB_MAJOR=10.4
    MYSQL_ENV_MARIADB_VERSION=1:10.4.12+maria~bionic
    ...

Por tanto llegamos a la conclusión que toda la información que necesitamos para instalar wordpress (dirección y puerto del servidor de base de datos, contraseña del usuario de la base de datos,...) lo tenemos a nuestra disposición en variables de entorno. El script bash que ejecutamos por defecto al crear el contenedor desde la imagen wordpress utilizará toda esta información, que tiene en variables de entorno, para crear el fichero de configuración de wordpress: `wp-config.php`. Además podremos crear nuevas variables a la hora de crear el contenedor como nos informa en la documentación del <a href="https://hub.docker.com/_/wordpress/">repositorio</a> de docker hub:

* `-e WORDPRESS_DB_HOST=...` (defaults to the IP and port of the linked `mysql` container)
* `-e WORDPRESS_DB_USER=...` (defaults to "root")
* `-e WORDPRESS_DB_PASSWORD=...` (defaults to the value of the `MYSQL_ROOT_PASSWORD` environment variable from the linked `mysql` container)
* `-e WORDPRESS_DB_NAME=...` (defaults to "wordpress")
* `-e WORDPRESS_TABLE_PREFIX=...` (defaults to "", only set this when you need to override the default table prefix in wp-config.php)
* `-e WORDPRESS_AUTH_KEY=...`, `-e WORDPRESS_SECURE_AUTH_KEY=...`, `-e WORDPRESS_LOGGED_IN_KEY=...`, `-e WORDPRESS_NONCE_KEY=...`, `-e WORDPRESS_AUTH_SALT=...`, `-e WORDPRESS_SECURE_AUTH_SALT=...`, `-e WORDPRESS_LOGGED_IN_SALT=...`, `-e WORDPRESS_NONCE_SALT=...` (default to unique random SHA1s)

Y podemos comprobar el contenido del fichero `wp-config.php`:

    docker exec servidor_wp cat wp-config.php

    ...
    // ** MySQL settings - You can get this info from your web host ** //
    /** The name of the database for WordPress */
    define( 'DB_NAME', 'bd_wp');

    /** MySQL database username */
    define( 'DB_USER', 'user_wp');

    /** MySQL database password */
    define( 'DB_PASSWORD', 'asdasd');

    /** MySQL hostname */
    define( 'DB_HOST', 'mysql');

    /** Database Charset to use in creating database tables. */
    define( 'DB_CHARSET', 'utf8');
    ...

### Actualizando el fichero /etc/hosts

Otro mecanismo que se realiza para permitir la comunicación entre contenedores asociados es modificar el fichero `/etc/hosts` para que tengamos resolución estática entre ellos. Podemos comprobarlo:

    docker exec servidor_wp cat /etc/hosts

    ...
    172.17.0.4	mysql 9f7eeb5a0634 servidor_mysql

Accede a la ip del servidor docker y comprueba la instalación de wordpress.