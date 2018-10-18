---
title: "Ejercicio 2: DNSmasq como DNS cache/forward en una red local"
permalink: /serviciosgs/u04/ejercicio2.html
---

El paquete ``dnsmasq`` permite poner en marcha un servidor DNS de una forma muy sencilla. Simplemente instalando y arrancando el servicio dnsmasq, sin realizar ningún tipo de configuración adicional, nuestro PC se convertirá en un servidor caché DNS y además, resolverá los nombres que tengamos configurados en el archivo /etc/hosts de nuestro servidor. La resolución funcionará tanto en sentido directo como en sentido inverso, es decir, resolverá la IP dado un nombre de PC y el nombre del PC dada la IP.

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red, vamos a instalar el servidor DNS en el mismo ordenador que tenemos instalado el servidor web. Las características del servidor DNS que queremos instalar son las siguientes:

* El servidor web (IP que tenga el servidor linux) se llama ``nombredelservidor.iesgn.com``
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.iesgn.com`` y que está en 192.168.1.201 (esto es ficticio)
* Además queremos nombrar a otros clientes.
* Las páginas webs que hiciste en la práctica de apache (``www.iesgn.org``,...) tienen que ser accesibles desde los clientes.

Una vez instalado, el paquete, editamos el fichero ``/etc/dnsmasq.conf`` y modificamos las siguientes líneas:

* Descomentamos ``strict-order`` para que se realicen las peticiones DNS a los servidores que aparecen en el fichero ``/etc/resolv.conf`` en el orden en el aparecen.
* Incluimos las interfaces de red que deben aceptar peticiones DNS, descomentando la línea interface por ejemplo: ``interface=eth0``

Finalmente reiniciamos el servicio.

```eval_rst
.. warning::

	1. Configura los clientes para que utilicen el servidor DNS que has instalado.
	2. Realiza las consultas dig/nslookup desde los clientes preguntando por los siguientes:	

		* Dirección de ``nombredelservidor.iesgn.org``, ``www.iesgn.org``, ``ftp.iesgn.org``
		* La dirección IP de ``www.josedomingo.org``	

	3. Comprueba que se puede entrar en las páginas webs
```