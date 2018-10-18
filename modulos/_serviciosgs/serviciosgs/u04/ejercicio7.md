---
title: "Ejercicio 7: Instalación y configuración de un servidor DNS dinámico"
permalink: /serviciosgs/u04/ejercicio7.html
---

```eval_rst
.. note::

	Suponemos que tenemos instalado el servidor DNS del `ejercicio anterior <ejercicio3.html>`_.
```

Suponemos que actualmente tenemos instalado un servidor DNS caché que da servicio a los ordenadores de nuestra intranet y además actúa como servidor maestro (master) de un dominio DNS (``iesgn.org``), de forma que todos los equipos de la red local tengan un nombre DNS completo o FQHN (Full Qualified Host Name). Por otra parte, tenemos instalado en la misma máquina un servidor DHCP para que asigne direcciones IPv4 únicas a los equipos de la red local y les facilite el resto de parámetros necesarios para tengan conectividad y salida a Internet.

 Las características del servidor DNS serán:

* El nombre del servidor DNS para la zona ``iesgn.org`` sera ``nombredelservidor.iesgn.org``.
* En un primer momento el único nombre que resuelve nuestro servidor será el suyo propio, con la dirección 192.168.2.1 *(Cambia el direccionamiento según tu escenario)*.

Las características del servidor DHCP instalado serán:

* Tiempo de concesión: 1 mes
* Rango de direcciones: 192.168.2.100 - 192.168.2.150
* Puerta de enlace: 192.168.2.1
* Servidores DNS: 192.168.2.1

```eval_rst
.. warning:: 

	1. Entrega la configuración en el servidor DNS necesaria para que tenga la funcionalidad de de DNS dinámico.
	2. Muestra la configuración necesaria en el servidor DHCP para comunicarse con el DNS.
	3. Configura un cliente de forma dinámica para que tome una configuración ofrecida por el servidor DHCP y comprueba que su nombre se ha incluido en la zona correspondiente en el servidor DNS: visualiza los logs que no informan de ello y realiza una consulta al servidor DNS preguntando por su nombre.
	4. Fuerza a que un cliente cambie de DNS y comprueba que la modificación se ha comunicado al DNS.
```