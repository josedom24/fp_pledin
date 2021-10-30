---
title: "Práctica 2: Instalación/migración de aplicaciones web PHP eb tu VPS"
---

## Tarea 1

Realizar la migración de la primera aplicación que tienes instalada en la práctica anterior a nuestro entorno de producción, para ello ten en cuenta lo siguiente:

1. La aplicación se tendrá que migrar a un nuevo virtualhost al que se accederá con el nombre `portal.tudominio.algo`.
2. Vamos a nombrar el servicio de base de datos que tenemos en producción. Como es un servicio interno no la vamos a nombrar en la zona DNS, la vamos a nombrar usando resolución estática. El nombre del servicio de base de datos se debe llamar: `bd.tudominio.algo`.
3. Realiza la migración de la aplicación.
4. Asegurate que las URL limpias de drupal siguen funcionando en nginx.
5. La aplicación debe estar disponible en la URL: `portal.tudominio.algo` (Sin ningún directorio).


## Tarea 2

Instalación / migración de la aplicación Nextcloud:

1. Instala la aplicación web Nextcloud en tu entorno de desarrollo.
2. Realiza la migración al servidor en producción, para que la aplicación sea accesible en la URL: `www.tudominio.algo/cloud`
3. Instala en un ordenador el cliente de nextcloud y realiza la configuración adecuada para acceder a "tu nube".

{% capture notice-text %}
Documenta de la forma más precisa posible cada uno de los pasos que has dado, y entrega pruebas de funcionamiento para comprobar el proceso que has realizado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>










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
