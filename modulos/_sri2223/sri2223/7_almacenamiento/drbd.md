---
title: Introducción a DRBD y OCFS2
---

## DRBD

**DRBD** (*Distributed Replicated Block Device*) es un sistema de almacenamiento replicado distribuido para la plataforma Linux.

Es parecido a un RAID1, pero en este caso, se hace la duplicación de los datos entre diferentes **dispositivos de bloque** en diferentes hosts a través de la red.

DRBD es software libre desarrollado por la empresa LinBit. [Documentación oficial.](https://linbit.com/drbd-user-guide/drbd-guide-9_0-en/)

## Recurso DRBD

El **recurso DRBD** es el espacio de almacenamiento y la información relacionada administrada por DRBD. Un recurso tendrá cuatro características:

* Nombre
* Nombre del dispositivo de bloque que se crea (ejemplo: `/etc/drbd1`)
* Configuración del dispositivo de bloque que se va a replicar en cada nodo.
* Configuración de red de los nodos del cluster.

## Modos de funcionamiento DRBD

Podemos configurar DRBD en dos modos:

* **Modo "Un sólo primario" (Single-primary)**: Uno de los nodos es el primario y el que puede montar el recurso. El otro nodo es el secundario y no podrá montar el recurso. Normalmente cuando el recurso lo formateamos con un sistema de archivo tradicional. Se utiliza para cluster activo-pasivo. 
* **Modo "Dos primarios" (Dual-primary)**: En este caso los dos nodos se configuran como primario, por lo que pueden montar el recurso al mismo tiempo. Es necesario usar un sistema de ficheros distribuidos (OCFS2, GlusterFS, ...). Se utiliza en cluster activo-activo.

## Configuración del modo Single-primary 

Tenemos un escenario donde tenemos dos máquinas. Cada máquina tiene conectado un disco, que es el dispositivo de bloque que vamos a duplicar.

Lo primero que haremos es instalar las herramientas del espacio de usuario de DRBD:

```bash
apt install drbd-utils
```

Creamos el recurso DRBD. Creamos el fichero `/etc/drbd.d/datos.res`:

```code
resource datos {
 protocol C;
 meta-disk internal;
 device /dev/drbd1;
 syncer {
  verify-alg sha1;
 }
 net {
  allow-two-primaries;
 }
 on nodo1 {
    disk /dev/sdb;
    address 10.1.1.101:7789;
 }
 on nodo2 {
    disk /dev/sdb;
    address 10.1.1.102:7789;
 }
}
```

En la creación del recurso hemos indicado:

* El nombre: `resource datos`.
* El dispositivo de bloque que se va a crear: `device /dev/drbd1;`
* Los dispositivos de bloque que se van a replicar en cada nodo: `disk /dev/sdb;`
* Las direcciones ip de cada nodo y el puerto que se va a utilizar para la sincronización.

A continuación vamos a crear el recurso drbd y lo vamos a activar en ambos nodos:
```bash
drbdadm create-md datos
drbdadm up datos
```

Asignamos el nodo1 como primario y el nodo2 como secundario, por lo tanto **ejecutamos en el nodo1**:

```bash
drbdadm primary --force datos
```

Y comprobamos que empieza la sincronización de discos:

```bash
$ drbdadm status datos
datos role:Primary
  disk:UpToDate
  peer role:Secondary
    replication:SyncSource peer-disk:Inconsistent done:1.86
```

Trascurrido un tiempo comprobamos que los discos ya están sincronizados:


```bash
$ drbdadm status datos
datos role:Primary
  disk:UpToDate
  peer role:Secondary
    replication:Established peer-disk:UpToDate
```

Podemos ver la característica de nuestros recursos DRBD:

```bash
$ cat /proc/drbd
version: 8.4.10 (api:1/proto:86-101)
srcversion: 9B4D87C5E865DF526864868 

 1: cs:Connected ro:Primary/Secondary ds:UpToDate/UpToDate C r-----
    ns:530108 nr:0 dw:5872 dr:526461 al:14 bm:0 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:0
```

Y finalmente podemos formatear el dispositivo de bloque, montarlo y crear un fichero `index.html` en el (todo esto se ejecuta en el nodo primario, **en el nodo1**):

```bash
$ apt install xfsprogs

$ mkfs.xfs /dev/drbd1

$ mount /dev/drbd1 /mnt
$ cd /mnt/
$ echo "<h1>Prueba</h1>" >> index.html
$ umount /mnt
```

Si en el nodo2 (que tiene el papel de secundario) intentamos montar el recurso:

```bash
$ mount /dev/drbd1 /mnt
mount: /mnt: mount(2) system call failed: Wrong medium type.
```

## Configuración del modo Dual-primary

Si queremos que los dos nodos tengan montado simultáneamente el recurso tenemos que configurar los dos nodos como primario. En el **nodo2**:

```bash
$ drbdadm primary datos
$ drbdadm status datos
datos role:Primary
  disk:UpToDate
  peer role:Primary
    replication:Established
        peer-disk:UpToDate
$ mount /dev/drbd1 /mnt
```

Para que esto funcione de forma adecuada tenemos que usar un **Sistema de Ficheros en Clúster o Distribuidos** (por ejemplo OCFS2, GlusterFS,...)

## OCFS2

**OCFS** (Oracle Cluster File System) es un sistema de archivos distribuido de alto rendimiento desarrollado por Oracle Corporation. Es un sistema de archivos nativo de clúster que permite a varios nodos del clúster acceder y modificar los mismos archivos al mismo tiempo.

Vamos a usar dos servicios:
* **o2cb**: Encargado de gestionar el clúster.
* **ocfs2**: Encargado de gestionar el sistema de fichero distribuido.

Para la instalación, ejecutamos en los dos nodos:

```
apt install ocfs2-tools
```

En primer lugar tenemos que crear un clúster ocfs2 indicando los nodos que van
a formar parte de él. Ejecutamos lo siguiente en **uno de los nodos** e indicamos el nombre del clúster que vamos a crear:

```
o2cb add-cluster micluster
```

Ahora tenemos que añadir los nodos del clúster, desde uno de los nodos ejecutamos:

```
o2cb add-node micluster nodo1 --ip 10.1.1.101
o2cb add-node micluster nodo2 --ip 10.1.1.102
```

Podemos ver el estado del clúster ejecutando:

```
o2cb list-cluster micluster   

node:
	number = 0
	name = nodo1
	ip_address = 10.1.1.101
	ip_port = 7777
	cluster = micluster

node:
	number = 1
	name = nodo2
	ip_address = 10.1.1.102
	ip_port = 7777
	cluster = micluster

cluster:
	node_count = 2
	heartbeat_mode = local
	name = micluster
```
A continuación, copiamos el contenido del fichero `/etc/ocfs2/cluster.conf` (que prácticamente es la salida del comando anterior) en la otra máquina.

En una de las máquinas editamos el fichero `/etc/default/o2cb` y modificamos los siguientes parámetros:

```
# O2CB_ENABLED: 'true' means to load the driver on boot.
O2CB_ENABLED=true

# O2CB_BOOTCLUSTER: If not empty, the name of a cluster to start.
O2CB_BOOTCLUSTER=micluster  # Cambiamos el valor de este parámetro por el nombre de nuestro cluster.
```


Ahora tenemos que formatear el dispositivo drbd, de nuevo en un solo nodo:

```
mkfs.ocfs2 --cluster-stack=o2cb --cluster-name=micluster /dev/drbd1
```




