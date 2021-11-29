---
title: Despliegue de CMS java
---

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
* Escribe una guía de los pasas fundamentales para realizar la instalación.
* ¿Has necesitado instalar alguna librería?¿Has necesitado instalar un conector de una base de datos?
* Entrega una captura de pantalla donde se vea la aplicación funcionando desde tomcat.
* Realiza la configuración necesaria en apache2 y tomcat para que la aplicación sea servida por el servidor web.
* Muestra al profesor la aplicación funcionando servida por apache2.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
