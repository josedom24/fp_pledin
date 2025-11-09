---
Clase 3: "Práctica - Protocolos de almacenamiento"
---

En esta tarea vamos a trabajar con los protocolos de almacenamiento que hemos estudiado. Crea instancias en OpenStack: una será el servidor, otra será el cliente Linux y otra el cliente Windows. Recuerda abrir en el grupo de seguridad los puertos de los protocolos con los que vamos a trabajar.

## Servidor SAN

Vamos a configurar el servidor SAN para que podamos compartir dispositivos de discos a otros servidores de nuestra infraestructura. Tenemos que tener en cuenta lo siguiente:

* El servidor SAN tiene 3 discos 2Gb.
* Vamos a crear un RAID5 de los tres discos con mdadm. ¿Qué tamaño tiene el dispositivo de bloque correspondiente al RAID5?
* Vamos a crear un grupo de volúmenes cuyo dispositivo físico es el disco RAID5. En este grupo de volúmenes crearemos volúmenes que serán los dispositivos que vamos a compartir con otros servidores.
* Es importante darse cuenta que cuando tengamos el dispositivo de bloque compartido en otro servidor, todo lo que se guarde en ese disco se guardará en nuestro servidor SAN en un dispositivo disco RAID5 con lo que la información estará respaldada y se podrá recuperar aunque algunos de los discos fallen.

Ya tenemos el servidor SAN preparado, ya podemos empezar a compartir dispositivos de bloque:

* Crea un target con una Unidad lógica (LUN) correspondiente a un volumen lógico de 1Gb y conéctala a un cliente GNU/Linux. Explica cómo escaneas desde el cliente buscando los targets disponibles y utiliza la unidad lógica proporcionada, formateándola si es necesario y montándola.
* Utiliza [systemd mount](https://eltallerdelbit.com/montar-unidades-con-systemd/) para que el target se monte automáticamente al arrancar el cliente.
* Crea un target con 2 LUN (correspondientes a dos volúmenes lógicos de 512Mb cada uno) y autenticación por CHAP y conéctala a un cliente windows. Explica cómo se escanea la red en windows y cómo se utilizan las unidades nuevas (formateándolas con NTFS)

El sistema debe funcionar después de un reinicio de las máquinas.

## Servidor NAS

Ahora vamos a crear un servidor NAS en la misma máquina en la que tenemos el servicio SAN, para compartir almacenamiento mediante **NFS**, de forma que otros servidores GNU/Linux puedan montar carpetas remotas y utilizarlas como si fueran locales.

* Crea en el servidor un **volumen lógico** de 1 GB dentro del grupo de volúmenes existente (basado en el RAID5). Ese volumen será el que se compartirá mediante NFS.
* Crea un punto de montaje en el servidor y configura el servicio NFS para **exportar** dicho directorio a la red local, de modo que cualquier servidor del mismo segmento pueda acceder con permisos de lectura y escritura.
* En un cliente GNU/Linux, verifica qué recursos NFS ofrece el servidor SAN y **monta el directorio compartido** en una carpeta local.
* Crea algún archivo o directorio en el cliente y comprueba que el contenido aparece también en el servidor SAN.
* Configura el cliente para que el **montaje NFS se realice automáticamente al arrancar** utilizando una unidad de montaje de systemd.
* Monta el mismo directorio en una máquina Windows.