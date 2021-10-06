---
title: "Servidor isc-dhcp-server"
---

## Instalación del servidor isc-dhcp-server

Para instalar nuestro servidor dhcp ejecutamos:

```bash
apt-get install isc-dhcp-server
```

Cuando instalamos el servidor por primera se produce un error, ya que no está configurado. Puedes ver los errores producidos por el servidor en el fichero `/var/log/syslog` o `systemctl -u isc-dhcp-server`.
{: .notice--info}

## Configuración del servidor isc-dhcp-server

Lo primero que tenemos que hacer es configurar el interfaz de red por el que va a trabajar el servidor dhcp, para ello editamos el siguiente fichero `/etc/default/isc-dhcp-server`.

Donde configuramos el parámetro interfaces, por ejemplo:
	
```
INTERFACES="eth1"
```
 
El fichero principal de configuración del servidor es `/etc/dhcp/dhcpd.conf`.

El fichero de configuración está dividido en dos partes:

* Parte principal (valores por defecto): especifica los parámetros generales que definen la concesión y los parámetros adicionales que se proporcionarán al cliente.
* Secciones (concretan a la principal)
     * Subnet: Especifican rangos de direcciones IPs que serán cedidas a los clientes que lo soliciten.
     * Host: Especificaciones concretas de equipos.

En la parte principal podemos configurar los siguientes parámetros, que más tarde podremos reescribir en las distintas secciones:

Parámetros de tiempos:

  * `max-lease-time`: Es el tiempo máximo en segundos de concesión que un cliente puede solicitar. Si por ejemplo, un cliente solicita una concesión de 900 segundos pero el tiempo máximo es de 600 segundos, la concesión tendrá una duración de 600 segundos. No tiene por qué ser T3 o temporizador de alquiler.
  * `min-lease-time`: Es el tiempo mínimo en segundos de concesión que un cliente puede solicitar. Si por ejemplo, un cliente solicita una concesión de 900 segundos pero el tiempo mínimo es de 1200 segundos, la concesión tendrá una duración de 1200 segundos.
  * `default-lease-time`: Es el tiempo por defecto en segundos de concesión que se le asignará a un cliente en caso de que éste no haya solicitado ningún periodo en concreto. No confundir con **T1 o temporizador de renovación de alquiler**.
  * `option dhcp-renewal-time`: Es el tiempo en segundos que ha de transcurrir hasta que el cliente pase al estado RENEWAL. También conocido como **T1 o temporizador de renovación de alquiler**. No confundir con `default-lease-time`.
  * `option dhcp-rebinding-time`: Es el tiempo en segundos que ha de transcurrir hasta que el cliente pase al estado REBINDING. También conocido como `T2 o temporizador de reenganche`.

Parámetros de configuración:

  * `option routers`: Indicamos la dirección red de la puerta de enlace que se utiliza para salir a internet.
  * `option domain-name-servers`: Se pone las direcciones IP de los servidores DNS que va a utilizar el cliente.
  * `option domain­-name`: Nombre del dominio que se manda al cliente.
  * `option subnet­mask`: Subred enviada a los clientes.
  * `option broadcast-­address`: Dirección de difusión de la red.

Al indicar una sección subnet tenemos que indicar la dirección de la red y la mascara de red y entre llaves podemos poner los siguientes parámetros:

* `range`: Indicamos el rango de direcciones IP que vamos a asignar.
* Algunos de los parámetros que hemos explicado en la sección principal.

Ejemplo de configuración de la sección subnet puede ser:

```bash
subnet 192.168.0.0 netmask 255.255.255.0 {
  range 192.168.0.60 192.168.0.90;
  option routers 192.168.0.254;
  option domain-name-servers 80.58.0.33, 80.58.32.9;
}
```
	
Reinciciamos el servidor dhcp:

```bash
systemctl restart isc-dhcp-server
```

Sólo falta configurar los clientes para que tomen la configuración de red de forma dinámica.

En Windows la instrucción ``ipconfig /release`` libera la concesión, la instrucción ``ipconfig /renew`` la renueva. En linux el comando para liberar la concesión es ``dhclient -r`` y el que nos permite renovarla será ``dhclient``.
{: .notice--info}

Cuando el servidor va respartiendo la configuración a los clientes va guardando las concesiones en el fichero `/var/lib/dhcp/dhcpd.leases`.

## Creación de reservas

Veamos la sección `host`, en ella configuramos un host para reservar una dirección IP para él.

En una sección `host` debemos poner el nombre que identifica al host y los siguientes parámetros:

* ``hardware ethernet``: Es la dirección MAC de la tarjeta de red del host.
* ``fixed-address``: La dirección IP que le vamos a asignar. 
* Podemos usar también las opciones ya explicadas en la sección principal.

Por ejemplo:

```bash
host macaco {
  hardware ethernet 00:19:de:ad:ba:be;
  fixed-address 192.168.1.5;
}
```