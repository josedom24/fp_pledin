---
title: "Ejercicio 3: Configuración de apache mediante archivo .htaccess"
---

Un fichero ``.htaccess`` (hypertext access), también conocido como archivo de configuración distribuida, es un fichero especial, popularizado por el Servidor HTTP Apache que nos permite definir diferentes directivas de configuración para cada directorio (con sus respectivos subdirectorios) sin necesidad de editar el archivo de configuración principal de Apache.

Para permitir el uso de los ficheros `.htaccess` o restringir las directivas que se pueden aplicar usamos ela directiva [AllowOverride](http://httpd.apache.org/docs/2.4/mod/core.html#allowoverride>), que puede ir acompañada de una o varias opciones: ``All``, ``AuthConfig``, ``FileInfo``, ``Indexes``, ``Limit``, ... Estudia para que sirve cada una de las opciones.


## Ejercicios

Date de alta en un **proveedor de hosting**. ¿Si necesitamos configurar el servidor web que han configurado los administradores del proveedor?, ¿qué podemos hacer? ¿Para qué sirve la directiva ``AllowOverride`` de apache2?. Utilizando archivos `.htaccess` realiza las siguientes configuraciones:

1. Habilita el listado de ficheros en la URL  ``http://host.dominio/nas``.
2. Crea una redirección permanente: cuando entremos en ``http://host.dominio/google`` salte a ``www.google.es``.
3. Pedir autentificación para entrar en la URL ``http://host.dominio/prohibido``. (No la hagas si has elegido como proveedor CDMON, en la plataforma de prueba, no funciona.)

{% capture notice-text %}
**Entrega**

1. Pantallazo que se vea el acceso a `http://host.dominio/nas`.
2. Utilizando la opción de "Desarrollador web" del navegado, entrega un pantallazo donde se vea que cuando a accedemos a `host.dominio/google` se produce un redireccionamiento a `www.google.es`.
3. Pantallazo donde se vea el acceso a `host.dominio/prohibido` y que te sale la autenficación, y otro pantallazo después de introducir nombre de usuario y contraseña.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
