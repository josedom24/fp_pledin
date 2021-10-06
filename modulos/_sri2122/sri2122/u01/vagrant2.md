---
title: Introducción a Vagrant. Redes.
---

## Red de mantenimiento

Como hemos visto en los ejemplos anteriores, por defecto, las máquinas creadas por vagrant se conectan a una red de tipo NAT llamada `vagrant-libvirt` cuya definición es la siguiente:

```bash
virsh -c qemu:///system net-dumpxml vagrant-libvirt
```

```xml
<network connections='1' ipv6='yes'>
  <name>vagrant-libvirt</name>
  <uuid>aa24398a-7495-45ef-bf88-5c2a49836c5c</uuid>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='virbr1' stp='on' delay='0'/>
  <mac address='52:54:00:fc:db:97'/>
  <ip address='192.168.121.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.121.2' end='192.168.121.254'/>
    </dhcp>
  </ip>
</network>
```
Esta conexión es utilizada por vagrant para acceder a la máquina cuando ejecutamos `vagrant ssh` y al ser tipo NAT con dhcp posibilita que nuestra máquina tenga acceso a internet. Como vemos la ruta por defecto de la máquina es la siguiente:

```bash
$ ip r
default via 192.168.121.1 dev eth0 
192.168.121.0/24 dev eth0 proto kernel scope link src 192.168.121.2 
```

Podemos cambiar la red de mantenimiento si nos interesa, añadiendo al `Vagrantfile` el nombre de la red a la que se debe conectar y su direccionamiento:

```ruby
  ...
  config.vm.provider :libvirt do |libvirt|
    libvirt.management_network_name = "default"
    libvirt.management_network_address = '192.168.122.0/24'
  end
  ...
```

**Tenemos que tener en cuenta que todas las máquinas van a tener una interfaz de red de tipo NAT, que le dan direccionamiento por dhcp y le posibilitan acceder al exterior. En determinados escenarios deberemos no tener en cuenta en esta interfaz, por ejemplo cambiando la ruta por defecto para la máquina no salga por esta interfaz.**

## Redes privadas de tipo NAT con dhcp

Podemos hacer que una máquina se conecte a otra red privada de tipo NAT, configurando lo siguiente en el `Vagrantfile`:

```ruby
...
config.vm.network :private_network,
    :type => "dhcp",
    :libvirt__network_address => '192.168.200.0'
...
```

Al crear el escenario se crea una red llamada `vagrant-private-dhcp` con la siguiente definición:

```xml
<network connections='1' ipv6='yes'>
  <name>vagrant-private-dhcp</name>
  <uuid>989bc924-adba-42f5-9b29-3a0fe54b157c</uuid>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='virbr2' stp='on' delay='0'/>
  <mac address='52:54:00:a4:b9:99'/>
  <ip address='192.168.200.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.200.2' end='192.168.200.254'/>
    </dhcp>
  </ip>
</network>
```

Podemos configurar el rango del dhcp, con los parámetros `:libvirt__dhcp_start` y `:libvirt__dhcp_stop`, y la ip que toma el host con `:libvirt__host_ip`.

Podemos comprobar que la máquina creada ha configurado otra interfaz por dhcp en el fichero `/etc/network/interfaces`:

```
auto eth1
iface eth1 inet dhcp
```

## Redes privadas de tipo NAT con ip estática

Podemos configurar una red de tipo NAT, pero indicando una ip estática en la máquina virtual creada, para ello añadimos al `Vagrantfile`:

```ruby
  config.vm.network :private_network,
    :libvirt__dhcp_enabled => false,
    :ip => "10.20.30.40"
```
Al crear el escenario se crea una red cuyo nombre es igual al directorio donde está el `Vagrantfile` seguido de un número, en mi caso `ej10` con la siguiente definición:

```xml
<network connections='1' ipv6='yes'>
  <name>ej10</name>
  <uuid>b1b9622b-1473-48f9-a3bb-c2f7b8fdc0e1</uuid>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='virbr2' stp='on' delay='0'/>
  <mac address='52:54:00:e7:36:46'/>
  <ip address='10.20.30.1' netmask='255.255.255.0'>
  </ip>
</network>
```

Y podemos comprobar que la segunda interfaz se ha configurado de forma estática en la máquina creada, mirando el fichero `/etc/network/interfaces`:

```bash
auto eth1
iface eth1 inet static
      address 10.20.30.40
      netmask 255.255.255.0
```

**Nota: Si no indicamos el parámetro `:libvirt__dhcp_enabled => false` la red tendrá un servidor dhcp, pero el escenario seguirá funcionando de forma adecuada, ya que la configuración de la interfaz se hace de forma estática.**

## Red aislada (isolated)

Para crear una red aislada entre dos máquinas, configuramos el siguiente `Vagrantfile`:

```ruby
Vagrant.configure("2") do |config|

  config.vm.define :nodo1 do |nodo1|
    nodo1.vm.box = "debian/bullseye64"
    nodo1.vm.hostname = "nodo1"
    nodo1.vm.synced_folder ".", "/vagrant", disabled: true
    nodo1.vm.network :private_network,
      :libvirt__network_name => "red1",
      :libvirt__dhcp_enabled => false,
      :ip => "10.0.0.10",
      :libvirt__forward_mode => "none"
  end
  config.vm.define :nodo2 do |nodo2|
    nodo2.vm.box = "generic/ubuntu2010"
    nodo2.vm.hostname = "nodo2"
    nodo2.vm.synced_folder ".", "/vagrant", disabled: true
    nodo2.vm.network :private_network,
      :libvirt__network_name => "red1",
      :libvirt__dhcp_enabled => false,
      :ip => "10.0.0.11",
      :libvirt__forward_mode => "none"
  end
end
```

Como son redes aisladas es importante ponerle un nombre (`:libvirt__network_name`) para asegurarnos que las dos máquinas están conectas a la misma red. La red `red1` se crea con la siguiente definición:

```xml
<network connections='2' ipv6='yes'>
  <name>red1</name>
  <uuid>e102c6f4-5837-41ea-9acd-a62b61563e79</uuid>
  <bridge name='virbr2' stp='on' delay='0'/>
  <mac address='52:54:00:c8:da:72'/>
  <ip address='10.0.0.1' netmask='255.255.255.0'>
  </ip>
</network>
```

Si nos damos cuenta a esta red aislada estará conectada los dos nodos y el host, para que el host no se conecte podemos indicar `veryisolated` en el parámetro `:libvirt__forward_mode` y se crearía la siguiente red:

```xml
<network connections='2' ipv6='yes'>
  <name>red1</name>
  <uuid>18911d36-10fa-4bb4-9605-d7fb7c397378</uuid>
  <bridge name='virbr5' stp='on' delay='0'/>
  <mac address='52:54:00:2c:94:d7'/>
</network>
```

## Redes públicas

Para crear una red pública desde vagrant necesitamos un bridge externo (por ejemplo que se llame `br0`) que este configurado en nuestro host. En el `Vagrantfile` configuraremos una red pública de la siguiente manera:

```ruby
...
  config.vm.network :public_network,
    :dev => "br0",
    :mode => "bridge",
    :type => "bridge"
```

En este caso podemos comprobar que la máquina tiene una segunda interfaz que está conectada a la red del host:

```bash
$ ip a
...
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:39:75:df brd ff:ff:ff:ff:ff:ff
    altname enp0s6
    altname ens6
    inet 192.168.100.250/24 brd 192.168.100.255 scope global dynamic eth1
...
```

Desde el host podemos comprobar las interfaces conectadas al bridge externo:

```bash
$ brctl show br0
bridge name	bridge id		STP enabled	interfaces
br0		8000.32a20d0ddc35	no		enp5s0
        						vnet53
```
La interfaz `vnet53` corresponde a la de la máquina virtual.


