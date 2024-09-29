---
title: "Introducción al servidor ISC DHCP"
---

Para instalar y configurar el servidor ISC DHCP sigue los siguientes pasos:

1. Para instalar nuestro servidor dhcp ejecutamos:

	```bash
	apt-get install isc-dhcp-server
	```
	**Nota: Cuando instalamos el servidor por primera se produce un error, ya que no está configurado. Puedes ver los errores producidos por el servidor en el fichero `/var/log/syslog` o `systemctl -u isc-dhcp-server`.**
	
2. Vamos a configurar la interfaz por la que va a trabajar el servidor dhcp, para ello editamos el siguiente fichero `/etc/default/isc-dhcp-server`. Donde configuramos el parámetro interfaces (modifícalo según tu escenario), por ejemplo:
	
```
INTERFACES="eth1"
```
3. Vamos a estudiar el fichero de configuración del servicio `/etc/dhcp/dhcpd.conf`.

	El fichero de configuración está dividido en dos partes:

	* **Parte principal (valores por defecto)**: especifica los parámetros generales que definen la concesión y los parámetros adicionales que se proporcionarán al cliente.
	* **Secciones** (concretan a la principal):
	
		* **Subnet**: Especifican rangos de direcciones IPs que serán cedidas a los clientes que lo soliciten.
		* **Host**: Especificaciones concretas de equipos.

	En la parte principal podemos configurar los siguientes parámetros, que más tarde podremos reescribir en las distintas secciones:

	Parámetros de tiempos:

	* `max-lease-time`: Es el tiempo máximo en segundos de concesión que un cliente puede solicitar. Si por ejemplo, un cliente solicita una concesión de 900 segundos pero el tiempo máximo es de 600 segundos, la concesión tendrá una duración de 600 segundos. No tiene por qué ser T3 o temporizador de alquiler.
	* `min-lease-time`: Es el tiempo mínimo en segundos de concesión que un cliente puede solicitar. Si por ejemplo, un cliente solicita una concesión de 900 segundos pero el tiempo mínimo es de 1200 segundos, la concesión tendrá una duración de 1200 segundos.
	* `default-lease-time`: Es el tiempo por defecto en segundos de concesión que se le asignará a un cliente en caso de que éste no haya solicitado ningún periodo en concreto. Estos tres primeros parámetro determinan el **tiempo T3 o tiempo de concesión**.
	* `option dhcp-renewal-time`: Es el tiempo en segundos que ha de transcurrir hasta que el cliente pase al estado RENEWING. También conocido como **T1 o temporizador de renovación de alquiler**. No confundir con `default-lease-time`.
	* `option dhcp-rebinding-time`: Es el tiempo en segundos que ha de transcurrir hasta que el cliente pase al estado REBINDING. También conocido como **T2 o temporizador de reenganche**.

	Parámetros de configuración:

	* `option routers`: Indicamos la dirección red de la puerta de enlace que se utiliza para salir a internet.
	* `option domain-name-servers`: Se pone las direcciones IP de los servidores DNS que va a utilizar el cliente.
	* `option domain-name`: Nombre del dominio que se manda al cliente.
	* `option subnet-mask`: Subred enviada a los clientes.
	* `option broadcast-address`: Dirección de difusión de la red.

	Al indicar una sección subnet tenemos que indicar la dirección de la red y la mascara de red y entre llaves podemos poner los siguientes parámetros:

	* `range`: Indicamos el rango de direcciones IP que vamos a asignar.
	* Algunos de los parámetros que hemos explicado en la sección principal.

4. Configura el servidor DHCP con las siguientes características

	* Rango de direcciones a repartir: `192.168.0.100` - `192.168.0.110`
	* Máscara de red: `255.255.255.0`
	* Duración de la concesión: 1 hora
	* Puerta de enlace: `192.168.0.1`
	* Servidores DNS: `192.168.202.2` y `1.1.1.1`

	La configuración quedaría:

	```
	subnet 192.168.0.0 netmask 255.255.255.0 {
	  default-lease-time 3600;
	  max-lease-time 3600;  
	  range 192.168.0.100 192.168.0.110;
	  option subnet-mask 255.255.255.0;
	  option broadcast-address 192.168.0.255;
	  option routers 192.168.0.1;
	  option domain-name-servers 192.168.202.2, 1.1.1.1;
	}
	```

	* **Nota 1: Si ponemos algún parámetro fuera de la sección `subnet` afectará a todas las secciones `subnet`. Si dentro de la sección `subnet` se reescribe el parámetro no se utilizará el valor del parámetro general.**
	* **Nota 2: El tiempo T3 será `default-lease-time` si el cliente no ha solicitado tiempo de concesión. Si el cliente lo ha solicitado no será mayor que `max-lease-time` ni menor que `min-lease-time`.**
	* **Nota 3: No hemos indicado ni el T1, ni el T2, por lo que estos valores se calcularán a partir de T3.**
5. Configura los clientes para obtener direccionamiento dinámico. Comprueba las configuraciones de red que han tomado los clientes.

	**Nota: En Windows la instrucción `ipconfig /release` libera la concesión, la instrucción `ipconfig /renew` la renueva. En linux el comando para liberar la concesión es `dhclient -r` y el que nos permite renovarla será `dhclient`.**

6. Cuando el servidor va repartiendo la configuración a los clientes va guardando las concesiones en el fichero `/var/lib/dhcp/dhcpd.leases`.

7. Para crear una reserva en el servidor vamos a trabajar en la sección `host`.
	En una sección `host` debemos poner el nombre que identifica al host y los siguientes parámetros:
	
	* `hardware ethernet`: Es la dirección MAC de la tarjeta de red del host.
	* `fixed-address`: La dirección IP que le vamos a asignar. 
	* Podemos usar también las opciones ya explicadas en la sección principal.

	Realiza una reserva para el cliente Windows, para que tenga la IP `192.168.0.200`. La configuración quedaría:

	```
	host cliente-windows {
	  hardware ethernet xx:xx:xx:xx:xx:xx;
	  fixed-address 192.168.0.200;
	}
	```

	¿Se guarda la reserva en la lista de concesiones?

