---
title: "Taller 0: Configuración del cliente VPN"
---

## ¿Qué vas a aprender en este taller?

* A generar un certificado x509 y solicitar que sea firmado por la Autoridad Certificadora del IES Gonzalo Nazareno.
* A configurar el cliente OpenVPN en tu equipo de trabajo para conectar a la red del instituto y poder acceder a proxmox y openstack desde casa.


## ¿Qué tienes que hacer?


### Configuración del cliente VPN

Para poder acceder a la red local desde el exterior, existe una red privada configurada con OpenVPN que utiliza certificados x509 para autenticar los usuarios y el servidor. 

Desde el cliente OpenVPN (en casa) nos conectaremos (puerto 1194/tcp) a ~~`satelite.gonzalonazareno.org`~~`macaco.gonzalonazareno.org` (servidor contratado en OVH), que a su vez está conectado a nuestra red del instituto usando la fibra óptica del instituto (puerto 10001/tcp).

Necesitamos dos cosas: disponer de un certificado x509 para nuestro equipo firmado por la **CA Gonzalo Nazareno** y configurar el cliente OpenVPN para que se conecte a ~~**satelite**~~ **macaco**.


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

	Se sube el correspondiente fichero csr mediante la aplicación [Gestiona](https://dit.gonzalonazareno.org/gestiona), dentro del menú **Utilidades -> Certificados**. Se tiene que subir como **Certificado de equipo**. Una vez firmado el fichero csr aparecerá un fichero con extensión crt que se corresponde con el certificado firmado por la autoridad certificadora del Gonzalo Nazareno. Ese fichero lo puedes guardar en /etc/openvpn/certs`

3. [Descargar](https://dit.gonzalonazareno.org/gestiona/info/documentacion/ca) el certificado de la **CA Gonzalo Nazareno**. Este fichero se llama `gonzalonazareno.crt`. ~~Una vez descargado y para evitar que estés usando otro de cursos pasos asegúrate que la fecha de caducidad del certificado es 2034, para ello si lo hemos guardado `/etc/ssl/certs/gonzalonazareno.crt` ejecuta la siguiente instrucción:~~

	```
	# openssl x509 -text -noout -in /etc/ssl/certs/gonzalonazareno.crt
	...
	Validity
            Not Before: Sep  4 11:05:13 2024 GMT
            Not After : Sep  2 11:05:13 2034 GMT
	```

3. Configuración de OpenVPN

	* Instalamos el cliente OpenVPN:

		```
		apt install openvpn
		```
	
	* 

	* Creamos el siguiente fichero con extensión `.conf` (exigencia de OpenVPN) en el directorio `/etc/openvpn/client`:
		```
		dev tun
		remote macaco.gonzalonazareno.org
		pull
		proto tcp-client
		tls-client

		ca /etc/ssl/certs/gonzalonazareno.crt 
		cert /etc/openvpn/certs/[nombredemimaquina].crt 
		key /etc/ssl/private/[nombredemimaquina].key 
		
		keepalive 10 60
		log /var/log/openvpn-satelite.log
		verb 1
		```
	* Inicia OpenVPN:
	
		```
		# systemctl start openvpn-client@[nombre del fichero de configuración]
		```

	 	Comprueba que se haya creado el túnel y que se ha añadido una regla de encaminamiento adicional para acceder a los equipos de la `172.22.0.0/16`:
		
		```
		$ ip r
		...
		172.22.0.0/16 via 172.29.0.x dev tun0 
		...
		```

		Si no funciona el túnel comprueba los mensajes de error en el fichero `/var/log/openvpn-satelite.log`.
	
	* **Nota importante**: El servicio vpn no está habilitado, por lo tanto debemos indicarlo cada vez que arranquemos el ordenador (también podemos configurarlo a través de network-manager).
	
	* ~~Es también conveniente actualizar el fichero `/etc/hosts` para realizar resolución estática de las máquinas más usadas del centro:~~

		```
		172.22.123.100    openstack.gonzalonazareno.org
		172.22.123.1      proxmox.gonzalonazareno.org
		```
	
{% capture notice-text %}

## ¿Qué tienes que entregar?

1. Desde casa, una vez configurado e iniciado el cliente OpenVPN: la IP del interfaz `tun0`, la ruta que nos permite acceder a la red `172.22.0.0/16` y un ping a la puerta de enlace, a la dirección `172.22.0.1`.
2. El contenido del fichero para hacer la resolución estática y un pantallazo del acceso desde un navegador web a `openstack.gonzalonazareno.org` desde casa ~~(**No te debe pedir autentificación**)~~.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
