---
title: "Taller 4: Gestión de redes en QEMU/KVM + libvirt"
---

## ¿Qué vas a aprender en este taller?

* Conocer los distintos tipos de redes virtuales que podemos definir con KVM/libvirt.
* Gestionar switch virtuales con Linux Bridge
* Gestionar los distintos tipos de redes con `virsh` y `virt-manager`.
* Configurar un bridge externo para conectar las máquinas virtuales a una red pública.
* Gestionar las interfaces de red en las máquinas virtuales.

## Recursos para realizar este taller

* Capítulo 7 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## ¿Qué tienes que hacer?

1. Crea distintos tipos de redes con `virsh`:
	* Una red privada de tipo NAT
		* Nombre: **red-nat**
		* Nombre del bridge: virbr1
		* Direccionamiento: `192.168.125.0/24`
		* Dirección del host (puerta de enlace): `192.168.125.1`
		* Rango DHCP: `192.168.125.2  - 192.168.125.100`
	* Una red privada aislada
		* Nombre: **red-aislada**
		* Nombre del bridge: virbr2
		* Direccionamiento: `192.168.126.0/24`
		* Dirección del host (puerta de enlace): `192.168.126.1`
		* Rango DHCP: `192.168.126.2  - 192.168.126.100`
	* Una red privada muy aislada
		* Nombre: **red-muy-aislada**
		* Nombre del bridge: virbr3

	Activa las redes y configúralas para que se inicien de forma automática.

	* **Entrega**: Y el comando `virsh` y la salida para listar las redes que se han creado. 

	Vamos a trabajar con dos máquinas virtuales (las puedes clonar a partir de la plantilla del taller anterior). Las máquinas las vamos a llamar **cliente1** y **cliente2**. 

2. Desconecta la máquina `cliente1` de la red `default` y conéctala a la red `red-nat`. Obtén de nuevo una dirección y comprueba la dirección IP que ha tomado, que tiene acceso a internet y que la dirección del host (puerta de enlace) corresponde a la `192.168.125.1`.
	* **Entrega**: Capturas de pantalla donde se vea el direccionamiento, la puerta de enlace y la prueba de funcionamiento de que tiene conectividad al exterior.
3. Desconecta la máquina `cliente2` del la red `default`. Conecta las máquinas `cliente1` y `cliente2` a la red `red-aislada`. Comprueba que las máquinas han cogido una dirección IP en la red `192.168.126.0/24`, comprueba que pueden hacer ping entre ellas, y hacer ping al host (`192.168.126.1`). Comprueba que la máquina `cliente1` tiene conexión al exterior (por estar conectada a la red NAT `red-nat`), pero sin embargo el `cliente2` no tiene conexión al exterior.
	* **Entrega**: Capturas de pantalla donde se vean las direcciones que han tomado, que se pueden hacer ping, que pueden hacer ping al host, pero que el `cliente2` no puede hacer ping al exterior.
4. Desconecta todas las interfaces de las dos máquinas. Conéctalas a la red `red-muy-aislada`. Configura de forma estática sus direcciones y comprueba que pueden hacer ping entre ellas, sin embargo no pueden hacer ping ni al host, ni al exterior.
	* **Entrega**: Capturas de pantalla donde se vean las direcciones que han tomado, que se pueden hacer ping y que no pueden hacer ping al exterior.
5. Crea un puente externo, llamado **br0** como se explica en el apartado [Creación de un Puente Externo con Linux Bridge](https://github.com/josedom24/curso_virtualizacion_linux/blob/main/modulo7/bridge.md). Crea una red de tipo Puente que nos permita conectar las máquinas a este bridge, llámala **red-externa**. Conecta el `cliente1` a esta red y obtén direccionamiento, comprueba que se configura con una IP del direccionamiento de nuestra red local `172.22.0.0/16` (ha obtenido la dirección del servidor DHCP de nuestro instituto). Comprueba que podemos acceder a esta máquina desde cualquier máquina conectada a la misma red.
	* **Entrega**: Capturas de pantalla donde se vean la dirección que ha tomado y la comprobación de que hay conexión a la máquina virtual desde el exterior.
