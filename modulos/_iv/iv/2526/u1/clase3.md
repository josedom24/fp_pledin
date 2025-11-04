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

{% capture notice-text %}
## Entrega

1. Del ejercicio 1: La instrucción `virt-clone` que has usado para clonar la máquina. ¿Qué cambios has hecho en la nueva máquina para que no sea igual a la original?
2. Del ejercicio 2: Explica los pasos que has realizado y las instrucciones que has ejecutado para crear la plantilla. Pon una captura donde se vea que nos da un error al intentar iniciarla. 
3. Del ejercicio 3: Captura de pantalla donde se vea la dirección IP que ha tomado. Otra captura donde se vea el acceso por SSH.
4. Del ejercicio 4: Explica los pasos que has realizado y las instrucciones que has ejecutado para realizar la clonación enlazada. El comando y la salida que nos da información del volumen de la nueva máquina donde se demuestra que se ha creado desde una imagen base (**Backing Store**). La instrucción y la salida del comando que nos permite ver lo que ocupa el disco creado. ¿Por qué ocupa tan poco espacio?
5. Del ejercicio 5: Capturas de pantalla para demostrar el ejercicio. El comando y la salida para mostrar las listas de snapshots desde la línea de comandos.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>