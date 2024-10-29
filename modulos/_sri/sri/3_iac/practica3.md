---
title: "Práctica (2 / 3): Creación y configuración de un servidor LAMP"
---

## SAN y iSCSI

Vamos a configurar el servidor SAN para que podamos compartir dispositivos de discos a otros servidores de nuestra infraestructura. Tenemos que tener en cuenta lo siguiente:

* El servidor SAN tiene 3 discos 2Gb.
* Vamos a crear un RAID5 de los tres discos con `mdadm`. ¿Qué tamaño tiene el dispositivo de bloque correspondiente al RAID5?
* Vamos a crear un grupo de volúmenes cuyo dispositivo físico es el disco RAID5. En este grupo de volúmenes crearemos volúmenes que serán los dispositivos que vamos a compartir con otros servidores.
* Es importante darse cuenta que cuando tengamos el dispositivo de bloque compartido en otro servidor, todo lo que se guarde en ese disco se guardará en nuestro servidor SAN en un dispositivo disco RAID5 con lo que la información estará respaldada y se podrá recuperar aunque algunos de los discos fallen. 

Ya tenemos el servidor SAN preparado, ya podemos empezar a compartir dispositivos de bloque:

1. Crea un target con una Unidad lógica (LUN) correspondiente aun volumen lógico de 1Gb y conéctala a un cliente GNU/Linux. Explica cómo escaneas desde el cliente buscando los targets disponibles y utiliza la unidad lógica proporcionada, formateándola si es necesario y montándola.
2. Utiliza [systemd mount](https://eltallerdelbit.com/montar-unidades-con-systemd/) para que el target se monte automáticamente al arrancar el cliente.
3. Crea un target con 2 LUN (correspondientes a dos volúmenes lógicos de 512Mb cada uno) y autenticación por CHAP y conéctala a un cliente windows. Explica cómo se escanea la red en windows y cómo se utilizan las unidades nuevas (formateándolas con NTFS)
4. El sistema debe funcionar después de un reinicio de las máquinas.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Las instrucciones que has ejecutados en el cliente iscsi para escanear los targets y formatear u montar el dispositivo compartido.
2. La configuración que has realizado para que el montaje sea automático tras iniciar el sistema.
3. Capturas de pantallas donde se vea cómo se ha escaneado los targets y se han formateado los dispositivos de bloque y se han montado en el cliente windows.
4. Se realizará una prueba delante del profesor para comprobar que el sistema funciona después de un reinicio. 

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
