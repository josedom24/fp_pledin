---
title: "Práctica RAID 1"
permalink: /seguridadgm/u03/raid1.html
---

## RAID 1 en windows

Tienes que montar un raid 1 en windows con dos discos de 1 Gb. ¿Cuánto ocupara la nueva unidad de discos? Realiza un vídeo donde captures el escritorio y explicando cómo has realizado la práctica.

## RAID 1 en linux

Realiza el mismos ejercicio en Linux, utilizando la herramienta `mdadm`. Documenta con detalle todo el proceso de realización del RAID (suponemos que partimos de una máquina con dos discos conectados y con una partición primaria). ¿Qué significa las dos U que aparecen cuando ejecutas el comando `cat /dev/mdstat`?.

### ¿Qué ocurre cuando un disco falla?

Podemos simular la avería o fallo de un disco con la instrucción:

    # mdadm -f /dev/sdxx

Provoca el fallo de un dispositivo del raid, muestra la información del RAID para comprobar que realmente un disco se ha caído. ¿Sigue funcionando el RAID? Averigua la instrucción para eliminar el disco dañado del RAID.

Añade un nuevo disco de 1Gb a la máquina y averigua cómo puedes añadirlo al RAID, ejecuta `cat /dev/mdstat` para comprobar cómo se produce la sincronización (tienes que ejecutarlo lo más rápido posible porque la sincronización de 1Gb es muy rápida).
