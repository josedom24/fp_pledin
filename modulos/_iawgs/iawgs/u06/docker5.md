---
title: "Ejercicio: Creando escenarios docker con docker-compose"
permalink: /iawgs/u06/docker5.html
---

Cuando trabajamos con escenarios donde necesitamos correr varios contenedores podemos utilizar [docker-compose](https://docs.docker.com/compose/) para gestionarlos.

## Instalación de docker-compose

    apt install docker-compose

También se puede con `pip` en un entorno virtual:

    python3 -m venv docker-compose
    source docker-compose/bin/activate
    (docker-compose) ~# pip install docker-compose

## El fichero docker-compose.yml

En el fichero `docker-compose.yml` vamos a definir el escenario. El programa `docker-compose` se debe ejecutar en el directorio donde este ese fichero. Por ejemplo para la ejecución de wordpress persistente podríamos tener un fichero con el siguiente contenido:

    version: '3.1'

    services:

      wordpress:
        container_name: servidor_wp
        image: wordpress
        restart: always
        environment:
          WORDPRESS_DB_HOST: db
          WORDPRESS_DB_USER: user_wp
          WORDPRESS_DB_PASSWORD: asdasd
          WORDPRESS_DB_NAME: bd_wp
        ports:
          - 80:80
        volumes:
          - /opt/wordpress:/var/www/html/wp-content

      db:
        container_name: servidor_mysql
        image: mariadb
        restart: always
        environment:
          MYSQL_DATABASE: bd_wp
          MYSQL_USER: user_wp
          MYSQL_PASSWORD: asdasd
          MYSQL_ROOT_PASSWORD: asdasd
        volumes:
          - /opt/mysql_wp:/var/lib/mysql

Cuando creamos un escenario con `docker-compose` se crea una nueva red definida por el usuario docker donde se conectan los contenedores, por lo tanto están enlazados, pero no comparten las variables de entorno (Por esta razón hemos creado las variables de entorno al definir el contenedor de wordpress). Además tenemos resolución por dns que resuelve tanto el nombre del contendor (por ejemplo, `servidor_mysql`) como el alias (por ejemplo, `db`).

Para crear el escenario:

    # docker-compose up -d
    Creating network "dc_default" with the default driver
    Creating servidor_wp    ... done
    Creating servidor_mysql ... done

Para listar los contenedores:

    # docker-compose ps
         Name                   Command               State         Ports       
    ----------------------------------------------------------------------------
    servidor_mysql   docker-entrypoint.sh mysqld      Up      3306/tcp          
    servidor_wp      docker-entrypoint.sh apach ...   Up      0.0.0.0:80->80/tcp

Para parar los contenedores:

    # docker-compose stop 
    Stopping servidor_wp    ... done
    Stopping servidor_mysql ... done

Para borrar los contenedores:

    # docker-compose rm
    Going to remove servidor_wp, servidor_mysql
    Are you sure? [yN] y
    Removing servidor_wp    ... done
    Removing servidor_mysql ... done
