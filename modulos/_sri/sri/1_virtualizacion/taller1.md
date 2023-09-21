---
title: "Taller 1: Gestión del almacenamiento en QEMU/KVM + libvirt"
---

## ¿Qué vas a aprender en este taller?

* Los conceptos de pool de almacenamiento y volúmenes.
* La gestión de los pool de almacenamientos.
* La gestión de los volúmenes.
* La características de aprovisionamiento ligero de los ficheros de discos qcow2.
* La gestión de nuevos discos en las máquinas virtuales.

## Recursos para realizar este taller

* Capítulo 5 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## ¿Qué tienes que hacer?

1. Muestra los pool de almacenamientos con `virsh` que tienes definido. ¿De qué tipo son?. ¿Qué se guarda en cada uno de ellos?. Muéstralos también con `virt-manager`.
2. Con `virsh` crea un nuevo pool de almacenamiento de tipo **dir**, que se llame **discos** y que los ficheros se guarden en el directorio `/srv/discos`. Inicia el nuevo pool de almacenamiento. Comprueba que se ha creado el nuevo pool.
3. Muestra con `virsh` los volúmenes (imágenes de discos) que tienes creado en el pool de almacenamiento `default`. Comprueba con `virt-manager` los volúmenes que tienes creados.
4. Con `virsh` crea un nuevo volumen en el pool de almacenamiento `discos` que se llame **disco1.qcow2** y de tamaño 1Gb.
5. Con `qemu-img` crea un fichero de imagen en el directorio `/srv/discos` que se llame **disco2.qcow2** con 2Gb de tamaño. Conviértelo a un volumen y muestra los volúmenes en el pool de almacenamiento `discos` para comprobar que se ha creado de forma correcta.
6. ¿Qué características tienen los ficheros de imágenes **qcow2**? Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco.
7. Añade a la máquina linux con la que estás trabajando el **disco1** utilizando `virsh` y el **disco2** utilizando `virt-manager`. Formatea los disco y móntalos de forma persistente.
8. Redimensiona el **disco1** a 2 Gb usando `virsh`, redimensiona el **disco2** a 3Gb usando `qemu-img`. Finalmente redimensiona el sistema de ficheros de cada uno de los discos.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. El comando `virsh` y su salida que nos permite ver los pool de almacenamiento. Responde las preguntas del punto 1.
2. Cuando crees el nuevo pool de almacenamiento, la salida del comando `virsh -c qemu:///system pool-info discos`.
3. El comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `default`.
4. Una vez que crees los dos nuevos volúmenes, el comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `discos` (utiliza el parámetro adecuada para que se demostrar el aprovisionamiento ligero). Indica las instrucciones que has usado para crear los dos volúmenes.
5. Antes de redimensionar los discos, cuando tengas añadidos los discos a la máquina, la salida del comando `df -h` para comprobar que están montado de forma correcta.
6. Después de redimensionar los discos, de nuevo la salida del comando `df -h` donde se compruebe que se ha cambiado el tamaño de los mismos.  

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
