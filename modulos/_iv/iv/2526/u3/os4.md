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

## Gestión de redes con OSC

Para gestionar las redes y las subredes, usaremos los comandos de `openstac network` y `openstack subnet`.

Para listar las redes  y las subredes:

        openstack network list
        openstack subnet list

Para crear una red:

        openstack network create mi_red

Ahora tenemos que asociar una subred, para ello se pueden indicar los siguientes parámetros:

* `--network` (**Obligatorio**): Nombre de la red a la que estamos asociando la subnet.
* `--subnet-range` (**Obligatorio**): Direccionamiento de la red.
* `--gateway` (**Opcional**): Puerta de enlace que se envía a las instancias si tenemos activo el DHCP. Si no se indica se envía la primera dirección del direccionamiento indicado. Si se inicializa con **`none`** se **deshabilita la puerta de enlace**. Esto es para que `cloud-init` no configure la puerta de enlace en las instancias conectada a esta red.
* `--no-dhcp` (**Opcional**): No se activa el servidor DHCP. Si no se pone, por defecto, está activado el DHCP.
* `--allocation-pool start=<ip-address>,end=<ip-address>` (**Opcional**): Se indica el rango de direcciones que se reparten. Si no se pone, se configura por defecto.
* `--dns-nameserver` (**Obligatorio**): Se indica el servidor DNS que se envía a la instancia. Se pueden indicar varios parámetros si queremos mandar varios servidores DNS.

Por ejemplo:

        openstack subnet create --network mi_red --subnet-range 192.168.0.0/24 --dns-nameserver 172.22.0.1 mi_subred

## Gestión de routers

Para listar los routers:

        openstack router list

Para crear un nuevo router:

        openstack router create mi_router

Ahora conectamos el router a la red externa:

        openstack router set mi_router --external-gateway ext-net
    
Ahora enlazamos con la red creada:

        openstack router add subnet mi_router mi_subred

Para conectar una instancia a la red que hemos creado, ejecutaremos:

        openstack server add network nombre_instancia mi_red

Podemos crear una nueva instancia conectada a la red que hemos creado:

        openstack server create --flavor m1.mini \
        --image "Debian 13.0 - Trixie" \
        --security-group default \
        --key-name clave_jdmr \
        --network mi_red \
        instancia_prueba3

{% capture notice-text %}
## Ejercicio

1. Crea una nueva red (llamada `mired1`) y una subred con DHCP, DNS el `172.22.0.1` y direccionamiento `192.168.0.0/24`. Crea un nuevo router. Conecta la nueva red al router, y el router a red pública.
2. Crea una instancia (llamada `maquina1`) conectada a la nueva red. Comprueba que la IP fija está en el direccionamiento de la nueva red. ¿Puedes añadirle una IP flotante a la nueva instancia? ¿Por qué?.
3. Conecta esta instancia a la red de tu proyecto. Configura la nueva interface de la instancia.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


