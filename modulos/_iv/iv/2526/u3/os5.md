---
title: "Redes en OpenStack desde el CLI (Parte 2)"
---

## Trabajar con puertos

Podemos listar los puertos de una red, o de un router o de una instancia:

        openstack port list --network mi_red
        openstack port list --router mi_router
        openstack port list --server instancia_prueba2

Si necesitamos que una instancia o un router tenga una interfaz con una **dirección IP determinada** tenemos que crear un puerto. Esta circunstancia se puede dar:

* Cuando trabajamos con una red con DHCP, estaremos haciendo una **reserva**.
* Cuando trabajamos con una red sin DHCP.

Para crear un puerto con una dirección IP fija: 

        openstack port create --network mi_red --fixed-ip ip-address=192.168.0.100 mi_port

A partir de un puerto creado, podemos usarlo para crear por ejemplo una instancia que use dicho puerto:

        openstack server create --flavor m1.mini \
        --image "Debian 13.0 - Trixie" \
        --security-group default \
        --key-name clave_jdmr \
        --port mi_port \
        instancia_prueba4

A partir de un puerto creado, podemos añadir una interfaz a un router:

        openstack port create --network mi_red --fixed-ip ip-address=192.168.0.200 mi_port2
        openstack router create mi_router3
        openstack router add port mi_router3 mi_port2

De manera similar podemos añadir una nueva interfaz a una instancia correspondiente al puerto que hemos creado:

        openstack port create --network mi_red --fixed-ip ip-address=192.168.0.201 mi_port3
        openstack server add port nombre_instancia mi_port3

{% capture notice-text %}
## Ejercicio

1. Crea una instancia llamada `maquina2` en la red `mired1` que tenga la dirección IP fija `192.168.0.200`.
2. Añade una interfaz de red a la esta máquina para conectarla a la red de tu proyecto con la dirección `10.0.0.100`.
3. Configura la nueva interface de la instancia.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Deshabilitar el grupo de seguridad de una instancia

* OpenStack nos proporciona un **cortafuegos por cada interfaz de red** que tiene una instancia. Las reglas de este cortafuegos están gestionadas en los **Grupos de Seguridad**.
* Tenemos la opción de **habilitar o deshabilitar** la seguridad de un determinado puerto, es decir **activar o desactivar el cortafuegos** para cada interfaz.
* El cortafuegos, tiene reglas asociadas a nuestra configuración de los Grupos de Seguridad (por ejemplo, abrir el puerto 80).
* Además tiene reglas adicionales para evitar **ataques de spoofing**. Estas reglas que aumentan la seguridad de los puertos provocan que algunos escenarios que montamos en OpenStack no funcionen de manera adecuada, por ejemplo, **si queremos que una instancia haga de router**.

Para quitar el grupo de seguridad a una instancia, para quitar el cortafuego que le hemos asignado:

    * Lo primero es quitar el grupo de seguridad a la instancia:

        openstack server remove security group instancia_prueba4 default

    * Ahora la instancia tiene todos los puertos cerrado, por lo que a continuación hay que deshabilitar la seguridad del puerto:

        openstack port set --disable-port-security mi_port
    
    * Nota: Si el puerto no tiene nombre tenemos que indicar el id del puerto.

Se pueden hacer también, las dos operaciones, ejecutando:

```
openstack port set --disable-port-security --no-security-group mi_port
```

{% capture notice-text %}
## Ejercicio

1. Deshabilita la seguridad de los interfaces de la instancia `maquina2`.
2. Comprueba que aunque no tengas el puerto 22 abierto en el Grupo de Seguridad puedes acceder sin problema con SSH a la instancia.


{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Eliminación de la infraestructura de red creada

El orden para eliminar la infraestructura de red creada es:

1. Eliminar todas las instancias conectadas a la red.
2. Desconectar la red del router.

        openstack router remove subnet mi_router mi_subred

3. Eliminar la red y el router.

{% capture notice-text %}
## Ejercicio

1. Elimina las instancias, la red y el router que has creado en este ejercicio.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>