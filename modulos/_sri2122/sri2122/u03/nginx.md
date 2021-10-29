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

Para activar un nuevo sitio tenemos que crear el enlace directo en el directorio `/etc/nginx/sites-enabled/`:

	ln -s /etc/nginx/sites-available/test.com /etc/nginx/sites-enabled/

En el fichero `/etc/nginx/sites-availables/default` nos encontramos la directiva:

	listen 80 default_server;

`default_server;` nos permite indicar el sitio virtual por defecto.

## Migrando configuración de Apache2 a nginx

Ejemplo de configuración básdica de un sitio virtual en apache2:

	<VirtualHost *:80>
		ServerName www.example.com
		ServerAdmin webmaster@localhost
		DocumentRoot /var/www/html

        Alias /prueba/ /var/www/html/prueba
	    <Directory /var/www/html/prueba>
	        Options Indexes FollowSymLinks MultiViews
	        AllowOverride None
	        Require all granted
	    </Directory>

	    Alias /doc/ "/usr/share/doc/"
    	<Directory "/usr/share/doc/">
    	    Options Indexes MultiViews FollowSymLinks
    	    AllowOverride None
    	    require ip 127.0.0.0/255.0.0.0 ::1/128
    	</Directory>

		ErrorLog ${APACHE_LOG_DIR}/error.log
		CustomLog ${APACHE_LOG_DIR}/access.log combined

	</VirtualHost>

Si traducimos la misma configuración en un servidor nginx:

	server {
	    listen 80;

	    root /var/www/html;
	    index index.html index.htm;

	    server_name www.example.com;

	    location / {
	        try_files $uri $uri/ /index.html;
	    }

		location /prueba/ {
	        alias /var/www/html/prueba;
	        autoindex on;
	        allow all;
	    }

	    location /doc/ {
	        alias /usr/share/doc/;
	        autoindex on;
	        allow 127.0.0.1;
	        deny all;
	    }
	}

Podríamos resumir las correspondencias en el siguiente cuadro:

|Apache                                     |
|-------------------------------------------|
|`<VirtualHost *:80>`<br/>                  |   
|ServerName yoursite.com<br/>	      	    |
|DocumentRoot /path/to/root <br/>           |
|AllowOverride All  <br/>                   |
|DirectoryIndex index.php<br/>              |
|ErrorLog /path/to/log        <br/>         |
|CustomLog /path/to/log combined <br/>      |
|Alias /url/ "/path/to/files"               |
|<Directory "/path/to/files">  <br/>        |
|Options Indexes      <br/>                 |
|Require all granted  <br/>                 |
|allow 127.0.0.1        <br/>               |
|deny all               <br/>               |
|proxy_pass / http://localhost:8080         |
|proxy_pass_reverse / http://localhost:8080 |


Nginx                           
--------------------------------
server {
     listen 80;
   server_name www.yoursite.com;
root /path/to/root;
(No Available Alternative)
index index.php;
error_log /path/to/log error;
access_log /path/to/log main;
location /url/ {
      alias /path/to/files;
autoindex on
allow all
allow 127.0.0.1;
deny all;
|proxy_pass / http://localhost:8080 
|