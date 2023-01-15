---
title: "Ejercicio 1: Sistemas de ficheros avanzados Btrfs"
---

Para hacer este ejercicio puedes usar este fichero [`Vagranfile`](files/btrfs/Vagrantfile).

Tenemos una máquina debian con 5 discos duros de 1Gb. Para empezar realiza los siguientes pasos:

1. Instala btrfs:

	```
	apt install btrfs-progs
	```
2. Formatea con btrfs todos los discos:

	```
	mkfs.btrfs /dev/vdb 
	mkfs.btrfs /dev/vdc 
	mkfs.btrfs /dev/vdd 
	mkfs.btrfs /dev/vde 
	mkfs.btrfs /dev/vdf
	```

3. Comprueba que el formato ha sido correcto ejecutando `btrfs -f`.
4. Una vez que los hemos formateado, podemos empezar a trabajar con ellos. Para empezar, vamos a montar el primer disco en el directorio `/mnt`:

	```
	mount /dev/vdb /mnt
	```

	Una vez hecho esto, podemos usar una de las características de btrfs: **añadir volúmenes al sistema de ficheros montado**. Para ello, usamos el siguiente comando:

	```
	btrfs device add -f /dev/vdc /mnt
	btrfs device add -f /dev/vdd /mnt
	btrfs device add -f /dev/vde /mnt
	btrfs device add -f /dev/vdf /mnt
	```

	Como vemos, hemos añadido dos volúmenes al sistema de fichero que habíamos montado en `/mnt`. Podemos ver las características de dicho sistema usando el siguiente comando:

	```
	btrfs fi usage /mnt
	```

	Nos muestra información sobre el sistema de ficheros, incluyendo el espacio total, el disponible, volúmenes que lo forman, etc. Tras añadir nuevos dispositivos al sistema de ficheros, es conveniente **equilibrar el almacenamiento (repartir los ficheros entre los discos que acabamos de introducir)**, para lo que usaríamos el siguiente comando:

	```
	btrfs balance start /mnt
	```

	Comprueba el tamaño del directorio `/mnt` ejecutando el comando `df -h`.
	
## Compresión

Por defecto,btrfs no usa ningún método de compresión ya que tenemos que indicarle cual usar (se indica durante el montaje). Así pues probemos con diferentes método de compresión: zlib, lzo, ...

Hagamos una prueba con el método de compresión zlib:

1. Desmontamos y volvemos a montar el sistema de ficheros indicando el método de compresión:

	```
	umount /mnt
	mount -o compress=zlib /dev/vdb /mnt
	```

2. Ahora creamos un fichero de 3Gb:

	```
	cd /mnt
	dd if=/dev/zero of=/mnt/prueba count=3072 bs=1024000

	ls -alh
	-rw-r--r--  1 root root 3.0G Jan 15 19:25 prueba
	```

3. Veamos cuanto ocupa dicho fichero según btrfs, ejecutando `btrfs fi usage /mnt` y nos fijamos en el campo `Used` (**La actualización de este campo no es inmediata, hay que esperar un tiempo para que se actualice**):

	```
	...
	Used:			 102.00MiB
	```

	De esta forma, podemos observar que usando zlib, btrfs es capaz de comprimir un fichero de 3GB en 102 Mb.

## Copy on Write (COW) 

La técnica "copy on write" sirve para que al copiar un fichero, este realmente no se copia, sino que se crean punteros que apuntan al fichero original. Solo cuando se producen cambios sobre ese fichero, se crea realmente la copia.

1. Para probar esto, vamos a crear un fichero y comprobar el tamaño que ocupa en el disco (hemos borrado el fichero `prueba` del apartado anterior y hemos vuelto a montar el sistema de ficheros sin compresión):

	```
	umount /mnt
	mount /dev/vdb /mnt
	cd /mnt
	
	dd if=/dev/zero of=/mnt/prueba bs=2048 count=200k
	/mnt# ls -lh 
	total 400M
	-rw-r--r-- 1 root root 400M Jan 15 19:29 prueba
	```

	Comprobamos, ejecutando `btrfs fi usage /mnt` que este fichero ocupa unos 400Mb (`Used:			 401.35MiB`).

2. Ahora realizaremos una copia, y como tiene activado el CoW, no debería aumentar el tamaño, ya que no hemos realizado ningún cambio. Para realizar una copia con estas características usamos el parámetro `-reflink=always`:

	```
	cp --reflink=always /mnt/prueba /mnt/prueba2
	```

	Ahora comprobemos que el espacio usado no es el doble, ya que realmente no se ha copiado el fichero:

	```
	btrfs fi usage /mnt
	...
	Used:			 401.35MiB
	```

## Deduplicación

La deduplicación consiste en buscar ficheros que se han escrito dos o más veces en el disco (como al copiar un fichero) y combinarlos en un solo fichero, creado punteros en los diferentes directorios que apunten hacia ese único fichero. De esta forma, se intenta maximizar el espacio de disco disponible, al no tener la misma información escrita más de una vez.

Para poder hacer uso de esta funcionalidad, es necesario instalar un paquete adicional:

```
apt install duperemove
```

1. Desmontamos el sistema de ficheros y lo volvemos a montar sin la opción de compresión. Borramos los ficheros del ejercicio anterior, y nos descargamos un fichero:

	```
	umount /mnt 
	mount /dev/vdb /mnt
	
	wget https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso
	```			
2. Realizamos una copia (sin usar la característica de CoW) del fichero y comprobamos que ocupa unos 778 Mb.

	```
	cp debian-11.6.0-amd64-netinst.iso debian-11.6.0-amd64-netinst.iso.bak
	btrfs fi usage /mnt
	...
	Used:			 778.29MiB
	...
	```

3. Ahora usaremos el paquete que hemos descargado antes para hacer la deduplicación:

	```
	duperemove -d --lookup-extents=no /mnt
	```

	Como vemos ha encontrado dos ficheros iguales y podemos comprobar que aunque tenemos dos ficheros (aproximadamente 780 Mb), en realizada ocupa sólo lo que ocupa uno de los ficheros:

	```
	btrfs fi usage /mnt
	...
	Used:			 389.41MiB
	...
	```

	Como vemos, ha funcionado, volviendo a ocupar el mismo espacio, ya que ambos ficheros eran idénticos.

## Redimensión 

Btrfs también puede redimensionarse en caliente. Veamos como:

1. En primer lugar comprobamos es espacio de que dispone el sistema de ficheros:

	```
	btrfs filesystem show /mnt/
	```

	Como vemos hay cinco discos anexados de 1GiB cada uno.

2. Reducimos el tamaño del sistema de ficheros:

	```
	btrfs filesystem resize -500M /mnt/
	```

	Comprueba con la instrucción del punto 1 que ha funcionado. Además podemos ejecutar un `df -h` y también lo comprobamos.

3. Aumentamos el tamaño con la instrucción `btrfs filesystem resize +500M /mnt/`.
## Desfragmentación

Debido a singularidad del sistema de ficheros, Btrfs sufre de una fragmentación elevada. Es por ello, que es necesario desfragmentar el disco frecuentemente. Para ello vamos a usar la herramienta que viene incluida con btrfs:

```
btrfs filesystem defrag -r /mnt
```

# Subvolumen

Btrfs nos permite crear subvolúmenes. Esto es como crear otro sistema de ficheros (puede considerarse también como un directorio con más funcionalidades) dentro del sistema de ficheros. Para poder crear los subvolúmenes debemos ejecutar los siguientes comandos:

```
btrfs subvolume create /mnt/subvolumenprueba
```

Podemos ver el subvolumen que hemos creado:

```
ls -l /mnt
...
drwxr-xr-x  1 root root         0 Jan 15 20:47 subvolumenprueba
```

Este subvolumen puede montarse en otros lugares del disco, aunque para ello primero debemos obtener su identificador. Para obtener dicho identificador ejecutamos lo siguiente:

```
btrfs subvolume list /mnt
ID 262 gen 68 top level 5 path subvolumenprueba
```

Como vemos, tenemos el identificador 262. Ahora para montar el subvolumen en otro lado, usamos lo siguiente:

```
mount -o subvolid=262 /dev/vdb /mnt2
```

Con esto ya lo hemos montado en el nuevo directorio. Para borrar un subvolumen, ejecutamos lo siguiente:

```
btrfs subvolume delete /mnt/subvolumenprueba/
```

## Snapshots

Antes dijimos que los subvolúmenes eran directorios con más funcionalidades. Pues bien, esta es una de ellas: podemos hacer snapshots del subvolumen. Para ello vamos a crear otro subvolumen como hicimos en el apartado anterior. También crearemos un fichero dentro del subvolumen para posteriores pruebas:

```
btrfs subvolume create /mnt/subvolumenprueba2
Create subvolume '/mnt/subvolumenprueba2'

dd if=/dev/zero of=/mnt/subvolumenprueba2/prueba.txt count=3072 bs=1048576
```

Ahora crearemos un snapshot de dicho subvolumen:

```
btrfs subvolume snapshot /mnt/subvolumenprueba2/ /mnt/snapshotprueba
Create a snapshot of '/mnt/subvolumenprueba2/' in '/mnt/snapshotprueba'
```

Hemos creado un snapshot en el directorio `/mnt`:

```
tree /mnt/
/mnt/
├── snapshotprueba
│        └── prueba.txt
└── subvolumenprueba2
    └── prueba.txt

2 directories, 2 files
```

Este snapshot ya funciona como un subvolumen, por lo que podemos montarlo o desmontarlo a nuestro gusto. También podemos recuperar información concreta del snapshot:

```
rm -r /mnt/subvolumenprueba2/prueba.txt

cp /mnt/snapshotprueba/prueba.txt /mnt/subvolumenprueba2/prueba.txt
```

Con esto hemos recuperado el fichero que hemos borrado. También podemos seleccionar un subvolumen o snapshot para que se monte automáticamente al montar el sistema de ficheros. Para ello, al igual que antes, debemos obtener el identificador del subvolumen o snapshot:

```
btrfs subvolume list /mnt
ID 266 gen 44 top level 5 path subvolumenprueba2
ID 274 gen 41 top level 5 path snapshotprueba
```

En este caso configuraremos el snapshot para que se monte automáticamente en `/mnt` al montar el sistema de ficheros:

```
btrfs subvolume set-default 274 /mnt
```

Ahora, si desmontamos el sistema de ficheros y lo volvemos a montar, debería haberse montado el snapshot en `/mnt`:

ls -l /mnt
total 3145728
-rw-r--r-- 1 root root 3221225472 Dec  5 14:47 prueba.txt

	
## RAID

Otra características de btrfs es que es capaz de crear dispositivos RAID sin necesidad de hacer uso de `mdadm`. Para ello volveremos a hacer uso de `balance`, pero esta indicando que queremos que lo convierta en raid 1:

```
btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt
```

Si volvemos a ver la información del sistema de ficheros, vemos que nos indica que es un RAID 1, para ello volvemos a ejecutar `btrfs fi usage /mnt` y ejecutando `df -h` vemos que `mnt` ocupa 2,5 Gb.
