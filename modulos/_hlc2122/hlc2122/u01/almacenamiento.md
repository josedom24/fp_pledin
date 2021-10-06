---
title: "Almacenamiento en libvirt"
---

## Volúmenes e imágenes

Hay que diferenciar entre volumen y fichero de imagen. 

* Un **volumen** es un medio de almacenamiento que podemos crear en un **pool de almacenmaiento** en kvm.
* Si el pool de almacenamiento es de tipo *dir* entonce el volumen será un **fichero de imagen**. Sin embargo, si el pool es de tipo LVM, el volumen sera un volumen lógico.

Por ejemplo, podemos crear un fichero de imagen con la instrucción:

    $ qemu-img create -f qcow2 /var/lib/libvirt/images/disk.qcow2 10G

Y sin embargo no se ha creado un volumen asociado:

    $ virsh -c qemu:///system vol-list default
    ...

## Formatos de imágenes: raw, qcow2, vmdk. Redimensiones. Transformaciones de formato

Vamos a trabajar con ficheros de imágenes. Tenemos varios tipos:

* **raw**: el formato raw es una imagen binaria sencilla de la imagen del disco. Se ocupa todo el espacio que hayamos indicado al crearla. El acceso es más eficiente.
* **qcow2**: formato QEMU copy-on-write. Al crearse sólo se ocupa el espacio que se está ocupando con los datos, el fichero irá creciendo cuando escribamos en el él. Acepta instantaneas o snapshots. Es menos eficiente en cuanto al acceso.
* **vdi**, **vmdk**,...: formatos de otros sistemas de virtualización.

#### Redimensiones

Podemos redimensionar el volumen que está utilizando una máquina, para ello:

* Apagamos la máquina virtual.
* Determinamos el volumen que está usando la máquina, por ejemplo:

        $ virsh -c qemu:///system domblklist debiantesting
         Destino   Fuente
        -------------------------------------------
        vda       /var/lib/libvirt/images/debiantest.qcow2

* Obtenemos información sobre el fichero de imagen:

        $ qemu-img info  /var/lib/libvirt/images/debiantest.qcow2
        image: /var/lib/libvirt/images/debiantest.qcow2
        file format: qcow2
        virtual size: 10 GiB (10737418240 bytes)
        disk size: 2.31 GiB
        ...

* Redimensionamos el volumen, por ejemplo:

        $ qemu-img resize /var/lib/libvirt/images/debiantest.qcow2 +5G
    
    El comando anterior redimensiona un fichero de imagen, si lo queremos hacer a nivel de volumen, podemos usar el comando :`virsh vol-resize`. Comprobamos el nuevo tamaño.

        $ qemu-img info  /var/lib/libvirt/images/debiantest.qcow2
        image: /var/lib/libvirt/images/debiantest.qcow2
        file format: qcow2
        virtual size: 15 GiB (10737418240 bytes)
        disk size: 2.31 GiB

* Iniciamos la máquina y redimensionamos el sistema de archivo: Hemos redimensionado la imagen, pero no el sistema de archivo. Según el forma del sistema de archivo tendremos que usar diferentes métodos para redimensionarlo: [How To resize an ext2/3/4 and XFS root partition without LVM](https://computingforgeeks.com/resize-ext-and-xfs-root-partition-without-lvm/).

### Transformación de formato

Podemos modificar el formato de cualquier fichero de imágen, con el comando `qemu-img convert`, por ejemplo:

        $ qemu-img convert  /var/lib/libvirt/images/debiantest.qcow2  /var/lib/libvirt/images/debiantest.raw

## Definición de almacenamiento en una máquina virtual

1. A partir de su definición de XML, y el comando `virsh vol-create`.
2. Indicando una serie de parámetros, usando el comando `virsh create-vol-as`, por ejemplo:

        $ virsh -c qemu:///system vol-create-as default pr.qcow2 --format qcow2 --capacity 2GiB

    A este volumen vacio se le puede copiar el contenido de otro volumen con el comando `virsh vol-upload`.

3. A partir de un fichero de imagen creado con `qemu-img create`: Si tenemos un fichero que hemos creado en el directorio del pool, entonces tendremos que refrescar el pool para que se cree el volumen correspondiente, para ello: 

        $ virsh -c qemu:///system pool-refresh default

4. Al utilizar `virt-install` para crear una imagen, indicamos con el parámetro `--disk` los discos que va a tener la manga, tenemos varias opciones:

    * `--disk size=10`: Se crea un volumen de 10Gb.
    * `--disk vol=default/debiantest.qcow2`: Se indica que se use un volumen que ya existe.
    * ...

5. Para definir el disco de una máquina usando el XML, usaremos la etiqueta `disk`, por ejemplo:

    ```xml
    ...
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/var/lib/libvirt/images/debiantest.qcow'/>
      <target dev="vda" bus="virtio"/>
    </disk>
    ```
6. Añadir nuevos discos a una máquina virtual ejecutandose: Podemos editar el XML de la máquina y meter nuevos discos usando la etiqueta `disk`, o usando la siguiente instrucción:

        $ virsh -c qemu:///system attach-disk maquina --source var/lib/libvirt/images/disk.qcow2 --target vdb --persistent


## Aprovisionamiento ligero

Elm aprovisionamiento ligero nos permite definir el disco que vamos a usar en una máquina a partir de una imagen base (backing-vol) de solo lectura, y otro volumen que se usará cuando la máquina vaya haciendo cambios en el disco. Este tipo de almacenamiento nos permite iniciar muchas máquinas desde el mismo disco y que se ocupe muy poco espacio de disco.

Para crear el aprovisionamiento ligero usamos la siguiente instrucción:

        $ virsh -c qemu:///system vol-create-as default new_disk.qcow2 10G --format=qcow2 --backing-vol /var/lib/libvirt/images/debiantest.qcow2 
    
    Y podemos ver sus características:

        $ qemu-img info new_disk.qcow2 
        image: new_disk.qcow2
        file format: qcow2
        virtual size: 10 GiB (10737418240 bytes)
        disk size: 196 KiB
        cluster_size: 65536
        backing file: /home/jose/vm/debiantest.qcow2
        ...


## Instantaneas (Snapshots)

* [How to create snapshot in Linux KVM VM/Domain](https://www.cyberciti.biz/faq/how-to-create-create-snapshot-in-linux-kvm-vmdomain/)
* [How to Create KVM Virtual Machine Snapshot with virsh command](https://www.linuxtechi.com/create-revert-delete-kvm-virtual-machine-snapshot-virsh-command/)