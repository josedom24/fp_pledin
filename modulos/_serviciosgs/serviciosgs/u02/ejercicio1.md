---
title: "Ejercicio: Instalación y configuración del servidor dhcp en linux"
permalink: /serviciosgs/u02/ejercicio1.html
---

Después de leer la documentación, instala el servidor dhcp. Recuerda que al inicializar el servicio nos dará un error, esto es debido a que no hemos configurado el servidor.

## Instalación del servidor isc-dhcp-server


Para instalar nuestro servidor dhcp ejecutamos:

```bash
apt-get install isc-dhcp-server
```

Cuando instalamos el servidor por primera se produce un error, ya que no está configurado. Puedes ver los errores producidos por el servidor en el fichero /var/log/syslog
{: .notice--info}

## Configuración del servidor isc-dhcp-server

Lo primero que tenemos que hacer es configurar el interfaz de red por el que va a trabajar el servidor dhcp, para ello editamos el siguiente fichero `/etc/default/isc-dhcp-server`.

Donde configuramos el parámetro interfaces, por ejemplo:
	
```bash
INTERFACES="eth1"
```
 
El fichero principal de configuración de DHCP es `/etc/dhcp/dhcpd.conf`.

El fichero de configuración está dividido en dos partes:

* Parte principal (valores por defecto): especifica los parámetros generales que definen la concesión y los parámetros adicionales que se proporcionarán al cliente.
* Secciones (concretan a la principal)
     * Subnet: Especifican rangos de direcciones IPs que serán cedidas a los clientes que lo soliciten.
     * Host: Especificaciones concretas de equipos.

En la parte principal podemos configurar los siguientes parámetros, que más tarde podremos reescribir en las distintas secciones:

* ``max-lease-time``: Tiempo de la concesión de la dirección IP
* ``default-lease-time``: Tiempo de renovación de la concesión
* ``option routers``: Indicamos la dirección red de la puerta de enlace que se utiliza para salir a internet.
* ``option domain-name-server``: Se pone las direcciones IP de los servidores DNS que va a utilizar el cliente.
* ``option domain­-name``: Nombre del dominio que se manda al cliente.
* ``option subnet­mask``: Subred enviada a los clientes.
* ``option broadcast-­address``: Dirección de difusión de la red.

Al indicar una sección subnet tenemos que indicar la dirección de la red y la mascara de red y entre llaves podemos poner los siguientes parámetros:

* ``range``: Indicamos el rango de direcciones IP que vamos a asignar.
* Algunos de los parámetros que hemos explicado en la sección principal.

Ejemplo de configuración de la sección subnet puede ser:

```bash
subnet 192.168.0.0 netmask 255.255.255.0 {
  range 192.168.0.60 192.168.0.90;
  option routers 192.168.0.254;
  option domain-name-server 80.58.0.33, 80.58.32.9;
}
```
	
Reinciciamos el servidor dhcp:

```bash
service isc-dhcp-server restart
```

Sólo falta configurar los clientes para que tomen la configuración de red de forma dinámica.

En Windows la instrucción ``ipconfig /release`` libera la concesión, la instrucción ``ipconfig /renew`` la renueva. En linux el comando para liberar la concesión es ``dhclient -r`` y el que nos permite renovarla será ``dhclient``.
{: .notice--info}

**Ejercicios**
{: .notice--warning}

1. Configura el servidor dhcp con las siguientes características
	* Rango de direcciones a repartir: 192.168.0.100 - 192.168.0.110 
	* Máscara de red: 255.255.255.0
	* Duración de la concesión: 1 hora
	* Puerta de enlace: 192.168.0.1
	* Servidores DNS: 8.8.8.8, 8.8.4.4
2. Configura los clientes para obtener direccionamiento dinámico. Comprueba las configuraciones de red que han tomado los clientes. Visualiza el fichero del servidor donde se guarda las configuraciones asignadas.
{: .notice--warning}

## Creando reservas

Veamos la sección host, en ella configuramos un host para reservar una dirección IP para él.

En una sección host debemos poner el nombre que identifica al host y los siguientes parámetros:

* ``hardware ethernet``: Es la dirección MAC de la tarjeta de red del host.
* ``fixed-address``: La dirección IP que le vamos a asignar. 
* Podemos usar también las opciones ya explicadas en la sección principal.

**Ejercicios**	
1. Crea en el servidor dhcp una sección HOST para conceder a un cliente una dirección IP determinada (por ejemplo la 192.168.0.105)
2. Obtén una nueva dirección IP en el cliente y comprueba que es la que has asignado por medio de la sección host.
{: .notice--warning}

**Realiza las siguientes comprobaciones**
Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstacia, para ello vamos a poner un tiempo de conseción muy bajo.
1. Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
2. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
{: .notice--warning}