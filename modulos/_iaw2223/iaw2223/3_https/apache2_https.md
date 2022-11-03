---
title: Configuración de HTTPS en Apache2
---

Vamos a configurar el acceso con el protocolo HTTPS a `prueba.josedomingo.org`.

Suponemos que ya hemos solicitado el certificado a Let's Encrypt y lo tenemos guardado en los siguientes ficheros:

* El certificado: `/etc/letsencrypt/live/prueba.josedomingo.org/fullchain.pem`
* La clave privada: `/etc/letsencrypt/live/prueba.josedomingo.org/privkey.pem`

Lo primero que tenemos que hacer es activar el módulo SSL:

	# a2enmod ssl

A continuación vamos a crear un virtual host para nuestro FQDN a partir del fichero por defecto para la configuración de HTTPS, en el directorio `/etc/apache2/sites-available`, ejecutamos:

	# cp default-ssl.conf prueba-ssl.conf

Y lo configuramos de forma adecuada:

	...
	ServerName prueba.josedomingo.org
    DocumentRoot /var/www/prueba
    ...
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/prueba.josedomingo.org/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/prueba.josedomingo.org/privkey.pem
    ...

Con la directiva [`SSLEngine`](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslengine) activamos el uso de HTTPS, [`SSLCertificateFile`](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslcertificatefile) nos permite indicar el certificado emitido por la CA y con [`SSLCertificateKeyFile`](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslcertificatekeyfile) indicamos nuestra clave privada.

**Nota: Toda la configuración especifica que tenía el virtualhost HTTP lo tendremos que poner el virtualhost HTTPS.**

Finalmente activamos el sitio:

	# a2ensite prueba-ssl.conf

## Redirigiendo el trafico HTTP a HTTPS

Podemos hacer una redirección para que cuando accedamos con HTTP se solicite el recurso utilizando HTTPS. Para ello en el fichero de configuración del virtual host `/etc/apache2/sites-available/prueba.conf` podemos incluir un `redirect`:

	...
	redirect premanent / https://prueba.josedomingo.org
	...

Si tenemos activo el módulo `rewrite` también podemos hacer la redirección con la siguiente configuración:

	...
	RewriteEngine On
	RewriteCond %{HTTPS} !on
	RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}
	...



	
