---
title: "Clase 1: Introducción a la virtualización y a QEMU/KVM/libvirt. Creación de máquinas virtuales desde la línea de comandos"
---

## ¿Qué vas a aprender en esta clase?

* A realizar la instalación del sistema de virtualización KVM/QEMU y libivrt
* A trabajar con la conexión privilegiada a libvirt.
* A usar la línea de comandos para gestionar los recursos virtualizados.

## Teoría

* [Presentación: Virtualización Linux](https://fp.josedomingo.org/sri/pdf/virtualizacion.pdf)

## Recursos

* Curso completo: [Profundización a la virtualización con KVM/libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2)
* En concreto los apartados:
  * Introducción a la virtualización con KVM/libvirt
  * Instalación de KVM/libvirt
  * Creación de máquinas virtuales
* [Presentación: Resumen virtualización en Linux](https://fp.josedomingo.org/sri/pdf/resumen_virtualizacion.pdf)

## Ejercicio

1. Realiza la instalación de QEMU/KVM, libvirt. Apartado: [Instalación de QEMU/KVM + libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad02/clase2.md).
2. Siguiendo lo indicando en el apartado [Conexión local privilegiada a libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad02/clase3.md), comprueba que por defecto estamos usando **una conexión privilegiada a libvirt**, y comprueba la red y el almacenamiento disponible. Estudia las características de la red *default* que tenemos a nuestra disposición.
3. Aunque una máquina máquina virtual se puede crear desde su definición XML como nos explican en el apartado [Definición de un dominio con virsh](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase1.md), vamos a seguir el apartado [Creación de máquinas virtuales con virt-install](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase2.md) para crear una máquina virtual con el sistema operativo Linux.
    * Si no tienes un fichero ISO para la instalación puedes probar [Creación de máquinas virtuales por red](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad07/clase1.md).
    * Una vez instalada la máquina comprueba las [Características de las máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase3.md).
    * Estudia las distintas operaciones para la [Gestión de máquinas virtuales con virsh](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase4.md).
    * Muestra la definición XML de la máquina virtual siguiendo el apartado [Definición XML de una máquina virtual](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase5.md) y estudia como puedes realizar la [Modificación de la definición de una máquina virtual](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase6.md).
    * Accede a la máquina virtual usando el protocolo SSH siguiendo el apartado [Acceso a las máquinas virtuales desde el exterior](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase7.md). Accede usando a la máquina virtual usando la consola, siguiendo el apartado [Acceso a la máquina virtual usando la consola serie](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad03/clase7.md).