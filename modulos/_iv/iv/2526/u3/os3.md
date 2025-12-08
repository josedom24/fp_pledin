---
title: "Clase 5: Almacenamiento en OpenStack desde el CLI"
---

## Conceptos previos de volúmenes

* **Cinder** (OpenStack block storage) gestiona de forma sencilla una SAN.
* **Volumen**: 
    * Dispositivo de bloques que se puede asociar y desasociar de una instancia cuando se desee.
    * Utilizado para proporcionar almacenamiento permanente o independiente de la vida de una instancia.
    * El componente de OpenStack que gestiona los volúmenes se llama **Cinder**.
    * Un volumen en cinder es equivalente a una unidad lógica en SAN.
    * Cinder es equivalente a [Amazon EBS](http://aws.amazon.com/es/ebs/).

## Gestión de volúmenes con OpenStack client (OSC)

Para gestiona los volúmenes con OSC, usamos los comandos de `openstack volume`. Por ejemplo:

* Creación de volumen:
    
        openstack volume create --size 1 mi_disco1

* Listar los volúmenes:
        
        openstack volume list

* Para asociar el volumen a una instancia:
        
        openstack server add volume --device /dev/sdb instancia_prueba mi_disco1

* Para desasociar el volumen de la instancia:
        
        openstack server remove volume instancia_prueba mi_disco1

* Para eliminar el volumen:

        openstack volume delete mi_disco1

{% capture notice-text %}
## Ejercicio

1. Crea un volumen.
2. Asócialo a una instancia. En la instancia formatéalo y móntalo.
3. Intenta eliminar el volumen. ¿Puedes hacerlo? ¿Por qué?
4. Desacocia el volumen de la instancia.
5. Elimina el volumen.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Creación de una instancia con el disco raíz sobre un volumen

Creamos un volumen *arrancable* de 8 GiB que contenga la imagen:

``` 
openstack volume create --bootable --size 8 --image "Debian 13.0 - Trixie" disco_debian
```

Creamos una nueva instancia con este volumen:

    openstack server create --flavor vol.mini \
    --volume disco_debian \
    --security-group default \
    --key-name clave_jdmr \
    --network "red de josedom" \
    instancia_prueba2

Nota: He escogido el sabor `vol.mini` que tiene 0 de disco duro, porque estoy usando un volumen.

{% capture notice-text %}
## Ejercicio

1. Crea un volumen arrancable de 10 Gb desde una imagen.
2. Crea una instancia cuyo disco principal sea este volumen. Recuerda que el sabor debe ser de tipo `vol`.
3. Instala algún servicio.
4. Elimina la instancia y crea una nueva a partir del mismo volumen.
5. Comprueba que no se ha perdido la información guardada en el volumen.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Creación de una instantánea de un volumen

No es recomendable hacer una instantánea de un volumen asociado, puede provocar la corrupción de la instantánea.

* Para crear una instantánea de volumen:

        openstack server remove volume instancia_prueba mi_disco1
	    openstack volume snapshot create --volume mi_disco1 copia_mi_disco1
		
* Listar las instantáneas:

	    openstack volume snapshot list
		
* Crear un nuevo volumen a partir de la instantánea:

	    openstack volume create --snapshot copia_mi_disco1 disco2
		
* Para borramos el snapshot y el volumen creado:

	* Si intentamos borrar el volumen desde el que hemos creado la instantánea:

		    openstack volume delete mi_disco1
		    Invalid volume: Volume still has 1 dependent snapshots. (HTTP 400) (Request-ID: req-...)

	* Debemos borrar primero el snapshot y posteriormente el volumen:

		    openstack volume snapshot delete copia_mi_disco1
		    openstack volume delete mi_disco1

{% capture notice-text %}
## Ejercicio

1. Crea un volumen.
2. Asócialo a una instancia. En la instancia formatéalo y móntalo. Añade algún fichero.
3. Crea una instantánea del volumen. Recuerda que antes debe desacociarlo de la instancia.
4. Elimina el volumen.
5. Crea un nuevo volumen desde la instantánea, vuele a asociarlo a la instancia y comprueba que sigue teniendo la información.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
    
## Extender el tamaño de un volumen

Para redimensionar el tamaño de un volumen:

	openstack volume set --size 2 disco2

{% capture notice-text %}
## Ejercicio

1. Redimensiona el volumen que tienes asociado a la instancia.
2. Recuerda que posteriormente tendrás que redimensionar el sistema de archivos.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>