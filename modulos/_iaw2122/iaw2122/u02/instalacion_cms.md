---
title: Principales pasos para instalar un CMS PHP
---
1. Crear la base de datos y el usuario de la base de datos que vamos a utilizar para que la aplicación acceda a los datos.
2. ¿Dónde vamos a implantar la aplicación? O en un virtual host o en un directorio dentro de un virtualhost.
    Por ejemplo, si instalo WordPress:

    * En un VirtualHost accederíamos con `wordpress.gonzalonazareno.org`, los ficheros del CMS estarían en la raíz del DocumentRoot.
    * En un directorio dentro de un VirtualHost, se accedería, por ejemplo, con `dit.gonzalonazareno.org/wordpress`, los ficheros del CMS estarían en el directorio `wordpress` dentro del DocumentRoot.

3. Descargar los ficheros del CMS y subirlos los ficheros del CMS al servidor. Varias formas: FTP, scp, wget, ...)
4. Acceso a la URL de instalación e iniciar el proceso de configuración.
5. Un punto importante en el proceso de configuración es indicar las credenciales para el acceso a la Base de Datos: hay que indicar el usuario y contraseña que vamos a utilizar, el nombre de la base de datos y ela dirección donde se encuentra el servidor de base de datos. Si el servidor de BD está en la misma máquina que el servidor web se pondrá `localhost`, sino se pondrá la ip o el nombre dl servidor.
6. En el proceso de configuración e instalación, quizás se nos pida instalar determinadas librerias de PHP.
7. Terminamos la configuración de la aplicación: Nombre, usuario administrador, ...
8. La información que introducimos para configurar la aplicación se puede guardar en un fichero o en la base de datos:
    * Las credenciales de conexión se suelen guardar en un fichero de configuración.
    * Las demás configuraciones se suelen guardar en la base de datos, pero esto varia según el CMS que estemos instalando.
