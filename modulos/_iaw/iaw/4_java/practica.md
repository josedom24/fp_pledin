---
title: Despliegue de aplicaciones Java
---

## Tarea 1: Desarrollo y despliegue de una aplicación Java simple

De forma similar a lo que hemos hecho en el Taller 1, despliegue de forma manual la aplicación Java que encontrarás en el repositorio [https://github.com/josedom24/rock-paper-scissors](https://github.com/josedom24/rock-paper-scissors).

{% capture notice-text %}
* Escribe una guía de los pasos fundamentales para realizar la instalación.
* Entrega una captura de pantalla donde se vea la aplicación funcionando desde tomcat.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Despliegue de un CMS Java

En esta práctica vamos a desplegar un CMS escrito en java. ¿Qué debes tener en cuenta?

1. Debes desplegar la aplicación desde un fichero war. 
2. No usar instalaciones "bundler". Estas instalaciones instalan la aplicación y tomcat al mismo tiempo. La aplicación se debe desplegar en el tomcat que tienes instalado.
3. Utiliza una máquina virtual que tenga suficiente memoria, al menos 2Gb, algunos CMS requieren mucha memoria RAM.
4. La aplicación debe guardar los datos en una base de datos

Se evaluará la complejidad de la instalación (por ejemplo, necesidad de tener que instalar un conector de base de datos, configuración especifica, ...), ejemplo de puntuación (de un máximo de 10 puntos):

* openCMS (5 puntos)
* jenkins (6 puntos)
* Guacamole (7 puntos)
* Alfresco (10 puntos)

Sin categorizar:

* Magnolia
* OpenWGA
* XWiki
* eXo Platform
* Liferay

Puedes buscar más aplicaciones en:

* [Wikipedia - List of content management systems JAVA ](https://en.wikipedia.org/wiki/List_of_content_management_systems#Java)
* [Awesome CMS](https://github.com/postlight/awesome-cms#java)

{% capture notice-text %}
* Indica la aplicación escogida y su funcionalidad.
* Escribe una guía de los pasos fundamentales para realizar la instalación.
* ¿Has necesitado instalar alguna librería?¿Has necesitado instalar un conector de una base de datos?
* Entrega una captura de pantalla donde se vea la aplicación funcionando desde tomcat.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Acceso a las aplicaciones

Cuando trabajamos con tomcat no se accedemos directamente al servidor de aplicaciones, se instala un proxy inverso que nos permita el acceso a las aplicaciones. 

Tienes que configurar un proxy inverso con nginx para acceder a las aplicaciones con las siguientes urls:

* A la aplicación **rock-paper-scissors** se accede con la url `java.tunombre.org/game`.
* A la aplicación Java se accede con la url `java.tunombre.org`.



{% capture notice-text %}

1. Configuración del proxy inverso para acceder a las aplicaciones cómo nos indica la práctica.
2. Acceso desde un navegador web a la aplicación **rock-paper-scissors** con la url `java.tunombre.org/game`.
3. Acceso desde un navegador web a la aplicación **OpenCMS** con la url `java.tunombre.org`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
