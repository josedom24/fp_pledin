---
title: "Configuración básica de Apache2"
---

## Mapear URL a ubicaciones de un sistema de ficheros

* **Alias**: La directiva [Alias](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#alias) nos permite que el servidor sirva ficheros desde cualquier ubicación del sistema de archivo aunque esté fuera del directorio indicado en el *DocumentRoot*. Ejemplo:

```
Alias "/image" "/ftp/pub/image"
<Directory "/ftp/pub/image">
    Require all granted
</Directory>
```

Cuando accedamos a la ruta `image` se estarán sirviendo los ficheros que se encuentran en `/ftp/pub/image`. como este directorio no tiene los permisos de apache2 definidos tenemos que definirlos con una directiva `Directory`. 

* **Opciones de directorio**: Todos los directorios servidos por el servidor web tienen definida una serie de opciones. Para ello usamos la directiva [Options](http://httpd.apache.org/docs/2.4/mod/core.html#options). Veamos las opciones que tiene el directorio `/var/www` defindio en el fichero `/etc/apache2/apache2.conf` (recuerda que la directiva `Directory` afecta al directorio indicado y a todos sus subdirectorios):

	```
	<Directory /var/www/>
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>
	```
	
	* `Indexes`: Si no existe un fichero con un nombre por defecto (`index.html`, `index.php`,...) muestra la lista de ficheros y directorios que hay en el *DocumentRoot*.
	* `FollowSymLinks`: El servidor web servirá el contenido de un fichero o directorio apuntado por un enlace simbólico que este en el *DocuemntRoot*.

	Existen más opciones que no vamos a estudiar en este curso. Si defino una sección `Directory` para un subdirectorio podremos quitar opciones usando el signo `-` y añadirle usando el símbolo `+`.

* **Redirecciones**: La directiva [Redirect](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirect) nos permite crear redirecciones temporales o permanentes. La directiva `redirect` es usada para pedir al cliente que haga otra petición a una URL diferente. Normalmente la usamos cuando el recurso al que queremos acceder **ha cambiado de localización**.

	Ejemplos de redirección temporal (302):

	```
	Redirect "/service" "http://www.pagina.com/service"
	Redirect "/one" "/two"
	```

	Ejemplos de redirecciones permanentes (301):

	```
	Redirect permanent "/one" "http://www.pagina2.com/two"
	Redirect 301 "/otro" "/otra"
	```

	También se puede usar la directiva `RedirectMatch` para trabajar con expresiones regulares:

	```
	RedirectMatch "(.*)\.gif$" "http://www.pagina2.org/$1.jpg"
	```

## Control de acceso, autentificación y autorización



