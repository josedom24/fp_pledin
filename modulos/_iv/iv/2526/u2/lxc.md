---
title: "Introducción a Linux Containers (LXC)"
---

**LinuX Containers**, también conocido por el acrónimo **LXC**, es una tecnología de virtualización ligera o por contenedores, que es un método de virtualización en el que, sobre el núcleo del sistema operativo se ejecuta una capa de virtualización que permite que existan múltiples instancias aisladas de espacios de usuario, en lugar de solo uno. A estas instancias la llamamos **contenedores**.

**LXC** pertenece a los denominados **contenedores de sistemas**, su gestión y ciclo de vida es similar al de una máquina virtual tradicional. Está mantenido por Canonical y la página oficial es [linuxcontainers.org](https://linuxcontainers.org/).

## Instalación de LXC

Vamos a trabajar sobre una distribución GNU/Linux Debian 11. Para la instalación de LXC ejecutamos:

```bash
apt install lxc
```

Podemos crear contenedores LXC *privilegiados* (ejecutados como root) y *no privilegiados* (ejecutados por un usuario normal). En este curso vamos a trabajar con contenedores *privilegiados*.

## Creación y gestión de contenedores LXC

Para crear un contenedor ejecutamos como `root`:

```bash
$ lxc-create -n contenedor1 -t download
```

Con la opción -n indicamos el nombre del contenedor.

Con este comando ocurrirán varias cosas:

1. El comando te mostrará una lista de distribuciones Linux.
2. Te pedirá que indiques la distribución, la versión y la arquitectura.
3. La primera vez que indiquemos una distribución, versión y arquitectura, se descargará el sistema de ficheros comprimido (**plantilla**), que se guardará en caché en el directorio `/var/cache/lxc`.
4. Se crea el contenedor. Su sistema de fichero se creara a partir de Se descomprime la plantilla y se guardará en `/var/lib/lxc/contenedor1/rootfs/`.
5. El próximo contenedor que creemos con la misma distribución , versión y arquitectura, se creará más rápido ya que no se descargará la plantilla.

Si no queremos que el comando sea interactivo podemos indicar la distribución, versión y arquitectura desde la línea de comandos:

```bash
lxc-create -n contenedor2 -t download -- -d debian -r trixie -a amd64
```

## Listado de contenedores

Podemos listar los contenedores, ejecutando:

```bash
$ lxc-ls
contenedor1 
```

Con la opción `-f` nos da más información de los contenedores.

## Gestión de contenedores

Para iniciar un contenedor:

```bash
$ lxc-start contenedor1
$ lxc-ls -f
NAME        STATE   AUTOSTART GROUPS IPV4       IPV6 UNPRIVILEGED 
contenedor1 RUNNING 0         -      10.0.3.180 -    false        
```

Y para conectarnos a él:

```bash
$ lxc-attach contenedor1
root@contenedor1:~# 
```
Para detener un contenedor usamos `lxc-stop`.

## Ejecución de comandos en un contenedor

Podemos ejecutar un comando en un contenedor que se esté ejecutando de la siguiente manera:

```bash
$ lxc-attach contenedor1 -- ls -al
```

Si el contenedor está apagado, lo haríamos de la siguiente forma:

```bash
$ lxc-stop contenedor1
$ lxc-execute contenedor1 -- ls -al
```

## Obteniendo información de un contenedor

Para obtener información de un contenedor podemos ejecutar:

```bash
$ lxc-info contenedor1
```
Con la opción `-i` sólo nos da  la dirección ip, con la opción `-S` nos da la estadística de información enviada y recibida por la interfaz de red y con la opción `-s` nos da información del estado.