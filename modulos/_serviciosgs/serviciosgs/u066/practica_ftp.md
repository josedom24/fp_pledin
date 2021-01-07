---
title: "Práctica: Gestionar un hosting por ftp"
permalink: /serviciosgs/u066/practica_ftp.html
---

**(11 tareas - 25 puntos)(3 tareas obligatorias - 8 puntos)**
{: .notice--warning}

**Cuando termines las tareas tienes que realizar una prueba de funcionamiento al profesor.**
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

El uso de usuarios reales del sistema para el acceso FTP puede tener varias desventajas (gestión, seguridad,...). Modifica la configuración del sistema para que se usen usuarios virtuales para el acceso por FTP, cuya información este guardada en vuestro directorio ldap.
{% capture notice-text %}
* **Tarea 5 (3 puntos):** Entrega los pasos más relevantes para realizar esta tarea. Y muestra al profesor su funcionamiento.
* **Tarea 6 (2 puntos):** Modifica el script `alta_pagina_web` para que la gestión de los usuarios FTP se haga a través del servidor LDAP.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejecución de scripts PHP

Queremos que nuestro hosting sea capaz de ejecutar ficheros PHP. realiza la instalación de los paquetes y las configuraciones necesarias para ello.

{% capture notice-text %}
* **Tarea 7 (3 puntos)(Obligatorio):** Sube un fichero `index.php` que contenga la función `phpinfo()` y comprueba la página que obtenemos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Gestión de los datos: servidor MySQL

En uno de nuestros servidores tenemos instalado un servidor mysql. Vamos a utilizarlos para dar más servicios a nuestro hosting. En este momento a la hora de dar de alta un usuario para que pueda tener una página web, vamos a crear un usuario en la base de datos.

Siguiendo el ejemplo del usuario `josedom` se creará un usuario en la base de datos llamado `myjosedom`. Este usuario tendrá una contraseña distinta a la del usuario del servidor FTP.

{% capture notice-text %}
* **Tarea 8 (1 punto):** Explica el proceso que tienes que hacer para crear un nuevo usuario a la base de datos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Vamos a tener la aplicación `phpmyadmin` accesible en la url ``www.tu_nombre.gonzalonazareno.org/basededatos``. (**Esto es una tarea de la práctica anterior**)

{% capture notice-text %}
* **Tarea 9 (1 punto):** Comprueba que el usuario creado en la tarea 6 es accesible a la base de datos utilizando la aplicación `phpmyadmin`. Comprueba que puede crear una base de datos.**
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Vamos a modificar nuestro script `alta_pagina_web`, para que al dar de alta un nuevo cliente cree el usuario de la base de datos. El script devolverá también la contraseña del usuario de la base de datos.

{% capture notice-text %}
* **Tarea 10 (1 punto):** Entrega la url del repositorio github, y haz una prueba al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Instalación de un CMS

Ya tenemos todos los elementos para poder instalar un CMS en nuestro hosting. 

{% capture notice-text %}
* **Tarea 11 (3 puntos):** Enseña al profesor el proceso completo de un CMS dando de alta a un nuevo usuario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

