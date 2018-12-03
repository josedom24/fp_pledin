---
title: "Prueba: RAID y copia de seguridad"
permalink: /seguridadgm/u04/prueba.html
---

# RAID5

1. Utilizando discos de 1Gb queremos crear un disco RAID5 de 3Gb con un disco de reserva. Explica los pasos para realizarlo. Muestra información sobre el raid creado.

2. Particiona el disco con dos particiones, formatealas con ext4 y montalá en dos directorio que tengan como nombre *tunombre1* y *tunombre2*.

3. Simula el fallo de un disco. ¿Qué ocurre con el RAID? Demuestra que el RAID sigue funcionando y muestra información sobre el RAID.

4. Simula el fallo de otro disco. ¿Qué ocurre ahora? Realiza las acciones que creas conveniente para que vuelva a funcionar el RAID. Demuestra que el RAID sigue funcionando y muestra información sobre el RAID.

# Copia de seguridad

1. Descarga las siguientes [copias de seguridad](backup.zip) y recupera:

    * El día 2
    * El día 4

2. Añade el `fich5.txt` a los ficheros del día 4 y crea una copia total. Realiza los siguientes copias:

    * Borra el `fich5.txt`, añade el `fich6.txt` y crea una copia incremental.
    * Borra el `fich6.txt` y crea una copia diferencial.

Recupera los ficheros de la última copia.
