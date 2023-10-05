---
title: "Ejercicio 1:Instalación de un servidor LAMP"
---

## ¿Qué vas a aprender en este ejercicio?

* A instalar un servidor LAMP que nos permita el despliegue de aplicaciones PHP.

## ¿Qué tienes que hacer?

Realiza esta tarea en una máquina virtual.

El acrónimo *LAMP* se refiere a un entorno configurado en un servidor que nos posibilita servir aplicaciones web escritas en PHP.

El entorno que vamos a configurar se consigue mediante la unión de las siguientes tecnologías:

* **L**inux, el sistema operativo;
* **A**pache, el servidor web;
* **M**ySQL, **M**ariaDB, el gestor de bases de datos;
* **P**HP el lenguajes de programación.

Ahora vamos a instalar los paquetes necesarios para tener un entorno LAMP en su sistema operativo GNU/Linux Debian 12.

1. Realiza la instalación del servidor de base de datos:

		apt install mariadb-server

	Por defecto el usuario `root` no tiene contraseña, para acceder necesitaremos hacer con el root del sistema. Es muy recomendable ejecutar el programa `mariadb-secure-installation` para configurar la base de datos de manera segura, por ejemplo para indicar una contraseña al root.

	Si necesitas crear una base de datos y un usuario que tenga acceso a la misma:

		mysql -u root -p
		CREATE DATABASE newdb;
		CREATE USER 'username'@'localhost' IDENTIFIED BY 'userpassword';
		GRANT ALL PRIVILEGES ON newdb.* to 'username'@'localhost';
		FLUSH PRIVILEGES;
		quit
2. Instalación de Apache y PHP. A continuación instalamos el interprete de PHP (en Debian 12 la versión es la 8.2). Al menos instalamos la librerías de PHP necesarias para conectar los programas PHP con la base de datos (dependiendo de la aplicación que instalemos necesitaremos instalar las librerías PHP necesarias).

	También instalamos el servidor web. Además vamos a instalar el módulo que permite que apache2 interprete PHP (es decir, apache2 hará el papel de servidor web y de servidor de aplicaciones).

		apt install apache2 libapache2-mod-php php php-mysql

	* `apache2`: Servidor web apache2.
	* `libapache2-mod-php`: Módulo de apache2 que le permite ejecutar el código PHP. Es decir, apache2 será servidor web y servidor de aplicaciones PHP.
	* `php`: Es un metqpaquete que apunta al paquete de Debian 12, en este caso apunta al paquete `php8.2`.
	* `php-mysql`: Librería PHP que posibilita el acceso a la base de datos.

3. Para comprobar si el servidor LAMP está funcionando, puedes crear un fichero `info.php` en el DocumentRoot (el directorio `/var/www/html`) con el siguiente contenido:

		<?php phpinfo(); ?>

	Recuerda que los ficheros que sirve el servidor web deben tener como propietario el usuario `www-data:www-data`.

4. Para acceder a la página podríamos usar la dirección IP del servidor. Sin embargo vamos a usar un nombre. Si queremos usar un nombre para acceder a la página, tenemos que tener un sistema para convertir el nombre en dirección IP. Como no tenemos servidor DNS vamos a usar la **resolución estática**.

	Para usar la **resolución estática**, modificamos el fichero `/etc/hosts` del ordenador desde el que vamos acceder a la página, de la siguiente forma:

		<direccion_ip_servidor_web>      <nombre_con_el_que_accedemos>

	Por ejemplo:

		192.168.121.10      www.example.org

	Ahora podemos acceder a la URL: `http://www.example.org/info.php`

5. Si tenemos problemas de acceso podemos ver los logs del servidor:

* El fichero de logs de acceso por "defecto": `/var/log/apache/access.log`. Donde se registra los accesos al servidor desde los clientes.
* El fichero de logs de errores por" defecto": `/var/log/apache/error.log`.
* También podemos ver los logs del servicio ejecutando: `journalctl -u apache2`.


