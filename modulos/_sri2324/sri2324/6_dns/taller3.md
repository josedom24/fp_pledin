---
title: "Taller 3: Delegación de subdominios con bind9"
---

## ¿Qué vas a aprender en este taller?

* Entender el concepto de delegación de dominio.
* Configurar un servidor DNS para delegar un subdominio en otro servidor DNS.
* Realizar consultas a los nombres del dominio delegado.

## ¿Qué tienes que hacer?

1. Crea una nueva máquina e instala un servidor DNS bind9, será el servidor DNS con autoridad para la zona delegada que será `informatica.tunombre.org`. Nombra de manera adecuada esta máquina para que tenga el nombre `dns.informatica.tunombre.org`. Voy a suponer que la dirección de esta nueva máquina es la `172.22.200.120`.

	* Tendremos el servidor `dns1.tunombre.org` (y el esclavo `dns2.tunombre.org`) con autoridad para la zona `tunombre.org`. En esta zona, por ejemplo, puede existir el nombre `www.tunombre.org`.
	* Tendremos el servidor `dns.informatica.tunombre.org` con autoridad sobre el subdominio delegado, es decir tendrá autoridad para la zona `informatica.tunombre.org`.  En esta zona, por ejemplo, puede existir el nombre `www.informatica.tunombre.org`.

2. Vamos a realizar la delegación de autoridad para el subdominio en el servidor DNS principal (en `dns1.tunombre.org`) para ello modificamos el fichero `/var/cache/bind/db.tunombre.org` añadiendo las siguientes líneas donde realizamos la delegación:

		...
		$ORIGIN informatica.tunombre.org.
		@		IN	 NS		dns
		dns 	IN	 A 		172.22.200.120

	* El parámetro `$ORIGIN` nos permite usar nombres no cualificados totalmente.
	* Indicamos que el servidor con autoridad para la zona `informatica.tunombre.org` (registro `NS`), es `dns.informatica.tunombre.org`.
	* Y se indica la dirección IP del servidor DNS.
	* **Si incrementas el número de serie la delegación que hemos realizado se transferirá al servidor DNS esclavo.**
	
3. Ahora vamos a configurar el servidor DNS delegado. Por lo tanto en el servidor `dns.informatica.tunombre.org` creamos una nueva zona en el fichero `/etc/bind/named.conf.local`:

		zone "informatica.tunombre.org" {
			type master;
			file "db.informatica.tunombre.org";
		};

	Y creamos la zona en el fichero `db.informatica.tunombre.org`:

		$TTL    86400
		@       IN      SOA     dns.informatica.tunombre.org. root.informatica.tunombre.org. (
		                              1         ; Serial
		                         604800         ; Refresh
		                          86400         ; Retry
		                        2419200         ; Expire
		                          86400 )       ; Negative Cache TTL
		;
		@	IN	NS		dns.informatica.tunombre.org.
		@	IN	MX	10	mail.informatica.tunombre.org.

		$ORIGIN informatica.tunombre.org.

		dns			IN	A		172.22.200.120
		mail			IN	A		172.22.200.121 
		web			IN	A 		172.22.200.122
		www			IN 	CNAME 		web
		...


4. No modifiques el fichero `/etc/resolv.conf` del cliente, es decir, las consultas se hacen al servidor DNS principal, cuando preguntemos por un nombre en la zona delegada el servidor DNS principal, preguntará al servidor DNS delegado y guardara la respuesta en su caché. Pregunta por la dirección ip del nombre `www.informatica.tunombre.org`. ¿Quién ha respondido?. 

{% capture notice-text %}	
## ¿Qué tienes que entregar?

1. Una captura de pantalla donde se vea la consulta para averiguar la dirección IP de `www.informatica.tunombre.org`.
2. Una captura de pantalla donde se vea la consulta para averiguar el servidor DNS con autoridad para la zona del dominio `informatica.tunombre.org`. ¿Es el mismo que el servidor DNS con autoridad para la zona `tunombre.org`?
3. Una captura de pantalla donde se vea la consulta para averiguar el servidor de correo configurado para `informatica.tunombre.org`.
4. Realiza el ejercicio que te va a proponer el profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
