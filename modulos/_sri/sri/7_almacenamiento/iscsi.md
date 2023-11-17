---
title: Introducción a iSCSI
---

## iSCSI server con tgt

En el servidor (donde tenemos un disco /dev/vdb), instalamos el servidor:

    apt install tgt

### Configuración manual de targets

Creamos un nuevo target llamado `target1`:

    tgtadm --lld iscsi --op new --mode target --tid 1 -T iqn.2021-11.org.example:target1

Si lo queremos borrar:

    tgtadm --lld iscsi --op delete --mode target --tid 1

Añadimos una unidad lógica (LUN) al target (podemos añadir todas las que queramos):

    tgtadm --lld iscsi --op new --mode logicalunit --tid 1 --lun 1 -b /dev/vdb

Para borrar la unidad lógica:

    tgtadm --lld iscsi --op delete --mode logicalunit --tid 1 --lun 1

Para ver los targets definidos:

    tgtadm --lld iscsi --op show --mode target

Habilitamos el poder compartir el target por todos los interfaces:

    tgtadm --lld iscsi --op bind --mode target --tid 1 -I ALL

### Creación automática de targets

La configuración anterior no es persistente. Para hacerla persistente podemos usar `tgt-admin`.

Para ver los targets definidos:

    tgt-admin -s

Para guardar la configuración de los targets:

    tgt-admin --dump > /etc/tgt/conf.d/example.es.conf

De tal manera que al reiniciar la máquina, la definición de targets este realizada.

## Cliente iSCSI. iSCSI Initiator

En otra máquina cliente con conectividad con el servidor, instalamos:

    apt install open-iscsi

Automaticamente se configura un nombre para el incializador, que se guardará en el fichero `/etc/iscsi/initiatorname.iscsi`:

    ## DO NOT EDIT OR REMOVE THIS FILE!
    ## If you remove this file, the iSCSI daemon will not start.
    ## If you change the InitiatorName, existing access control lists
    ## may reject this initiator.  The InitiatorName must be unique
    ## for each iSCSI initiator.  Do NOT duplicate iSCSI InitiatorNames.
    InitiatorName=iqn.1993-08.org.debian:01:8c389c72931

Lo primero que hacemos es descubrir los targets que se están compartiendo por el servidor (suponemos que el servidor tiene la IP 10.0.0.1, aunque podemos también usar un nombre):

    iscsiadm --mode discovery --type sendtargets --portal 10.0.0.1

Nos muestra el nombre del target y ya podemos hacer la conexión:

    iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 --login

A partir de ahora tendremos un nuevo dispositivo de bloque en la máquina cliente que podremos formatear y montar.

Si el target tiene definido un usuario y contraseña para la conexión, tendremos que definirla después de conectarnos:

    iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 -o update \
    -n node.session.auth.username -v username
    iscsiadm --mode node -T iqn.2021-11.org.example:target1 --portal 10.0.0.1 -o update \
    -n node.session.auth.password -v password    

Es posible conectarse a todos los targets disponibles con:

    iscsiadm --mode node --portal 10.0.0.1 -L

Para visualizar la sesión actual:

    iscsiadm -m session

Si queremos desconectarnos de un target:

    iscsiadm -m node -T iqn.2021-11.org.example:target1 -p 10.0.0.1 -u

Y si queremos desconectarnos de todos los targets:

    iscsiadm -m node -p 10.0.0.1 --logout

open-iscsi proporciona un demonio que se encarga de las sesiones e iniciará sesión en los destinos targets  después del próximo reinicio.

## Para seguir investigando

* Autentificación CHAP en iSCSI
* iSCSI iterator en Windows


