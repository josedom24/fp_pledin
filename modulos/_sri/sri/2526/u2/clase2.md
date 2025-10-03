---
title: "Clase 2: Instalación del servidor Kea DHCP"
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

  Crea una reserva en el servidor para que el **servidorWeb* tenga la misma IP que había configurado de forma estática.
7. Modifica la configuración de red del **servidorWeb** para que configure la red de forma .
