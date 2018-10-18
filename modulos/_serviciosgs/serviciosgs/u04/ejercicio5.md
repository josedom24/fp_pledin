---
title: "Ejercicio 5: Configuración de subdominios virtuales con bind9"
permalink: /serviciosgs/u04/ejercicio5.html
---

```eval_rst
.. note::

	Suponemos que tenemos instalado el servidor DNS del `ejercicio anterior <ejercicio3.html>`_.
```

Tenemos un servidor DNS que gestiona la zona correspondiente al nombre de dominio ``iesgn.org``, queremos configurar dicho servidor para crear el subdominio ``informatica.iesgn.org``. Los nombres que vamos a tener en ese subdominio son los siguientes:

* ``www.informatica.iesgn.org`` corresponde a un sitio web que está en la dirección 10.0.0.100.
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.informatica.iesgn.org`` y que está en la misma máquina.

```eval_rst
.. warning::

	1. Configura el servidor DNS para poder tener el subdominio virtual ``informatica.iesgn.org``. 
	2. Realiza las consultas dig/neslookup desde los clientes preguntando por los siguientes:

		* Dirección de ``www.informatica.iesgn.org``, ``ftp.informatica.iesgn.org``
		* El servidor DNS que tiene configurado la zona del dominio ``informatica.iesgn.org``. Comprueba que es el mismo que el de la zona ``iesgn.org``.
```