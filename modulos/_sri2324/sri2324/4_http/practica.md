---
title: "Práctica: Instalación de nginx con PHP"
---

## Recursos para realizar este taller

* [Introducción al servidor web nginx](nginx.html)

## Descripción

1. Realiza la configuración básica de nginx que ejecute scripts PHP creando una receta ansible. Utilizando como base la receta ansible que utilizaste para el taller 3, modifícala para añadir las siguientes funcionalidades:

	* Instalación de los servicios (cada servicio se instalará y configurará en un rol diferenciado).
	* Debemos configurar fpm-php para que escuche en un socket TCP.
	* Además de copiar un `index.html` en el *DocumentRoot*, copiará también un fichero `info.php` que muestre la información de la configuración de PHP.
	* Como hace la receta original, creará VirtualHost que tengas definido en una lista. Estos virtual host estarán configurados para ejecutar PHP.
	* La receta debe poder desactivar los VirtualHost que tengas definido en otra lista.

2. Configura sobre una máquina virtual, usando la receta de ansible, un servidor nginx + PHP con dos VirtualHost:

	* `www.pagina1.org`, cuyo *DocumentRoot* estará en `/srv/www/pagina1`.
	* `www.pagina2.org`, cuyo *DocumentRoot* estará en `/srv/www/pagina2`.

	Una vez que la receta haya configurado el servidor web con los dos VirtualHost, configura manualmente las siguientes características:

3. Cuando se acceda a `www.pagina1.org` se realizará una redirección a a la página `www.pagina1.org/principal`. En el directorio principal no se permite ver la lista de los ficheros, no se permite que se siga los enlaces simbólicos.
4. En la página `www.pagina1.org/principal` se debe mostrar una página web estática (utiliza alguna plantilla para que tenga hoja de estilo o la página estática que has generado en IAW).
5. Si accedes a la página `www.pagina1.org/principal/documentos` se visualizarán los documentos que hay en `/srv/doc`. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces simbólicos.
6. Limita el acceso a la URL `www.pagina1.org/secreto` con autentificación básica.
{% capture notice-text %}
## Entrega

1. Entrega un zip con el código que has generado en la práctica.
2. Pantallazos para comprobar que se han creado los dos VirtualHost después de ejecutar el playbook ansible y están activos.
3. Comprobación de que el servidor fpm-php está configurado para recibir las peticiones en un socket TCP.
4. Comprobación de que al acceder a `www.pagina1.org` se produce una redirección. Prueba de funcionamiento usando `curl`.
5. Pantallazo accediendo a `www.pagina1.org/principal/documentos` (pon algunos ficheros para que se vea la lista).
6. Pantallazos de la autentificación básica.
7. Finalmente, configura el playbook ansible para desactivar el VirtualHost `www.pagina2.org`. Pasa de nuevo el playbook y manda algún prueba de que se ha desactivado dicho VirtualHost.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


