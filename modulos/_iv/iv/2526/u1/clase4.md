---
title: "Clase 4: Gestión de redes en QEMU/KVM + libvirt"
---

## ¿Qué vas a aprender en esta clase?

* Conocer los distintos tipos de redes virtuales que podemos definir con KVM/libvirt.
* Gestionar switch virtuales con Linux Bridge
* Gestionar los distintos tipos de redes.
* Configurar un bridge externo para conectar las máquinas virtuales a una red pública.
* Gestionar las interfaces de red en las máquinas virtuales.

## Recursos

* Curso completo: [Profundización a la virtualización con KVM/libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2)
* En concreto los apartados:
  * Gestión de redes
* [Presentación: Resumen virtualización en Linux](https://fp.josedomingo.org/sri/pdf/resumen_virtualizacion.pdf)

## Ejercicio

1. Crea distintos tipos de redes con `virsh`:
	* Una red privada de tipo NAT
		* Nombre: **red-nat**
		* Nombre del bridge: virbr1
		* Direccionamiento: `192.168.125.0/24`
		* Dirección del host (puerta de enlace): `192.168.125.1`
		* Rango DHCP: `192.168.125.2  - 192.168.125.100`
	* Una red privada aislada sin DHCP
		* Nombre: **red-aislada**
		* Nombre del bridge: virbr2
		* Direccionamiento: `192.168.126.0/24`
		* Dirección del host (puerta de enlace): `192.168.126.1`

	Activa las redes y configúralas para que se inicien de forma automática. **Si tienes conficto con el nombre del bridge o el direccionamiento modifícalos.**

2. Desconecta una maquina que tengas conectada a la red `default` y conéctala a `red-nat`. ¿Puedes hacer esta modificación con la máquina encendida?. Comprueba la nueva IP que ha tomado.
3. Si tuvieras que crear una nueva máquina virtual conectada a la red `red-nat`, ¿cómo sería la instrucción `virt-install`?. **No hay que hacer la instalación**.
4. Conecta la máquina a la `red-aislada`. ¿Qué tienes que hacer en la máquina para que tenga direccionamiento?. Realiza la configuración. ¿Puedes hacer `ping` a la `192.168.126.1`?. Razona la respuesta.
5. Crea un puente externo, llamado **br0**. Si estás usando Gnome sigue esta guía: [Creación de un puente externo en un entorno gráfico](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad06/clase3.md), si estás en una máquina sin entorno gráfico: [Creación de un puente externo con Linux Bridge](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad06/clase4.md). Crea una red de tipo puente con libvirt.
6. Desconecta la máquina de la `red-nat` y conéctala a la red puente (**recuerda que en la conexión puedes indicar la red o el puente**). Comprueba que se configura con una IP del direccionamiento de nuestra red local `172.22.0.0/16` (ha obtenido la dirección del servidor DHCP de nuestro instituto). Comprueba que podemos acceder a esta máquina desde cualquier máquina conectada a la misma red.

{% capture notice-text %}
## Entrega

1. Del ejercicio 1: Los ficheros XML que has usado. Y la lista de redes que has creado usando el comando `virsh`.
2. Del ejercicio 2: La instrucción para desconectar la red. La instrucción para conectarla a la nueva red. Comprobación del nuevo direccionamiento (dirección ip y puerta de enlace). Responde la pregunta.
3. Del ejercicio 3: La instrucción `virt-install`.
4. Del ejercicio 4: La instrucción para realizar la nueva conexión. Comprobación de que tiene una nueva configuración de red. Responde las preguntas.
5. Del ejercicio 5 y 6: Entrega dos instrucciones para conectar la máquina a la red puente (**una conectando a la red y otra conectando al bridge**). Comprobaciones del nuevo direccionamiento (IP, puerta de enlaces, servidor DNS). Comprobación de que hay conexión a la máquina virtual desde el exterior.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>