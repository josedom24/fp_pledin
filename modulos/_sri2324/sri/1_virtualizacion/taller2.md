---
title: "Taller 2: Gestión de pool de almacenamiento lógico en KVM/libvirt"
---

## ¿Qué vas a aprender en este taller?

* A gestionar pool de almacenamiento lógicos en KVM/libvirt.
* A gestionar volúmenes lógicos para crear discos para las máquinas virtuales.
* A montar los volúmenes lógicos para acceder a los ficheros de los discos.

## ¿Qué tienes que hacer?

Para realizar este taller tenemos dos opciones:

1. Usar el KVM/libvirt que tenemos en nuestra máquina física, pero **necesitamos tener un grupo de volúmenes con espacio libre**.
2. Usar **Virtualización Anidada**: Con esta característica se permite la ejecución de instrucciones KVM dentro de máquinas virtuales KVM, lo cual nos posibilita la ejecución de máquinas virtuales dentro de máquinas virtuales. De esta manera,podemos crear un laboratorio de prueba de QEMU/KVM ejecutándolos en una máquina virtual. En este caso crearíamos una máquina virtual, en ella tendríamos que tener un grupo de volúmenes con espacio libre. En esa máquina instalaríamos KVM/libvirt y realizaríamos el taller.

1. Crea con `virsh` un nuevo pool de almacenamiento de tipo lógico. Para ello, lo más fácil, es tener un grupo de volúmenes con espacio libre. 
    * **Entrega**: Instrucción para crear el pool de almacenamiento.
2. Crea un volumen en ese pool de almacenamiento. Comprueba que se ha creado un volumen lógico nuevo en el grupo de volúmenes.
    * **Entrega**: Instrucción para crear el volumen. Instrucción y salida donde se vea el volumen creado.
3. Usa `virt-install` para crear una máquina virtual cuyo disco corresponda al volumen que has creado anteriormente.
    * **Entrega**: Instrucción para realizar la instalación. 
4. Una vez que la máquina este funcionando, crea un nuevo volumen en el pool de tipo **lógico** y añádelo a la máquina.
    * **Entrega**: La configuración XML de la máquina donde se ve el almacenamiento de la misma (se deben ver los dos discos).
5. Apaga la máquina, y siguiendo el artículo [Acceder a una imagen de disco KVM ubicada en un volumen lógico](https://albertomolina.wordpress.com/2009/12/14/acceder-a-una-imagen-de-disco-kvm-ubicada-en-un-volumen-logico/) monta la partición del disco de la máquina en tu anfitrión para acceder al sistema de archivos.
    * **Entrega**: Las instrucciones ejecutadas para montar la partición del disco, y la lista de ficheros del sistema de archivos.

