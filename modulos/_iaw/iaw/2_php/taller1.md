---
title: "Taller 1: Instalación de la aplicación Biblioteca"
---

## ¿Qué vas a aprender en este taller?

* A desplegar una aplicación PHP construida a medida en nuestro servidor LAMP.

## Recursos para realizar este taller

Como ya sabemos tenemos 3 maneras principales para ejecutar código PHP:

* Desde la línea de comandos (**cli**).
* Con el servidor web **Apache2** y el módulo **libapache2-mod-php**. 
* Con un servidor web y el servidor de aplicaciones **fpm-php**. 

La configuración de php está dividida según desde donde se use:

* `/etc/php/8.2/cli`: Configuración de php para `php8.2-cli`, cuando se utiliza php desde la línea de comandos.
* `/etc/php/8.2/apache2`: Configuración de php para apache2 cuando utiliza el módulo.
* `/etc/php/8.2/fpm`: Configuración de php para php-fpm.
* `/etc/php/8.2/mods-available`: Módulos disponibles de php que puedes estar configurados en cualquiera de los escenarios anteriores.

Si nos fijamos en la configuración de php para apache2 con el módulo:

* `/etc/php/8.2/apache2/conf.d`: Módulos instalados en esta configuración de php (enlaces simbólicos a `/etc/php/8.2/mods-available`).
* `/etc/php/8.2/apache2/php.ini`: Configuración de php para este escenario.


## ¿Qué tienes que hacer?

Vamos a instalar la aplicación Biblioteca, una aplicación web a medida para llevar el control de los prestamos en una biblioteca. Puedes encontrar la aplicación en [Sistema-de-biblioteca-basico-php-8-y-mysql](https://github.com/VidaInformatico/Sistema-de-biblioteca-basico-php-8-y-mysql).

Para realizar la instalación sigue los siguientes pasos:

1. Crea una base datos. Utilizando el esquema de tablas que encuentras en el fichero `biblioteca.sql` para crear las tablas. Crea un usuario que tenga privilegios sobre dicha base de datos.
2. Crea un virtualhost con el que accederás con el nombre `biblioteca.tunombre.org`. Copia en el *DocumentRoot* los ficheros de la aplicación (podrías clonar el repositorio en el *DocumentRoot*). Como el nombre del directorio es muy grande puedes cambiar su nombre, por ejemplo le puedes poner `biblio`.
3. Vamos a configurar el acceso a la base de datos desde la aplicación, para ello cambia el fichero `Config/Config.php` indicando la URL con la que vas a acceder a la aplicación, el usuario de acceso (el que has creado en el punto 1), su contraseña, la base de datos que has creado y la dirección donde se encuentra la base de datos, que en este caso es `localhost`.
4. El módulo **rewrite** de apache2 nos va a permitir acceder a una URL e internamente estar accediendo a otra. En esta aplicación lo tenemos que activar para ello, ejecutamos `a2enmod rewritte` y reinicia el servidor.
5. La configuración del módulo rewrite está realizada en el fichero de configuración apache2 `.htaccess`. Tenemos que permitir al servidor web leer este fichero, para ello modifica la directiva `AllowOverride` con el valor `All` en el fichero `/etc/apache2/apache2.conf` en la configuración del directorio `/var/www`, quedaría de la siguiente forma:
	```
	...
	<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
	</Directory>
	```
6. Accede a la aplicación web usando la URL configurada en el virtualhost (usa el usuario `admin` y contraseña `admin`).
7. Para esta aplicación no es necesario, pero en determinadas aplicaciones es posible que necesitemos cambiar la memoria RAM que puede utilizar. Cambia la memoria máxima de uso de un script PHP (parámetro `memory_limit`) a 256Mb. ¿En qué fichero lo tienes que cambiar?.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega la configuración del virtualhost.
2. Entrega el contenido del fichero `Config.php`.
3. Entrega una captura con el acceso a la aplicación, después del login.
4. Indica el fichero que has modificado (con el path completo) para modificar el límite de memoria. Muestra un pantallazo de la salida del fichero `info.php` donde se vea el cambio.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
