---
title: "Práctica: Gestión del almacenamiento de la información" 
permalink: /seguridadgs/u01/practica_almacenamiento.html
---

## Ejercicio: RAID 1

Vamos a crear una máquina virtual con un sistema operativo Linux. Esta máquina va a tener conectada dos discos virtuales de 1 GB. Debemos instalar el software necesario para crear un raid 1 con dichos discos, para ello realiza los siguientes ejercicios:

{% capture notice-text %}
* **Tarea 1:** Entrega un fichero `Vagranfile` donde definimos la máquina con los discos necesarios para hacer el ejercicio. Además al crear la máquina con vagrant se debe instalar el programa `mdadm` que nos permite la construcción del RAID. 
* **Tarea 2:** Crea una raid llamado md1 con los dos discos que hemos conectado a la máquina.
* **Tarea 3:** Comprueba las características del RAID. Comprueba el estado del RAID. ¿Qué capacidad tiene el RAID que hemos creado?
* **Tarea 4:** Crea una partición primaria de 500Mb en el raid1.
* **Tarea 5:** Formatea esa partición con un sistema de archivo ext3.
* **Tarea 6:** Monta la partición en el directorio `/mnt/raid1` y crea un fichero. ¿Qué tendríamos que hacer para que este punto de montaje sea permanente?
* **Tarea 7:** Simula que un disco se estropea. Muestra el estado del raid para comprobar que un disco falla. ¿Podemos acceder al fichero?
* **Tarea 8:** Recupera el estado del raid y comprueba si podemos acceder al fichero.
* **Tarea 9:** ¿Se puede añadir un nuevo disco al raid 1?. Compruebalo.
* **Tarea 10:** Redimensiona la partición y el sistema de archivo de 500Mb al tamaño del raid.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio: RAID 5

A continuación queremos crear un raid 5 en una máquina de 2 GB, para ello vamos a utilizar discos virtuales de 1 GB. Modifica el fichero `Vagrantfile` del ejercicio anterior para crear una nueva máquina.

{% capture notice-text %}
* **Tarea 1:** Crea una raid llamado md5 con los dos discos que hemos conectado a la máquina.
* **Tarea 2:** Comprueba las características del RAID. Comprueba el estado del RAID. ¿Qué capacidad tiene el RAID que hemos creado?
* **Tarea 3:** Crea un volumen lógico de 500Mb en el raid 5.
* **Tarea 4:** Formatea ese volumen con un sistema de archivo xfs.
* **Tarea 5:** Monta el volumen en el directorio `/mnt/raid5` y crea un fichero. ¿Qué tendríamos que hacer para que este punto de montaje sea permanente?
* **Tarea 6:** Marca un disco como estropeado. Muestra el estado del raid para comprobar que un disco falla. ¿Podemos acceder al fichero?
* **Tarea 7:** Una vez marcado como estropeado, lo tenemos que retirar del raid.
* **Tarea 8:** Imaginemos que lo cambiamos por un nuevo disco nuevo (el dispositivo de bloque se llama igual), añádelo al array y comprueba como se sincroniza con el anterior.
* **Tarea 9:** Añade otro disco como reserva. Vuelve a simular el fallo de un disco y comprueba como automática se realiza la sincronización con el disco de reserva.
* **Tarea 10:** Redimensiona el volumen y el sistema de archivo de 500Mb al tamaño del raid.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

