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
    * **Entrega**: El comando `virsh` y su salida que nos permite ver los pool de almacenamiento. La captura de pantalla de `virt-manager` donde se ven los pools de almacenamiento. Responde las preguntas.
2. Con `virsh` crea un nuevo pool de almacenamiento de tipo **dir**, que se llame **discos** y que los ficheros se guarden en el directorio `/srv/discos`. Inicia el nuevo pool de almacenamiento. Comprueba que se ha creado el nuevo pool.
    * **Entrega**: El comando `virsh` y la salida que nos muestra información del pool que has creado. El comando `virsh` que crea el directorio aasociado al nuevo pool.
3. Muestra con `virsh` los volúmenes (imágenes de discos) que tienes creado en el pool de almacenamiento `default`. Comprueba con `virt-manager` los volúmenes que tienes creados.
    * **Entrega**: El comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `default`. Una captura de pantalla para ver los volúmenes desde `virt-manager`.
4. Con `virsh` crea un nuevo volumen en el pool de almacenamiento `discos` que se llame **disco1.qcow2** y de tamaño 1Gb.
5. Con `qemu-img` crea un fichero de imagen en el directorio `/srv/discos` que se llame **disco2.qcow2** con 2Gb de tamaño. Conviértelo a un volumen y muestra los volúmenes en el pool de almacenamiento `discos` para comprobar que se ha creado de forma correcta.
    * **Entrega**:  Una vez que crees los dos nuevos volúmenes, el comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `discos`. Indica las instrucciones que has usado para crear los dos volúmenes.
6. ¿Qué características tienen los ficheros de imágenes **qcow2**? Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco.
    * **Entrega**: Responde la pregunta. Los comandos y las salidas que nos permiten comprobar el aprovisionamiento ligero.
7. Añade a la máquina linux con la que estás trabajando el **disco1** utilizando `virsh` y el **disco2** utilizando `virt-manager`. Formatea los disco y móntalos de forma persistente.
    * **Entrega**: Instrucción para añadir el disco1, captura de pantalla de `virt-amangar` donde se ve que has añadido el disco2. La salida del comando `df -h`. La modificación realizada para montarlos de forma persistente.
8. Redimensiona el **disco1** a 2 Gb usando `virsh`, redimensiona el **disco2** a 3Gb usando `qemu-img`. Finalmente redimensiona el sistema de ficheros de cada uno de los discos.
    * **Entrega**: Entrega las instrucciones que has ejecutado para redimensionar los discos y los sistemas de archivos.
