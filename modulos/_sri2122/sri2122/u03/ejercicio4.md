---
title: "Ejercicio 4: Módulos en apache"
---

## Directorios web para cada usuario (public_html)

El módulo [userdir](http://httpd.apache.org/docs/2.4/mod/mod_userdir.html) permite que cada usuario del sistema tenga la posibilidad de tener un directorio (por defecto se llama ``public_html``) donde alojar su página web.

### Ejercicios

1. Activa el módulo y comprueba su funcionamiento.
2. Comprueba las opciones configuradas para los directorios public_html.
3. Cambia el nombre de directorio public_html por otro nombre.
4. Publica una página de un usuario, y accede a la misma.

{% capture notice-text %}
1. Muestra la configuración del módulo `user_dir` donde se vea que has cambiado el directorio de publicación.
2. Pantallazo donde se vea el acceso a una página personal de un usuario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Creación de un servidor WebDAV

**WebDAV** ("*Edición y versionado distribuidos sobre la web*") es un protocolo para hacer que la www sea un medio legible y editable. Este protocolo proporciona funcionalidades para crear, cambiar y mover documentos en un servidor remoto (típicamente un servidor web). Esto se utiliza sobre todo para permitir la edición de los documentos que sirve un servidor web, pero puede también aplicarse a sistemas de almacenamiento generales basados en web, que pueden ser accedidos desde cualquier lugar. La mayoría de los sistemas operativos modernos proporcionan soporte para WebDAV, haciendo que los ficheros de un servidor WebDAV aparezcan como almacenados en un directorio local.

**Configuración de un servidor WebDAV**

Para crear un directorio en nuestro servidor Web que pueda ser accesible por medio de un cliente WebDAV debemos activar los módulos **dav** y **dav_fs**.

Lo primero es indicar el nombre de la base de datos de lock que se utilizará, mediante la directiva DAVLockDB. Es importante tener especial cuidado con esta directiva, ya que es frecuente fuente de errores:

    DavLockDB /tmp/DAVLockDB

Lo que indica la directiva no es ni el nombre de un archivo ni el de una carpeta, si no la parte inicial del nombre de un archivo. El módulo creará un archivo de nombre ``DAVLockDB.orig`` y otro de nombre ``DAVLockDB.xxxxx`` dentro de la carpeta indicada, para lo cual es necesario que el usuario *"Apache"* tenga permisos de escritura en ella.

A continuación creamos una sección directory para el directorio que queremos acceder por WebDav y activar el modo WebDav con la directiva ``dav on``. Además por seguridad se debe autentificar el acceso, por lo que quedaría parecido a esto:
    
    DavLockDB /tmp/DavLockDB
    <Directory /var/www/html/webdav>
        dav on
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Require all granted
        AuthType digest
        AuthUserFile "/etc/apache2/digest.txt"
        AuthName "Dominio"
        Require valid-user
    </Directory>

Por último prueba un cliente WebDAV en Linux y otro en Windows y comprueba el funcionamiento.

## Módulo rewrite

Antes de comenzar con el módulo **rewrite** vamos a instalar el módulo que nos permite ejecutar php:

    apt install libapache2-mod-php

El módulo **rewrite** nos va a permitir acceder a una URL e internamente estar accediendo a otra. Ayudado por los ficheros ``.htaccess``, el módulo rewrite nos va a ayudar a formar URL amigables que son más consideradas por los motores de búsquedas y mejor recordadas por los humanos. Por ejemplo estas URL:

	www.dominio.com/articulos/muestra.php?id=23
	www.dominio.com/pueblos/pueblo.php?nombre=torrelodones

Es mucho mejor escribirlas como:

	www.dominio.com/articulos/23.php
	www.dominio.com/pueblos/torrelodones.php

**Ejemplo 1: Reescribir URL**

Si tenemos el siguiente fichero php ([descargar](https://raw.githubusercontent.com/josedom24/serviciosgs_doc/master/web/doc/php.txt)) llamado operacion.php, podríamos usarlo de la siguiente manera:

    http://localhost/operacion.php?op=suma&op1=6&op2=8

Y si queremos reescribir la URL y que usemos en vez de php html, de esta forma:

    http://localhost/operacion.html?op=suma&op1=6&op2=8

Para ello activamos el ``mod_rewite``, y escribimos un ``.htaccess`` de la siguiente manera:

    Options FollowSymLinks
    RewriteEngine On
    RewriteRule ^operacion.html$ operacion.php 


**Ejemplo 2: Cambiar la extensión de los ficheros**

Si queremos usar la extensión do en vez de html podríamos usar este ``.htaccess``:

    Options FollowSymLinks
    RewriteEngine On
    RewriteBase /
    RewriteRule ^(.+).do$ $1.html [nc]

La opción `[nc]` es para que no tenga en cuenta mayúsculas o minúsculas.

Esto puede ser penalizado por los motores de búsqueda ya que podemos acceder a la misma página con dos URL distintas, para solucionar esto podemos hacer una redirección:

    RewriteRule ^(.+).do$ $1.html [r,nc]

**Ejemplo 3: Crear URL amigables**

Como habíamos visto anteriormente el fichero operacion.php se podía ejecutar de la siguiente manera:

    http://localhost/operacion.php?op=suma&op1=6&op2=8

Creando una URL amigable podríamos llamar a este fichero de la siguiente manera:

    http://localhost/suma/8/6

¿Cómo podemos conseguir esto?

Crea un ``.htaccess`` con el siguiente contenido:

    Options FollowSymLinks
    RewriteEngine On
    RewriteBase /
    RewriteRule ^([a-z]+)/([0-9]+)/([0-9]+)$ operacion.php?op=$1&op1=$2&op2=$3

**Ejemplo 4: Acortar URL**

Supongamos que dentro de nuestro *DocumentRoot* tenemos una carpeta búsqueda con un fichero ``buscar.php`` ([descargar](https://raw.githubusercontent.com/josedom24/serviciosgs_doc/master/web/doc/buscar.txt)). Este fichero me permite obtener la página de búsqueda de google con el parámetro dado, de esta forma:

    http://localhost/busqueda/buscar.php?id=hola

Nos gustaría poder crear una URL más corta que haga lo mismo, escribiríamos en nuestro ``.htaccess`` un *RewriteRule* de la siguiente forma:

    RewriteRule ^buscar busqueda/buscar.php

De esta forma accederíamos por medio de la URL:

    http://localhost/buscar?id=hola

¿y si queremos buscar de la siguiente manera: `http://localhost/buscar/hola.html`?

    RewriteRule ^buscar/([a-z]+).html$ busqueda/buscar.php?id=$1

**Ejemplo 5: Uso del RewriteCond**

La directiva ``RewriteCond`` nos permite especificar una condición que si se cumple se ejecuta la directiva ``RewriteRule`` posterior. Se pueden poner varias condiciones con ``RewriteCond``, en este caso cuando se cumplen todas se ejecuta la directiva ``RewriteRule`` posterior.

Como vemos en la documentación podemos preguntar por varios parámetros , entre los que destacamos los siguientes:

* **%{HTTP_USER_AGENT}**: Información del cliente que accede. Por ejemplo, podemos mostrar una página distinta para cada navegador:

    ```bash
    RewriteCond %{HTTP_USER_AGENT} ^Mozilla
    RewriteRule ^/$ /index.max.html [L]
    RewriteCond %{HTTP_USER_AGENT} ^Lynx
    RewriteRule ^/$ /index.min.html [L]
    RewriteRule ^/$ /index.html [L]
    ```

* **%{QUERY_STRING}**: Guarda la cadena de parámetros de una URL dinámica.Por ejemplo:

Teníamos un fichero index.php que recibía un parámetro lang, para traducir el mensaje de bienvenida:

	http://localhost/index.php?lang=es

Actualmente hemos cambiado la forma de traducir, y se han creado distintos directorios para cada idioma y dentro un index.php con el mensaje traducido:

    http://localhost/es/index.php

Sin embargo se quiere seguir utilizando la misma forma de traducir:

    RewriteCond %{QUERY_STRING} lang=(.*)
    RewriteRule ^index.php$ /%1/$1

* **%{REMOTE_ADDR}**: Dirección de destino. Por ejemplo puedo denegar el acceso a una dirección:

    ```bash
    RewriteCond %{REMOTE_ADDR} 145.164.1.8
    RewriteRule ^(.*)$ / [R,NC,L]
    ```

También podemos controlar la reescritura de URL según la hora y la fecha, para saber más lee este [artículo](http://www.askapache.com/htaccess/time_hour-rewritecond-time.html).

* **%{HTTP_REFERER}**: Guarda la URL que accede a nuestra página y %{REQUEST_URI} guarda la URI, URL sin nombre de dominio. Podemos evitar el Hot_Linking, o uso de recursos de tu servidor desde otra web. Por ejemplo, un caso muy común es usar imágenes alojadas en tu servidor puestas en otras web. Para ello podemos escribir el siguiente ``.htaccess``:

    ```bash
    RewriteCond %{HTTP_REFERER} !^$
    RewriteCond %{HTTP_REFERER} !^http://(www\.)?dominio\.com/ [NC]
    RewriteCond %{REQUEST_URI} !hotlink\.(gif|png) [NC]
    RewriteRule .*\.(gif|jpg|png)$ http://www.dominio.com/image/hotlink.png [NC]
    ```

En el anterior ejemplo el primer ``RewriteCond`` permite la solicitud directa pero no desde otras páginas (referrer vacío). La siguiente línea indica que si el navegador ha enviado una cabecera ``Referrer`` y esta no contiene la palabra "dominio.com" se ejecutará el ``RewriteRule``. La ultima instrucción ``RewriteCond`` indica que si en la url solicitada se encuentra el nombre de la imagen "hotlink" no se realizará el ``RewriteRule``; esto se pone porque la imagen hotlink.png va a ser la que vamos a usar en ``RewriteRule`` y si no ponemos este ``RewriteCond`` también sería redirigida la solicitud a esta imagen. La última instrucción del ejemplo es el ``RewriteRule`` que indica que cualquier solicitud a una imagen desde otro referrer será reescrita en el servidor hacia la imagen hotlink.png y esta será la imagen que se vea en la web que te esté intentando robar la imagen.

### Ejercicio

En tu servidor crea una carpeta ``php`` donde vamos a tener un fichero ``index.php`` con el siguiente contenido::

```html

<!DOCTYPE html>
<html lang="es">  
  <head>    
    <title>Conversor de Monedas</title>    
    <meta charset="UTF-8">
  </head>  
  <body>    
	<form action="index.php" method="get">
	   	<input type="text" size="30" name="monto" /><br/>
		<select name="pais">
			<option name="Dolar">Dolar</option>
			<option name="Libra">Libra</option>
			<option name="Yen">Yen</option>
		</select>
	    <input type="submit" value="convertir" />
	   </form>
	<?php
		// averiguamos si se ha introducido un dinero
		if (isset($_GET['monto'])) {
		  define ("cantidad", $_GET['monto']);
		} else {
	 	  define ("cantidad", 0);
		}
		if($_GET){
		// definimos los países
		$tasacambios = array ("Libra"=>0.86,"Dolar"=>1.34,"Yen"=>103.56);
		// imprimimos el monto ingresado
		echo "<b>".cantidad." euros</b><br/> ".$_GET["pais"]." = ".cantidad*$tasacambios[$_GET["pais"]];
		}
	   ?>
	</body>
	</html>
```

Prueba la página utilizando parámetros en la URL (parámetros GET), por ejemplo: ``http://nombre_página/php/index.php?monto=100&pais=Libra``

Configura mediante un fichero ``.htaccess``, la posibilidad de acceder a la URL **http://nombre_página/php/moneda/cantidad**, donde moneda indica el nombre de la moneda a la que queremos convertir (Dolar,Libra,Yen) y cantidad indica los euros que queremos convertir.
{% capture notice-text %}
1. Entrega la regla de reescritura que has configurado.
2. Pantallazo donde se vea el acceso a la URL **http://nombre_página/php/moneda/cantidad**.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
