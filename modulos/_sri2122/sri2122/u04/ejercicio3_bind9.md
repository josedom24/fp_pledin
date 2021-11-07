---
title: "Ejercicio 3: Delegación de subdominios con bind9"
---

Tenemos un servidor DNS que gestiona la zona correspondiente al nombre de dominio ``iesgn.org``, en esta ocasión queremos delegar el subdominio ``informatica.iesgn.org`` para que lo gestione otro servidor DNS. Por lo tanto tenemos un escenario con dos servidores DNS:

* ``tunombre.iesgn.org``, es servidor DNS autorizado para la zona ``iesgn.org``.
* ``tunombre-ns.informatica.iesgn.org``, es el servidor DNS para la zona ``informatica.iesgn.org`` y, está instalado en otra máquina.

Los nombres que vamos a tener en ese subdominio son los siguientes:

* ``www.informatica.iesgn.org`` corresponde a un sitio web que está alojado en el servidor web del departamento de informática.
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.informatica.iesgn.org`` y que está en la misma máquina.
* Vamos a suponer que tenemos un servidor para recibir los correos que se llame ``correo.informatica.iesgn.org``.

Realiza la instalación y configuración del nuevo servidor dns con las características anteriormente señaladas.

{% capture notice-text %}

* Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:	
	* Dirección de ``www.informatica.iesgn.org``, ``ftp.informatica.iesgn.org``
	* El servidor DNS que tiene configurado la zona del dominio ``informatica.iesgn.org``. ¿Es el mismo que el servidor DNS con autoridad para la zona ``iesgn.org``?
	* El servidor de correo configurado para ``informatica.iesgn.org``
**Enseña al profesor el funcionamiento de la delegación de dominio.**
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

