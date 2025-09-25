---
title: "Clase 3: Clonación e instantáneas de maquinas virtuales"
---

## ¿Qué vas a aprender en esta clase?

* A clonar máquinas virtuales.
* A crear plantillas para crear a partir de ellas clonaciones completas o enlazadas.
* Trabajar con instantáneas de máquinas virtuales.

## Recursos

* Curso completo: [Profundización a la virtualización con KVM/libvirt](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2)
* En concreto los apartados:
  * Clonación e instantáneas de máquinas virtuales
* [Presentación: Resumen virtualización en Linux](https://fp.josedomingo.org/sri/pdf/resumen_virtualizacion.pdf)

## Ejercicio

1. Siguiendo el apartado [Clonación de máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad05/clase1.md), utiliza la herramienta `virt-clone` para clonar tu máquina linux. Llámala **máquina-clonada**. Realiza los cambios necesarios en la nueva máquina para que no se llame igual que la original.
2. Siguiendo el apartado [Plantillas de máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad05/clase2.md), crea una plantilla a partir de la máquina que acabamos de crear en el punto anterior. Llámala **plantilla-linux**. Recuerda que no debería poder inicializar la máquina que hemos creado la plantilla al poner el disco en sólo lectura.
3. Siguiendo el apartado [Clonación a partir de plantillas](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad05/clase3.md), realiza una clonación completa usando `virtsh` de la plantilla que has creado. La nueva máquina la llamará **clone-full**. Accede a esta nueva máquina por ssh.
4. Siguiendo el apartado [Clonación a partir de plantillas](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad05/clase3.md), realiza una clonación enlazada. Para ello, crea un disco que tenga como imagen base (**backing store**) la imagen de la plantilla (lo puedes hacer con cualquier herramienta). Una vez creado el nuevo disco, realiza la clonación enlazada, la nueva máquina se llamará **clone-link** (lo puedes hacer con cualquier herramienta). Muestra el comando y la salida que nos da información del volumen de la nueva máquina donde se demuestra que se ha creado desde una imagen base (**Backing Store**). La instrucción y la salida del comando que nos permite ver lo que ocupa el disco creado. ¿Por qué ocupa tan poco espacio?
5. Siguiendo el apartado [Instantáneas de máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso2/contenidos/unidad05/clase4.md), crea un directorio en cualquiera de las máquinas y realiza una instantánea de la máquina virtual. Borra el directorio y vuelve al estado anterior de la máquina recuperando la instantánea que hemos creado (lo puedes hacer con cualquier herramienta).
    