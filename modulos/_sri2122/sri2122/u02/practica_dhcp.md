---
title: "Práctica: Servidor DHCP" 
---

## Preparación del escenario

Crea un escenario en libvirt/kvm (no uses Vagrant) de la siguiente manera:

* Máquina **Servidor**: Tiene tres tarjetas de red: una que le da acceso a internet (NAT o pública) y dos redes privadas (muy aisladas).
* Máquina **nodo_lan1**: Un cliente linux conectado a la primera red privada.
* Máquina **nodo_lan2**: Un cliente linux conectado a la segunda red privada.

## Servidor dhcp

Instala un servidor dhcp en el ordenador **"servidor"** que de servicio a los ordenadores de red local, teniendo en cuenta:

* Por la red privada 1: Reparte configuración en la red `192.168.100.0/24`. El tiempo de concesión es de 12 horas.
* Por la red privada 2: Reparte configuración en la red `192.168.200.0/24`. El tiempo de concesión es de 1 hora.

Para los dos ámbitos los servidores DNS deben ser el 1.1.1.1 y 1.0.0.1. Piensa que puertas de acceso se deben mandar a cada red.

## Router-nat

Configura la máquina **"servidor"** para que haga router-nat para los clientes de ambas redes.

## Funcionamiento del dhcp

Vamos a conectar un cliente windows a una de las redes. Vamos a comprobar que ocurre con la configuración de los clientes en determinadas circunstancias, para ello vamos a poner un tiempo de concesión muy bajo. 

{% capture notice-text %}
* **Tarea 1 (1 punto)**: Explica brevemente cómo has creado el escenario con libvirt/KVM.
* **Tarea 2 (2 puntos)**: Muestra el fichero de configuración del servidor, la lista de concesiones, la modificación en la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ` ip a` en los clientes.
* **Tarea 3 (2 puntos):** Configura el servidor para que funcione como router y NAT, de esta forma los clientes tengan internet. Muestra las rutas por defecto del servidor y los clientes. Realiza una prueba de funcionamiento para comprobar que el cliente tiene acceso a internet (utiliza nombres, para comprobar que tiene resolución DNS).
* **Tarea 4 (1 punto):** Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?. Entrega pruebas de funcionamiento.
* **Tarea 5 (1 punto):** Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?. Entrega pruebas de funcionamiento.
* **Tarea 6 (3 puntos):** Realiza un playbook con ansible que configure de forma automática el servidor, para que haga de servidor DHCP y de router-NAT (no es necesario que se haga la configuración en los clientes). Entrega la URL del repositorio.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
