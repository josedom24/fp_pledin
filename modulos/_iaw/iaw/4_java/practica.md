---
title: Despliegue de aplicaciones Java
---

## Tarea 1: Desarrollo y despliegue de una aplicación Java simple

De forma similar a lo que hemos hecho en el Taller 1, despliegue de forma manual la aplicación Java que encontrarás en el repositorio [https://github.com/josedom24/rock-paper-scissors](https://github.com/josedom24/rock-paper-scissors).


## Tarea 2: Despliegue de un CMS Java

Aunque Java se utiliza normalmente para desarrollar aplicaciones a medida, tenemos varios CMS construidos con Java: [Wikipedia - List of content management systems Java](https://en.wikipedia.org/wiki/List_of_content_management_systems#Java).

En esta tarea vamos a hacer un despliegue sencillo de una aplicación Java: **OpenCMS**. El problema que tenemos que este CMS no es compatible con tomcat10, pero no hay problemas lo vamos a instalar sobre un contenedor docker:

* Puedes seguir esta guía para trabajar con tomcat en docker: [Configuración de imágenes con una aplicación Java](https://github.com/josedom24/curso_docker_ow/blob/main/contenido/modulo7/ejemplo5.md).
* Puedes seguir la [documentación](https://documentation.opencms.org/central/) de OpenCMS.
* Tienes que descargar el fichero war para realizar el despliegue. [Enlace](http://www.opencms.org/en/modules/downloads/dl-opencms-8.0.4-distribution.html).
* Necesitas una base de datos MariaDB para que el CMS funcione. Lo más fácil es crear un docker compose que te ayude a desplegar los dos contenedores.

Cuando este desplegado, accede a la aplicación y realiza alguna modificación para que aparezca tu nombre en la página principal.

Despliega la aplicación **rock-paper-scissors** en este contenedor con tomcat.

## Tarea 3: Acceso a las aplicaciones

Cuando trabajamos con tomcat no se accedemos directamente al servidor de aplicaciones, se instala un proxy inverso que nos permita el acceso a las aplicaciones. 

Vamos a instalar un proxy inverso en un contenedor docker con la imagen `nginx`. En el contenedor vamos a montar con bind mount el fichero de configuración de nginx. Puedes ver un ejemplo en el artículo [Ejemplo 4: Despliegue de tomcat + nginx](https://github.com/josedom24/curso_docker_ies/blob/main/modulo4/tomcat.md). Tienes que configurar el proxy inverso para acceder a las aplicaciones con las siguientes urls:

* A la aplicación **rock-paper-scissors** se accede con la url `java.tunombre.org/game`.
* A la aplicación **OpenCMS** se accede con la url `java.tunombre.org`.

Añade a tu docker Compose otro servicio para levantar el proxy inverso. Evidentemente el contenedor de nginx será el único que exponga el puerto para acceder a la aplicación.


{% capture notice-text %}

1. Configuración del proxy inverso para acceder a las aplicaciones cómo nos indica la práctica.
2. Acceso desde un navegar web a la aplicación **rock-paper-scissors** con la url `java.tunombre.org/game`.
3. Acceso desde un navegar web a la aplicación **OpenCMS** con la url `java.tunombre.org`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
