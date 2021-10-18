---
title: "Ejercicio 1: Instalación y configuración del servidor dhcp en linux"
---

Crea una infraestructura que te permita tener una máquina donde instalar un servidor dhcp y un cliente que se configuren para tomar la configuración de forma dinámica.

**Ejercicios**

1. Configura el servidor dhcp con las siguientes características
	* Rango de direcciones a repartir: 192.168.0.100 - 192.168.0.110 
	* Máscara de red: 255.255.255.0
	* Duración de la concesión: 1 hora
	* Puerta de enlace: 192.168.0.1
	* Servidores DNS: 8.8.8.8, 8.8.4.4
2. Configura los clientes para obtener direccionamiento dinámico. Comprueba las configuraciones de red que han tomado los clientes. 

{% capture notice-text %}
## Entrega

1. Entrega la configuración del servidor DHCP.
2. Muestra la lista de concesiones en el servidor. 
3. Muestra la modificación en la configuración que has hecho en el cliente para que tome la configuración de forma automática.
4. Muestra la salida del comando ` ip address` en el cliente.
5. Nuestro servidor DHCP ha cambiado la ruta por defecto del cliente, así que ahora es necesario que actúe como router NAT.  
Tras hacerlo, ya puedes mostrar una comprobación de resolución DNS en el cliente.

{% endcapture %}   
<div class="notice--info">{{ notice-text | markdownify }}</div>

