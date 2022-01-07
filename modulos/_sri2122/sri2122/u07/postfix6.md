---
title: "Alias y redirecciones"
permalink: /serviciosgs/u06/postfix6.html
---

## Alias

Cuando se define un alias para un determinado usuario se redirige el correo que llegue a otro usuario de la misma máquina. Los alias de correo se utilizan principalmente para gestionar el correo de las "cuentas de administración" y se definen en el fichero ``/etc/aliases``, que tiene el siguiente aspecto::

	# /etc/aliases
	mailer-daemon: postmaster
	postmaster: root
	nobody: root
	hostmaster: root
	usenet: root
	news: root
	webmaster: root
	www: root
	ftp: root
	abuse: root
	noc: root
	security: root
	www-data: root
	logcheck: root
	root: alberto, jose, raul

En este caso el correo que llega a los usuarios postmaster, webmaster, etc. se redirige a la cuenta de root, que a su vez se redirige a los usuarios reales alberto, jose y raul, que son los administradores del equipo.

Cada vez que se modifica el fichero ``/etc/aliases`` hay que ejecutar la instrucción ``newaliases`` para que los cambios tengan efecto.

## Redirecciones

Una redirección se utiliza para enviar el correo que llegue a un usuario a una cuenta de correo exterior. Para usuarios reales las redirecciones se definen en el fichero ``~/.forward`` y el formato de este fichero es simplemente un listado de cuentas de correo a las que se quiere redirigir el correo.


<!--
## Usuarios virtuales

En muchas ocasiones es necesario usar nombres de usuario que no correpondan con los nombres de los usuarios de sistema. Por ejemplo me gustaría usar `josedom24` en vez de `debian`. `josedom24` es un usuario virtual, que lo vamos a relacionar con el usuario de sistema `debian`. Por lo tanto cuando `josedom24` reciba un correo se guardará en el buzón del usuario `debian`. Para conseguir eso hacemos lo siguiente:

Añadimos al fichero de configuración `/etc/postfix/main.cf` las siguientes líneas:

	virtual_alias_domains = $mydomain'
	virtual_alias_maps = hash:/etc/postfix/virtual

Creamos el fichero `/etc/postfix/virtual` con el siguiente contenido:

	josedom24@iesgnXX.es debian

Creamos el fichero base de datos que va a leer postfix, que se llamará `/etc/postfix/virtual.db`:

	postmap /etc/postfix/virtual

Y reiniciamos postfix.

-->