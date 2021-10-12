---
title: "Ejercicio 3: Trabajo con almacenamiento en libvirt"
---
Realiza las siguientes tareas con `virsh` conectándote a `qemu:///system`:

1. Crea un nuevo pool de almacenamiento de tipo lvm, y crea un volumen de 3Gi dentro que sea una volumen lógico. Con `virt-install` instala una máquina que se llame *original_tunombre* cuyo disco sea el volumen creado.
2. Convierte el volumen anterior en un fichero de imagen qcow2 que estará en el pool `default`. Puedes usar la instrucción que aparece en esta [página](http://nocoast-tech.blogspot.com/2010/05/converting-kvm-guests-from-lvm-to-qcow2.html).
3. Crea dos máquinas virtuales (*nodo1_tunombre* y *nodo2_tunombre*) que utilicen la imagen construida en el punto anterior como imagen base (aprovisonamiento ligero). Una vez creada accede a las máquinas para cambiarle el nombre.
4. Transforma la imagen de la máquina *nodo1_tunombre* a formato raw. Realiza las modificaciones necesarias en la definición de la máquina virtual (`virsh edit <maquina>`), para que pueda seguir funcionando con el nuevo formato de imagen.
5. Redimensiona la imagen de la máquina *nodo2_tunombre*, añadiendo 1 GiB y utiliza la herramienta `guestfish` para redimensionar también el sistema de ficheros definido dentro de la imagen (si no usas esta herramientas puedes redimensionar el sistema de archivo desde la máquina con las herramientas específicas).
6. Crea un snapshot de la máquina *nodo1_tunombre*, modifica algún fichero de la máquina y alguna caracteristica de la misma (por ejemplo cantidad e memoria). Recupera el estado de la máquina desde el snapshot y comprueba que lo cambios se han perdido (tanto en el disco como en la configuración).
7. Crea un nuevo pool de tipo "dir" llamado `discos_externos`, crea un volumen de 1Gb dentro de este pool, y añádelo "en caliente" a la máquina *nodo2_tunombre*. Formatea el disco y móntalo.

{% capture notice-text %}
## Entrega...

1. Del punto 1, un pantallazo de la definición del dominio *original_nombre*, donde se vea el dispositivo de disco que está utilizando.
2. Del punto 2, un pantallazo de la definición del dominio *nodo1_tunombre*, donde se vea el dispositivo de disco que está utilizando (que se vea claramente que has usado aprovisonamiento ligero).
3. Del punto 3, un pantallazo donde se compruebe que *nodo2_tunombre* tiene acceso a internet y que le has cambiado el nombre.
4. Del punto 4, un pantallazo de la definición del dominio *nodo1_tunombre*, donde se vea el dispositivo de disco que está utilizando. Y una captura de pantalla donde se vea que está funcionando.
5. Del punto 5, un pantallazo de la ejecución de *nodo2_tunombre*, donde se vea el comando lsblk, y df -h. Para comprobar que se ha redimensionado el dispositivo de bloque y el sistema de fichero.
6. Del punto 6, muestra información del volumen donde se vea que se ha creado un snapshot. Explica los cambios que has hecho en la máquina y demuestra que al recuperar el estado del snapshot se han recuperado los cambios.
7. Del punto 7, demuestra que tenemos un nuevo disco y ha sido montado.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>