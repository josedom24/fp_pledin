---
title: "Práctica: Cortafuegos perimetral con DMZ"
permalink: /seguridadgs/u03/practica.html
---

## Esquema de red

Vamos a utilizar tres máquinas en openstack, que vamos a crear con la receta heat: [escenario3.yaml](escenario3.yaml). La receta heat ha deshabilitado el cortafuego que nos ofrece openstack (todos los puertos de todos los protocolos están abiertos). Una máquina (que tiene asignada una IP flotante) hará de cortafuegos, otra será una máquina de la red interna 192.168.100.0/24 y la tercera será un servidor en la DMZ donde iremos instalando distintos servicios y estará en la red 192.168.200.0/24.

{% capture notice-text %}
## Ejercicios

Configurar un cortafuegos perimetral en la máquina `router-fw` teniendo en cuenta los siguientes puntos:

* Política por defecto DROP para las cadenas INPUT, FORWARD y OUTPUT.
* Se pueden usar las extensiones que queremos adecuadas, pero al menos debe implementarse seguimiento de la conexión.
* Debemos implementar que el cortafuego funcione después de un reinicio de la máquina.
* Debes indicar pruebas de funcionamiento de todos las reglas.
* El cortafuego debe cumplir al menos estas reglas:
    * La máquina `router-fw` tiene un servidor ssh escuchando por el puerto 22, pero al acceder desde el exterior habrá que conectar al puerto 2222.
    * Desde la LAN y la DMZ se debe permitir la conexión ssh por el puerto 22 al la máquina `router-fw`.
    * La máquina `router-fw` debe tener permitido el tráfico para la interfaz loopback.
    * A la máquina `router-fw`  se le puede hacer ping desde la DMZ, pero desde la LAN se le debe rechazar la conexión (REJECT). 
    * La máquina `router-fw` puede hacer ping a la LAN, la DMZ y al exterior.
    * Desde la máquina `DMZ` se puede hacer ping y conexión ssh a la máquina `LAN`.
    * Desde la máquina `LAN` no se puede hacer ping, pero si se puede conectar por ssh a la máquina `DMZ`.
    * Configura la máquina `router-fw` para que las máquinas `LAN` y `DMZ` puedan acceder al exterior.
    * La máquina `LAN` se le permite hacer ping al exterior.
    * La máquina `LAN` puede navegar.
    * La máquina `DMZ` puede navegar. Instala un servidor web, un servidor ftp y un servidor de correos.
    * Configura la máquina `router-fw` para que los servicios web y ftp sean accesibles desde el exterior.
    * El servidor web y el servidor ftp deben ser accesible desde la LAN y desde el exterior.
    * El servidor de correos sólo debe ser accesible desde la LAN.
    * En la máquina `LAN` instala un servidor mysql. A este servidor sólo se puede acceder desde la DMZ.

* Si crees que necesitas más reglas de las que nos han indicado, describe porque pueden ser necesarias.
* **MEJORA**: Utiliza nuevas cadenas para clasificar el tráfico.
* **MEJORA**: Consruye el cortafuego utilizando nftables.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>