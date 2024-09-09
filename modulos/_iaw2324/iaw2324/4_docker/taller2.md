---
title: "Taller 2: Escenarios multicontenedor en Docker"
---

## Despliegue de Nextcloud

Vamos a desplegar la aplicación nextcloud con una base de datos (puedes elegir mariadb o PostgreSQL) utilizando la aplicación docker-compose. Puedes coger cómo modelo el fichero `docker-compose.yaml` el que hemos estudiado para desplegar WordPress.

1. Instala docker-compose en tu ordenador. 
2. Dentro de un directorio crea un fichero `docker-compose.yaml` para realizar el despliegue de nextcloud con una base de datos. Recuerda las variables de entorno y la persistencia de información.
3. Levanta el escenario con `docker compose`.
4. Muestra los contenedores con `docker compose`.
5. Accede a la aplicación y comprueba que funciona.
6. Comprueba el almacenamiento que has definido y que se ha creado una nueva red de tipo bridge.
7. Borra el escenario con `docker compose`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Contenido del fichero `docker-compose.yaml`.
2. Instrucción para levantar el escenario con Compose.
3. Instrucción para ver los contenedores con Compose.
4. Pantallazos accediendo a nextcloud para comprobar que funciona de manera correcta.
5. Comprobación del almacenamiento que has definido y que se ha creado una nueva red de tipo bridge.
6. Instrucción para borrar el escenario con Compose.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
