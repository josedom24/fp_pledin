---
title: "Práctica: Servidor DHCP" 
permalink: /serviciosgs/u02/practica_dhcp.html
---

## Teoría

{% capture notice-text %}
* **Tarea 1 (1 punto):** Lee el documento [Teoría: Servidor DHCP](dhcp.html) y explica el funcionamiento del servidor DHCP resumido en este [gráfico](img/dhcp.png).	
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## DHCPv4

### Preparación del escenario

Crea un escenario usando Vagrant que defina las siguientes máquinas:

* **Servidor**: Tiene dos tarjetas de red: una pública y una privada que se conectan a la red local.
* **nodo_lan1**: Un cliente conectado a la red local.

### Servidor dhcp

Instala un servidor dhcp en el ordenador **"servidor"** que de servicio a los ordenadores de red local, teniendo en cuenta que el tiempo de concesión sea 12 horas y que la red local tiene el direccionamiento `192.168.100.0/24`.

{% capture notice-text %}
* **Tarea 2:** Entrega el fichero `Vagrantfile` que define el escenario.
* **Tarea 3 (2 puntos):** Muestra el fichero de configuración del servidor, la lista de concesiones, la modificación en la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ` ip address`.
* **Tarea 4 (1 puntos):** Configura el servidor para que funcione como router y NAT, de esta forma los clientes tengan internet. Muestra las rutas por defecto del servidor y el cliente. Realiza una prueba de funcionamiento para comprobar que el cliente tiene acceso a internet (utiliza nombres, para comprobar que tiene resolución DNS).
* **Tarea 5 (1 punto):** Realizar una captura, desde el servidor usando `tcpdump`, de los cuatro paquetes que corresponden a una concesión: `DISCOVER`, `OFFER`, `REQUEST`, `ACK`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Funcionamiento del dhcp

Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstancias, para ello vamos a poner un tiempo de concesión muy bajo. 

{% capture notice-text %}
* **Tarea 6 (1 punto):** Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
* **Tarea 7 (1 punto):** Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Reservas

Crea una reserva para el que el cliente tome siempre la dirección 192.168.100.100.

{% capture notice-text %}
* **Tarea 8 (1 puntos):** Indica las modificaciones realizadas en los ficheros de configuración y entrega una comprobación de que el cliente ha tomado esa dirección.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Uso de varios ámbitos

Modifica el escenario Vagrant para añadir una nueva red local y un nuevo nodo:

* Servidor: En el servidor hay que crear una nueva interfaz
* nodo_lan2: Un cliente conectado a la segunda red local.

Configura el servidor dhcp en el ordenador "servidor" para que de servicio a los ordenadores de la nueva red local, teniendo en cuenta que el tiempo de concesión sea 24 horas y que la red local tiene el direccionamiento 192.168.200.0/24.

{% capture notice-text %}
* **Tarea 9**: Entrega el nuevo fichero Vagrantfile que define el escenario.
* **Tarea 10 (1 punto)**: Explica las modificaciones que has hecho en los distintos ficheros de configuración. Entrega las comprobaciones necesarias de que los dos ámbitos están funcionando.
* **Tarea 11 (1 punto)**: Realiza las modificaciones necesarias para que los cliente de la segunda red local tengan acceso a internet. Entrega las comprobaciones necesarias.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

