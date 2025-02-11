---
title: "Taller 3: Vagrant - Creación de una máquina virtual"
---

## ¿Qué vas a aprender en este taller?

* Realizar la configuración de vagrant con el plugin libvirt.
* Trabajar con boxes.
* Definir en un `Vagranfile` la declaración de una máquina virtual.
* Crear y gestionar el ciclo de vida de una máquina virtual.
* Modificar las características de una máquina virtual.
* Comprobar los recursos que se han creado en QEMU/KVM + libvirt

## Recursos para realizar este taller

Los contenidos necesarios para la realización de este taller y para profundizar en la introducción de Vagrant, lo puedes encontrar en el siguiente artículo:

* [Introducción al uso de vagrant + libvirt + QEMU/KVM](https://www.josedomingo.org/pledin/2021/09/introduccion-vagrant-libvirt/)

## ¿Qué tienes que hacer?

1. Realiza la instalación de vagrant y del plugin `vagrant-libvirt` como se indica en el artículo.
2. **A partir de este punto, vamos a trabajar con un usuario sin privilegios. Cada usuario tendrá sus box propios y sus máquinas virtuales.** 
3. Descarga el box de Debian 12 (**`debian/bookworm64`** de [Vagrant Cloud](https://app.vagrantup.com/boxes/search). Y comprueba los boxes que tienes descargado, como se indica en el artículo.
4. Vamos a crear un fichero `Vagrantfile`, para ello en un directorio ejecuta `vagrant init` y modifica el fichero. tienes un modelo de `Vagrantfile` en el directorio **Taller3** del repositorio [taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant). Veamos la configuración que hemos indicado:

	* `.vm.box`: Indicamos el box que vamos a utilizar.
	* `.vm.hostname`: Indicamos el *hostname* de la máquina.
	* `.vm.synced_folder ".", "/vagrant", disabled: true`: No es obligatorio, pero con esta opción deshabilitamos el directorio de sincronización entre el host y la máquina virtual.

5. Recuerda que las instrucciones `vagrant` hay que ejecutarlas en el directorio donde se encuentra el fichero `Vagrantfile`. Ejecuta la instrucción para iniciar la máquina. Posteriormente ejecuta la instrucción para acceder a la máquina.
6. Ejecuta las instrucciones para parar e iniciar de nuevo la máquina. 
7. Cambia la configuración de memoria RAM y asignación de vCPU. Ejecuta un `reload` y comprueba si se han modificado estas nuevas configuraciones.
8. Comprueba con `virsh` o con `virt-manager` lo siguiente: que se ha creado una máquina virtual, que se ha creado una nueva red llamada `vagrant-libvirt` y que se utiliza aprovisionamiento ligero en el volumen que se usa como almacenamiento.
9. Por último, localiza la clave privada con la que se accede a la máquina en el directorio `.vagrant/machines/default/libvirt/`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. El fichero `Vagrantfile` con el que has trabajado.
2. Una captura de pantalla donde se vea la instrucción de creación de la máquina y el acceso a la máquina virtual.
3. Capturas de pantallas donde se vean la memoria RAM y las CPU asignadas.
4. Captura de pantalla donde se vean la máquina KVM que se ha creado, la red que se ha creado y el volumen que está usando la máquina usa aprovisionamiento ligero.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
