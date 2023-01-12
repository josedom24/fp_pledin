---
title: "Ejercicio 4: Escenarios multicontenedor en Docker"
---

## Despliegue de Nextcloud

Vamos a desplegar la aplicación nextcloud con una base de datos (puedes elegir mariadb o PostgreSQL) utilizando la aplicación docker-compose. Puedes coger cómo modelo el fichero `docker-compose.yml` el que hemos estudiado para desplegar WordPress.

1. Instala docker-compose en tu ordenador. 
2. Dentro de un directorio crea un fichero `docker-compose.yml` para realizar el despliegue de nextcloud con una base de datos. Recuerda las variables de entorno y la persistencia de información.
3. Levanta el escenario con `docker-compose`.
4. Muestra los contenedores con `docker-compose`.
5. Accede a la aplicación y comprueba que funciona.
6. Comprueba el almacenamiento que has definido y que se ha creado una nueva red de tipo bridge.
7. Borra el escenario con `docker-compose`.