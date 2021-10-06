---
title: Instalación local de un CMS PHP 
---

Esta tarea consiste en instalar un CMS de tecnología PHP en un servidor local. Los pasos que tendrás que dar los siguientes:

## Tarea 1: Instalación de un servidor LAMP

* Crea una instancia de vagrant basado en un box debian o ubuntu
* Instala en esa máquina virtual toda la pila LAMP

{% capture notice-text %}
Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Instalación de drupal en mi servidor local

* Configura el servidor web con virtual hosting para que el CMS sea accesible desde la dirección: `www.nombrealumno-drupal.org`.
* Crea un usuario en la base de datos para trabajar con la base de datos donde se van a guardar los datos del CMS.
* Descarga la versión que te parezca más oportuna de Drupal y realiza la instalación.
* Realiza una configuración mínima de la aplicación (Cambia la plantilla, crea algún contenido, ...)
* Instala un módulo para añadir alguna funcionalidad a drupal.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando en local. Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Configuración multinodo

* Realiza una copia de seguridad de la base de datos
* Crea otra máquina con vagrant, conectada con una red interna a la anterior y configura un servidor de base de datos.
* Crea un usuario en la base de datos para trabajar con la nueva base de datos.
* Restaura la copia de seguridad en el nuevo servidor de base datos.
* Desinstala el servidor de base de datos en el servidor principal.
* Realiza los cambios de configuración necesaria en drupal para que la página funcione.

{% capture notice-text %}
Entrega una documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
	En este momento, muestra al profesor la aplicación funcionando en local. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Instalación de otro CMS PHP

* Elige otro CMS realizado en PHP y realiza la instalación en tu infraestructura.
* Configura otro virtualhost y elige otro nombre en el mismo dominio.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando en local. Y describe en redmine los pasos fundamentales para realizar la tarea. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Necesidad de otros servicios

* La mayoría de los CMS tienen la posibilidad de mandar correos electrónicos (por ejemplo para notificar una nueva versión, notificar un comentario,...)
* Instala un servidor de correo electrónico en tu servidor. Debes configurar un servidor relay de correo, para ello en el fichero `/etc/postfix/main.cf`, debes poner la siguiente línea:

		relayhost = babuino-smtp.gonzalonazareno.org

* Configura alguno de los CMS para utilizar tu servidor de correo y realiza una prueba de funcionamiento.

{% capture notice-text %}
Muestra al profesor algún correo enviado por tu CMS. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

