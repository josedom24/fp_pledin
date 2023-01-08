---
title: Despliegue de aplicaciones Java
---

## Tarea 1: Desarrollo y despliegue de una aplicación Java simple

De forma similar a lo que hemos hecho en el Taller 1, despliegue de forma manual la aplicación Java que encontrarás en el repositorio [https://github.com/josedom24/rock-paper-scissors](https://github.com/josedom24/rock-paper-scissors).


## Tarea 2: Despliegue de un CMS Java

Aunque Java se utiliza normalmente para desarrollar aplicaciones a medida, tenemos varios CMS construidos con Java: [Wikipedia - List of content management systems Java](https://en.wikipedia.org/wiki/List_of_content_management_systems#Java).

En esta tarea vamos a hacer un despliegue sencillo de una aplicación Java: **OpenCMS**. Siguiendo la [documentación](https://documentation.opencms.org/central/) realiza la implantación en el tomcat que instalaste en el taller1. Tienes que tener en cuenta lo siguiente:

* Tienes que descargar el fichero war para realizar el despliegue.
* Necesitas una base de datos MariaDB para que el CMS funcione.

Cuando este desplegado, accede a la aplicación y realiza alguna modificación para que aparezca tu nombre en la página principal.

## Tarea 3: Acceso a las aplicaciones

Cuando trabajamos con tomcat no se accedemos directamente al servidor de aplicaciones, se instala un proxy inverso que nos permita el acceso a las aplicaciones. Instala un proxy inverso para acceder a las aplicaciones con las siguientes urls:

* A la aplicación **rock-paper-scissors** se accede con la url `java.tunombre.org/game`.
* A la aplicación **OpenCMS** se accede con la url `java.tunombre.org/portal`.


{% capture notice-text %}

1. Entrega una captura de la aplicación de administración `Tomcat-Manager` donde se compruebe que las aplicaciones están desplegadas.
2. Configuración del proxy inverso para acceder a las aplicaciones cómo nos indica la práctica.
3. Acceso desde un navegar web a la aplicación **rock-paper-scissors** con la url `java.tunombre.org/game`.
4. Acceso desde un navegar web a la aplicación **OpenCMS** con la url `java.tunombre.org/portal`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
