---
title: "Práctica (1 / 3): Virtualización en Linux y servidor DHCP (Parte 2)"
---

{% capture warning-text %}
## Aviso
Antes de comenzar esta práctica, **enseña al profesor el funcionamiento de la práctica anterior**.
{% endcapture %}<div class="warning--info">{{ warning-text | markdownify }}</div>


## Descripción

Vamos as seguir trabajando con el escenario que hemos construido en la práctica anterior. En esta práctica vamos instalar y configurar servicios en las máquinas creadas, en concreto un servidor dhcp y un servidor web.

## Instalación del servidor DHCP 

1. Instala un servidor DHCP en el contenedor **servidorDHCP** con las siguientes características:
	* Rango de direcciones: `192.168.200.10` - `192.168.200.200`.
	* Máscara de red: `255.255.255.0`
	* Duración de la concesión: 30 minutos
	* Puerta de enlace: `192.168.200.1`
	* Servidor DNS: `172.22.0.1`
2. Configura la máquina **cliente1** para que tome configuración de red dinámica y puedas probar que realmente está funcionando el servidor.
3. Conecta una máquina Windows a la **red_intra** y comprueba que también toma direccionamiento dinámico.
4. Realizar una captura, desde el servidor usando `tcpdump`, de los cuatro paquetes que corresponden a una concesión: `DISCOVER`, `OFFER`, `REQUEST`, `ACK`.
5. **Para hacer esta prueba configura un tiempo de concesión bajo**. Los clientes toman una configuración, y a continuación apagamos el servidor DHCP. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
6. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor DHCP (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
7. Actualmente el servidor web **servidorWeb** tiene una configuración de red estática. Vamos a configurar una reserva para esta máquina. Configura de forma adecuada el servidor dhcp para que ofrezca al servidor Web la misma IP (**reserva**) que habíamos configurado de forma estática.
8. Modifica la configuración de red del servidor Web para que tome la configuración de red de forma dinámica.

{% capture notice-text %}
## Entrega

1. Contenido de los ficheros de configuración que has modificado en el servidor DHCP.
2. Una comprobación donde se vea la ip que ha tomado de forma dinámica el **cliente1** y el cliente windows.
3. Una comprobación donde se comprueba que los dos clientes tienen conectividad al exterior.
4. El contenido del fichero de concesiones en el servidor dhcp para comprobar que se han concedido esas direcciones IP.
5. Comprobación donde se vean los 4 paquetes que se transmite en la negociación de la concesión.
6. Explica, con pruebas de funcionamiento, el motivo del comportamiento que se indica en los puntos 5 y 6. **Muestra al profesor el funcionamiento del punto 5 y 6**.
7. Muestra la configuración para hacer la reserva.
8. Una captura de pantalla donde se vea la ip que ha tomado de forma dinámica el servidor web. ¿Las reservas se guardan en el fichero de concesión del servidor dhcp?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
