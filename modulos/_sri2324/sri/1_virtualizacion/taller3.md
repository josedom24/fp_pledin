---
title: "Taller 3: Clonación e instantáneas de máquinas virtuales"
---

## ¿Qué vas a aprender en este taller?

* A clonar máquinas virtuales.
* A crear plantillas para crear a partir de ellas clonaciones completas o enlazadas.
* Trabajar con instantáneas de máquinas virtuales.

## Recursos para realizar este taller

* Capítulo 6 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## ¿Qué tienes que hacer?

1. Utiliza la herramienta `virt-clone` para clonar tu máquina linux. Llámala **máquina-clonada**. Realiza los cambios necesarios en la nueva máquina para que no se llame igual que la original.
    * **Entrega**: La instrucción `virt-clone` que has usado para clonar la máquina. ¿Qué cambios has hecho en la nueva máquina para que no sea igual a la original?
2. Crea una plantilla a partir de la máquina que acabamos de crear en el punto anterior. Llámala **plantilla-linux**. Recuerda que no debería poder inicializar la máquina que hemos creado la plantilla al poner el disco en sólo lectura.
    * **Entrega**: Explica los pasos que has realizado y las instrucciones que has ejecutado para crear la plantilla. Pon una captura donde se vea que nos da un error al intentar iniciarla. 
3. Realiza una clonación completa usando `virt-manager` de la plantilla que has creado. La nueva máquina la llamará **clone-full**. Accede a esta nueva máquina por ssh.
    * **Entrega**: Captura de pantalla donde se vea la dirección IP que ha tomado. Otra captura donde se vea el acceso por SSH.
4. Ahora vamos a realizar una clonación enlazada. Para ello, crea un disco que tenga como imagen base (**backing store**) la imagen de la plantilla (lo puedes hacer con cualquier herramienta). Una vez creado el nuevo disco, realiza la clonación enlazada, la nueva máquina se llamará **clone-link** (lo puedes hacer con cualquier herramienta).
    * **Entrega**: Explica los pasos que has realizado y las instrucciones que has ejecutado para realizar la clonación enlazada. El comando y la salida que nos da información del volumen de la nueva máquina donde se demuestra que se ha creado desde una imagen base (**Backing Store**). La instrucción y la salida del comando que nos permite ver lo que ocupa el disco creado. ¿Por qué ocupa tan poco espacio?
5. Crea un directorio en cualquiera de las máquinas y realiza una instantánea de la máquina virtual. Borra el directorio y vuelve al estado anterior de la máquina recuperando la instantánea que hemos creado (lo puedes hacer con cualquier herramienta).
    * **Entrega**: Capturas de pantalla para demostrar el ejercicio. El comando y la salida para mostrar las listas de snapshots desde la línea de comandos.