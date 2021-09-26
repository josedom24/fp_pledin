---
title: Introducción a Vagrant
---

Vagrant es una aplicación libre desarrollada en ruby que nos permite crear y personalizar entornos de desarrollo livianos, reproducibles y portables. Vagrant nos permite automatizar la creación y gestión de máquinas virtuales. Las máquinas virtuales creadas por vagrant se pueden ejecutar con distintos gestores de máquinas virtuales (oficialmente VirtualBox, VMWare e Hyper-V).

El objetivo principal de vagrant es aproximar los entornos de desarrollo y producción, de esta manera el desarrollador tiene a su disposición una manera  muy sencilla de desplegar una infraestructura similar a la que se va a tener en entornos de producción. A los administradores de sistemas les facilita la creación de infraestructuras de prueba y desarrollo.


## Vagrant y libvirt

Aunque no de manera oficial, podemos crear escenarios en Vagrant usando libvirt + QEMY/kvm. Para ello puede seguir la documentacción del plugin de vagrant [Vagrant Libvirt Provider](https://github.com/vagrant-libvirt/vagrant-libvirt).

### Instalación de vagrant

En una máquina donde tengamos ya instalado libvirt + QEMU/kvm, instalamos vagrant:

```bash
root@maquina:~$ apt install vagrant
```

Y posteriormente activamos el plugin:

```bash
root@maquina:~$ vagrant plugin install vagrant-libvirt
```

## Instalación de un "box" debian/bullseye64

Nos descargamos desde el repositorio oficial el box de Debian bullseye de 64 bits, esto lo hacemos un usuario sin privilegios:

```bash
usuario@maquina:~$ vagrant box add debian/bullseye64
```

**Es importante fijarnos que lo estamos haciendo con usuarios sin privilegios. Cada usuario tendrás sus box propios.**
{: .notice--warning}        

Puedo ver la lista de boxes que tengo instalada en mi usuario ejecutando la siguiente instrucción:
    
```bash
usuario@maquina:~$ vagrant box list
```

## Creación de una máquina virtual

1. Nos creamos un directorio y dentro vamos a crear el fichero `Vagrantfile`, podemos crear uno vacío con la instrucción:
        
    ```bash
    usuario@maquina:~/vagrant$ vagrant init
    ```
        
2. Modificamos el fichero Vagrantfile y los dejamos de la siguiente manera:

    ```ruby
    Vagrant.configure("2") do |config|
      config.vm.box = "debian/bullseye64"
      config.vm.hostname="prueba"
    end
    ```
    
3. Iniciamos la máquina:

    ```bash
    usuario@maquina:~/vagrant$ vagrant up
    ```
        
4. Para acceder a la instancia:
  	
    ```bash
    usuario@maquina:~/vagrant$ vagrant ssh
    ```
    	      
5. Suspender, apagar o destruir:
    	
    ```bash
    usuario@maquina:~/vagrant$ vagrant suspend
    usuario@maquina:~/vagrant$ vagrant halt
    usuario@maquina:~/vagrant$ vagrant destroy
    ```

### Algunas consideraciones

1. Como podemos probar la máquina tiene acceso al exterior. Aunque no hayamos configurado ninguna conexión de red, esta máquina se ha conectado a un red de tipo NAT que ha creado vagrant:

    ```bash
    usuario@maquina:~/vagrant$ virsh -c qemu:///system net-list --all
    Nombre            Estado     Inicio automático   Persistente
    ---------------------------------------------------------------
    ...
    vagrant-libvirt   activo     no                  si
    ```

2. La instrucción `vagrant ssh` accede a la máquina con el usuario `vagrant` y con una clave privada, la clave pública relacionada se ha guardado en el sistema de archivo de la máquina. **¿Dónde se encuentra la clave privada que se utiliza para acceder a esta máquina?**.

3. Se han creado dos volúmenes en el pool `default`:

    ```bash
    usuario@maquina:~/vagrant$ virsh -c qemu:///system vol-list default
    Nombre                                                               Ruta
    ---------------------------------------------------------------------------------------------------
    ...   
    ej1_default.img                                                      /home/jose/vm/ej1_default.img
    debian-VAGRANTSLASH-bullseye64_vagrant_box_image_11.20210829.1.img   /home/jose/vm/debian-VAGRANTSLASH-bullseye64_vagrant_box_image_11.20210829.1.img
  ```

Si comprobamos la definición de la máquina creada veremos lo siguiente:

  ```bash
  usuario@maquina:~/vagrant$ virsh -c qemu:///system dumpxml ej1_default
  ...
  <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/home/jose/vm/ej1_default.img' index='1'/>
      <backingStore type='file' index='2'>
        <format type='qcow2'/>
        <source file='/home/jose/vm/debian-VAGRANTSLASH-bullseye64_vagrant_box_image_11.20210829.1.img'/>
        <backingStore/>
      </backingStore>
      <target dev='vda' bus='virtio'/>
      <alias name='virtio-disk0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </disk>
  ...
  ```

Estamos usando aprovisionamiento ligero ("thin provisioning") que permite utilizar la misma imagen base para varias máquinas virtuales y crear rápidamente nuevas máquinas virtuales sin tener que instalar desde cero. Es decir:

* La primera vez que se crea una máquina con un box determina, se clona este box y se crea una imagen que servira de base para todas las máquinas creada con el mismo box.
* Para cada máquina se se crea n nuevo fichero de imagen, que "comparte" una imagen base (sólo lectura) y que realmente registra sólo las modificaciones que vaya teniendo a medida que va cambiando.
* Con esta técnica se ahorra mucho espacio en disco. Por cada vm no se clona un nuevo volumen.
* Cuando eliminamos la máquina con `vagrant destroy` se elimina la imagen de la máquina, pero no la imagen base.



{% capture notice-text %}
## Realiza las siguientes comprobaciones

1. Usando virsh comprueba las características (RAM y CPU) que tiene la máquina creada.
2. ¿Qué usuario tiene creado por defecto el sistema?¿Cómo se ejecutan instrucciones de superusuario?
3. Comprueba que se ha cambiado el nombre de la máquina (fichero `/etc/hostname`) y la resolución estática del sistema (fichero `/etc/hosts`).
4. Busca el directorio donde se ha guardado la clave privada que se utiliza para acceder a la máquina con `vagrant ssh`. Accede a la máquina usando `ssh`.
5. Comprueba que se ha instalado un servidor NFS y que el directorio donde se encuentre el `Vagrantfile` es accesible desde la máquina desde el directorio `/vagrant`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Práctica 4: Creación de varias máquinas virtuales

En esta ocasión vamos a crear otro directorio y dentro un fichero `Vagrantfile` con el siguiente contenido:

  ```ruby
  Vagrant.configure("2") do |config|

    config.vm.define :nodo1 do |nodo1|
      nodo1.vm.box = "debian/bullseye64"
      nodo1.vm.hostname = "nodo1"
    end
    config.vm.define :nodo2 do |nodo2|
      nodo2.vm.box = "generic/ubuntu2010"
      nodo2.vm.hostname = "nodo2"
    end
  end
  ```

Cuando iniciemos el escenario veremos que hemos creado dos máquinas virtuales: nodo1 y nodo2. Cada una de ella con un sistema operativo. Las dos máquinas estarán conectada a la misma red. Para acceder a las máquinas usaremos el nombre de la máquina: `vagrant ssh nodo1`.

## Modificar las características de la máquina creada

Veamos cómo podemos cambiar la configuración (RAM y CPU) de la máquina creada en un `Vagrantfile`:

  ```ruby
  Vagrant.configure("2") do |config|
    config.vm.box = "debian/bullseye64"
    config.vm.hostname="prueba"
    config.vm.synced_folder ".", "/vagrant", disabled: true
    config.vm.provider :libvirt do |libvirt|
      libvirt.memory = 1024
      libvirt.cpus = 2
    end
  end
  ```

Si no vamos a usar la característica de compartir ficheros entre el host y la máquina virtual podemos deshabilitar el directorio de sincronización (synced_folder).

Si cambiamos las características de las máquinas de un escenario modificando el fichero `Vagrantfile` podríamos intentar la modificación de la máquina ejecutando un `vagrant reload`.

