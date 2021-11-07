---
title: Ficheros importantes en la resolución de nombres
---
## /etc/nsswitch.conf

Hay varios mecanismos de resolución de nombres y los que utilice una máquina GNU/Linux se especifican en el fichero ``/etc/nsswitch.conf``, que contiene una línea como::

	hosts: files dns

que indica los métodos que se van a utilizar para la resolución de nombres de equipos y el orden en el que se va a hacer, es decir, en primer lugar se va a consultar el fichero ``/etc/hosts`` y si no se consigue resolver el nombre del equipo se va a consultar a los servidores DNS que estén configurados en el fichero ``/etc/resolv.conf``.

## /etc/hosts

Fichero para la resolución estática de nombres (normalmente de la red local).

Las líneas de ``/etc/hosts`` tienen el formato:

	dirección_IP nombre_largo nombre_corto
	127.0.0.1 localhost.localdomain localhost
	192.168.45.123 sauron.mordor.com sauron


## /etc/resolv.conf

Fichero que especifica los servidores DNS y los dominios de búsqueda.

Ejemplo:

	domain osmosislatina.com 
	search osmosislatina.com supple.com telmex.net 
	nameserver 124.13.24.1 
	nameserver 124.13.17.2
	nameserver 64.12.45.12
	sortlist 124.13.24.0/255.255.255.0 64.0.0.0

La parte más importante de este archivo son los parámetros  ``nameserver``, estos indican  cuales  son las direcciones IP de los servidores DNS que deben ser utilizados. La sección  ``sortlist``  aunque opcional es utilizada para indicar la preferencia de los  nameserver's , esto garantiza que el servidor DNS en  124.13.24.1  tendrá preferencia sobre todos los demás, esta preferencia se puede deber a cercanía o capacidad del "Host"

El parámetro  ``domain``  indica el dominio al cual pertenece el "Host", en este caso  ``osmosislatina.com``, mientras que el parámetro ``search`` es utilizado como un auxiliar para la resolución de nombres, esto es, si se ejecuta el comando: ``ssh lejano``, al momento que se utilice la resolución DNS, éste agregará los dominios que se encuentren en  ``search``, intentará  ``ssh lejano.osmosislatina.com``,  ``ssh lejano.hostway.com``...lo anterior ahorra tiempo de escritura al usuario final.

