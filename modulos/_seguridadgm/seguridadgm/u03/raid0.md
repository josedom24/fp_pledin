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

