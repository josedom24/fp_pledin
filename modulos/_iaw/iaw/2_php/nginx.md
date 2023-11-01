---
title: "Introducción al servidor web nginx"
---

## Instalación de nginx

	apt-get update
	apt-get install nginx

## Introducción a virtual hosting con nginx

Podemos encontrar los sitios disponibles y activos del servidor nginx, siguiendo la filosofía de Apache2 en los directorios:

	/etc/nginx/sites-availables/
	/etc/nginx/sites-enabled/

Por ejemplo podemos crear un nuevo Virtual Host haciendo una copiar del sitio virtual `default`:

	cd /etc/nginx/sites-availables/
	cp default pagina1

Ahora en el fichero `pagina1` configuro el nuevo sitio virtual, teniendo en cuenta los siguientes parámetros:

* `server_name`: El nombre con el que vamos a acceder al sitio virtual. 
* `root`: Directorio donde guardamos los ficheros que se van a servir.
* `index`: Lista con los nombres de los ficheros que va a intentar servir si no se indica ninguno en la URL.
* En `listen 80;` y en `listen [::]:80`: Se indica el puerto y las direcciones desde donde se esperan peticiones. En el sitio virtual `default` tiene configurado la directiva `default_server` nos permite indicar que es el sitio virtual por defecto. **Esta directiva hay que quitarla en los nuevos sitios virtuales**.
* En el fichero `/etc/nginx/nginx.conf` nos encontramos las directivas `error_log` y `access_log`, para indicar el fichero de log de errores y de accesos respectivamente. Si queremos podemos indicar un fichero diferencia en cada sitio virtual indicando estas directivas.


Para activar un nuevo sitio tenemos que crear el enlace directo en el directorio `/etc/nginx/sites-enabled/`:

	ln -s /etc/nginx/sites-available/pagina1 /etc/nginx/sites-enabled/

## .htaccess en nginx

El fichero `.htaccess` en apache2 permite introducir configuración de apache2 en el DocumentRoot del sitio virtual, de esta manera un usuario final puede hacer configuraciones de apache2 sin intervención del administrador. Controlamos la utilización de estos ficheros con la directiva `AllowOverride`.

**En nginx no podemos hacer uso de los ficheros `.htaccess` de apache2.**

En determinadas ocasiones podemos necesitar convertir la configuración de apache2 que existe en un fichero `.htaccess` a configuración de nginx, para ello podemos hacer uso de algunas páginas web que nos hacen la conversión:

* [htaccess to nginx converter](https://winginx.com/en/htaccess)
* [Apache .htaccess to NGINX converter](https://www.getpagespeed.com/apache-to-nginx)

## Ejecución de php con nginx

En nginx no existe un módulo propio que permita la ejecución del lenguaje PHP. Por lo que tenemos que utilizar un servidor de aplicaciones php como **php-fpm**.

Para ejecutar en un virtualhost nginx el proxy inverso para fpm_php:

En el virtualhost descomentamos las siguientes líneas:

	location ~ \.php$ {
        include snippets/fastcgi-php.conf;

        # With php-fpm (or other unix sockets):
        #fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
        # With php-cgi (or other tcp sockets):
        #fastcgi_pass 127.0.0.1:9000;
    }

Descomentando la opción que nos interese: 

* Si php-fpm está en un socket Unix, descomentamos la línea `fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;`.
* Si php-fpm escucha en un socket TCP, descomentamos la línea: `fastcgi_pass 127.0.0.1:9000;`

