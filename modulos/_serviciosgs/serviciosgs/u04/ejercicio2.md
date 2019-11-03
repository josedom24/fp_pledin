---
title: "Ejercicio 2: DNSmasq como DNS cache/forward en una red local"
permalink: /serviciosgs/u04/ejercicio2.html
---

El paquete ``dnsmasq`` permite poner en marcha un servidor DNS de una forma muy sencilla. Simplemente instalando y arrancando el servicio dnsmasq, sin realizar ningún tipo de configuración adicional, nuestro PC se convertirá en un servidor caché DNS y además, resolverá los nombres que tengamos configurados en el archivo `/etc/hosts` de nuestro servidor. La resolución funcionará tanto en sentido directo como en sentido inverso.

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red. Las características del servidor DNS que queremos instalar son las siguientes:

* Vamos a suponer que tenemos un servidor web que se llame ``www.iesgn.com`` y que está en 192.168.1.200 (esto es ficticio).
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.iesgn.com`` y que está en 192.168.1.201 (esto es ficticio).
* Además queremos nombrar a otras máquinas.

Una vez instalado, el paquete, editamos el fichero ``/etc/dnsmasq.conf`` y modificamos las siguientes líneas:

* Descomentamos ``strict-order`` para que se realicen las peticiones DNS a los servidores que aparecen en el fichero ``/etc/resolv.conf`` en el orden en el aparecen.
* Incluimos las interfaces de red que deben aceptar peticiones DNS, descomentando la línea `interface` por ejemplo: ``interface=eth0``

Finalmente reiniciamos el servicio.

{% capture notice-text %}
1. Configura los clientes para que utilicen el servidor DNS que has instalado.
2. Realiza las consultas dig/nslookup desde los clientes preguntando por los siguientes:	

	* Dirección de  ``www.iesgn.org``, ``ftp.iesgn.org``
	* La dirección IP de ``www.josedomingo.org``	
	* El nombre de la ip `192.168.1.200`
	* ¿Te devuelve el nombre del servidor DNS con autoridad para la zona `iesgn.com`?


{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>