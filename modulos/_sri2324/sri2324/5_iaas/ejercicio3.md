---
title: "Gestión de almacenamiento"
---

En este ejercicio vamos a crear instancias cuyos discos duros están guardados en un volumen. Si se pierde la instancia, su información no se pierde y podremos crear una nueva instancia con el mismo volumen.

Para crear una instancia sobre un volumen, tenemos dos posibilidades:
* Crear un volumen con el contenido de una imagen.
* Al crear una instancia, indicar que se va a crear un volumen para guardar la información.

Vamos a realizar la primera opción que encontrarán en la sección [Creación de instancia ejecutadas sobre volúmenes](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo4/instancias_volumen.md), para ello sigue los siguientes pasos:

1. Crea un nuevo volumen de 10 Gb a partir de una imagen.
2. Crea una nueva instancia a partir de este volumen. 
	* Recuerda elegir el sabor de tipo **vol** (indica 0 Gb en el disco ya que el tamaño del disco será el tamaño del volumen).
	* Configúrala con cloud-init, utilizando un script parecido al del ejercicio anterior.
3. Accede a la instancia, comprueba el tamañao del disco, crea un fichero en el home del usuario. Instala apache2.
4. Elimina la instancia, y crea una nueva a partir del mismo volumen. ¿Tiene la misma información que la instancia anterior.

Siguiendo la sección [Gestión de volúmenes con OpenStack client (OSC)](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo4/osc_cinder.md) y usando OSC:

1. Crea un volumen de 2Gb.
2. Creamos un volumen arrancable de 8 GiB que contenga una imagen.
3. Crea una instancia a partir de dicho volumen. Esta instancia la puede configurar con cloud-init.
4. Añade el primer volumen de 2 Gb a la instancia.
5. Accede a la instancia y comprueba que tiene el disco añadido. Instálale apache2.
6. Crea una instantánea del disco de la instancia. Se creará una una imagen privada en tu proyecto.
7. Busca información y crea una nueva instancia a partir de la instantánea. ¿Tiene instalado apache2?

