---
title: "Taller 1: Introducción a iSCSI"
---

## ¿Qué vas a aprender en este taller?

* Configuración de un servidor iscsi.
* Gestión de targets y LUN.
* Uso de un cliente iscsi. iscsi initiator.
* Autentificación CHAP en iSCSI
* iSCSI iterator en Windows

## ¿Qué tienes que hacer?

Utiliza el siguiente fichero [`Vagrantfile`](files/iscsi/Vagrantfile) para realizar el taller:

1. En el servidor, crea un target con una LUN y conéctala a un cliente GNU/Linux. Explica cómo escaneas desde el cliente buscando los targets disponibles y utiliza la unidad lógica proporcionada, formateándola si es necesario y montándola.
2. Utiliza [systemd mount](https://eltallerdelbit.com/montar-unidades-con-systemd/) para que el target se monte automáticamente al arrancar el cliente.
3. Crea un target con 2 LUN y autenticación por CHAP y conéctala a un cliente windows. Explica cómo se escanea la red en windows y cómo se utilizan las unidades nuevas (formateándolas con NTFS)
4. El sistema debe funcionar después de un reinicio de las máquinas.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Las instrucciones que has ejecutados en el cliente iscsi para escanear los targets y formatear u montar el dispositivo compartido.
2. La configuración que has realizado para que el montaje sea automático tras iniciar el sistema.
3. Capturas de pantallas donde se vea cómo se ha escaneado los targets y se han formateado los dispositivos de bloque y se han montado en el cliente windows.
4. Se realizará una prueba delante del profesor para comprobar que el sistema funciona después de un reinicio. 

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>		
