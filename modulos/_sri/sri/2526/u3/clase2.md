---
title: "Clase 1: Configuración de un servidor Apache2"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de alias.
* Las distintas opciones que podemos definir en un directorio servido por apache2.
* El concepto de redirección.
* El control de acceso a los ficheros y directorios de un servidor web apache2.
* La autentificación para acceder a recursos del servidor web.
* Configuración descentralizada usando ficheros `.htaccess`.
* Introducción a los módulos en apache2.

## Recursos

Los contenidos necesarios para la realización de este ejercicio y para profundizar en la configuración de Apache2, lo puedes encontrar en el siguiente apartado:

* [Introducción al servidor web Apache2](apache2.html)

## Ejercicio

Utilizando el **escenario 1** del repositorio [terraform-libvirt](https://github.com/josedom24/terraform-libvirt) vas a crear un escenario donde existe una máquina **servidorweb** y un **cliente**. Los dos están conectados a una red NAT, por lo que tienen internet. Simulamos que el cliente accede al servidor web por una red muy aislada (`servidorweb` 10.0.0.1, y `cliente` 10.0.0.2). Modifica los ficheros de configuración de cloud-init para ajustar tu configuración.

Una vez creado el escenario:

1. Instala un servidor web apache2 en `servidorweb`.
2. Crea un virtualhost con el que accederemos con el nombre `www.taller1.com`. En este virtualhost realizaremos los siguientes ejercicios.
3. Cuando se entre a la dirección `www.taller1.com` se redireccionará automáticamente a `www.taller1.com/principal`, donde se mostrará el mensaje de bienvenida.
4. Si accedes a la página `www.taller1.com/principal/documentos` se visualizarán los documentos que hay en `home/usuario/doc`. Por lo tanto se permitirá el listado de ficheros (opción `Indexes`).
5. A la URL `www.taller1.com/intranet` sólo se debe tener acceso desde el cliente de la red interna, y no se pueda acceder desde la anfitriona por la red pública. A la URL `www.taller1.com/internet`, sin embargo, sólo se debe tener acceso desde la anfitriona por la red pública, y no desde la red interna.
6. Autentificación básica. Limita el acceso a la URL `www.taller1.com/secreto`. 
7. Vamos a combinar el control de acceso (ejercicio 5) y la autentificación (ejercicio 6), y vamos a configurar el virtual host para que se comporte de la siguiente manera: el acceso a la URL `www.taller1.com/secreto` se hace forma directa desde la intranet, desde la red pública te pide la autentificación. 
8. El módulo **rewrite** nos va a permitir acceder a una URL e internamente estar accediendo a otra. Esto nos puede ayudar a hacer URL amigables y hacer redirecciones. Por ejemplo para redireccionar a otra URL:

	```
	RewriteEngine On
	RewriteRule ^(.*)$ http://www.nueva.com/$1 [R=301,L]
	```

	Usando un fichero `.htaccess` haz que al acceder a la URL `www.taller1.com/documentos` se produce una redirección a `www.taller1.com/principal/documentos` usando el modulo rewrite (recuerda que tienes que activarlo). Además, deniega el acceso desde la red interna.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configuración completa del virtualhost.
2. Comprobación de que al acceder a `www.taller1.com` se produce una redirección.
3. Pantallazo accediendo a `www.taller1.com/principal/documentos` (pon algunos ficheros para que se vea la lista).
4. Pantallazos de accesos a `www.taller1.com/intranet` desde el host y el cliente interno. Pantallazos de acceso a `www.taller1.com/internet` desde el host y el cliente interno.
5. Pantallazos de la autentificación básica.
6. Pantallazos de acceso a `www.taller1.com/secreto` desde el host y el cliente interno.
7. Contenido del fichero `.htaccess`. Acceso a `www.taller1.com/documentos` comprobando que se produce una redirección desde el exterior y prueba de acceso desde el cliente interno para comprobar que no tiene permiso de acceso.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
