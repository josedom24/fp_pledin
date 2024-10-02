---
title: "Práctica (1 / 3): Virtualización en Linux y servidor DHCP (Parte 1)"
---

## Descripción

Vamos a crear una infraestructura con varias máquinas virtuales y contenedores donde vamos a instalar un servidor DHCP para configurar de forma dinámica la configuración de red.

## Creación de la plantilla para las máquinas clientes

Vamos a crear una plantilla que utilizaremos para la creación de las máquinas que utilizaremos como clientes. Para ello:

1. Crea con `virt-install` una máquina virtual de Debian 12 con formato qcow2 y un tamaño de 3GiB. 
	* La máquina debe tener un usuario `debian` con contraseña `debian` que puede utilizar `sudo` sin contraseña.
	* Instala el servidor ssh en la máquina.
	* ~~En el usuario `debian` copia tu clave pública y la [mia](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Claves_p%C3%BAblicas_de_los_profesores) para que podamos acceder sin introducir la contraseña por ssh~~.
2. Convierte la máquina virtual en una plantilla llamada **plantilla-cliente**. El hostname de la máquina debe ser **plantilla-cliente-tunombre**. ¿Cuánto ocupa el volumen de la plantilla en disco?
3. Utiliza la herramienta `virt-sparsify` para reducir el tamaño ocupado en disco del volumen. ¿Cuánto ocupa ahora el volumen de la plantilla en disco?

{% capture notice-text %}
## Entrega

1. Explica los pasos que has ejecutado para crear la plantilla **plantilla-cliente**.
2. Captura de pantalla donde se demuestre que la plantilla no se puede ejecutar.
3. ¿Qué ocupa el volumen de la plantilla en disco antes de ejecutar `virt-sparsify`? Una vez ejecutado, ¿cuánto ocupa el volumen en disco?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
