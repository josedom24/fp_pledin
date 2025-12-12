---
title: "Clase 6: Redes en OpenStack desde el CLI (Parte 1)"
---

## Conceptos previos de Neutron

* **Red**: Red Dominio aislado de capa 2. Sería el equivalente a una VLAN. Las redes externas solo pueden ser definidas por el administrador.
* **Subred**: Bloque de direcciones IPv4 o IPv6 que se asignan a las máquinas virtuales que se conectan a ella.
* **Router**: Dispositivo de capa 3 para conectar redes.
* **Puerto**: Puerto virtual de un router o una instancia.
* **IP Fija**: Dirección IP con la que se crean una instancia en una red y que se utiliza para comunicación interna. La dirección IP fija no cambia durante la vida de la instancia.
* **IP Flotante**: Dirección IP asociada a una instancia en un momento dado para poder acceder a ella desde fuera. Una IP flotante puede asignarse a otra instancia diferente cuando se estime oportuno.

## Gestión de routers

Los routers nos permiten **interconectar redes**, En nuestro caso vamos a usar routers conectados a la red externa y una red interna para que nuestras instancias conectadas a la red interna tengan:

* Acceso al exterior, ya que el router hace **SNAT**.
* Acceder a la instancia por medio de **IP flotantes**, el router hace **DNAT**.

Veamos algunas operaciones:

* Listar los routers: `openstack router list`
* Crear un nuevo router: `openstack router create mi_router`
* Conectar el router a la red externa: `openstack router set mi_router --external-gateway ext-net`
* Mostrar información detallada de un router: `openstack router show mi_router`
* Listar los puertos del router: `openstack port list --router mi_router`
* Quitar la puerta de enlace externa: `openstack router unset mi_router --external-gateway`
* Eliminar un router: `openstack router delete mi_router`


{% capture notice-text %}
## Ejercicio

1. Crea un nuevo router conectado a la red externa.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Gestión de redes NAT en OpenStack

Un **red NAT** en OpenStack, es una red interna **conectada a un router que está conectada al exterior. Tiene las siguientes características:

* Pueden tener servidor DHCP o no (lo normal es que lo tenga).
* Las instancias tienen **gateway** (puerta de enlace) que corresponde al router y suele ser la primera dirección del direccionamiento de red.
* Las instancias tienes acceso a internet (el router hace  **SNAT**).
* Podemos acceder a las instancias con **IP flotante** (el router hace **DNAT**).

Para gestionar las redes y las subredes, usaremos los comandos de `openstac network` y `openstack subnet`.

Para listar las redes  y las subredes:

        openstack network list
        openstack subnet list

Para crear una red:

        openstack network create red1

Ahora tenemos que asociar una subred, para ello se pueden indicar los siguientes parámetros para crear una red NAT:

* `--network` (**Obligatorio**): Nombre de la red a la que estamos asociando la subnet.
* `--subnet-range` (**Obligatorio**): Direccionamiento de la red.
* `--gateway` (**Opcional**): Puerta de enlace con la que se va a configurar las instancias. **Si no se indica se envía la primera dirección del direccionamiento indicado**.
* `--no-dhcp` (**Opcional**): No se activa el servidor DHCP. Si no se pone, por defecto, está activado el DHCP.
* `--allocation-pool start=<ip-address>,end=<ip-address>` (**Opcional**): Se indica el rango de direcciones que se reparten. Si no se pone, se configura por defecto.
* `--dns-nameserver` (**Obligatorio**): Se indica el servidor DNS que se envía a la instancia. Se pueden indicar varios parámetros si queremos mandar varios servidores DNS. **Se debe configurar aunque no tengamos el servidor DHCP activo**, para que, como veremos a continuación, el cloud-init lo pueda configurar de forma estática en redes sin DHCP.

Por ejemplo, para crear una red de tipo NAT

        openstack subnet create --network red1 --subnet-range 192.168.0.0/24 --dns-nameserver 172.22.0.1 subred1

A continuación tenemos que conectar la red al router que hemos creado en el apartado anterior:

        openstack router add subnet mi_router subred1

Si queremos desconectar la red del router podemos ejecutar:

        openstack router remove subnet mi_router subred1

Podemos listar los puertos de una red: `openstack port list --network red1`
        
{% capture notice-text %}
## Ejercicio

1. Crea una nueva red (llamada `red1`) y una subred con DHCP, DNS el `172.22.0.1` y direccionamiento `192.168.0.0/24`. Crea un nuevo router. 
2. Conecta la nueva red al router.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Creación de una instancia a una red NAT con DHCP

Al crear las intancias podemos indicar **la red p las redes** a las que se conecta. Podemos crear una nueva instancia conectada a la red que hemos creado:

        openstack server create --flavor m1.mini \
        --image "Debian 13 Trixie" \
        --security-group default \
        --key-name jdmr \
        --network red1 \
        maquina1

Podemos asociar una IP flotante:

        openstack floating ip create ext-net
        openstack server add floating ip maquina1 <IP_FLOTANTE>

Acceder a la instancia, comprobar el direccionamiento y comprobar como **cloud-init ha configurado de forma dinámica la configuración de la interface en netplan**.

Podemos listar los puertos de una instancia: `openstack port list --server maquina1`.

{% capture notice-text %}
## Ejercicio

1. Crea una instancia (llamada `maquina1`) conectada a la nueva red. 
2. Comprueba que la IP fija está en el direccionamiento de la nueva red. ¿Puedes añadirle una IP flotante a la nueva instancia? ¿Por qué?.
3. Comprueba en el fichero de configuración de netplan que la interfaz ha sido configurada por DHCP.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Creación de una instancia a una red NAT con DHCP y una reserva

Si necesitamos que una instancia o un router tenga una interfaz con una **dirección IP determinada** tenemos que crear un puerto. Si estamos trabajando con una red NAT con DHCP, estaremos haciendo una **reserva**.

Para crear un puerto con una dirección IP fija: 

        openstack port create --network red1 --fixed-ip ip-address=192.168.0.100 mi_port

A partir de un puerto creado, podemos usarlo para crear por ejemplo una instancia que use dicho puerto:

        openstack server create --flavor m1.mini \
        --image "Debian 13 Trixie" \
        --security-group default \
        --key-name jdmr \
        --port mi_port \
        maquina2

{% capture notice-text %}
## Ejercicio

1. Crea una instancia llamada `maquina2` en la red `mired1` que tenga la dirección IP fija `192.168.0.200`.
2. Comprueba que la IP fija es la reserva que hemos creado en el puerto.
3. Comprueba en el fichero de configuración de netplan que la interfaz ha sido configurada por DHCP.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Redes NAT sin DHCP

Podríamos crear una red de tipo NAT conectada a un router, sin DHCP, para ello:

        openstack network create red2
        openstack subnet create --network red2 --no-dhcp --subnet-range 192.168.10.0/24 --dns-nameserver 172.22.0.1 subred2

* En este tipo de red la configuración de la instancia **no se hace por DHCP**.
* **cloud-init configura la instancia de forma estática**.
* **Hemos indica el DNS al crear la subred**, para que cloud-init pueda configurarlo de manera estática.

A continuación vamos a conectar la red al router que hemos creado en el apartado anterior:

        openstack router add subnet mi_router subred2

## Creación de una una instancia a una red NAT sin DHCP

Creamos una instancia conectada a esta nueva red, tenemos que tener en cuenta que **no va a tener conectividad** porque no hay servidor DHCP. Por lo tanto no se va poder configurar por cloud-init porque no es capaz de acceder al **servidor de metadatos**. Por lo tanto tenemos que activar el **config drive** (`--config-drive True`) para que la configuración de cloud-init se realice mediante un **CDROM conectado a la instancia**.

        openstack server create --flavor m1.mini \
        --image "Debian 13 Trixie" \
        --security-group default \
        --key-name jdmr \
        --network red2 \
        --config-drive True \
        maquina3

Puedes asociarle una **IP flotante** y comprobar que se ha configurado la IP fija de la instancia de forma estática (mira la configuración de netplan).

{% capture notice-text %}
## Ejercicio

1. Puedes eliminar `maquina1` y `maquina2`.
2. Crea una instancia (llamada `maquina3`) conectada a la nueva red. 
3. Comprueba que la IP fija está en el direccionamiento de la nueva red. ¿Puedes añadirle una IP flotante a la nueva instancia? ¿Por qué?.
4. Comprueba en el fichero de configuración de netplan que la interfaz ha sido configurada de forma estática. Además de la dirección IP, se ha configurado el DNS y la puerta de enlace.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Creación de una instancia a una red NAT sin DHCP y una IP fija estática

Cuando en la red no tenemos configurado el servidor DHCP, puedo **de manera estática configurar una IP fija**. Para ello usamos un puerto:

        openstack port create --network red2 --fixed-ip ip-address=192.168.10.100 mi_port_sin_dhcp

Y creamos la nueva instancia:

        openstack server create --flavor m1.mini \
        --image "Debian 13 Trixie" \
        --security-group default \
        --key-name jdmr \
        --port mi_port_sin_dhcp \
        --config-drive True \
        maquina4

Puedes asociarle una **IP flotante** y comprobar que se ha configurado la IP fija de la instancia de forma estática (mira la configuración de netplan).

{% capture notice-text %}
## Ejercicio

1. Crea una instancia (llamada `maquina4`) conectada a la nueva red. 
2. Comprueba en el fichero de configuración de netplan que la interfaz ha sido configurada de forma estática. Además de la dirección IP, se ha configurado el DNS y la puerta de enlace.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Eliminación de la infraestructura de red creada

El orden para eliminar la infraestructura de red creada es:

1. Eliminar todas las instancias conectadas a la red.
2. Eliminar todos los puertos **desaociados** de la red.
3. Desconectar la red del router.

        openstack router remove subnet mi_router mi_subred

4. Eliminar la red y el router.

{% capture notice-text %}
## Ejercicio

1. Elimina las instancias `maquina3` y `maquina4` y la red `red2`.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>