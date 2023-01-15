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
	
## RAID

Otra características de btrfs es que es capaz de crear dispositivos RAID sin necesidad de hacer uso de `mdadm`. Para ello volveremos a hacer uso de `balance`, pero esta indicando que queremos que lo convierta en raid 1:

```
btrfs balance start -dconvert=raid1 -mconvert=raid1 /mnt
```

Si volvemos a ver la información del sistema de ficheros, vemos que nos indica que es un RAID 1, para ello volvemos a ejecutar `btrfs fi usage /mnt` y ejecutando `df -h` vemos que `mnt` ocupa 2,5 Gb.

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

	df -h
	-rw-r--r--  1 root root 3.0G Jan 15 19:25 prueba
	```

3. Veamos cuanto ocupa dicho fichero según btrfs, ejecutando `btrfs fi usage /mnt`y nos fijamos en el campo:

	```
	...
	Used:			 195.97MiB
	```

	De esta forma, podemos observar que usando zlib, btrfs es capaz de comprimir un fichero de 3GB en 195 Mb.

## Copy on Write (COW) 

La técnica "copy on write" sirve para que al copiar un fichero, este realmente no se copia, sino que se crean punteros que apuntan al fichero original. Solo cuando se producen cambios sobre ese fichero, se crea realmente la copia. 

1. Para probar esto, vamos a crear un fichero y comprobar el tamaño que ocupa en el disco (hemos borrado el fichero `prueba` del apartado anterior):

	```
	dd if=/dev/zero of=/mnt/prueba bs=2048 count=200k
	/mnt# ls -lh 
	total 400M
	-rw-r--r-- 1 root root 400M Jan 15 19:29 prueba
	```

	Comprobamos, ejecutando `btrfs fi usage /mnt` que este fichero ocupa unos 26Mb (`Used:			  26.73MiB`).

2. Ahora realizaremos una copia, y como tiene activado el CoW, no debería aumentar el tamaño, ya que no hemos realizado ningún cambio. Para realizar una copia con estas características usamos el parámetro `-reflink=always`:

	```
	cp --reflink=always /mnt/prueba /mnt/prueba2
	```

	Ahora comprobemos que el espacio usado no es el doble, ya que realmente no se ha copiado el fichero:

	```
	btrfs fi usage /mnt
	...
	Used:			  27.20MiB
	```

## Deduplicación

La deduplicación consiste en buscar ficheros que se han escrito dos o más veces en el disco (como al copiar un fichero) y combinarlos en un solo fichero, creado punteros en los diferentes directorios que apunten hacia ese único fichero. De esta forma, se intenta maximizar el espacio de disco disponible, al no tener la misma información escrita más de una vez.

Para poder hacer uso de esta funcionalidad, es necesario instalar un paquete adicional:

```
apt install duperemove
```

1. Desmontamos el sistema de ficheros y lo volvemos a montar sin la opción de compresión. Borramos los ficheros del ejercicio anterior, y volvemos a crear un fichero:

	```
	umount /mnt 
	mount /dev/vdb /mnt
	
	dd if=/dev/zero of=/mnt/prueba2 bs=2048 count=50k
	```			
2. Realizamos una copia (sin usar la característica de CoW) del fichero y comprobamos que ocupa unos 200Mb.

	```
	cp prueba2 prueba3
	btrfs fi usage /mnt
	...
	Used:			 200.89MiB
	...
	```

3. Ahora usaremos el paquete que hemos descargado antes para hacer la deduplicación:

	```
	


	
