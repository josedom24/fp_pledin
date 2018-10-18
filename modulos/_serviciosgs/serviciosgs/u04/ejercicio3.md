---
title: "Ejercicio 3: Instalación y configuración del servidor bind9 en nuestra red local"
permalink: /serviciosgs/u04/ejercicio3.html
---

```eval_rst
.. note::

	1. Desinstala el servidor dnsmasq que has instalado en la práctica anterior para que no tengas conflictos.
	2. Para hacer este ejercicio vamos a suponer que nuestro ordenadores están en la red 10.0.0.0/24, siendo nuestro servidor el 10.0.0.3, y los clientes 10.0.0.4 y 10.0.0.5. Adapta este direccionamiento a tu escenario.
```

Queremos instalar un servidor DNS local en nuestra intranet que nos permita gestionar los nombres de las máquinas y recursos de nuestra red, vamos a instalar el servidor DNS en nuestro servidor debian. Las características del servidor DNS que queremos instalar son las siguientes:

1. Vamos a crear una zona para el dominio: ``iesgn.org``
2. Vamos a crear una zona de resolución inversa.
3. Vamos a tener los siguientes FQDN

* El servidor DNS se llama ``nombredelservidor.iesgn.org``
* Vamos a suponer que tenemos un servidor para recibir los correos que se llame ``correo.iesgn.org`` y que está en 10.0.0.200 (esto es ficticio)
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.iesgn.org`` y que está en 10.0.0.201 (esto es ficticio)
* Además queremos nombrar a varios clientes.
* Suponemos que tenemos un servidor web con las páginas: ``www.iesgn.org`` y ``departementos.iesgn.org``

```eval_rst
.. warning::

	1. Configura el servidor DNS con los registros A, CNAME, MX y NS necesarios, configura el SOA. 
	2. Configura los clientes para que su DNS sea el servidor Debian, debes indicar en la configuración de red del cliente como DNS primario la ip del servidor linux.
	3. Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:	

	* Dirección de ``nombredelservidor.iesgn.org``,``www.iesgn.org``,``ftp.iesgn.org``
	* El servidor DNS que tiene configurado la zona del dominio ``iesgn.org``
	* El servidor de correo configurado para ``iesgn.org``
	* La dirección IP de ``www.josedomingo.org``
	* Un resolución inversa
```