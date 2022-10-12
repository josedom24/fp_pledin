---
title: "Práctica: Protocolo DHCP"
---

![router](img/router.png)

## Descripción

{% capture notice-text %}

Vamos a continuar trabajando en el escenario que desarrollamos en la [Práctica: Creación y configuración de un escenario router-nat](https://fp.josedomingo.org/sri2223/1_iac/practica.html).

Para evitar los problemas que nos puede causar vagrant a la hora de trabajar con el DHCP (los clientes tendrían dos servidores DHCP, el que estamos configurando y el de la red de mantenimiento por eth0), os sugiero:

1. Que montéis el mismo escenario pero en kvm/libvirt, en relación a las redes:
	* No tendríamos la interfaz conectada a la red de mantenimiento de vagrant.
	* Conectaríamos las máquinas a una red aislada sin dhcp (con IP estática) que utilizaríamos para configurar las máquinas por ansible. Además no tendríamos el problema que tenemos en vagrant, ya que las direcciones ip no cambiarían.
2. Ejecutamos el playbook de la práctica anterior y comprobamos que las máquinas tienen el funcionamiento esperado.

A partir de esta configuración podríamos seguir con esta práctica.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Queremos instalar un servidor DHCP en la máquina `router` para que configure de forma automática las máquinas que se conectan en la red interna. Tenemos que tener en cuenta lo siguiente:

1. La máquina `cliente` de la práctica anterior, que tiene instalado el servidor web, debe tener la misma IP que la que le asígnate estáticamente, por lo tanto haremos una reserva para que tenga la misma IP.
2. Al añadir una nueva máquina a la red local (recuerda que no se le instalará el servidor web) se configurará de forma dinámica.
3. Realiza los cambios oportunos en el fichero `Vagrantfile` para añadir una nueva máquina al escenario conectada a la red interna.
4. Crea un nuevo rol en el playbook de ansible llamado `dhcp` que configure el servidor DHCP de forma correcta. Quizás sea necesario modificar el comportamiento de algún rol de la práctica anterior.
5. Todos los parámetros que reparta el servidor DHCP, así como cualquier otro dato, por ejemplo la dirección MAC del `cliente` se guardarán en variables.

{% capture notice-text %}
## Entrega

1. Entrega la URL del repositorio GitHub donde has alojado todos los ficheros.
2. Entrega el fichero de configuración del servidor DHCP después de ejecutar el playbook de ansible.
3. Entrega el fichero de configuración de red del `cliente` (para comprobar que toma direccionamiento dinámico) y que ha tomado la dirección reservada en el servidor DHCP.
4. Entrega el fichero de configuración de red de la otra máquina cliente, la dirección que ha tomado y el fichero de concesiones del servidor donde se demuestra que se ha repartido.
5. Comprueba que la nueva máquina cliente no tiene el servidor apache2 instalado, y una captura de pantalla comprobando que sigue siendo accesible el servidor web de `cliente`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


