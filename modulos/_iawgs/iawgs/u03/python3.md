---
title: "Depliegue de CMS python: Mezzanine"
permalink: /iawgs/u03/python3.html
---

En estas práctica vamos a desplegar un [CMS python](https://wiki.python.org/moin/ContentManagementSystems). Hemos elegido [Mezzanine](http://mezzanine.jupo.org/).

## Tarea 1: Instalación de Mezzanine en el entorno de desarrollo

Instala localmente (usando un entrono virtual) el CMS Mezzazine. Realiza una modificación en la página web. Guarda los ficheros generados durante la instalación en un repositorio github.

{% capture notice-text %}
Entrega una breve documentación de los pasos para realizar la instalación. Entrega una captura de pantalla donde se vea el acceso al servidor web de desarollo (2 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Migración a un entorno de producción

Prepara el entorno de producción con un entrono virtual. Instala el servidor web que vas a utilizar (apache o nginx). Instala el gestor de base de datos que vas a utilizar (mysql, postgress).

* Clona tu repositorio con tus ficheros del CMS.
* Realiza una copia de seguridad de los datos del gestor de contenido en desarrollo, y realiza la migración de forma adecuada.

{% capture notice-text %}
Entrega una breve documentación de los pasos para realizar la instalación. Teniendo en cuenta las siguientes puntuaciones:

* Usar un entorno virtual con python2 (1 punto), utilizar python3 (2 puntos).
* Usar apache2 (1 punto), usar nginx (2 puntos).
* Usar mysql (1 punto), usar postgreSQL (2 puntos).
* Usar una URL del tipo ``www.tupagina.com`` (1 punto), usar una URL del tipo ``www.tupagina.com/blog`` (2 puntos)

 Entrega una captura de pantalla donde se vea el acceso al servidor web de producción.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
