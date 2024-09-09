---
title: "Taller 0: Configuración del cliente VPN"
---

## ¿Qué vas a aprender en este taller?

* A generar un certificado x509 y solicitar que sea firmado por la Autoridad Certificadora del IES Gonzalo Nazareno.
* A configurar el cliente OpenVPN en tu equipo de trabajo para conectar a la red del instituto y poder acceder a proxmox y openstack desde casa.


## ¿Qué tienes que hacer?


### Configuración del cliente VPN

Para poder acceder a la red local desde el exterior, existe una red privada configurada con OpenVPN que utiliza certificados x509 para autenticar los usuarios y el servidor. 

Desde el cliente OpenVPN (en casa) nos conectaremos (puerto 1194/tcp) a `sputnik.gonzalonazareno.org` (servidor contratado en OVH), que a su vez está conectado a macaco usando la fibra óptica del instituto (puerto 10001/tcp).

Necesitamos dos cosas: disponer de un certificado x509 para nuestro equipo firmado por la **CA Gonzalo Nazareno** y configurar el cliente OpenVPN para que se conecte a **sputnik**.



Seguimos los siguientes pasos:

1. Creación de una solicitud de firma de certificado (Certificate Signing Request o CSR).
	* Creamos una clave privada RSA de 4096 bits (como `root`):
		```	
		openssl genrsa 4096 > /etc/ssl/private/[nombredemimaquina].key
		```
	
	* Creamos un fichero csr para que sea firmado por la **CA Gonzalo Nazareno**, para lo que tendremos que poner los mismos campos que tiene la entidad:

		```
		openssl req -new -key /etc/ssl/private/[nombredemimaquina].key -out /root/[nombredemimaquina].csr
		```
		
	* Nos pedirá una serie de valores para identificar al certificado, que tendremos que rellenar correctamente y son:
	
		```
		C=ES
		ST=Sevilla
		L=Dos Hermanas
		O=IES Gonzalo Nazareno
		OU=Informatica
		CN=[Nombre del equipo] (debe ser único)
		```

2. Hacer llegar el csr a la entidad certificadora

	Se sube el correspondiente fichero csr mediante la aplicación [Gestiona](https://dit.gonzalonazareno.org/gestiona), dentro del menú **Utilidades -> Certificados**. Se tiene que subir como **Certificado de equipo**. Una vez firmado el fichero csr aparecerá un fichero con extensión crt que se corresponde con el certificado firmado por la autoridad certificadora del Gonzalo Nazareno.

3. Configuración de OpenVPN

	* Instalamos el cliente OpenVPN:

		```
		apt install openvpn
		```
	* Te puedes bajar el certificado de la CA Gonzalo nazareno en este [enlace](https://dit.gonzalonazareno.org/gestiona/info/documentacion/ca).
	
	* Creamos el siguiente fichero con extensión `.conf` (exigencia de OpenVPN) en el directorio `/etc/openvpn`:
		```
		dev tun
		remote sputnik.gonzalonazareno.org
		ifconfig 172.23.0.0 255.255.255.0
		pull
		proto tcp-client
		tls-client
		# remote-cert-tls server
		ca /etc/ssl/certs/gonzalonazareno.crt <- Cambiar por la ruta al certificado de la CA Gonzalo Nazareno (el mismo que utilizamos para la moodle, redmine, etc.)
		cert /etc/openvpn/mut-albertomolina.crt <- Cambiar por la ruta al certificado CRT firmado que nos han devuelto
		key /etc/ssl/private/mut.key <- Cambiar por la ruta a la clave privada, aunque en ese directorio es donde debe estar y con permisos 600
		comp-lzo
		keepalive 10 60
		log /var/log/openvpn-sputnik.log
		verb 1
		```
	* Reinicia OpenVPN, comprueba que se haya creado el túnel y que se ha añadido una regla de encaminamiento adicional para acceder a los equipos de la `172.22.0.0/16`:
		```
		$ ip r
		...
		172.22.0.0/16 via 172.23.0.5 dev tun0 
		...
		```
		También se comprueban los mensajes del fichero `/var/log/openvpn-sputnik.log`:
		```
		2022-09-28 17:23:52 OpenVPN 2.5.1 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on May 14 2021
		2022-09-28 17:23:52 library versions: OpenSSL 1.1.1n  15 Mar 2022, LZO 2.10
		2022-09-28 17:23:52 WARNING: using --pull/--client and --ifconfig together is probably not what you want
		2022-09-28 17:23:52 WARNING: No server certificate verification method has been enabled.  See http://openvpn.net/howto.html#mitm for more info.
		2022-09-28 17:23:52 TCP/UDP: Preserving recently used remote address: [AF_INET]5.39.73.79:1194
		2022-09-28 17:23:52 Attempting to establish TCP connection with [AF_INET]5.39.73.79:1194 [nonblock]
		2022-09-28 17:23:52 TCP connection established with [AF_INET]5.39.73.79:1194
		2022-09-28 17:23:52 TCP_CLIENT link local: (not bound)
		2022-09-28 17:23:52 TCP_CLIENT link remote: [AF_INET]5.39.73.79:1194
		2022-09-28 17:23:52 [sputnik.gonzalonazareno.org] Peer Connection Initiated with [AF_INET]5.39.73.79:1194
		2022-09-28 17:23:53 TUN/TAP device tun0 opened
		2022-09-28 17:23:53 net_iface_mtu_set: mtu 1500 for tun0
		2022-09-28 17:23:53 net_iface_up: set tun0 up
		2022-09-28 17:23:53 net_addr_ptp_v4_add: 172.29.0.34 peer 172.29.0.33 dev tun0
		2022-09-28 17:23:53 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
		2022-09-28 17:23:53 Initialization Sequence Completed
		```
	* **Nota importante**: Como no queremos que se levante el túnel VPN cada vez que encendemos el ordenador deshabilitamos el servicio:

		```
		systemctl disable openvpn.service
		```

		Y lo levantaremos a mano cada vez que sea necesario (también podemos configurarlo a través de network-manager).

	* Es también conveniente actualizar el fichero `/etc/hosts` para realizar resolución estática de las máquinas más usadas del centro:

		```
		172.22.123.100    openstack.gonzalonazareno.org
		172.22.123.1      proxmox.gonzalonazareno.org
		```
	
{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Desde casa, una vez configurado e iniciado el cliente OpenVPN: la IP del interfaz `tun0`, la ruta que nos permite acceder a la red `172.22.0.0/16` y un ping a la puerta de enlace, a `macaco`, a la dirección `172.22.0.1`.
2. El contenido del fichero para hacer la resolución estática y un pantallazo del acceso desde un navegador web a `openstack.gonzalonazareno.org` desde casa (**No te debe pedir autentificación**).

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
