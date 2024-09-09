---
title: "Práctica: Virtualización en Linux"
---

## Descripción

En esta práctica vamos a realizar la migración de un servicio (en este caso `mariadb`) de una máquina virtual a otra.

### Creación de la imagen base

Vamos a crear una imagen base que utilizaremos para la creación de las máquinas que utilizaremos en la práctica. Para ello:

1. Crea con `virt-install` una imagen de Debian Bullseye con formato qcow2 y un tamaño máximo de 3GiB. Esta imagen se denominará `bullseye-base.qcow2`. El sistema de ficheros del sistema instalado en esta imagen será XFS. La imagen debe estar configurada para poder usar hasta dos interfaces de red por dhcp. El usuario `debian` con contraseña `debian` puede utilizar `sudo` sin contraseña.
2. Crea un par de claves ssh en formato ecdsa y sin frase de paso y agrega la clave pública al usuario `debian`.
3. Utiliza la herramienta `virt-sparsify` para reducir al máximo el tamaño de la imagen.
4. Sube la imagen base a alguna ubicación pública desde la que se pueda descargar.

Cuando hayas finalizado puedes borrar la máquina creada. Lo que no interesa es la imagen `bullseye-base.qcow2` que has creado.

### Script de migración

Escribe un shell script que ejecutado por un usuario con acceso a `qemu:///system` realice los siguientes pasos:


1. Crea una imagen nueva, que utilice `bullseye-base.qcow2` como imagen base y tenga 5 GiB de tamaño máximo. Esta imagen se denominará `maquina1.qcow2`.
2. Crea una red interna de nombre **intra** con salida al exterior mediante NAT que utilice el direccionamiento `10.10.20.0/24`.
3. Crea una máquina virtual (**maquina1**) conectada a la red **intra**, con 1 GiB de RAM, que utilice como disco raíz `maquina1.qcow2` y que se inicie automáticamente. Arranca la máquina.
4. Crea un volumen adicional de 1 GiB de tamaño en formato RAW ubicado en el pool por defecto
5. Una vez iniciada la MV **maquina1**, conecta el volumen a la máquina, crea un sistema de ficheros XFS en el volumen y móntalo en el directorio `/var/lib/mysql`. Ten cuidado con los propietarios y grupos que pongas, para que funcione adecuadamente el siguiente punto.
6. Instala en **maquina1** el sistema de BBDD mariaDB que ubicará sus ficheros con las bases de datos en `/var/lib/mysql` utilizando una conexión ssh. Configura `mariaDB` para que acepte conexiones desde el exterior.
7. (Opcional) Puebla la base de datos con una BBDD de prueba (escribe en la tarea el nombre de usuario y contraseña para acceder a la BBDD).
8. Muestra por pantalla la dirección IP de **máquina1**.
9. Pausa la ejecución para comprobar los pasos hasta este punto.
10. Continúa la ejecución cuando el usuario pulse 'C'.
11. Crea una imagen que utilice `bullseye-base.qcow2` como imagen base y que tenga un tamaño de 4 GiB. Esta imagen se llamará `maquina2.qcow2`.
12. Crea una nueva máquina (**maquina2**) que utilice imagen anterior, con 1 GiB de RAM y que también esté conectada a la red **intra**.
 13. Para el servicio mariaDB, desmonta el dispositivo de bloques, desmonta el volumen de **maquina1**, monta el volumen en **maquina2** en el directorio `/var/lib/mysql` teniendo de nuevo cuidado con los propietarios y permisos del directorio. Todas estas acciones la tienes que hacer utilizando una conexión ssh.
14. Copia de forma adecuada los ficheros de configuración que modificaste de mariaDB de **maquina1** a **maquina2**.
15. Instala mariaDB en **maquina2** a través de ssh.
16. Conecta **maquina2** al bridge exterior de tu equipo, comprueba la IP que tiene el equipo en el bridge exterior y muéstrala por la salida estándar. Desconecta **maquina2** de intra.
17. Comprueba que el servicio mariaDB funciona accediendo a través del bridge exterior.
18. Apaga **maquina1** y aumenta la RAM de **maquina2** a 2 GiB.

Se valorara la limpieza del código, los comentarios, la utilización adecuada de variables, portabilidad (es decir, que no dependa de directorios concretos y se pueda ejecutar en cualquier equipo), si se hacen comprobaciones antes de realizar una acción,...

Alternativamente se puede entregar la tarea sin hacer el script, describiendo paso a paso la secuencia de comandos a ejecutar. En este caso la nota de la tarea será inferior.


{% capture notice-text %}
## Entrega

1. Entrega la URL del repositorio GitHub donde has alojado el proyecto.
2. Indica los pasos que has realizado para la creación de la imagen base.
3. Entrega la clave privada que has utilizado y un enlace para descargarme la imagen base.
4. Ejecuta el script y cuando se pause. Entrega pantallazo donde se compruebe que se puede acceder a la base de datos en la **maquina1**. Si has realizado el punto 7 muestra las tablas de la base de datos. Indica nombre de usuario y contraseña para acceder a la base de datos.
5. Al finalizar el script: pantallazo donde se compruebe que se puede acceder a la base de datos en la **maquina2** usando la IP pública.
6. Al finalizar el script: pantallazo donde se compruebe que la **maquina1** está parada y que la **maquina2** tiene 2Gb de RAM.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


