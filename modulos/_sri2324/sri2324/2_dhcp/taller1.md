---
title: "Taller 1: Instalación y configuración del servidor DHCP"
---

## ¿Qué vas a aprender en este taller?

* Instalación del servidor isc-dhcp-server.
* configuración básica del servicio isc-dhcp-server.
* Conocer los principales parámetros de configuración
* Configuración de los clientes para obtener configuración automática.

## ¿Qué tienes que hacer?

1. Crea una infraestructura en QEMU/KVM que te permita tener una máquina donde instalar un servidor dhcp y un cliente que se configuren para tomar la configuración de forma dinámica. El servidor estará conectado al cliente por una red interna muy aislada.
2. Para instalar nuestro servidor dhcp ejecutamos:

	```bash
	apt-get install isc-dhcp-server
	```
	**Nota: Cuando instalamos el servidor por primera se produce un error, ya que no está configurado. Puedes ver los errores producidos por el servidor en el fichero `/var/log/syslog` o `systemctl -u isc-dhcp-server`.**
	
3. Vamos a configurar la interfaz por la que va a trabajar el servidor dhcp, para ello editamos el siguiente fichero `/etc/default/isc-dhcp-server`. Donde configuramos el parámetro interfaces (modifícalo según tu escenario), por ejemplo:
	
```
INTERFACES="eth1"
```
4. Vamos a estudiar el fichero de configuración del servicio `/etc/dhcp/dhcpd.conf`.

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

5. Configura el servidor DHCP con las siguientes características

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
6. Configura los clientes para obtener direccionamiento dinámico. Comprueba las configuraciones de red que han tomado los clientes.

	**Nota: En Windows la instrucción `ipconfig /release` libera la concesión, la instrucción `ipconfig /renew` la renueva. En linux el comando para liberar la concesión es `dhclient -r` y el que nos permite renovarla será `dhclient`.**

7. El servidor debe hacer router-nat para que el cliente tenga acceso a internet. La configuración debe ser persistente.

8. Cuando el servidor va repartiendo la configuración a los clientes va guardando las concesiones en el fichero `/var/lib/dhcp/dhcpd.leases`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Configuración del cliente para que configure la red de forma dinámica.
2. Una vez que el cliente se haya configurado, capturas de pantalla donde se vea en el cliente: su dirección IP, su puerta de enlace y su servidor DNS.
3. La concesión que se ha hecho en el servidor. Estará en el fichero donde se guarda la lista de concesiones.
4. Una comprobación del que el cliente puede hacer resolución a un nombre de internet.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>