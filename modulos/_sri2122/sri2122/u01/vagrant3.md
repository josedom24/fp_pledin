---
title: Introducción a Vagrant. Almacenamiento.
---

## Crear una máquina y añadirle un nuevo disco

Para ello, en el `Vagrantfile`, podemos indicar los discos extras que va a tener la máquina, para ello indicamos tantos bloques como discos queramos conectar:

```ruby
  ...
  config.vm.provider :libvirt do |libvirt|
    libvirt.storage :file, :size => '20G'
  end
  ...
```

Ademas del tamaño (`size`) podemos indicar otros [parámetros](https://github.com/vagrant-libvirt/vagrant-libvirt#additional-disks).

Podemos observar que se ha creado un nuevo volumen:

```bash
$ virsh -c qemu:///system vol-list default
 Nombre                                    Ruta
----------------------------------------------------------------------------------------------------------
 ...
 ej1_default-vdb.qcow2                     /var/lib/libvirt/images/ej1_default-vdb.qcow2
...
```

Cuando eliminamos el escenario, el volumen también se borrará.

## Crear una máquina y añadirle un disco ya existente

Si tenemos un volumen creado también lo podemos usar para crear la nueva máquina, en esta ocasión la definición en el fichero `Vagrantfile` sería:

```ruby
  ...
  config.vm.provider :libvirt do |libvirt|
    libvirt.storage :file, 
      :path => 'new_disk.qcow2', 
      :allow_existing => true,  
      :type => 'qcow2'
  end
  
  ...
```

En este caso, no se crea un nuevo volumen, se utiliza uno que ya tenemos creado `new_disk.qcow2`, por lo que al eliminar el escenario, ese volumen no se borrará.
