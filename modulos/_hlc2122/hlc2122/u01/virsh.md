---
title: virsh
---
  
Virsh es una shell completa para gestionar la API de libvirt. Se puede
usar de forma interactiva o no, pasándole o no directamente las
órdenes correspondientes.

## Conexión al hipervisor

En el caso de utilizar qemu-kvm localmente, podemos establecer una
conexión no privilegiada con cada usuario del sistema
(`qemu:///session`) o una privilegiada (`qemu:///system`)

```
virsh -c qemu:///system
Welcome to virsh, the virtualization interactive terminal.

Type:  'help' for help with commands
       'quit' to quit

virsh # 
```

## Tipos de órdenes

Al pasar como parámetro `help` aparecen las órdenes agrupadas por
tipo:

```
virsh help
Grouped commands:

 Domain Management (help keyword 'domain'):
    attach-device                  attach device from an XML file
    attach-disk                    attach disk device
    attach-interface               attach network interface
...
```

* *Domain Management* Gestión y modificación de los dominios (MVs)
* *Domain Monitoring* Parámetros de ejecución de los dominios
* *Host and Hypervisor* Características del hipervisor
* *Interface* Interfaces de red
* *Network filter* Reglas de iptables
* *Networking*
* *Node device* Dispositivos físicos gestionados por los dominios
* *Secret*
* *Snapshot*
* *Storage Pool* Gestión de los recursos de almacenamiento
* *Storage Volume* Volúmenes

### Órdenes disponibles para cada tipo

Libvirt utiliza el término "dominio" para referirse a la máquina
virtual que se ejecuta sobre el hipervisor, término adoptado de los
sistemas de paravirtualización como Xen. Para obtener las órdenes
disponibles para gestionar dominios:

```
virsh help domain
 Domain Management (help keyword 'domain'):
    attach-device                  attach device from an XML file
    attach-disk                    attach disk device
    attach-interface               attach network interface
...
```


## Configuración inicial

Para la creación inicial de una máquina virtual necesitamos definir
una red a la que pueda conectarse y un espacio en el que ubicar el
dispositivo de almacenamiento principal.

Libvirt denomina "pool" de forma genérica a un medio de almacenamiento
disponible, independientemente de su naturaleza, así podemos tener
como pool de almacenamiento un directorio, un grupo de volúmenes de
LVM, un disco duro, un volumen gluster, etc.


### Red NAT por defecto

Si no existiese previamente, podemos crear una red de tipo NAT a la
que denominaremos `default`, creando el fichero `net-default.xml` con
el siguiente contenido:

```
<network>
  <name>default</name>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='virbr0' stp='on' delay='0'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
</network>
```

Que definimos y activamos con:

```
virsh -c qemu:///system net-define net-default.xml
virsh -c qemu:///system net-start default
```

### Pool de almacenamiento por defecto

Si no existe, creamos un pool por defecto en `/var/lib/libvirt/images`
con el fichero `default-pool.xml`:

```
<pool type='dir'>
  <name>default</name>
  <target>
    <path>/var/lib/libvirt/images</path>
  </target>
</pool>
```

Y lo añadimos con:

```
virsh -c qemu:///system pool-define default-pool.xml
virsh -c qemu:///system pool-start default
```

### Creación de un volumen qcow2 en el pool por defecto

Para crear un fichero de hasta 10 GiB de capacidad en un fichero en
formato qcow2, definimos el fichero `vol1.xml`:

```
<volume type='file'>
  <name>vol1.img</name>
  <key>/var/lib/libvirt/images/vol1.img</key>
  <source>
  </source>
  <allocation>0</allocation>
  <capacity unit="G">10</capacity>
  <target>
    <path>/var/lib/libvirt/images/vol1.img</path>
    <format type='qcow2'/>
  </target>
</volume>
```

Y lo agregamos al pool por defecto:

```
virsh -c qemu:///system vol-create vol1.xml
```

### Creación de un volumen con el contenido de un fichero de imagen

Supongamos que tenemos un fichero qcow2 que contiene la imagen de un
sistema y que queremos agregarlo como un volumen a un pool. En primer
lugar tendremos que ver el espacio ocupado por la imagen original:

```
qemu-img info debian-10-openstack-amd64.qcow2 
image: debian-10-openstack-amd64.qcow2
file format: qcow2
virtual size: 2.0G (2147483648 bytes)
disk size: 517M
cluster_size: 65536
Format specific information:
    compat: 0.10
    refcount bits: 16
```

En este caso, tenemos una imagen de un sistema debian buster en un
fichero qcow2 de 2G de tamaño virtual, por lo que creamos inicialmente
un volumen de ese tamaño (podemos usar `vol-create-as` para definir
los parámetros sin tener que escribir anteriormente el fichero XML:

```
virsh -c qemu:///system vol-create-as --format qcow2 --name buster \
--capacity 2GiB --pool default
```

Y copiamos el contenido del fichero original en el volumen:

```
virsh -c qemu:///system vol-upload buster \
debian-10-openstack-amd64.qcow2 --pool default
```

A continuación usaremos ese volumen para crear un dominio.

## Creación de un dominio (máquina virtual)

Vamos a crear un dominio que utilice como unidad de almacenamiento
principal el volumen creado anteriormente y que se conecte a la red
'default', también añadiremos un dispositivo gráfico tipo VNC para
conectarnos a una consola de forma remota utilizando este protocolo.

Creamos el fichero `dominio1.xml` con el siguiente contenido:

```
<domain type="kvm">
  <name>dominio1</name>
  <memory unit="G">1</memory>
  <vcpu>1</vcpu>
  <os>
    <type arch="x86_64">hvm</type>
  </os>
  <devices>
    <emulator>/usr/bin/kvm</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/var/lib/libvirt/images/buster'/>
      <target dev='vda'/>
    </disk>
    <interface type="network">
      <source network="default"/>
      <mac address="52:54:00:86:c6:a9"/>
    </interface>
    <graphics type='vnc' port='-1' autoport='yes' listen='0.0.0.0' />
  </devices>
</domain>
```

Lo definimos en el hipervisor:

```
virsh -c qemu:///system define dominio1.xml
```

Y arrancamos la máquina virtual:

```
virsh -c qemu:///system start dominio1
```

Podremos acceder a través de ssh si conocemos la contraseña o a una
consola mediante VNC.
