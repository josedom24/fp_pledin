---
title: "Ejercicio 1: Mapear URL a ubicaciones de un sistema de ficheros"
---
1. [Alias](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#alias): Un alias me permite servir ficheros que no se encuentran en el `DocumentRoot`.

2. [Options](http://httpd.apache.org/docs/2.4/mod/core.html#options): Determina para que sirven las siguientes opciones de funcionamiento:

	* All
	* FollowSymLinks
	* Indexes
	* MultiViews
	* SymLinksOwnerMatch
	* ExecCGI

	Determina como funciona si delante de las opciones pongo el signo + o -.

3. La directiva [Redirect](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirect) nos permite crear redirecciones temporaless o permanentes.

5. Con la directiva ``ErrorDocument`` se puede crear [Respuesta de error personalizadas](http://httpd.apache.org/docs/2.4/custom-error.html). Todo esto se puede llevar a cabo en el fichero ``/etc/apache2/conf-available/localized-error-pages.conf``. 


## Ejercicios

Crea un nuevo host virtual que es accedido con el nombre ``www.mapeo.com``, cuyo ``DocumentRoot``  sea /srv/mapeo. 

1. Cuando se entre a la dirección ``www.mapeo.com`` se redireccionará automáticamente a ``www.mapeo.com/principal``, donde se mostrará el mensaje de bienvenida. 
2. En el directorio **principal** no se permite ver la lista de los ficheros, no se permite que se siga los enlaces simbólicos y no se permite negociación de contenido. Muestra al profesor el funcionamiento. ¿Qué configuración tienes que poner?
3. Si accedes a la página ``www.mapeo.com/principal/documentos`` se visualizarán los documentos que hay en `/home/usuario/doc`. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces simbólicos siempre que el propietario del enlace y del fichero al que apunta sean el mismo usuario. 
4. En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error. Entrega las modificaciones necesarias en la configuración y una comprobación del buen funcionamiento.


{% capture notice-text %}
**Entrega**

1. Cuando termines el ejercicio entrega la configuración completa del fichero de configuración del virtualhost?
2. Utilizando la opción de "Desarrollador web" del navegado, entrega un pantallazo donde se vea que cuando a ccedemos a `www.mapeo.com` se produce un redireccionamiento a `principal`.
3. Entrega una captura de pantalla accediendo a `www.mapeo.com/principal/documentos`.
4. Entrega dos capturas de pantalla donde se vea la nueva página de error personalizada para 
objeto no encontrado y no permitido.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>