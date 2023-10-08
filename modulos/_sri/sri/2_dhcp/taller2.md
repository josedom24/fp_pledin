---
title: "Taller 2: Funcionamiento del servidor DHCP"
---

## ¿Qué vas a aprender en este teller?

* Creación de una reserva
* Identificar los paquetes que se transmiten entre el cliente y el servidor en la negociación DHCP.
* Profundizar en el funcionamiento del protocolo DHCP.

## ¿Qué tienes que hacer?

1. Continuamos trabajando en el escenario del taller anterior.
2. Introduce un cliente Windows y realiza la configuración necesario para que tome configuración de red del servidor DHCP.
3. Realizar una captura, desde el servidor usando `tcpdump`, de los cuatro paquetes que corresponden a una concesión: `DISCOVER`, `OFFER`, `REQUEST`, `ACK`.
4. **Para hacer esta prueba configura un tiempo de concesión bajo**. Los clientes toman una configuración, y a continuación apagamos el servidor DHCP. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
5. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor DHCP (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
6. Para crear una reserva en el servidor vamos a trabajar en la sección `host`.
	En una sección `host` debemos poner el nombre que identifica al host y los siguientes parámetros:
	
	* `hardware ethernet`: Es la dirección MAC de la tarjeta de red del host.
	* `fixed-address`: La dirección IP que le vamos a asignar. 
	* Podemos usar también las opciones ya explicadas en la sección principal.

	Realiza una reserva para el cliente Windows, para que tenga la IP `192.168.200.200`. La configuración quedaría:

	```
	host cliente-windows {
	  hardware ethernet xx:xx:xx:xx:xx:xx;
	  fixed-address 192.168.200.200;
	}
	```

	¿Se guarda la reserva en la lista de concesiones?


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Una vez que el cliente Windows se haya configurado, capturas de pantalla donde se vea en el cliente: su dirección IP, su puerta de enlace y su servidor DNS.
2. Captura de pantalla donde se vean los 4 paquetes que se transmite en la negociación de la concesión.
3. Explica, con pruebas de funcionamiento, el motivo del comportamiento que se indica en los puntos 4 y 5.
4. Capturas de pantalla donde se vea el funcionamiento de la reserva. ¿Se guarda la reserva en la lista de concesiones?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>