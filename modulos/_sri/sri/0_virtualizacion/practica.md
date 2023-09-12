---
title: "Práctica: Virtualización en Linux"
---

## Descripción

Vamos a crear una máquina virtual por medio de un script.

### Creación de la imagen base

Vamos a crear una imagen base que utilizaremos para la creación de la máquina que utilizaremos en la práctica. Para ello:

1. Crea con `virt-install` una imagen de Debian Bullseye con formato qcow2 y un tamaño máximo de 3GiB. Esta imagen se denominará `bullseye-base.qcow2`. El sistema de ficheros del sistema instalado en esta imagen será XFS. La imagen estará configurada para poder usar hasta dos interfaces de red por dhcp. El usuario `debian` con contraseña `debian` puede utilizar `sudo` sin contraseña.
2. Crea un par de claves ssh en formato ecdsa y sin frase de paso y agrega la clave pública al usuario `debian`.
3. Utiliza la herramienta `virt-sparsify` para reducir al máximo el tamaño de la imagen.
4. Sube la imagen base a alguna ubicación pública desde la que se pueda descargar.

Cuando hayas finalizado puedes borrar la máquina creada. Lo que nos interesa es la imagen `bullseye-base.qcow2` que has creado.

### Script de creación de MV

Escribe un shell script que ejecutado por un usuario con acceso a `qemu:///system` realice los siguientes pasos:


1. Crea una imagen nueva, que utilice `bullseye-base.qcow2` como imagen base y tenga 5 GiB de tamaño máximo. Esta imagen se denominará `maquina1.qcow2`.
2. Crea una red interna de nombre **intra** con salida al exterior mediante NAT que utilice el direccionamiento `10.10.20.0/24`.
3. Crea una máquina virtual (**maquina1**) conectada a la red **intra**, con 1 GiB de RAM, que utilice como disco raíz `maquina1.qcow2` y que se inicie automáticamente. Arranca la máquina. Modifica el fichero `/etc/hostname` con **maquina1**.
4. Crea un volumen adicional de 1 GiB de tamaño en formato RAW ubicado en el pool por defecto
5. Una vez iniciada la MV **maquina1**, conecta el volumen a la máquina, crea un sistema de ficheros XFS en el volumen y móntalo en el directorio `/var/www/html`. Ten cuidado con los propietarios y grupos que pongas, para que funcione adecuadamente el siguiente punto.
6. Instala en **maquina1** el servidor web apache2. Copia un fichero `index.html` a la máquina virtual. 
8. Muestra por pantalla la dirección IP de **máquina1**. Pausa el script y comprueba que puedes acceder a la página web.
9. Instala LXC y crea un linux container llamado `container1`.
10. Añade una nueva interfaz a la máquina virtual para conectarla a la red pública (al punte `br0`).
11. Muestra la nueva IP que ha recibido.
12. Apaga **maquina1** y auméntale la RAM a 2 GiB y vuelve a iniciar la máquina.
13. Crea un snapshot de la máquina virtual.


Una
Se valorara la limpieza del código, los comentarios, la utilización adecuada de variables, portabilidad (es decir, que no dependa de directorios concretos y se pueda ejecutar en cualquier equipo), si se hacen comprobaciones antes de realizar una acción,...

Alternativamente se puede entregar la tarea sin hacer el script, describiendo paso a paso la secuencia de comandos a ejecutar. En este caso la nota de la tarea será inferior.


{% capture notice-text %}
## Entrega

1. Entrega la URL del repositorio GitHub donde has alojado el proyecto.
2. Indica los pasos que has realizado para la creación de la imagen base.
3. Entrega la clave privada que has utilizado y un enlace para descargarme la imagen base.
4. Ejecuta el script y cuando se pause. Entrega pantallazo donde se compruebe que se puede acceder al servidor web en la **maquina1**. 
5. Al finalizar el script: pantallazo donde se compruebe que se puede acceder al servidor web con la IP pública.
6. Al finalizar el script: Pantalalzos para comprobar:
	* Que la máquina tiene montado un disco en el directorio `/var/www/html`.
	* Que la máquina tiene 2G de RAM.
	* Que accediendo a la máquina puedes acceder al contenedor.
	* Que se ha ha creado un snapshot.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


