---
title: "Sincronización de carpetas con rsync"
permalink: /seguridadgm/u04/rsync.html
---

Para realizar esta práctica te puede ser de mucha utilidad leer el siguiente artículo:

* [Copias de seguridad en Linux con rsync](https://gigastur.es/copias-seguridad-linux-rsync)

Para realizar esta práctica necesitas dos máquinas linux, en la misma red, y con `rsync` instalado. Por lo tanto si quieres puedes hacer la práctica ayudado de un compañero.

1. En la primera máquina virtual construya el directorio: `~/datos`
2. Ejecute el comando: `touch datos/fichero-{1..100}.txt`
3. Observe el contenido del directorio datos. Después utilice `rsync` para sincronizar el directorio datos de la primera a la segunda máquina.
4. Utilice un editor para editar alguno de los 100 ficheros escribiendo en su interior algunas líneas de texto. Utilice de nuevo rsync para sincronizar el directorio. ¿Se transfieren todos los ficheros?
5. Borre el fichero datos/fichero-100.txt y sincronice el directorio. En el destino ¿existe el fichero?¿Qué opción se debe utilizar para que en el destino se borren los ficheros que no existen en el origen?
6. ¿Qué debe hacer para sincronizar de manera recursiva el directorio `/home` de la primera máquina a `~/copia_de_seguridad` en la segunda máquina? Pide al compañero que realice algún cambio en algún fichero de su home y vuelve a realizar la sincronización. ¿Qué ficheros se han copiado?

