---
title: "Clase 2: Instalación y configuración del servidor bind9 en nuestra red local"
---

## ¿Qué vas a aprender en est a clase?

* Instalar un servidor DNS `bind9`.
* Crear una zona de resolución directa en nuestro servidor DNS.
* Crear una zona de resolución inversa en nuestro servidor DNS.
* Realizar consultas sobre el servidor DNS.

## ¿Qué tienes que hacer?

Crea una máquina (configúrala para que se llame `dns1.tunombre.org`). Ejecuta el comando `hostname -f` para comprobar que el nombre FQDN se ha configurado de forma adecuada.
En esta máquina vamos a instalar un servidor DNS `bind9`.

### Configuración inicial del servidor DNS

De principio no es necesario ninguna configuración para que el servidor funcione como servidor recursivo/caché. Sin embargo vamos a hacer una pequeña configuración:

* Para que no se intente resolver usando la dirección ipv6 de los servidores DNS, vamos a modificar la opción `OPTION` en el fichero de configuración `/etc/default/named` con las siguientes opciones:
	```
	OPTIONS="-4 -f -u bind"
	```
* Además tienes que tener en cuenta que el servidor bind9 sólo permite consultas desde la misma red local, si por ejemplo estamos en casa y con la VPN queremos hacer una consulta, se estaría realizando desde otra red, en este caso, en el fichero `/etc/bind/named.conf.options` debemos configurar el parámetro `allow-query`:
	```
	allow-query {172.201.0.0/16; 172.22.0.0/16;};
	```
* Desactivamos, en el mismo fichero, la validación DNSSEC, que es un sistema de seguridad para proteger nuestro servidor, para ello cambiamos la siguiente directiva:
	```
	dnssec-validation no;
	```

{% capture notice-text %}

Reiniciamos el servidor, y ya  está funcionando, para ello realiza la siguiente consulta desde tu ordenador: `dig @<IP de tu servidor DNS> www.josedomingo.org`.
* ¿Cuánto ha tardado en realizar la consulta? ¿Qué consultas se han realizado para averiguar la dirección IP? 
* Realiza de nuevo la consulta. ¿Cuánto ha tardado ahora? ¿Por qué ha tardado menos? ¿Qué consultas se han realizado para averiguar la dirección IP?
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

### Creación de la zona de resolución directa

Vamos a crear una zona directa para el dominio `tunombre.org`, para ello vamos a añadir en el fichero `/etc/bind/named.conf.local` la definición de la zona:

	zone "tunombre.org" {
		type master;
		file "db.tunombre.org";
	};

* Es una zona de tipo maestra.
* La información de la zona se guardará en el fichero `db.tunombre.org` que estará en `/var/cache/bind9`.

Vamos a crear el fichero de zona en el fichero `/var/cache/bind/db.tunombre.org` (podríamos copiar el fichero `/etc/bind/db.empty` que nos puede servir como plantilla). El contenido de este fichero quedaría (**Cambia la dirección de tu servidor `dns1.tunombre.org` para poner la dirección IP real**):

	$TTL    86400
	@       IN      SOA     dns1.tunombre.org. root.tunombre.org. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                          86400 )       ; Negative Cache TTL
	;
	@	IN	NS		dns1.tunombre.org.
	@	IN	MX	10	correo.tunombre.org.
	$ORIGIN tunombre.org.
	dns1			IN	A	172.22.XX.XX
	correo			IN	A	172.22.200.101
	asterix		IN	A	172.22.200.102
	obelix			IN	A	172.22.200.103
	www			IN	CNAME	asterix
	informatica		IN	CNAME	asterix
	ftp			IN	CNAME	obelix

* **Todos los nombres de dominios acaban en PUNTO.**
* `$TTL`: Tiempo en segundos (24 horas) que la resolución se va a guardar en una caché intermedia. 
* Registro `SOA`: *Start of Authoritive*, contiene información sobre la zona: el nombre del servidor DNS maestro, el correo de la persona responsable de la zona (sin la @), un número de serie (que ya estudiaremos) y unos tiempos que ya estudiaremos.
* La `@` sustituye al nombre de dominio. 
* Por lo tanto el servidor DNS con autoridad (registro `NS`) para **este dominio** (ya que tiene la `@` delante) es `dns1.tunombre.org`.
* Registro `MX`: Es el nombre del servidor de correo electrónico al que hay que mandar el correo cuando el destinatario es del dominio `tunombre.org`. Podemos tener varios registros `MX`, siendo el número que indicamos la prioridad de envío (más pequeño más prioritario).
* `ORIGIN`: No es obligatorio. A partir de la esta línea los nombres no hay que ponerlos cualificados (es decir, se pueden poner los nombres sin el dominio).
* A continuación se van añadiendo los registros: `A` para indicar direcciones IPv4, `CNAME` para indicar alias.
* Los nombres de las **máquinas físicas** (que tienen dirección IP) se suelen indicar usando registros `A`.
* Los nombres de los **servicios** se suelen indicar con registros `CNAME`.
* Por ejemplo, tenemos una máquina física que se llama `asterix` que tiene dos servicios (parece que es un servidor web) `www` y `informatica`.
* Por ejemplo, el servicio `ftp` está alojado en la máquina física `obelix`.


{% capture notice-text %}
## ¿Qué tienes que hacer?

* Modifica la zona para que el servidor DNS tenga la IP real de tu máquina.
* Configura tu DNS en otra máquina, y realiza las siguientes consultas a tu servidor DNS:
	* Dirección IP de una máquina o servicio de tu dominio.
	* Servidor DNS con autoridad del dominio.
	* Servidor de correo del dominio.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

### Creación de la zona de resolución inversa

Vamos a crear una zona inversa. suponemos que estamos trabajando en la red `172.22.0.0/16`. Lo primero es determinar el nombre de esta zona:

* El nombre de dominio será `<los números de la IP correspondiente a la red ordenados de forma inversa>.in-addr.arpa`.
* Si la máscara de red es 16 los dos primeros números de la dirección corresponde a la red y los dos último corresponden a la máquina. Por lo tanto, en nuestra red `172.22.0.0/16` el nombre de dominio sería `22.172.in-addr.arpa`.
* Si la máscara de red es 24, por ejemplo si la dirección de red es `192.168.0.0/24`, el nombre sería `0.168.192.in-addr.arpa`.

Por lo tanto en el fichero `/etc/bind/named.conf.local` añadimos la definición de la zona:

	zone "22.172.in-addr.arpa" {
		type master;
		file "db.172.22.0.0";
	};

Además tenemos que descomentar la línea `include "/etc/bind/zones.rfc1918";`, de esta manera se incluirán todas las zonas correspondientes a las redes privadas para que no se pregunten por ellas al servidor DNS raíz. Como nosotros estamos definiendo la zona `22.172.in-addr.arpa`, en ese fichero deberemos comentar su definición:

	...
	zone "21.172.in-addr.arpa"  { type master; file "/etc/bind/db.empty"; };
	//zone "22.172.in-addr.arpa"  { type master; file "/etc/bind/db.empty"; };
	zone "23.172.in-addr.arpa"  { type master; file "/etc/bind/db.empty"; };
	...

Vamos a crear el fichero de zona inversa en el fichero `/var/cache/bind/db.172.22.0.0`:

	$TTL    86400
	@       IN      SOA     dns1.tunombre.org. root.tunombre.org. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                          86400 )       ; Negative Cache TTL
	;
	@	IN	NS		dns1.tunombre.org.

	$ORIGIN 22.172.in-addr.arpa.
	XX.XX			IN	PTR		dns1.tunombre.org.
	101.200		IN	PTR		correo.tunombre.org.
	102.200		IN 	PTR		asterix.tunombre.org.
	103.200		IN 	PTR		obelix.tunombre.org.
		

* El registro `SOA` es **igual que el de la zona de resolución directa.**
* El registro `NS` es **igual que el de la zona de resolución directa.**
* No tiene registro `MX`.
* El nombre de la máquina en la zona inversa está formado por los números de la IP que corresponden al host colocados de forma inversa. Por ejemplo, si tengo la IP `172.22.200.100` de la red `172.22.0.0/16`, su nombre en la zona inversa será `100.200.22.172.in-addr.arpa`. Como hemos puesto la directiva `$ORIGIN`, el nombre lo ponemos sin dominio, es decir `100.200`. 
* Otro ejemplo, si tuviéramos una máquina con IP `192.168.0.50` de la red `192.168.0.0/24`, su nombre en la zona inversa será `50.0.168.192.in-addr.arpa`. El dominio sería `0.168.192.in-addr.arpa` y el nombre `50`.
* Tenemos un registro `PTR` por cada registro `A` en la zona de resolución directa.
* Los nombres de los servicios (`CNAME`) en la zona de resolución directa no se definen en esta zona.

{% capture notice-text %}
## ¿Qué tienes que hacer?

* Realiza varias consultas inversas sobre el servidor DNS.
	* Utiliza en algunas `dig -x`.
	* Y en otras `dit ptr`.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>



{% capture notice-text %}
## Importante
* Avisa al profesor y enséñale el servidor DNS funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
