---
title: "Clase 2: Configuración del cliente VPN "
---

## ¿Qué vas a aprender en esta clase?

* A generar un certificado x509 y solicitar que sea firmado por la Autoridad Certificadora del IES Gonzalo Nazareno.
* A configurar el cliente OpenVPN en tu equipo de trabajo para conectar a la red del instituto y poder acceder a proxmox y openstack desde casa.


## Ejercicio 


Vamos a configurar el cliente VPN. Para poder acceder a la red local desde el exterior, existe una red privada configurada con OpenVPN que utiliza certificados x509 para autenticar los usuarios y el servidor. 

Desde el cliente OpenVPN (en casa) nos conectaremos (puerto 1194/tcp) a `macaco.gonzalonazareno.org` (servidor contratado en OVH), que a su vez está conectado a nuestra red del instituto usando la fibra óptica del instituto (puerto 10001/tcp).

Necesitamos dos cosas: disponer de un certificado x509 para nuestro equipo firmado por la **CA Gonzalo Nazareno** y configurar el cliente OpenVPN para que se conecte a `macaco.gonzalonazareno.org`.


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

	Se sube el correspondiente fichero csr mediante la aplicación [Gestiona](https://dit.gonzalonazareno.org/gestiona), dentro del menú **Utilidades -> Certificados**. Se tiene que subir como **Certificado de equipo**. Una vez firmado el fichero csr aparecerá un fichero con extensión crt que se corresponde con el certificado firmado por la autoridad certificadora del Gonzalo Nazareno. Ese fichero lo puedes guardar en `/etc/openvpn/certs`

3. [Descargar](https://dit.gonzalonazareno.org/gestiona/info/documentacion/ca) el certificado de la **CA Gonzalo Nazareno**. Este fichero se llama `gonzalonazareno.crt`. 

4. Configuración de OpenVPN
	* Instalamos el cliente OpenVPN:
		```
		apt install openvpn
		```
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
		log /var/log/openvpn-macaco.log
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
		172.22.0.0/16 via 172.201.0.x dev tun0 
		...
		```

		Si no funciona el túnel comprueba los mensajes de error en el fichero `/var/log/openvpn-macaco.log`.
	
	* **Nota importante**: El servicio vpn no está habilitado, por lo tanto debemos indicarlo cada vez que arranquemos el ordenador (también podemos configurarlo a través de network-manager).
	
		
{% capture notice-text %}

## ¿Qué tienes que entregar?

1. Desde casa, una vez configurado e iniciado el cliente OpenVPN: la IP del interfaz `tun0`, la ruta que nos permite acceder a la red `172.22.0.0/16` y un ping a la puerta de enlace, a la dirección `172.22.0.1`.
2. El acceso a unas de las instancias de OpenStack.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
