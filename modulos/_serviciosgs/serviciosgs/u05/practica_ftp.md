---
title: "Práctica: Gestionar un hosting por ftp"
permalink: /serviciosgs/u05/practica_ftp.html
---

(5 tareas - 15 puntos)(2 tareas obligatorias - 5 puntos)
{: .notice--warning}

* Cuando termines las tareas tienes que realizar una prueba de funcionamiento al profesor.
{: .notice--warning}

Vamos a montar un hosting en nuestro servidor web. Por lo tanto tendremos que ir combinando la configuración de varios servicios (web, dns, ftp, mysql, ...)

## FTP anónimo

Queremos ofrecer una colección de documentos, y lo vamos a hacer mediante http y ftp anónimo, de esta forma se accederá al mismo directorio si accedo a las siguientes URL:

	* ``http://www.tunombre.gonzalonazareno.org/documentos``
	* ``ftp://ftp.tunombre.gonzalonazareno.org``

El servidor ftp lo vamos a instalar en el mismo equipo donde tenemos el servidor web.

{% capture notice-text %}
* **Tarea 1 (2 puntos)(Obligatorio):** Explica la instalación del servidor FTP. Configura apache2 y el servidor ftp de forma anónimo para obtener el resultado pedido. Entrega la configuración de ambos servidores y una prueba de funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Hosting: Creación de páginas web

Queremos que diferentes usuarios, puedan crear una página web en vuestro servidor que esté gestionada por medio de un FTP. 

Por ejemplo, el usuario `josedom` quiere hacer una página cuyo nombre será `servicios`:

* La página que vamos a crear será accesible en ``servicios.tunombre.gonzalonazareno.org``.
* Se creará un usuario ``user_josedom``, que tendrá una contraseña, para que accediendo a ``ftp.tunombre.gonzalonazareno.org``, pueda gestionar los ficheros de su página web.

Determina los cambios que tienes que ir realizando para ir creando el espacio web para cada uno de los departamentos.

* ¿Qué cambios tienes que hacer en el servidor DNS?
* ¿Qué cambios tienes que hacer en el servidor Web?
* ¿Cómo tienes que configurar el servidor FTP para obtener la funcionalidad deseada?

{% capture notice-text %}
* **Tarea 2 (3 puntos)(Obligatorio):** Entrega los cambios realizados en los distintos servicios para obtener la página web del usuario. Entrega la configuración del servidor FTP. Muestra una prueba de funcionamiento accediendo al servidor FTP y que si subimos un fichero, vemos la página web de forma adecuada.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Escribe un script ``alta_pagina_web``, que recibe como parámetro el nombre del usuario y realiza los pasos (configuraciones en los distintos servicios) para crear la página web de departamento y que un usuario accediendo por ftp pueda gestionarla. El script debe devolver la contraseña del servidor FTP.
{% capture notice-text %}
* **Tarea 3 (3 puntos):** Entrega la url del repositorio github, y haz una prueba al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Instala la aplicación web `net2ftp` en el servidor por si tenemos problemas de acceso por el puerto 20/21. Configura `net2ftp` para que no pida en el inicio la dirección del servidor donde va a acceder, sólo debe pedir el nombre de usuario y la contraseña. La aplicación debe estar accesible desde la URL `net2ftp.tunombre.gonzalonazareno.org`.
{% capture notice-text %}
* **Tarea 4 (3 puntos):** Entrega el proceso de instalación y la configuración de `net2ftp` y de apache2. realiza una prueba de funcionamiento al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejecución de scripts PHP





* El uso de usuarios reales del sistema para el acceso FTP puede tener varias desventajas (gestión, seguridad,...). Modifica la configuración del sistema para que se usen usuarios virtuales para el acceso por FTP, cuya información este guardada en una tabla mysql o en un directorio ldap.
```eval_rst
.. warning::

	**Tarea 5 (4 puntos):** Entrega los pasos más relevantes para realizar esta tarea. Y muestra al profesor su funcionamiento.
```