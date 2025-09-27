---
title: "Clase 2: Gestión del almacenamiento en QEMU/KVM + libvirt"
---

## ¿Qué vas a aprender en esta clase?

* Los conceptos de pool de almacenamiento y volúmenes.
* La gestión de los pool de almacenamientos.
* La gestión de los volúmenes.
* La característica de aprovisionamiento ligero de los ficheros de discos qcow2.
* La gestión de nuevos discos en las máquinas virtuales.

## Recursos

* Curso completo: [Profundización a la virtualización con KVM/libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2)
* En concreto los apartados:
  * Gestión del almacenamiento
* [Presentación: Resumen virtualización en Linux](https://fp.josedomingo.org/sri/pdf/resumen_virtualizacion.pdf)

## Ejercicio

1. Siguiendo el apartado [Gestión de pools de almacenamiento](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase2.md), muestra los pool de almacenamientos con `virsh` que tienes definidos. ¿De qué tipo son?. ¿Qué se guarda en cada uno de ellos?.
2. Con `virsh` crea un nuevo pool de almacenamiento de tipo **dir**, que se llame **discos** y que corresponda al directorio `/srv/discos`. Inicia el nuevo pool de almacenamiento. Comprueba que se ha creado el nuevo pool.
3. Siguiendo el apartado [Gestión de volúmenes de almacenamiento con virsh](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase3.md), muestra con `virsh` los volúmenes (imágenes de discos) que tienes creado en el pool de almacenamiento `default`. 
4. Con `virsh` crea un nuevo volumen en el pool de almacenamiento `discos` que se llame **disco1.qcow2** y de tamaño 1Gb.
5. Siguiendo el apartado [Gestión de volúmenes de almacenamiento con herramientas específicas](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase4.md), crea un fichero de imagen en el directorio `/srv/discos` que se llame **disco2.qcow2** con 2Gb de tamaño, con `qemu-img`. Conviértelo a un volumen y muestra los volúmenes en el pool de almacenamiento `discos` para comprobar que se ha creado de forma correcta.
6. ¿Qué características tienen los ficheros de imágenes **qcow2**? Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco.
7. Siguiendo el apartado [Trabajar con volúmenes en las máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase5.md), añade a la máquina linux con la que estás trabajando el **disco1** y el **disco2** utilizando `virsh`. Formatea los discos y móntalos de forma persistente.
8. Siguiendo el apartado [Redimensión de discos en máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase6.md), redimensiona el **disco1** a 2 Gb usando `virsh`, redimensiona el **disco2** a 3Gb usando `qemu-img`. Finalmente redimensiona el sistema de ficheros de cada uno de los discos.
9. Crea un nuevo volumen **nuevo_disco.img** de tipo raw y tamaño 10Gb en el pool **discos**. Lista los volúmenes del pool de almacenamiento `discos` visualizando la capacidad del disco y el tamaño que ocupa realmente en disco. ¿Cuánto espacio ocupa realmente el volumen **nuevo_disco.img**.
10. Siguiendo el apartado [Trabajar con volúmenes en las máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad04/clase5.md), realiza la instalación de una MV con `virt-install` que use el volumen anterior que has creado como disco de la máquina.
