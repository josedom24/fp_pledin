---
title: "Taller 4: Vagrant - Creación de escenarios"
---

## ¿Qué vas a aprender en este taller?

* Definir varias máquinas virtuales en el fichero `Vagrantfile`.
* Definir los distintos tipos de redes que podemos definir con Vagrant.
* Añadir almacenamiento a las máquinas virtuales.

## Recursos para realizar este taller

Los contenidos necesarios para la realización de este taller y para profundizar en la introducción de Vagrant, lo puedes encontrar en el siguiente artículo:

* [Presentación: Configuración de redes en KVM y en Vagrant](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/redes_kvm_vagrant.pdf)
* [Introducción al uso de vagrant + libvirt + QEMU/KVM. Definición de redes.](https://www.josedomingo.org/pledin/2021/10/introduccion-vagrant-libvirt-redes/)
* [Introducción al uso de vagrant + libvirt + QEMU/KVM. Almacenamiento.](https://www.josedomingo.org/pledin/2021/10/introduccion-vagrant-libvirt-almacenamiento/)


## ¿Qué tienes que hacer?

1. Utilizando el escenario que puedes obtener en el directorio **Taller4** del repositorio [taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant), crea el escenario con vagrant.
2. El `nodo2` utiliza otro box. Comprueba que se ha descargado antes de crear las máquinas.
3. Accede a cada una de las máquinas.
4. Comprueba la configuración de red de `eth0`. ¿Cuál es la dirección IP?, ¿y la puerta de enlace?, y ¿el DNS?. ¿Para qué se utiliza la interfaz de red `eth0`?.
5. Recuerda lo que pone el primer artículo: **Tenemos que tener en cuenta que todas las máquinas van a tener una interfaz de red de tipo NAT, que le dan direccionamiento por DHCP y le posibilitan acceder al exterior. En determinados escenarios deberemos no tener en cuenta en esta interfaz, por ejemplo cambiando la ruta por defecto para que la máquina no salga por esta interfaz.**
6. Modifica el fichero `Vagrantfile` para añadirle al `nodo1` una nueva interfaz de red conectada a una nueva red privada tipo NAT con DHCP en el direccionamiento `192.168.200.0/24`. Prueba el escenario y comprueba que se ha creado una nueva interfaz de red en la máquina y una nueva red con `virsh`.
7. Modifica el fichero `Vagrantfile` para conectar las dos máquinas por una red interna (muy aislada). El direccionamiento de las máquinas debe ser estático: `nodo1` debe tener la dirección IP `10.0.0.1` y el `nodo2` la `10.0.0.2`. Comprueba que hay conectividad por las nuevas interfaces de red entre las máquinas.
8. Modifica el fichero `Vagrantfile` para añadir a `nodo2` una nueva interfaz de red conectada a la red pública. Debes tener un Linux Bridge `br0`. Comprueba que `nodo2` tiene una nueva interfaz de red con el direccionamiento de la red pública.
9. Modifica el fichero `Vagrantfile` para añadir a `nodo2` dos nuevos discos de 1Gb de tamaño. Comprueba que efectivamente se han añadido a la máquina. 

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. El fichero `Vagrantfile` con el que has trabajado.
2. Una captura de pantalla donde se vea la configuración de red del `nodo1` (salida de `ip a`).
3. Una captura de pantalla donde se vea la configuración de red del `nodo2` (salida de `ip a`).
4. Captura de pantalla donde se vea el `ping` entre las máquinas usando la red interna muy aislada.
5. Comprueba que el nodo2 tiene una nueva interfaz conectada a `br0`. Prueba a hacer ping a esa dirección desde el exterior.
6. Captura de pantalla donde se vea que el `nodo2` tiene añadido los dos nuevos discos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
