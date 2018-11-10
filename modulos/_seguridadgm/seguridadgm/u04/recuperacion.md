---
title: "Recuperación de información"
permalink: /seguridadgm/u04/recuperacion.html
---

## Recuperación de particiones

Vamos a añadir un disco a una máquina virtual y vamos a crear dos particiones: una `ext4` y otra `ntfs`. Formatealas, monta las particiones y crea ficheros en ellas (copia ficheros reales en ellas).

A continuación vamos a simular la perdida de particiones. Con ´fdisk´ borra las particiones del disco.

El ejercicio que tienes que hacer es utilizando la herramienta [`TestDisk`](https://www.cgsecurity.org/wiki/TestDisk). Recupera las dos particiones. ¿Has podido recuperar los ficheros?

Nota: antes de tratar de recuperar datos del disco o de la unidad extraíble, podemos hacer una copia byte a byte y trabajar con la imagen.

    dd if=/dev/sdb1 of=/home/usuario/copia.dd

Documenta el proceso para realizar la recuperación. Esta práctica la puedes hacer en Windows o en Linux.

## Recuperación de ficheros

¿Cómo puede recuperarse información de un disco cuando se han borrado los ficheros? Lo que el SO hace es marcar las posiciones del disco como libres (o borradas), pero realmente no se borra la información.

Herramientas:

* [Foremost](http://foremost.sourceforge.net)
* [Scalpel](http://www.digitalforensicssolutions.com/Scalpel)
* [PhotoRec](http://www.cgsecurity.org/wiki/PhotoRec)
* [Recuva](http://www.piriform.com/recuva)

### Pero, ¿es posible eliminar de forma definitiva un fichero (o un disco)?

Usando la utilidad `shred` se puede sobrescribir el contenido de un fichero (o un disco completo) ya existente con contenido basura antes de eliminarlo, lo que imposibilitaría su recuperación posterior.

Sintaxis:

    $ shred -n numero_de_pasadas -vz nombre_fichero

Nota: Con la opción `-u` se eliminaría el fichero tras sobrescribirlo.

    $ shred -n numero_de_pasadas -vz /dev/nombre_disco

Documenta la utilización de una de las herramientas de recuperación de ficheros antes descrita para Windows y Linux, explicando todas las posibilidades que ofrece. En Linux borra un fichero con el comando `shred` y comprueba que no es posible su recuperación.
