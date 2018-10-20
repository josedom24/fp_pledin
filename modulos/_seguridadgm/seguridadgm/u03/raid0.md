---
title: "RAID 0 en Linux"
permalink: /seguridadgm/u04/raid0.html
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

2. Vamos a montar un raid0