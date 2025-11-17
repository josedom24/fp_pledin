---
title: "Clase 3: Práctica - Protocolos de almacenamiento"
---

En esta tarea vamos a trabajar con los **protocolos de almacenamiento** que hemos estudiado. Vamos a trabajar sobre el escenario que has creado en la tarea sobre el protocolo HTTP.
Crea una máquina virtual que va a ser nuestro **servidor de almacenamiento** que va a ofrecer una **SAN** (protocolo **iSCSI**) y una **NAS** (protocolo **NFS**). Dicha máquina virtual tendrá las siguientes características:

* Estará conectada a la red del **servidorweb**, al **backend1** y al **backend2**.  si lo hiciéramos más real crearíamos una **red de datos** que conecta los servidores web con el servidor de almacenamiento.
* Estará conectada a una red de tipo NAT para que tenga salida a internet.
* Tendrá tres discos adicionales de 3Gb.
* Crearemos un RAID5 de los tres discos con **`mdadm`**. ¿Qué tamaño tiene el dispositivo de bloque correspondiente al RAID5?
* Crearemos un grupo de volúmenes cuyo dispositivo físico es el disco RAID5. En este grupo de volúmenes crearemos volúmenes que serán los dispositivos que vamos a compartir con otros servidores.

Es importante darse cuenta que cuando tengamos el dispositivo de bloque compartido en otro servidor, todo lo que se guarde en ese disco se guardará en nuestro servidor SAN en un dispositivo disco RAID5 con lo que la información estará respaldada y se podrá recuperar aunque algunos de los discos fallen.


## Servidor SAN

Ya tenemos el servidor de almacenamiento preparado, vamos a añadir la funcionalidad de servidos SAN y poder empezar a compartir dispositivos de bloque:

* Crea un target con 2 LUN (correspondientes a dos volúmenes lógicos de 512Mb cada uno) y autenticación por CHAP y conéctala al **servidorweb**.
* Explica cómo escaneas desde el **servidorweb** (cliente iSCSI) buscando los targets disponibles y utiliza uno de las unidades lógicas proporcionadas, formateándola y montándola.
* Utiliza [systemd mount](https://eltallerdelbit.com/montar-unidades-con-systemd/) para que el target se monte automáticamente al arrancar el cliente.

El sistema debe funcionar después de un reinicio de las máquinas.

**Pregunta**: ¿Qué ocurriría si montamos el mismo dispositivo en otra máquina? ¿Podrían ller las dos máquinas del mismo disco? ¿Y escribir?

## Servidor NAS

Ahora vamos a crear un servidor NAS en nuestro servidor de almacenamiento, para compartir almacenamiento mediante **NFS**, de forma que otros servidores GNU/Linux puedan montar carpetas remotas y utilizarlas como si fueran locales.

* Crea en el servidor un **volumen lógico** de 1 GB dentro del grupo de volúmenes existente (basado en el RAID5). Ese volumen será el que se compartirá mediante NFS. Formatea el volumen.
* Crea un punto de montaje en el servidor con le volumen formateado y configura el servicio NFS para **exportar** dicho directorio a la red local, de modo que cualquier servidor del mismo segmento pueda acceder con permisos de lectura y escritura.
* En el **backend1**,  **monta el directorio compartido** en una carpeta local.
* Haz lo mismo en el **backend2**.
* Crea una página web en dicho directorio y modifica el virtual host de los servidores para que sirvan dicha página.
* Configura los servidores backend para que el **montaje NFS se realice automáticamente al arrancar** utilizando una unidad de montaje de systemd.

**Pregunta**: ¿Ha habido algún problema de que el directorio este compartido en los dos servidores? ¿Qué ocurre si modificas el fichero en uno de ellos? 

{% capture notice-text %}

## Entrega

### Del servidor SAN

1. El contenido del fichero de configuración del servidor iSCSI.
2. La salida de la instrucción en el cliente iSCSI para ver las sesiones que tienes activas.
3. La lista de dispositivos en el cliente iSCSI, para ver los dispositivos que se han compartido.
4. El fichero de configuración de la unidad de montaje.
5. Después de un reinicio, entrega las pruebas necesarias para comprobar que sigue funcionando el sistema.
6. Contesta la pregunta, después de buscar información.

### Del servidor SAN

1. El fichero de configuración de la unidad de montaje en el servidor.
2. El fichero de configuración del servidor NFS.
3. Prueba de que has montado el directorio en los servidores **backend1** y **backend2**.
4. Acceso a la página `app.tunombre.org` para acceder a la nueva página balanceada.
5. Contesta la pregunta, después de buscar información.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>