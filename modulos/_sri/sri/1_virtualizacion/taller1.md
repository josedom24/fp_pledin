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

1. Muestra los pool de almacenamientos con `virsh` que tienes definidos. ¿De qué tipo son?. ¿Qué se guarda en cada uno de ellos?. Puedes verlos también con `virt-manager`.
    * **Entrega**: El comando `virsh` y su salida que nos permite ver los pool de almacenamiento. Responde las preguntas.
2. Con `virsh` crea un nuevo pool de almacenamiento de tipo **dir**, que se llame **discos** y que corresponda al directorio `/srv/discos`. Inicia el nuevo pool de almacenamiento. Comprueba que se ha creado el nuevo pool.
    * **Entrega**: El comando `virsh` y la salida que nos muestra información del pool que has creado. El comando `virsh` que crea el directorio asociado al nuevo pool.
3. Muestra con `virsh` los volúmenes (imágenes de discos) que tienes creado en el pool de almacenamiento `default`. Puedes comprobar con `virt-manager` los volúmenes que tienes creados.
    * **Entrega**: El comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `default`. 
4. Con `virsh` crea un nuevo volumen en el pool de almacenamiento `discos` que se llame **disco1.qcow2** y de tamaño 1Gb.
5. Con `qemu-img` crea un fichero de imagen en el directorio `/srv/discos` que se llame **disco2.qcow2** con 2Gb de tamaño. Conviértelo a un volumen y muestra los volúmenes en el pool de almacenamiento `discos` para comprobar que se ha creado de forma correcta.
    * **Entrega**:  Una vez que crees los dos nuevos volúmenes, el comando `virsh` y su salida que nos permite ver los volúmenes que tienes creado en el pool `discos`. Muestra las instrucciones que has usado para crear los dos volúmenes.
6. ¿Qué características tienen los ficheros de imágenes **qcow2**? Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco.
    * **Entrega**: Responde la pregunta. Los comandos y las salidas que nos permiten comprobar el aprovisionamiento ligero.
7. Añade a la máquina linux con la que estás trabajando el **disco1** utilizando `virsh` y el **disco2** utilizando `virt-manager`. Formatea los disco y móntalos de forma persistente.
    * **Entrega**: Instrucción para añadir el **disco1**. Ejecución de un subcomando de `virsh` para visualizar los dispositivos de bloques conectados a la máquina.
8. Redimensiona el **disco1** a 2 Gb usando `virsh`, redimensiona el **disco2** a 3Gb usando `qemu-img`. Finalmente redimensiona el sistema de ficheros de cada uno de los discos.
    * **Entrega**: Las instrucciones que has ejecutado para redimensionar los discos y los sistemas de archivos.
9. Crea un nuevo volumen **nuevo_disco.img** de tipo raw y tamaño 10Gb en el pool **discos**. Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco. ¿Cuánto espacio ocupa realmente el volumen **nuevo_disco.img**.
    * **Entrega**: La instrucción y la salida de la instrucción que has ejecutado para crear el fichero raw. La instrucción y la salida que nos permite ver cuánto espacio ocupa el volumen que hemos creado.
10. Realiza la instalación de una MV con `virt-install` que use el volumen anterior que has creado como disco de la máquina.
    * **Entrega**: La instrucción que has usado para comenzar la instalación. Una vez la instalación haya terminado, la configuración XML de la máquina donde se comprueba que volumen está usando como disco principal.
