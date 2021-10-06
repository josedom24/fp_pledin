---
title: "Instalación y configuración básica de Apache"
---

## Instalación de Apache 2.4


1. Instala el servidor web Apache:

		apt-get install apache2

	Para controlar el servicio apache2 podemos usar (para más [información](http://httpd.apache.org/docs/2.4/es/stopping.html)):

		apache2ctl [-k start|restart|graceful|graceful-stop|stop]

2. ¿Qué es la opción graceful?

3. Comprueba la directiva donde indicamos el puerto de escucha del servidor. Modifica el puerto de escucha para que sea el 8080. Comprueba el acceso al servidor desde un navegador.

## Estructura de los ficheros de configuración

El fichero principal de configuración de Apache2 es `/etc/apache2/apache2.conf`. En ese fichero se incluyen los ficheros que forman parte de la configuración de Apache2:

	...
	IncludeOptional mods-enabled/*.load
	IncludeOptional mods-enabled/*.conf
	...
	Include ports.conf
	...
	IncludeOptional conf-enabled/*.conf
	IncludeOptional sites-enabled/*.conf

Por defecto se indican las opciones de configuración del directorio `/var/www` y de todos sus subdirectorios, por lo tanto los `DocumentRoot` de los virtualhost que se crean deben ser subdirectorios del este directorio:

	<Directory /var/www/>
	    Options Indexes FollowSymLinks
	    AllowOverride None
	    Require all granted
	</Directory>

Podemos indicar como directorio raíz de nuestros virtualhost otro directorio (tenemos que descomentar):

	#<Directory /srv/>
	#    Options Indexes FollowSymLinks
	#    AllowOverride None
	#    Require all granted
	#</Directory>


## Algunas directivas

* [IfDefine](http://httpd.apache.org/docs/2.4/mod/core.html#ifdefine).Las directivas de configuración de apache2 se pueden aplicar si está definido un determinado parámetro
* [IfModule](http://httpd.apache.org/docs/2.4/mod/core.html#ifmodule). Podemos aplicar determinadas directivas si hay cargado un determinado módulo.
* [LoadModule](http://httpd.apache.org/docs/2.4/mod/mod_so.html#loadmodule): Nos permite cargar dinámicamente los módulos.
* [Include](http://httpd.apache.org/docs/2.4/mod/core.html#include) nos permite añadir ficheros de configuración a la configuración general de apache2. 

Podemos aplicar directivas a partes concretas de nuestro servidor web, para ello estudia las siguientes directivas (Para aprender más lee [Secciones de Configuración](http://httpd.apache.org/docs/2.4/sections.html)):

* [Directory](http://httpd.apache.org/docs/2.4/mod/core.html#directory)
* [DirectoryMatch](http://httpd.apache.org/docs/2.4/mod/core.html#directorymatch)
* [Files](http://httpd.apache.org/docs/2.4/mod/core.html#files)
* [FilesMatch](http://httpd.apache.org/docs/2.4/mod/core.html#filesmatch)
* [Location](http://httpd.apache.org/docs/2.4/mod/core.html#location)
* [LocationMatch](http://httpd.apache.org/docs/2.4/mod/core.html#locationmatch)
* [VirtualHost](http://httpd.apache.org/docs/2.4/mod/core.html#virtualhost)

Directivas de identificación del servidor:

* [ServerName](http://httpd.apache.org/docs/2.4/mod/core.html#servername)
* [ServerAdmin](http://httpd.apache.org/docs/2.4/mod/core.html#serveradmin)
* [ServerTokens](http://httpd.apache.org/docs/2.4/mod/core.html#usecanonicalname)

Directivas de localización de ficheros

* [DocumentRoot](http://httpd.apache.org/docs/2.4/mod/core.html#documentroot)
* [ErrorLog](http://httpd.apache.org/docs/2.4/mod/core.html#errorlog)
* [CustomLog](http://httpd.apache.org/docs/2.4/mod/mod_log_config.html#customlog)
* [LockFile](http://httpd.apache.org/docs/2.4/mod/mpm_common.html#lockfile)
* [PidFile](http://httpd.apache.org/docs/2.4/mod/mpm_common.html#pidfile)
* [ServerRoot](http://httpd.apache.org/docs/2.4/mod/core.html#serverroot)
* [AccessFileName](http://httpd.apache.org/docs/2.4/mod/core.html#accessfilename)

Directivas de control de la conexión

* [Timeout](http://httpd.apache.org/docs/2.4/mod/core.html#timeout)
* [KeepAlive](http://httpd.apache.org/docs/2.4/mod/core.html#keepalive) ([Más información](http://systemadmin.es/2011/08/conexiones-con-keepalive-en-http1-0))
* [MaxKeepAliveRequests](http://httpd.apache.org/docs/2.4/mod/core.html#maxkeepaliverequests)
* [KeepAliveTimeout](http://httpd.apache.org/docs/2.4/mod/core.html#keepalivetimeout)

Otras directivas

* [User](http://httpd.apache.org/docs/2.4/mod/mpm_common.html#user)
* [Group](http://httpd.apache.org/docs/2.4/mod/mpm_common.html#group)
* [DefaultType](http://httpd.apache.org/docs/2.4/mod/core.html#defaulttype)
* [LogLevel](http://httpd.apache.org/docs/2.4/mod/core.html#loglevel)
* [LogFormat](http://httpd.apache.org/docs/2.4/mod/mod_log_config.html#logformat)


## Subir una página web al virtualhost default

Para terminar sube alguna pagina web al servidor web, tienes que copiar los ficheros al directorio DocumentRoot `/var/www/html`. Los ficheros que hemos subido al servidor deben tener como usuario propietario `www-data:www-data`, que es el usuario del sistema que usa el servidor web para acceder al DocumentRoot.

Desde otro ordenador accede al servidor web usando la dirección IP. Si queremos usar un nombre para acceder a la página, tenemos que tener un sistema para convertir el nombre en dirección ip.  Como no tenemos servidor DNS vamos a usar la **resolucion estática**.

Para usar la resolución estática, modificamos el fichero `/etc/hosts` del ordenador desde el que vamos acceder a la página, de la siguiente forma:

```
<direccion_ip_servidor_web>      <nombre_con_el_que_accedemos>
```

Por ejemplo:

```
192.168.121.10      www.example.org
```

Cambia la resolución estática y accede desde el cliente con una nombre a la misma página.

El virtualhost default tiene dos ficheros de logs importantes:

* El fichero de logs de acceso: `/var/log/apache/access.log`. Donde se registra los accesos al servidor desde los clientes.
* El fichero de logs de errores: `/var/log/apache/error.log`.

Comprueba el contenido de estos dos ficheros.