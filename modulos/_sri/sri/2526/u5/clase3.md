---
title: "Clase 3: Instalación y configuración de un servidor DNS esclavo"
---

## ¿Qué vas a aprender en esta clase?

* Configurar un servidor DNS de respaldo.
* Entender el proceso de transferencia de zona por el que se sincronizan los dos servidores DNS.
* Usar distintos comandos para verificar si la configuración de los servidores DNS es correcta.

## ¿Qué tienes que hacer?

Un **servidor DNS esclavo** contiene una réplica de las zonas del servidor maestro. Se debe producir una **transferencia de zona** (el esclavo hace una solicitud de la zona completa al maestro) para que se sincronicen los servidores.

### Configuración del servidor maestro y esclavo

Crea otra máquina que tendrá el rol de **servidor DNS esclavo**. Instala bind9 y nombrarlo de manera adecuada para que tenga el nombre `dns2.tunombre.org`. Voy a suponer que la dirección de esta nueva máquina es la `172.22.200.110`. La transferencia de zona entre maestro y esclavo usa el puerto 53/tcp, ábrelo en el grupo de seguridad.

Por seguridad, sólo debemos aceptar transferencias de zonas hacía los esclavos autorizados, para ello en el fichero `/etc/bind/named.conf.options`, deshabilitamos las transferencias:

	options {
		...
		allow-transfer { none; };
		...

### Configuración de la definición de las zonas

Modificamos la definición de las zona en el servidor DNS maestro. Modificamos el fichero `/etc/bind/named.conf.local`:

	zone "tunombre.org" {
		type master;
		file "db.tunombre.org";
		allow-transfer { 172.22.200.110; };
		notify yes;
	};
	zone "22.172.in-addr.arpa" {
		type master;
		file "db.172.22.0.0";
		allow-transfer { 172.22.200.110; };
		notify yes;
	};

* `allow-tranfer`: Se permite las transferencias de zonas al servidor DNS esclavo (`172.22.200.110`).
* `notify yes`: Cuando se reinicie el servidor DNS maestro se notificará al esclavo que ha habido cambios para que solicite una transferencia de zona.

Modificamos la definición de las zona en el servidor DNS esclavo. Modificamos el fichero `/etc/bind/named.conf.local`:

	include "/etc/bind/zones.rfc1918";
	zone "tunombre.org" {
		type slave;
		file "db.tunombre.org";
		masters { 172.22.200.100; };
	};
	zone "22.172.in-addr.arpa" {
		type slave;
		file "db.172.22.0.0";
		masters { 172.22.200.100; };
	};	

* `type slave`: Se indica que este servidor será esclavo para estas zonas.
* `masters`: Se indica cuál es el maestro, para saber a que servidor hay que solicitar la transferencia de zona.

## Configuración de las zonas

En el servidor DNS maestro añadimos la información del servidor DNS esclavo en las zonas. En la zona de resolución directa, en el fichero `/var/cache/bind/db.tunombre.org` añadimos un nuevo registro `NS` y su correspondiente registro `A`:

	$TTL    86400
	@       IN      SOA     dns1.tunombre.org. root.tunombre.org. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                          86400 )       ; Negative Cache TTL
	;
	@	IN	NS		dns1.tunombre.org.
	@	IN	NS		dns2.tunombre.org.
	@	IN	MX	10	correo.tunombre.org.
	$ORIGIN tunombre.org.
	dns1		IN	A	172.22.200.100
	dns2		IN	A	172.22.200.110
	...

La zona de resolución inverso quedaría de la siguiente forma, modificando el fichero `/var/cache/bind/db.172.22.0.0`:

	$TTL    86400
	@       IN      SOA     dns1.tunombre.org. root.tunombre.org. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                          86400 )       ; Negative Cache TTL
	;
	@	IN	NS		dns1.tunombre.org.
	@	IN	NS		dns2.tunombre.org.

	$ORIGIN 22.172.in-addr.arpa.
	100.200		IN	PTR		dns1.tunombre.org.
	110.200		IN	PTR		dns2.tunombre.org.
	...

**Nota: La información de los registros de las zonas sólo se modifican en el servidor DNS maestro. Estás modificaciones se copia en el esclavo por medio de una transferencia de zona**.

## Comprobación de errores

Reinicia el servidor DNS maestro y esclavo. Puedes ver en el esclavo que se han producidos las transferencias de zonas:


	root@dns2:~# systemctl restart bind9
	root@dns2:~# journalctl -u named
	... dns2 named[5739]: zone 22.172.in-addr.arpa/IN: transferred serial 1
	... dns2 named[5739]: transfer of '22.172.in-addr.arpa/IN' from 172.22.200.100#53: Transfer status: success
	... dns2 named[5739]: transfer of '22.172.in-addr.arpa/IN' from 172.22.200.100#53: Transfer completed: ...
	... dns2 named[5739]: managed-keys-zone: Key 20326 for zone . acceptance timer complete: key now trusted
	... dns2 named[5739]: resolver priming query complete
	... dns2 named[5739]: zone tunombre.org/IN: Transfer started.
	... dns2 named[5739]: transfer of 'tunombre.org/IN' from 172.22.200.100#53: connected using 172.22.200.110#58461
	... dns2 named[5739]: zone tunombre.org/IN: transferred serial 1
	... dns2 named[5739]: transfer of 'tunombre.org/IN' from 172.22.200.100#53: Transfer status: success
	... dns2 named[5739]: transfer of 'tunombre.org/IN' from 172.22.200.100#53: Transfer completed: ...

Si al reiniciar los servidores DNS tienes algún error, puedes detectar errores de sintaxis usando los siguientes comandos:

* `named-checkzone tunombre.org /var/cache/bind/db.tunombre.org`: Para comprobar la configuración de la zona directa.
* `named-checkzone 22.172.in-addr.arpa /var/cache/bind/db.172.22.0.0`: Para comprobar la configuración de la zona inversa.
* Para detectar errores de configuración en `named.conf`, podemos usar: `named-checkconf`.


## ¿Cuándo se hacen las copias?

* Los esclavos interrogan al maestro periódicamente, ésto es el "**Intervalo de actualización" (refresh interval)**, para obtener actualizaciones.
* El maestro también puede notificar a los esclavos cuando hay cambios (**`notify yes;`**), pero como puede haber pérdida de paquetes sigue siendo necesario interrogar periódicamente.
* El esclavo sólo iniciará la copia cuando el número de serie, configurado en el registro SOA de la zona, **AUMENTE**.
* Formato recomendado: **YYMMDDNN**
* Si se decrementa el número de serie, los esclavos nunca se actualizarán hasta que el número sea mayor que el valor anterior.

## Información en el registro SOA

	@       IN      SOA     dns1.tunombre.org. root.tunombre.org. (
	                              1         ; Serial
	                         604800         ; Refresh
	                          86400         ; Retry
	                        2419200         ; Expire
	                          86400 )       ; Negative Cache TTL

* El **intervalo de actualización (refresh)**: frecuencia con la que el esclavo debe revisar el número de serie del maestro para hacer una transferencia de zona.
* **Intervalo de reintento (retry)**: frecuencia con la que reintenta si el servidor maestro no responde.
* **Tiempo de caducidad (expiry)**: Si el esclavo no puede comunicarse con el maestro durante este intervalo, debe borrar su copia de la zona.
* **TTL negativo (negative)**: Significa tiempo de vida negativo, el tiempo durante el cual se debe almacenar en la cache de cualquier otro servidor DNS una respuesta negativa. Eso significa que si otro servidor DNS preguntas por `no-existe.example.com` y esa entrada no existe, ese servidor DNS considerará como válida esa respuesta (no existe) durante el tiempo indicado.

## Algunos trucos adicionales

* Puedes manejar el servidor DNS con el comando `rndc`. Por ejemplo `rndc reload`: reinicia el servicio; `rndc reload tunombre.org`: Reinicia sólo esa zona; `rndc flush`: Borra la caché de resoluciones guardadas en el servidor.
* Realiza una consulta al servidor maestro y el esclavo para comprobar que las respuestas son autorizadas (bit `AA`), además asegúrate que coinciden los números de serie:

	dig +norec @x.x.x.x tunombre.org. soa
		
* Solicita una copia completa de la zona y comprueba que sólo se puede hacer desde el esclavo:

	dig @x.x.x.x tunombre.org. axfr

* **Cada vez que realices una modificación en el servidor DNS maestro recuerda incrementar el número de serie**.

{% capture notice-text %}
## ¿Qué tienes que hacer?

* Configura el cliente con los dos servidores DNS. Para ello en su fichero `/etc/resolv.conf` utiliza dos directivas `nameserver`. Si hacemos una consulta desde un cliente, y el dns maestro no responde, responderá el esclavo. Prueba a realizar una consulta. ¿Quién ha respondido?. Apaga el servidor maestro, y vuelve a hacer la misma consulta. ¿Ha respondido el servidor DNS esclavo?
* Vamos a modificar la información de la zona. Para ello vamos a modificar en el servidor DNS maestro y en su fichero `/var/cache/bind/db.tunombre.org` vamos a añadir un nuevo registro:
``` 
	...
		prueba		IN	A	172.22.200.120
```
* **Recuerda incrementar el número de serie, para que al reiniciar el servidor DNS maestro se produzca la transferencia de zona.**
* Desde el cliente realiza una consulta para preguntar por la dirección IP de `prueba.tunombre.org`. ¿Quién ha respondido?. Apaga el servidor maestro, y vuelve a hacer la misma consulta. ¿Ha respondido el servidor DNS esclavo?. Comprueba en el esclavo que se ha producido la transferencia.


{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

 

{% capture notice-text %}	
## Importante

* Realiza el ejercicio que te va a proponer el profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
		
