---
title: "Práctica Servidores Cloud: Hosting"
permalink: /serviciosgs/u05/practica_ftp2.html
---

Queremos que diferentes usuarios, puedan gestionar una página web en vuestro servidor que esté gestionada por medio de un FTP. También se creará una base de datos para cada usuario.

Por ejemplo, el usuario `josedom` quiere hacer una página cuyo nombre será `servicios`:

* La página que vamos a crear será accesible en ``https://servicios.tunombre.gonzalonazareno.org``.
* Se creará un usuario ``user_josedom``, que tendrá una contraseña, para que accediendo a ``ftp.tunombre.gonzalonazareno.org``, pueda gestionar los ficheros de su página web.
* Se creará un usuario en la base de datos llamado `myjosedom`. Este usuario tendrá una contraseña distinta a la del usuario del servidor FTP.
* Se creará una bases de datos para el usuario anteriormente creado. Para que los usuarios gestionen su base de datos se puede instala la aplicación `phpmyadmin` a la que se accederá con la URL `https://sql.tunombre.gonzalonmazareno.org`.


{% capture notice-text %}
Tarea: Configura manualmente los distintos servicios para crear un nuevo usuario que gestione su propia página web y tenga una base de datos a su disposición. Instala un CMS.
Mejora 1: Modifica la configuración del sistema para que se usen usuarios virtuales para el acceso por FTP, cuya información este guardada en vuestro directorio ldap.
Mejora 2: Realiza un script que automatice la creación/borrado de nuevos usuarios en el hosting.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

