---
title: "Taller 3: Instalación de WordPress en un servidor LEMP"
---

## ¿Qué vas a aprender en este taller?

* Realizar la instalación de un servidor LEMP.
* Configurar nginx como proxy inverso para pasar las peticiones PHP al servidor de aplicación `fpm-php.`
* Realizar la instalación de un CMS PHP WordPress.

## Recursos para realizar este taller

### Configuración de Nginx con php-fpm

Para ejecutar en un virtualhost nginx el proxy inverso para fpm_php:

En el virtualhost descomentamos las siguientes líneas:

	location ~ \.php$ {
        include snippets/fastcgi-php.conf;

        # With php-fpm (or other unix sockets):
        #fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
        # With php-cgi (or other tcp sockets):
        #fastcgi_pass 127.0.0.1:9000;
    }

Descomentando la opción que nos interese: si php-fpm está en un socket Unix o en un socket TCP.

### Instalación de WordPress en LAMP

* [Vídeo: Como instalar Wordpress en un entorno LAMP](https://www.youtube.com/watch?v=muAKPiPqW6g)


## ¿Qué tienes que hacer?

1. Este taller lo vamos a hacer en una máquina virtual con un servidor LEMP instalado.
2. Crea una base de datos y un usuario con todos los privilegios para esa base de datos.
3. Configura un virtualhost donde vamos a realizar la instalación.
4. Descarga en el DocumentRoot la última versión de WordPress.
5. Accede a la URL de instalación.
6. Configura de forma adecuada: las credenciales para acceder a la base de datos, los módulos PHP que te hagan falta, la configuración de WordPress,...
7. Accede a la zona de administración de WordPress y escribe una entrada en el blog.
8. Intenta configurar WordPress para usar URL amigables. Recuerda que nginx no lee la configuración de apache2 en los ficheros `.htaccess`.

Te puede servir la configuración que encuentras en la página [WordPress de nginx](https://www.nginx.com/resources/wiki/start/topics/recipes/wordpress/).

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Pantallazo donde se vea la salida del fichero `info.php` donde se ve que la ejecución de PHP se hace con nginx + PHP-FPM.
2. Pantallazo accediendo a WordPress para comprobar que has escrito una entrada del blog.
3. Se valorará positivamente el uso de URL amigables.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
