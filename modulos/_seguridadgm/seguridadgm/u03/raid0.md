---
title: "RAID 0 en Linux"
permalink: /seguridadgm/u03/raid0.html
---

Vamos a configurar en una máquina virtual con Debian un raid0 por software entre dos discos de 1Gb que le hemos conectado. Para ello seguimos los siguientes pasos:

1. Instalación de mdadm

        # apt install mdadm

    Cargamos el módulo del kernel que necesitamos para realizar un raid0:

        # modprobe raid0
    
    Comprobamos que que todavía no hemos creado ningún raid:

        # cat /proc/mdstat 
        Personalities : 
        unused devices: <none>

    Por lo tanto no tenemos ningún dispositivo de bloque del raid:

        # mdadm --detail /dev/md0
        mdadm: cannot open /dev/md0: No such file or directory

        # mdadm --detail /dev/md1
        mdadm: cannot open /dev/md1: No such file or directory

2. Vamos a montar un raid 0 de los dos discos que hemos añadido. Para realizar un raid tenemos que indicar dispositivos de bloques, que puedes ser discos completos o particiones. Nosotros vamos a usar los dos discos completos:

        # lsblk
        ...
        sdb      8:16   0    1G  0 disk 
        sdc      8:32   0    1G  0 disk 

    Y para montar un raid0 con dos discos ejecutamos la siguiente instrucción:

        # mdadm --create /dev/md0 --level=0 --raid-devices=2 /dev/sdb /dev/sdc
        mdadm: Defaulting to version 1.2 metadata
        mdadm: array /dev/md0 started.

    Donde hemos indicado los siguientes parámetros:

    * `/dev/dm0`: Es el nombre que le asignamos al RAID0.
    * `--level=0`:  Especifica el tipo de RAID.
    * `--raid-devices=2`: Indica el número de dispositivos que forman el RAID.
    * `/dev/sdb /dev/sdc`: El nombre de los dispositivos que forman el RAID.

    Ahora podemos comprobar que hemos creado el raid:

        # cat /proc/mdstat 
        Personalities : [raid0] [raid1] [raid6] [raid5] [raid4] 
        md0 : active raid0 sdc[1] sdb[0]
              2095104 blocks super 1.2 512k chunks

        unused devices: <none>

    Y podemos obtener información del raid que hemos creado:

        # mdadm --detail /dev/md0
        /dev/md0:
                Version : 1.2
          Creation Time : Sat Oct 20 12:50:30 2018
             Raid Level : raid0
             Array Size : 2095104 (2046.00 MiB 2145.39 MB)
           Raid Devices : 2
          Total Devices : 2
            Persistence : Superblock is persistent
        
            Update Time : Sat Oct 20 12:50:30 2018
                  State : clean 
         Active Devices : 2
        Working Devices : 2
         Failed Devices : 0
          Spare Devices : 0
        
             Chunk Size : 512K
        
                   Name : nodo1:0  (local to host nodo1)
                   UUID : 3f9c3bd4:04e0c65c:c531ee50:25131986
                 Events : 0
        
            Number   Major   Minor   RaidDevice State
               0       8       16        0      active sync   /dev/sdb
               1       8       32        1      active sync   /dev/sdc

3. Ya tenmos un nuevo dispositivo de bloque (`/dev/md0`) que representa el raid0, ahora lo podemos tratar como otro dispositivo de bloque más, es decir lo puedo particionar, formatear y montarlo en mi sistema de ficheros.

    Podríamos particionar el dispositivo de bloque:

        # fdisk /dev/md0
        Welcome to fdisk (util-linux 2.29.2).
        Changes will remain in memory only, until you decide to write them.
        Be careful before using the write command.

        Device does not contain a recognized partition table.
        Created a new DOS disklabel with disk identifier 0x90678bec.

        Command (m for help): 

    Pero nosotros lo vamos a formatear directamente:

        # mkfs.ext4 /dev/md
        mke2fs 1.43.4 (31-Jan-2017)
        Creating filesystem with 523776 4k blocks and 131072 inodes
        Filesystem UUID: cbe308a1-9109-4029-b564-38a93b8537ee
        Superblock backups stored on blocks: 
        	32768, 98304, 163840, 229376, 294912

        Allocating group tables: done                            
        Writing inode tables: done                            
        Creating journal (8192 blocks): done
        Writing superblocks and filesystem accounting information: done 

    Ahora vamos a montarlo en el directorio `/mnt/raid0`, para ello:

        # mkdir -p /mnt/raid0
        # mount /dev/md0 /mnt/raid0
        # df -f
        ...
        /dev/md0        2.0G  6.0M  1.9G   1% /mnt/raid0

    Si queremos que el dispositivo se monte automáticamente tenmos que añadir al fichero `/etc/fstab` la siguiente línea:

        /dev/md0	/mnt/raid0	ext4	defaults		    0       0

    Y para montarlo ejecutamos:

        # umount -a

    