---
title: "Protocolo NFS"
---

## Recursos

* [Protocolos de almacenamiento HTTP](pdf/almacenamiento2526.pdf)

## Servidor NFS

**NFS (Network File System)** es un protocolo que permite compartir archivos y directorios a través de una red, de forma que un sistema cliente pueda acceder a los recursos remotos como si se tratara de carpetas locales. Fue desarrollado originalmente por Sun Microsystems y es ampliamente utilizado en sistemas Unix y Linux.

El funcionamiento básico consiste en que un **servidor NFS** exporta (comparte) uno o varios directorios, y uno o varios **clientes NFS** los montan en su propio sistema de archivos. Esto permite compartir datos, configuraciones o recursos comunes entre diferentes máquinas.

1. El **servidor NFS** define qué directorios se van a compartir y qué clientes pueden acceder a ellos, junto con los permisos de acceso.
2. El **cliente NFS** monta el directorio exportado en su propio sistema de archivos.
3. Las operaciones de lectura y escritura se realizan a través de la red, gestionadas por el protocolo NFS y el sistema de archivos remoto.

NFS suele usar el puerto **2049** y puede funcionar sobre TCP o UDP.

## Instalación del servidor NFS

En una distribución basada en Debian o Ubuntu:

```bash
sudo apt update
sudo apt install nfs-kernel-server
```

## Configuración del servidor NFS

Los directorios que se van a compartir se definen en el archivo **/etc/exports**.
Cada línea indica el directorio exportado, los clientes autorizados y las opciones de acceso.

Ejemplo de **/etc/exports**:

```
/srv/nfs/compartido 192.168.1.0/24(rw,sync,no_subtree_check)
```

Explicación de las opciones:

* **rw**: permite lectura y escritura.
* **sync**: confirma las operaciones de escritura en el disco antes de responder.
* **no_subtree_check**: desactiva la comprobación del subárbol, mejora el rendimiento.
* **192.168.1.0/24**: restringe el acceso a los clientes de esa red. Se puede restringir los clientes que pueden conectarse mediante direcciones IP o rangos de red.

Después de modificar el archivo, se aplican los cambios:

```bash
sudo exportfs -ra
```

Y se puede verificar lo que está exportado:

```bash
sudo exportfs -v
```

## Configuración del cliente NFS

En el cliente se instala el paquete correspondiente. En Debian o Ubuntu:

```bash
sudo apt install nfs-common
```

Se crea un punto de montaje local:

```bash
sudo mkdir -p /mnt/nfs/compartido
```

Y se monta el recurso remoto:

```bash
sudo mount 192.168.1.10:/srv/nfs/compartido /mnt/nfs/compartido
```

Donde `192.168.1.10` es la IP del servidor NFS.

Se puede comprobar que el montaje ha sido exitoso:

```bash
df -h | grep nfs
```

Para que el montaje sea permanente, se puede añadir una línea en el archivo **/etc/fstab** del cliente:

```
192.168.1.10:/srv/nfs/compartido /mnt/nfs/compartido nfs defaults 0 0
```

