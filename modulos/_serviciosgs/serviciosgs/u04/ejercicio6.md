---
title: "Ejercicio 6: Delegación de subdominios con bind9"
permalink: /serviciosgs/u04/ejercicio6.html
---

```eval_rst
.. note::

	Suponemos que tenemos instalado el servidor DNS del `ejercicio anterior <ejercicio3.html>`_.
```

Tenemos un servidor DNS que gestiona la zona correspondiente al nombre de dominio ``iesgn.org``, en esta ocasión queremos delegar el subdominio ``informatica.iesgn.org`` para que lo gestione otro servidor DNS. Por lo tanto tenemos un escenario con dos servidores DNS:

* ``nombredelservidor.iesgn.org``, es servidor DNS autorizado para la zona ``iesgn.org`` y tiene asignado la dirección 10.0.0.3.
* ``servidor_subdomio.informatica.iesgn.org``, es el servidor DNS para la zona ``informatica.iesgn.org`` y, suponemos que tiene asignado la dirección 10.0.0.50.

Los nombres que vamos a tener en ese subdominio son los siguientes:

* ``www.informatica.iesgn.org`` corresponde a un sitio web que está en la dirección 10.0.0.100.
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.informatica.iesgn.org`` y que está en la misma máquina.
*  Vamos a suponer que tenemos un servidor para recibir los correos que se llame ``correo.informatica.iesgn.org`` y que está en 10.0.0.51.

```eval_rst
.. warning:: 

	1. Configura el primer servidor DNS para poder tener el subdominio virtual ``informatica.iesgn.org``. 
	2. Configura el segundo servidor DNS con los registros A, CNAME, MX y NS necesarios para el subdominio ``informatica.iesgn.org``. 
	3. Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:	

		* Dirección de ``www.informatica.iesgn.org``, ``ftp.informatica.iesgn.org``
		* El servidor DNS que tiene configurado la zona del dominio ``informatica.iesgn.org``. ¿Es el mismo que el servidor DNS con autoridad para la zona ``iesgn.org``?
		* El servidor de correo configurado para ``informatica.iesgn.org``
```
