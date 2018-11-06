---
title: "Práctica RAID 1"
permalink: /seguridadgm/u03/raid1.html
---

## RAID 1 en windows

Tienes que montar un raid 1 en windows con dos discos de 1 Gb. ¿Cuánto ocupara la nueva unidad de discos? Realiza un vídeo donde captures el escritorio y explicando cómo has realizado la práctica.

## RAID 1 en linux

Realiza el mismos ejercicio en Linux, utilizando la herramienta `mdadm`. Documenta con detalle todo el proceso de realización del RAID (suponemos que partimos de una máquina con dos discos conectados y con una partición primaria). ¿Qué significa las dos U que aparecen cuando ejecutas el comando `cat /proc/mdstat`?.

### ¿Qué ocurre cuando un disco falla?

Podemos simular la avería o fallo de un disco con la instrucción:

    # mdadm /dev/md1 -f /dev/sdxx

Provoca el fallo de un dispositivo del raid, muestra la información del RAID para comprobar que realmente un disco se ha caído. ¿Sigue funcionando el RAID? Averigua la instrucción para eliminar el disco dañado del RAID.

Añade un nuevo disco de 1Gb a la máquina y averigua cómo puedes añadirlo al RAID, ejecuta `cat /proc/mdstat` para comprobar cómo se produce la sincronización (tienes que ejecutarlo lo más rápido posible porque la sincronización de 1Gb es muy rápida).

### Disco de reserva

Investiga como añadir un disco de reserva, y añádelo al RAID. Muestra información del RAID para comprobar que tienes un disco Hot Spare.

Vuelve a simular la rotura de un disco del RAID y comprueba como se añade automáticamente el disco de respaldo y se realiza la sincronización. 
