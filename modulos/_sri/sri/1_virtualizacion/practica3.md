---
title: "Práctica 3/3: Virtualización en Linux y servidor DHCP (Parte 1)"
---

## Creación de las máquinas clientes

1. Crea una nueva máquina virtual llamada **cliente1** a partir de la plantilla **plantilla-cliente** que tenga un volumen de 5G. Tienes que tener en cuenta los siguientes aspectos:
	* Antes de crear la máquina virtual redimensiona su sistema de fichero para que ocupe el espacio completo del disco.
	* La máquina se conecta a la red **red_intra**.
	* La máquina tiene una configuración estática de red.
	* La máquina debe tener el hostname **cliente1-tunombre**.
	* En el usuario `debian` copia tu clave pública y la [mia](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Claves_p%C3%BAblicas_de_los_profesores) para que podamos acceder sin introducir la contraseña por ssh
2. Accede a **cliente1**, realiza una configuración estática de la red y comprueba si tiene acceso al exterior.

{% capture notice-text %}
## Entrega

1. Demostración de que el volumen de la máquina **cliente1** utiliza como imagen base el volumen de la plantilla **plantilla-cliente**.
2. Demostración que tanto el volumen de **cliente1**, cómo su sistema de ficheros tiene el tamaño indicado en el enunciado.
3. Muestra la dirección IP de **cliente1** y la puerta de enlace.
4. Demostración que tiene acceso al exterior.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>