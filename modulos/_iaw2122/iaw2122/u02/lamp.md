---
title: Instalación de un servidor LAMP
---
El acrónimo ‘LAMP’ se refiere a un entorno configurado en un servidor que nos posibilita servir aplicaciones web escritas en PHP.

El entorno que vamos a configurar se consigue mediante la unión de las siguientes tecnologías:

* Linux, el sistema operativo;
* Apache, el servidor web;
* MySQL, MariaDB, el gestor de bases de datos;
* Perl, PHP, o Python, los lenguajes de programación.

Ahora vamos a instalar los paquetes necesarios para tener un entorno LAMP.

## mariadb

realizamos la instalación del servidor de base de datos:

```bash
apt install mariiadb-server
```

Por defecto el usuario `root` no tiene contraseña, para acceder necesitaremos hacer con el `root``del sistema. Es muy recomendable ejecutar el programa `mariadb-secure-installation` para configurar la base de datos de manera segura, por ejemplo para indicar una contraseña al root.

## PHP


```bash
apt install php php-mysql
```

## Apache y PHP


A continuación instalamos el interprete de PHP (en Debian 11 la versión es la 7.4). Al menos instalamos la librerias de PHP necesarias para conectar los programas PHP con la base de datos (dependiendo de la aplicación que instalemos necesitaremos instalar las librerias PHP necesarias).

También instalamos el servidor web. Además vamos a instalar el módulo que permite que apache2 interprete PHP (es decir, apache2 hará el papel de servidor web y de servidor de aplicaciones).

```bash
apt install apache2 libapache2-mod-php php php-mysql
```

### Configuración de PHP

La configuración de php está dividida según desde donde se use:

* `/etc/php/7.4/cli`: Configuración de php para `php7.4-cli`, cuando se utiliza php desde la línea de comandos.
* `/etc/php/7.4/apache2`: Configuración de php para apache2 cuando utiliza el módulo.
* `/etc/php/7.4/fpm`: Configuración de php para php-fpm
* `/etc/php/7.4/mods-available`: Módulos disponibles de php que puedes estar configurados en cualquiera de los escenarios anteriores.

Si nos fijamos en la configuración de php para apache2:

* `/etc/php/7.4/apache2/conf.d`: Módulos instalados en esta configuración de php (enlaces simbólicos a /etc/php/7.4/mods-available).
* `/etc/php/7.4/apache2/php.ini`: Configuración de php para este escenario.

## Comprobar que funciona el servidor LAMP

Para comprobar si el servidor LAMP está funcionando, puedes crear un fichero `info.php` en el documentRoot con el siguiente contenido:

```php
<?php phpinfo(); ?>
```

Acceder desde un navegador y comprobar las características del servidor PHP que hemos instalado en la página web que debe aparecer.
