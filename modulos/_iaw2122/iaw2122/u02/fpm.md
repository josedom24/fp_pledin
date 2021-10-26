---
title: "Ejecución de PHP con PHP-FPM"
---

FPM (FastCGI Process Manager) es una implementación alternativa al PHP FastCGI. FPM es un servidor de aplicaciones PHP que se encarga de interpretar código PHP. Aunque normalmente se utiliza junto a un servidor web (Apache2 o ngnix) vamos a hacer en primer lugar una instalación del proceso y vamos a estudiar algunos parámetros de configuración y estudiar su funcionamiento.

Para instalarlo en Debian 11:

	apt install php7.4-fpm php7.4

## Configuración

Con esto hemos instalado php 7.4 y php-fpm. Veamos primeros algunos ficheros de configuración de php:

Si nos fijamos en la configuración de php para php-fpm:

* `/etc/php/7.4/fpm/conf.d`: Módulos instalados en esta configuración de php (enlaces simbólicos a `/etc/php/7.4/mods-available`).
* `/etc/php/7.4/fpm/php-fpm.conf`: Configuración general de php-fpm.
* `/etc/php/7.4/fpm/php.ini`: Configuración de php para este escenario.
* `/etc/php/7.4/fpm/pool.d`: Directorio con distintos pool de configuración. Cada aplicación puede tener una configuración distinta (procesos distintos) de php-fpm.

Por defecto tenemos un pool cuya configuración la encontramos en `/etc/php/7.4/fpm/pool.d/www.conf`, en este fichero podemos configurar muchos parámetros, los más importantes son:

* `[www]`: Es el nombre del pool, si tenemos varios, cada uno tiene que tener un nombre.
* `user` y `grorup`: Usuario y grupo con el que se va ejecutar los procesos.
* `listen`: Se indica el socket unix o el socket TCP donde van a escuchar los procesos:
	* Por defecto, escucha por un socket unix:
		`listen = /run/php/php7.4-fpm.sock`
	* Si queremos que escuche por un socket TCP:
		`listen = 127.0.0.1:9000`
	* En el caso en que queramos que escuche en cualquier dirección:
		`listen = 9000`

* Directivas de procesamiento, gestión de procesos: 
	* `pm`: Por defecto igual a `dynamic` (el número de procesos se crean y destruyen de forma dinámica). Otros valores: `static` o `ondemand`.
	* Otras directivas: `pm.max_children`, `pm.start_servers`, `pm.min_spare_servers`,...

* `pm.status_path = /status`: No es necesaria, pero vamos a activar la URL de `status` para comprobar el estado del proceso.

Por último reiniciamos el servicio:

	systemctl restart php7.4-fpm


## Configuración de Apache2 con PHP-FPM

Apache2 va a funcionar como proxy inverso para la peticiones de los recursos php. Cuando solicitamos un fichero php, apache2 le pasará la petición a php-fpm para que interprete php y luego devuelva la respuesta al servidor web. Necesito activar los siguientes módulos:

	a2enmod proxy_fcgi setenvif


### Activarlo para cada virtualhost

Podemos hacerlo de dos maneras:

* Si php-fpm está escuchando en un socket TCP:

		ProxyPassMatch ^/(.*\.php)$ fcgi://127.0.0.1:9000/var/www/html/$1

* Si php-fpm está escuchando en un socket UNIX:

		ProxyPassMatch ^/(.*\.php)$ unix:/run/php/php7.4-fpm.sock|fcgi://127.0.0.1/var/www/html

Otra forma de hacerlo es la siguiente:

* Si php-fpm está escuchando en un socket TCP:

		<FilesMatch "\.php$">
	    	SetHandler "proxy:fcgi://127.0.0.1:9000"
		</FilesMatch>

* Si php-fpm está escuchando en un socket UNIX:

		<FilesMatch "\.php$">
   	    	SetHandler "proxy:unix:/run/php/php7.4-fpm.sock|fcgi://127.0.0.1/"
		</FilesMatch>

### Activarlo para todos los virtualhost

Tenemos a nuestra disposición un fichero de configuración `php7.4-fpm` en el directorio `/etc/apache2/conf-available`. Por defecto funciona cuando php-fpm está escuchando en un socket UNIX, si escucha por un socket TCP, hay que cambiar la línea:

	SetHandler "proxy:unix:/run/php/php7.4-fpm.sock|fcgi://localhost"

por esta:

	SetHandler "proxy:fcgi://127.0.0.1:9000"

Por último activamos la configuración:

	a2enconf php7.4-fpm

