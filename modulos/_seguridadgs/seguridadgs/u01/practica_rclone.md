---
title: "Práctica: rclone: Gestionando nuestro almacenamiento en la nube" 
permalink: /seguridadgs/u01/practica_rclone.html
---

## rclone

[rclone](https://rclone.org/) es una herramienta que nos permite trabajar con los ficheros que tenemos almacenados en distintos servicios de almacenamiento en la nube (dropbox, google drive, mega, box,... y muchos más que puedes ver en su página principal). Por lo tanto con rclone podemos gestionar y sincronizar los ficheros de nuestros servicios preferidos desde la línea de comandos.

{% capture notice-text %}
* **Tarea 1:** Instala rclone en tu equipo.
* **Tarea 2:** Configura dos proveedores cloud en rclone (dropbox, google drive, mega, ...)
* **Tarea 3:** Muestra distintos comandos de rclone para gestionar los ficheros de los proveedores cloud: lista los ficheros, copia un fichero local a la nube, sincroniza un directorio local con un directorio en la nube, copia ficheros entre los dos proveedores cloud, muestra alguna funcionalidad más,...
* **Tarea 4:** Monta en un directorio local de tu ordenador, los ficheros de un proveedor cloud. Comprueba que copiando o borrando ficheros en este directorio se crean o eliminan en el proveedor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



