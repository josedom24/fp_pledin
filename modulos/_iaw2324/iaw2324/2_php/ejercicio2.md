---
title: "Ejercicio 2: VirtualHosting con Apache"
---

## ¿Qué vas a aprender en este ejercicio?

* Crear distintos *Host Virtuales* en apache2 que nos permiten tener sitios web diferenciados.
* Acceder a cada *Host Virtual* con un determinado nombre de dominio.

## Recursos para realizar este ejercicio

### Introducción al VirtualHosting

El término *Hosting Virtual* se refiere a hacer funcionar más de un sitio web (tales como `www.company1.com` y `www.company2.com`) en una sola máquina. Los sitios web virtuales pueden estar "basados en direcciones IP", lo que significa que cada sitio web tiene una dirección IP diferente, o **"basados en nombres diferentes"**, lo que significa que con una sola dirección IP están funcionando sitios web con diferentes nombres de dominio (estos últimos son los que vamos a trabajar en este taller). 

El servidor web Apache2 se instala por defecto con un host virtual. La configuración de este sitio la podemos encontrar en:

    /etc/apache2/sites-available/000-default.conf

Cuyo contenido podemos ver:

	<VirtualHost *:80>
	        #ServerName www.example.com	
	        ServerAdmin webmaster@localhost
	        DocumentRoot /var/www/html	
	        ErrorLog ${APACHE_LOG_DIR}/error.log
	        CustomLog ${APACHE_LOG_DIR}/access.log combined	
	</VirtualHost>

Donde encontramos los siguientes parámetros:

* [ServerName](https://httpd.apache.org/docs/2.4/mod/core.html#servername): El nombre con el que vamos a acceder al sitio virtual. En el sitio virtual por defecto (como sólo tenemos uno) está comentado, podemos acceder por nombre o por dirección IP.
* [ServerAdmin](https://httpd.apache.org/docs/2.4/mod/core.html#serveradmin): Dirección de correo del administrador responsable del servidor.
* [DocumentRoot](https://httpd.apache.org/docs/2.4/mod/core.html#documentroot): Directorio donde guardamos los ficheros que se van a servir.
* [ErrorLog](https://httpd.apache.org/docs/2.4/mod/core.html#errorlog): Fichero de errores del host virtual.
* [CustomLog](http://httpd.apache.org/docs/current/mod/mod_log_config.html#customlog): Fichero de accesos al host virtual.

Por defecto este sitio virtual está habilitado, por lo que podemos comprobar que existe un enlace simbólico a este fichero en el directorio `/etc/apache2/sites-enabled`:

    lrwxrwxrwx 1 root root   35 Oct  3 15:24 000-default.conf -> ../sites-available/000-default.conf

Podemos habilitar o deshabilitar nuestros host virtuales utilizando los siguientes comandos:

	a2ensite
	a2dissite

En el fichero de configuración general `/etc/apache2/apache2.conf` nos encontramos las opciones de configuración del directorio padre del indicado en la directiva `DocumentRoot` (suponemos que todos los host virtuales van a estar guardados en subdirectorios de este directorio):

	...
	<Directory /var/www/>
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>
	...


## ¿Qué tienes que hacer?

Queremos construir en nuestro servidor web apache dos sitios web con las siguientes características:

* El nombre de dominio del primero será `www.iesgn.org`, su directorio base será `/var/www/iesgn` y contendrá una página llamada `index.html`, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será `www.departamentosgn.org`, y su directorio base será `/var/www/departamentos`. En este sitio sólo tendremos una página inicial `index.html`, dando la bienvenida a la página de los departamentos del instituto.

Para conseguir estos dos sitios virtuales debes seguir los siguientes pasos:

1. Los ficheros de configuración de los sitios webs se encuentran en el directorio `/etc/apache2/sites-available`, por defecto hay dos ficheros, uno se llama `000-default.conf` que es la configuración del sitio web por defecto. Necesitamos tener dos ficheros para realizar la configuración de los dos sitios virtuales, para ello vamos a copiar el fichero `000-default.conf`:

		cd /etc/apache2/sites-available
		cp 000-default.conf iesgn.conf
		cp 000-default.conf departamentos.conf

	De esta manera tendremos un fichero llamado `iesgn.conf` para realizar la configuración del sitio web `www.iesgn.org`, y otro llamado `departamentos.conf` para el sitio web `www.departamentosgn.org`.

2. Modificamos los ficheros `iesgn.conf` y `departamentos.conf`, para indicar el nombre que vamos a usar para acceder al host virtual (`ServerName`) y el directorio de trabajo (`DocumentRoot`). Además vamos cambiar los nombre del fichero log de acceso y de error.
3. No es suficiente crear los ficheros de configuración de cada sitio web, es necesario crear un enlace simbólico a estos ficheros dentro del directorio `/etc/apache2/sites-enabled`, para ello:

        a2ensite iesgn
        a2ensite departamentos

	La creación de los enlaces simbólicos se puede hacer con la instrucción `a2ensite nombre_fichero_configuracion`, para deshabilitar el sitio tenemos que borrar el enlace simbólico o usar la instrucción `a2dissite nombre_fichero_configuracion`.

4. Crea los directorios y los ficheros `index.html` necesarios en `/var/www` y reiniciamos el servicio. Recuerda que los directorios y los ficheros deben pertenecer al usuario `www-data:www-data`.

5. Para terminar lo único que tendremos que hacer es cambiar el fichero hosts (**resolución estática**) en los clientes y poner dos nuevas líneas donde se haga la conversión entre los dos nombre de dominio y la dirección IP del servidor.




