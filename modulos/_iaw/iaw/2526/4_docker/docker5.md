---
title: "Ejemplo 4: Construcción de imágenes configurables con variables de entorno (PHP)"
---

En este ejemplo vamos a construir una imagen de una aplicación PHP que necesita conectarse a una base de datos MariaDB para leer información. Para ello, construiremos la imagen de forma que la configuración de acceso a la base de datos se realice mediante **variables de entorno**, lo que permitirá reutilizar la misma imagen en distintos entornos sin necesidad de modificarla.

## Aplicación PHP

Como ejemplo vamos a “dockerizar” una aplicación PHP sencilla que accede a una tabla de una base de datos. La aplicación se encuentra en el directorio `build/app/index.php`.

Algunas consideraciones importantes:

* Cuando una aplicación va a ser desplegada usando Docker, su configuración no debe estar codificada en el propio código. En este caso, los datos de conexión a la base de datos se obtienen a partir de **variables de entorno**, que se definirán al crear el contenedor.

```php
<?php
 // Database host
 $host = getenv('DB_HOST');
 // Database user name
 $user = getenv('DB_USER');
 // Database user password
 $pass = getenv('DB_PASS');
 // Database name
 $db = getenv('DB_NAME');

 // Check the MySQL connection status
 $conn = new mysqli($host, $user, $pass, $db);

 if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
 }

 $sql = 'SELECT * FROM users';

 if ($result = $conn->query($sql)) {
     while ($data = $result->fetch_object()) {
         $users[] = $data;
     }
 }

 if (!empty($users)) {
     foreach ($users as $user) {
         echo "<br>";
         echo $user->username . " " . $user->password;
         echo "<br>";
     }
 }

 mysqli_close($conn);
 ?>
```

* En el fichero `schema.sql` ([descarga](https://raw.githubusercontent.com/josedom24/curso_docker_ies/refs/heads/main/ejemplos/modulo5/ejemplo4/build/schema.sql) se encuentran las instrucciones SQL necesarias para crear las tablas de la base de datos. Este fichero será utilizado por el contenedor de MariaDB en el momento de inicializar la base de datos.

## Configurar nuestra aplicación con variables de entorno

En muchos casos, además de configurar la aplicación mediante variables de entorno, es necesario realizar **alguna tarea previa** cuando el contenedor se inicia, antes de ejecutar el servidor web. Algunos ejemplos habituales son:

* Mostrar o validar la configuración recibida
* Ajustar permisos de directorios montados como volúmenes
* Generar ficheros de configuración dinámicos
* Comprobar la disponibilidad de servicios externos

Para estos casos, es habitual utilizar un **script de arranque**, que se ejecutará al iniciar el contenedor y que finalmente lanzará el servidor web como proceso principal.

## Estructura del directorio de trabajo

En el directorio de trabajo encontramos:

* `build`: contexto necesario para crear la imagen de la aplicación.
* El fichero `docker-compose.yaml`: definición del escenario completo.


## El contexto (directorio `build`)

En el directorio de contexto de la imagen de la aplicación tendremos los siguientes ficheros:

### Fichero `entrypoint.sh`

El fichero `entrypoint.sh` se copiará dentro de la imagen y se ejecutará al iniciar el contenedor. Su contenido es el siguiente:

```bash
#!/bin/bash
set -e

echo "Starting application with the following configuration:"
echo "DB_HOST=${DB_HOST}"
echo "DB_NAME=${DB_NAME}"

# Aquí podrían realizarse tareas adicionales de preparación

# Arrancar Apache en primer plano
exec apache2ctl -D FOREGROUND
```

Este script permite ejecutar tareas de inicialización antes de arrancar el servidor web. El uso de `exec` garantiza que Apache se ejecute como proceso principal del contenedor.


### Fichero `schema.sql`

Este fichero contiene las instrucciones SQL necesarias para crear las tablas de la base de datos.
Será ejecutado automáticamente por el contenedor de MariaDB cuando se inicialice la base de datos por primera vez.

### Fichero `Dockerfile`

El fichero `Dockerfile` de la aplicación es el siguiente:

```Dockerfile
# syntax=docker/dockerfile:1
FROM php:8.3-apache

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

COPY app /var/www/html/
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

CMD ["/usr/local/bin/entrypoint.sh"]
```

Algunas observaciones:

1. Creamos la imagen a partir de una imagen oficial de PHP con Apache.
2. Instalamos la extensión PHP `mysqli`, necesaria para conectarse a MariaDB.
3. Copiamos la aplicación al directorio del servidor web.
4. Copiamos el script de arranque y le damos permisos de ejecución.
5. No se incluye ningún cliente de base de datos ni lógica de inicialización del esquema.
6. El servidor web se arranca a través del script indicado en `CMD`.


### Creación de la imagen

Ejecutamos dentro del directorio de contexto:

```bash
$ docker build -t josedom24/aplicacion_php .
```


## Despliegue de la aplicación

Para desplegar el escenario completo utilizamos el fichero `docker-compose.yaml`:

```yaml
version: '3.1'
services:
  app:
    container_name: contenedor_php
    image: josedom24/aplicacion_php
    restart: always
    environment:
      DB_HOST: servidor_mysql
      DB_USER: user1
      DB_PASS: asdasd
      DB_NAME: usuarios
    ports:
      - 8080:80
    depends_on:
      - db

  db:
    container_name: servidor_mysql
    image: mariadb
    restart: always
    environment:
      MYSQL_DATABASE: usuarios
      MYSQL_USER: user1
      MYSQL_PASSWORD: asdasd
      MYSQL_ROOT_PASSWORD: asdasd
    volumes:
      - mariadb_data:/var/lib/mysql
      - ./schema.sql:/docker-entrypoint-initdb.d/schema.sql

volumes:
  mariadb_data:
```

El contenedor de MariaDB se encarga de crear la base de datos y las tablas a partir del esquema. El contenedor de la aplicación únicamente se conecta a una base de datos ya inicializada.


## Puesta en marcha del escenario

Para levantar el escenario ejecutamos:

```bash
$ docker compose up -d
```

Finalmente, podemos acceder a la aplicación desde el navegador y comprobar que funciona correctamente.

