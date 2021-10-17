---
title: "Práctica: Implantación de aplicaciones web PHP"
---

* Crea una instancia de vagrant basado en un box debian o ubuntu
* Instala en esa máquina virtual toda la pila LAMP

## Tarea 1: Instalación de un CMS PHP en mi servidor local

* Configura el servidor web con virtual hosting para que el CMS sea accesible desde la dirección: `www.nombrealumno-nombrecms.org`.
* Crea un usuario en la base de datos para trabajar con la base de datos donde se van a guardar los datos del CMS.
* Descarga el CMS seleccionado y realiza la instalación.
* Realiza una configuración mínima de la aplicación (Cambia la plantilla, crea algún contenido, ...)
* Instala un módulo para añadir alguna funcionalidad al CMS.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando en local. Entrega un documentación resumida donde expliques los pasos fundamentales para realizar esta tarea. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Configuración multinodo

* Realiza un copia de seguridad de la base de datos
* Crea otra máquina con vagrant, conectada con una red interna a la anterior y configura un servidor de base de datos.
* Crea un usuario en la base de datos para trabajar con la nueva base de datos.
* Restaura la copia de seguridad en el nuevo servidor de base datos.
* Desinstala el servidor de base de datos en el servidor principal.
* Realiza los cambios de configuración necesario en el CMS para que la página funcione.

{% capture notice-text %}
Entrega un documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
En este momento, muestra al profesor la aplicación funcionando en local. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Instalación de otro CMS PHP

* Elige otro CMS realizado en PHP y realiza la instalación en tu infraestructura. 
* Configura otro virtualhost para acceder con otro nombre: `www.nombrealumno-nombrecms.org`.

{% capture notice-text %}
En este momento, muestra al profesor la aplicación funcionando en local. Y describe en redmine los pasos fundamentales para realizar la tarea. (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Migración del CMS PHP en el hosting compartido.

Vamos a migrar la última aplicación que has instalado a un hosting externo, para ello sigue los siguientes pasos:

* Elige un servicio de hosting compartido con las características necesarias para instalar un CMS PHP (soporte PHP, base de datos,...)
* Date de alta en el servicio.
* Realiza la migración: Sube los ficheros al hosting externo, cambia las credenciales de acceso a la base de datos,...

{% capture notice-text %}
Entrega un documentación resumida donde expliques los pasos fundamentales para realizar esta tarea.
En este momento, muestra al profesor la aplicación funcionando en el otro hosting. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
