---
title: "Clase 2: Tarea - Instalación del servidor Kea DHCP"
---

## ¿Qué vas a aprender en esta clase?

* Realizar  la instalación del servidor Kea DHCP.
* Configurar el servidor Kea DHCP.
* Entender los tiempos involucrados en el protocolo DHCP.
* Comprender el comportamiento de los clientes cuando no tienen comunicación con el servidor DHCP.
* Configurar una reserva.

## Teoría

Para realizar esta tarea te puede ayudar una:

* [Introducción a Kea DHCP](kea.html)

## Ejercicio

Vamos a seguir trabajando con el escenario de la unidad anterior.

1.  Instala un servidor DHCP en la máquina `router.tunombre.org` con un ámbito que tenga las siguientes características:
  * Tiene que ofrecer configuración automática para los equipos clientes de la **red muy aislada*.
	* Determinar el rango de direcciones, la máscara de red, la puerta de enlace, el servidor DNS y la dirección de broadcast.
	* Duración de la concesión: 30 minutos
2. Configura las máquinas **cliente1** y **cliente2** para que tomen configuración de red dinámica y puedas probar que realmente está funcionando el servidor.
3. Realizar una captura, desde el servidor usando `tcpdump`, de los cuatro paquetes que corresponden a una concesión: `DISCOVER`, `OFFER`, `REQUEST`, `ACK`.
4. **Para hacer esta prueba configura un tiempo de concesión bajo**. Los clientes toman una configuración, y a continuación apagamos el servidor DHCP. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
5. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor DHCP (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?. Comprueba el funcionamiento y razona el motivo.
6. Actualmente el **servidorWeb** tiene una ip fija para que se pueda acceder a ese servicio. Configura un nuevo ámbito en el servidor DHCP con las siguientes características:
    * Tiene que ofrecer configuración automática para los equipos clientes de la **red aislada*.
	  * Determinar el rango de direcciones, la máscara de red, la puerta de enlace, el servidor DNS y la dirección de broadcast.
	  * Duración de la concesión: 24 horas.

  	Crea una reserva en el servidor para que el **servidorWeb** tenga la misma IP que había configurado de forma estática.
7. Modifica la configuración de red del **servidorWeb** para que configure la red de forma dinámica.
8. Conecta la máquina **router** a una red de tipo NAT con servidor DHCP (por ejemplo la `default`). Configura la interfaz correspondiente para que tome direccionamiento dinámico.
9. Recuerda que si la interfaz "pública" de un router toma direccionamiento dinámico, las reglas de SNAT deben usar la técnica de enmascaramiento, Modifica las reglas de SNAT para que el escenario siga funcionando.

{% capture notice-text %}
## Entrega

1. Entrega el fichero de configuración que tienes que realizar en el apartado 1 del servidor DHCP.
2. Muestra la configuración de los clientes para que tomen direccionamiento dinámico. Muestra la configuración de red (dirección ip, puesta de enlace, DNS,...) con la que se han configurado. Muestra la lista de concesiones.
3. Una comprobación donde se comprueba que los dos clientes tienen conectividad al exterior.
4. Comprobación donde se vean los 4 paquetes que se transmite en la negociación de la concesión, del apartado 3.
5. Explica, con pruebas de funcionamiento, el motivo del comportamiento que se indica en los puntos 4 y 5. Muestra al profesor el funcionamiento del punto 4 y 5.
6. la configuración del servidor DHCP que se solicita en el apartado 6. Muestra la configuración del **servidorWeb** después de cambiar su configuración de red. Comprueba que puedes seguir accediendo a la página web desde el exterior y desde los clientes.
7. Muestra el cambio que has realizado en la configuración de la interface "pública" del **router**. Muestra la configuración de red que ha tomado.
8. Muestras las nuevas reglas SNAT.
9. Comprueba que los clientes y el **servidorWeb** siguen teniendo conectividad con el exterior.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
