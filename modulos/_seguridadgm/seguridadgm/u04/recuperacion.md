---
title: "Recuperación de ficheros borrados"
permalink: /seguridadgm/u04/recuperacion.html
---

## Recuperación de la información

¿Cómo puede recuperarse información de un disco cuando se han borrado los ficheros? Lo que el SO hace es marcar las posiciones del disco como libres (o borradas), pero realmente no se borra la información.

Herramientas:

* Foremost: http://foremost.sourceforge.net (Tutorial)
* Scalpel: http://www.digitalforensicssolutions.com/Scalpel (Tutorial)
* Magicrescue: http://www.itu.dk/people/jobr/magicrescue (Tutorial)
* PhotoRec: http://www.cgsecurity.org/wiki/PhotoRec
* Recuva: http://www.piriform.com/recuva 

Nota: antes de tratar de recuperar datos del disco o de la unidad extraíble, podemos hacer una copia byte a byte y trabajar con la imagen.

    dd if=/dev/sdb1 of=/home/ususario/copia.dd

## Pero, ¿es posible eliminar de forma definitiva un fichero (o un disco)?

Usando la utilidad `shred` se puede sobrescribir el contenido de un fichero (o un disco completo) ya existente con contenido basura antes de eliminarlo, lo que imposibilitaría su recuperación posterior.

Sintaxis:

    $ shred -n numero_de_pasadas -vz nombre_fichero

Nota: Con la opción `-u` se eliminaría el fichero tras sobrescribirlo.

    $ shred -n numero_de_pasadas -vz /dev/nombre_disco

Documenta la utilización de una de las herramientas de recuperación de ficheros antes descrita para Windows y Linux, explicando todas las posibilidades que ofrece.
