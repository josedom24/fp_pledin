---
title: "Práctica (1 / 3): Instalación/migración de aplicaciones web PHP"
---

## Escenario

Crea un escenario con vagrant, kvm o openstack con las siguientes características:

* Dos máquinas virtuales que se llamen `servidor_web_tunombre` y `servidor_bd_tunombre`.
* Las máquinas estarán conectadas a una red que les proporcione salida a internet.
* Las dos máquinas están conectadas entre si por una red muy aislada.

## Instalación de un CMS PHP en mi servidor local

* Selecciona un CMS escrito en PHP para desplegarlo en nuestra infraestructura. No se puede elegir ni WordPress (que lo hemos visto en un vídeo, ni NextCloud que lo instalaremos a continuación).
* Configura en la máquina `servidor_web_tunombre` un servidor web apache2 que ejecute PHP, con un VirtualHost, para que el CMS sea accesible desde la dirección: `www.nombrealumno.org`.
* Configura en la máquina `servidor_bd_tunombre` una base de datos. Crea un usuario con privilegios sobre la base de datos donde se van a guardar los datos del CMS. Configura la base de datos para que permita conexión desde la otra máquina por la red muy aislada, es decir la máquina `servidor_web_tunombre` se conecta a `servidor_bd_tunombre` usando su ip que tiene configurada en la red privada muy aislada.
* Descarga el CMS seleccionado y realiza la instalación.
* Realiza una configuración mínima de la aplicación (cambia la plantilla, crea algún contenido, ...)
* Instala un módulo para añadir alguna funcionalidad al CMS.

{% capture notice-text %}
## Entrega

1. Entrega la configuración del virtualhost.
2. La configuración de resolución estática.
3. Una captura de pantalla donde se vea el acceso a la aplicación.
4. Indica que plugin has instalado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Instalación de un CMS NextCloud

* Instala el CMS PHP NextCloud en otro host virtual con el que accedemos con el nombre `cloud.nombrealumno.org`.

{% capture notice-text %}
## Entrega

1. Una captura de pantalla donde se vea el acceso a la aplicación.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

