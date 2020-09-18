---
title: "Práctica: Gestión del almacenamiento de la información" 
permalink: /seguridadgs/u01/practica_almacenamiento.html
---

## Ejercicio: RAID 5

Vamos a crear una máquina virtual con un sistema operativo Linux. En esta máquina, queremos crear un raid 5 de 2 GB, para ello vamos a utilizar discos virtuales de 1 GB. Crea un  fichero `Vagrantfile` para crear la máquina.

{% capture notice-text %}
* **Tarea 1:** Crea una raid llamado md5 con los discos que hemos conectado a la máquina. ¿Cuantós discos tienes que conectar? ¿Qué diferencia exiiste entre el RAID 5 y el RAID1?
* **Tarea 2:** Comprueba las características del RAID. Comprueba el estado del RAID. ¿Qué capacidad tiene el RAID que hemos creado?
* **Tarea 3:** Crea un volumen lógico (LVM) de 500Mb en el raid 5.
* **Tarea 4:** Formatea ese volumen con un sistema de archivo xfs.
* **Tarea 5:** Monta el volumen en el directorio `/mnt/raid5` y crea un fichero. ¿Qué tendríamos que hacer para que este punto de montaje sea permanente?
* **Tarea 6:** Marca un disco como estropeado. Muestra el estado del raid para comprobar que un disco falla. ¿Podemos acceder al fichero?
* **Tarea 7:** Una vez marcado como estropeado, lo tenemos que retirar del raid.
* **Tarea 8:** Imaginemos que lo cambiamos por un nuevo disco nuevo (el dispositivo de bloque se llama igual), añádelo al array y comprueba como se sincroniza con el anterior.
* **Tarea 9:** Añade otro disco como reserva. Vuelve a simular el fallo de un disco y comprueba como automática se realiza la sincronización con el disco de reserva.
* **Tarea 10:** Redimensiona el volumen y el sistema de archivo de 500Mb al tamaño del raid.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

