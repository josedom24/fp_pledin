---
title: Despliegue tradicional de CMS PHP
permalink: /iawgs/u02/practica_php2.html
---

{% capture warning-text %}
Tienes dos opciones para realizar esta práctica:
1. Consideramos que el primer hosting compartido es tu servidor dedicado, posteriormente tendrás que hacer la migración a un hosting externo.
2. Utilizar dos servicios de hosting distintos (tal cómo se explica en la práctica.)
{% endcapture %}<div class="notice--warning">{{ warning-text | markdownify }}</div>

## Tarea 1: Elección del escenario que vas a montar

{% capture notice-text %}
Indica que opción has elegido:

* Servidor dedicado y hosting externo (1 punto)
* Dos servicios de hosting distintos (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


Esta tarea consiste en instalar un CMS de tecnología PHP (elige un CMS que no hayas usado en la práctica anterior) en un hosting compartido. Los pasos que tendrás que dar los siguientes:

## Tarea 2: Elección de un hosting compartido

* Elige un servicio de hosting compartido con las caracterísitcas necesarias para instalar un CMS PHP (soporte PHP, base de datos,...)
* Date de alta en el servicio.

{% capture notice-text %}
Indica que servicio de hosting has elegido. Indica las características del hosting que vas a utilizar. Indica la URL que tendrá tu página web. Indica el CMS que vas a instalar. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Instalación del CMS PHP en el hosting compartido.

* Descarga en tu ordenado el CMS PHP que vas a instalar.
* Sube los ficheros al hosting compartido por FTP.
* Realizar la configuración de la base de datos de forma adecuada.
* Realiza la instalación.
* Realiza una configuración mínima de la aplicación (Cambia la plantilla, crea algún contenido, ...)
* Instala un módulo para añadir alguna funcionalidad al CMS PHP.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando. Entrega un documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Migración de la apliación web

* Elige otro servicio de hosting para PHP.
* Realiza el proceso de migración.

{% capture notice-text %}
Entrega un documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
En este momento, muestra al profesor la aplicación funcionando en el otro hosting. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Copia de seguridad de tu aplicación

* ¿Cómo harías una copia de seguridad de tu aplicación? ¿Crees que se puede automatizar dicha tarea?

{% capture notice-text %}
Entrega una documentación donde indiques los pasos para realizar una copia de seguridad. Si puedes realiza un pequeño script que automatice dicha tarea. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

{% capture warning-text %}
* Identificación de problemas: los cambios se realizan directamente en el servidor en producción
* Identificación de problemas: los hosting compartidos no son escalables ni elásticos
* Identificación de problemas: el uso de FTP no me permite control de versiones y no es el mecanismo más eficiente.
* Identificación de problemas: Este esquema no funciona si tenemos un equipo de desarrollo construyendo una aplicación web a medida.
* Identificación de problemas: Las copias de seguridad pueden ser complicadas de realizar y además es complicado la automatización.
{% endcapture %}<div class="notice--warning">{{ warning-text | markdownify }}</div>

