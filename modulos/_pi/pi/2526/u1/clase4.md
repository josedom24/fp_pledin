---
title: "Clase 4: Introducción a vagrant"
---

## ¿Qué vas a aprender en esta clase?

* El concepto de orquestador de escenarios.
* Realizar la configuración de vagrant con el plugin libvirt.
* Trabajar con boxes.
* Definir en un Vagranfile la declaración de una máquina virtual.
* Crear y gestionar el ciclo de vida de una máquina virtual.
* Modificar las características de una máquina virtual.
* Comprobar los recursos que se han creado en QEMU/KVM + libvirt

## Teoría

* Los programas que nos permite programar la creación de escenarios lo llamamos: **Software de Orquestación**.
* **Vagrant** es una aplicación libre desarrollada en ruby que nos permite crear y personalizar entornos de desarrollo livianos, reproducibles y portables. Vagrant nos permite automatizar la creación y gestión de máquinas virtuales. Las máquinas virtuales creadas por vagrant se pueden ejecutar con distintos gestores de máquinas virtuales (oficialmente VirtualBox, VMWare e Hyper-V).
* Los **box** son las imágenes de máquinas virtuales prediseñadas que utiliza Vagrant. Son una plantilla de máquina virtual desde la que se van a crear nuevas máquinas con discos creados por **clonación enlazada**.

## Recursos

Los contenidos necesarios para la realización de esta clase y para profundizar en la introducción de Vagrant, lo puedes encontrar en el siguiente artículo:

* [Presentación: Infraestructura como código. Ansible y Vagrant](https://fp.josedomingo.org/sri/pdf/iac.pdf). 
* [Introducción al uso de vagrant + libvirt + QEMU/KVM](https://www.josedomingo.org/pledin/2021/09/introduccion-vagrant-libvirt/)

## Ejercicio

1. Realiza la instalación de vagrant y del plugin `vagrant-libvirt` como se indica en el artículo.
2. **A partir de este punto, vamos a trabajar con un usuario sin privilegios. Cada usuario tendrá sus box propios y sus máquinas virtuales.** 
3. Descarga el box de Debian 12 (**`debian/bookworm64`** de [Vagrant Cloud](https://app.vagrantup.com/boxes/search). Y comprueba los boxes que tienes descargado, como se indica en el artículo.
4. Todavía no se encuentra en [Vagrant Cloud](https://app.vagrantup.com/boxes/search) la versión 13 de Debian. El profesor ha creado un box llamado `josedom24/debain13`. Descargalo de [Vagrant Cloud](https://app.vagrantup.com/boxes/search).
5. Vamos a crear un fichero `Vagrantfile`, para ello en un directorio ejecuta `vagrant init` y modifica el fichero. Tienes un modelo de `Vagrantfile` en el directorio **Taller3** del repositorio [taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant). Veamos la configuración que hemos indicado:

	* `.vm.box`: Indicamos el box que vamos a utilizar.
	* `.vm.hostname`: Indicamos el *hostname* de la máquina.
	* `.vm.synced_folder ".", "/vagrant", disabled: true`: No es obligatorio, pero con esta opción deshabilitamos el directorio de sincronización entre el host y la máquina virtual.

    **Nota**: Modifica el fichero `Vagrantfile` para indicar el box `josedom24/debain13`.

6. Recuerda que las instrucciones `vagrant` hay que ejecutarlas en el directorio donde se encuentra el fichero `Vagrantfile`. Ejecuta la instrucción para iniciar la máquina. Posteriormente ejecuta la instrucción para acceder a la máquina.
7. Ejecuta las instrucciones para parar e iniciar de nuevo la máquina. 
8. Cambia la configuración de memoria RAM y asignación de vCPU. Ejecuta un `reload` y comprueba si se han modificado estas nuevas configuraciones.
9. Comprueba con `virsh` o con `virt-manager` lo siguiente: que se ha creado una máquina virtual, que se ha creado una nueva red llamada `vagrant-libvirt` y que se utiliza aprovisionamiento ligero en el volumen que se usa como almacenamiento.
10. Por último, localiza la clave privada con la que se accede a la máquina en el directorio `.vagrant/machines/default/libvirt/`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. El fichero `Vagrantfile` con el que has trabajado.
2. Una captura de pantalla donde se vea la instrucción de creación de la máquina y el acceso a la máquina virtual.
3. Capturas de pantallas donde se vean la memoria RAM y las CPU asignadas.
4. Captura de pantalla donde se vean la máquina KVM que se ha creado, la red que se ha creado y el volumen que está usando la máquina usa aprovisionamiento ligero.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
