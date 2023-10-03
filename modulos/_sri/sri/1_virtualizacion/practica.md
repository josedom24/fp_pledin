---
title: "Práctica: Virtualización en Linux y servidor DHCP (Parte 1)"
---

## Descripción

Vamos a crear una infraestructura con varias máquinas virtuales y contenedores donde vamos a instalar un servidor DHCP para configurar de forma dinámica la configuración de red.

## 1. Creación de la plantilla para las máquinas clientes

Vamos a crear una plantilla que utilizaremos para la creación de las máquinas que utilizaremos como clientes. Para ello:

1. Crea con `virt-install` una máquina virtual de Debian 12 con formato qcow2 y un tamaño de 3GiB. 
	* La máquina debe tener un usuario `debian` con contraseña `debian` que puede utilizar `sudo` sin contraseña.
	* Instala el servidor ssh en la máquina.
	* En el usuario `debian` copia tu clave pública y la mia para que podamos acceder sin introducir la contraseña por ssh.
2. Convierte la máquina virtual en una plantilla llamada **plantilla-cliente**. El hostname de la máquina debe ser **plantilla-cliente-tunombre**. ¿Cuánto ocupa el volumen de la plantilla en disco?
3. Utiliza la herramienta `virt-sparsify` para reducir el tamaño ocupado en disco del volumen. ¿Cuánto ocupa ahora el volumen de la plantilla en disco?

{% capture notice-text %}
## Entrega

1. Explica los pasos que has ejecutado para crear la plantilla **plantilla-cliente**.
2. Captura de pantalla donde se demuestre que la plantilla no se puede ejecutar.
3. ¿Qué ocupa el volumen de la plantilla en disco antes de ejecutar `virt-sparsify`? Una vez ejecutado, ¿cuánto ocupa el volumen en disco?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## 2. Creación del escenario

![Práctica](img/practica.png)

Todas las operaciones las tiene que hacer desde la línea de comandos:

1. Crea una **red muy aislada**, que se llame **red_intra** que creará el puente `br-intra`. Esta red se tiene que iniciar cada vez que encendemos el host.
2. Crea con `virt-install` la máquina **router** con Debian 12: 
	* Está conectada a la red pública (al bridge `br0`) y la **red_intra**.
	* Esta máquina utiliza un disco en formato **raw** de 10 Gb.
	* El hostname de esta máquina debe ser `router-tunombre`.
	* Se debe poder acceder a ella por ssh con el usuario root sin que te pida contraseña (configura tu clave pública y la mia).
	* Debes configurar la segunda interfaz de red con direccionamiento estático para que tenga la dirección `192.168.200.1`.
	* Está máquina se debe iniciar cada vez que arrancamos el host.
3. Crea dos contenedores LXC conectados a la red **red_intra**. 
	* **servidorDHCP**: Es un contador creado a partir de la plantilla **Debian Bookworm**. Configura su red de forma estática. Su dirección IP debe ser la `192.168.200.2`.
	* **servidorWeb**: Es un contador creado a partir de la plantilla **Ubuntu 22.04 Jammy**. Configura su red de forma estática. Su dirección IP debe ser la `192.168.200.3`.
	* Los contenedores se deben iniciar de forma automática y se les debe limitar la memoria a 512Mb.
4. Configura la máquina **router** para que haga SNAT y permita que los contenedores tengan acceso al exterior. Instala en los contenedores el servidor ssh y configúralo para que podamos entrar con clave privada (configura tu clave pública y la mia) por ssh con el usuario `root`.

{% capture notice-text %}
## Entrega

1. Fichero xml con la definición de la red **red_intra**, la instrucción de creación y la que permite el inicio automático.
2. Comprobación que el volumen de la máquina **router** tiene el formato raw.
3. El comando `virsh` que muestra información de la máquina **router** para comprobar que se inicia de forma automática.
4. Salida del comando `ip a` en **router**.
5. Acceso por ssh sin que te pida la contraseña.
6. Lista los contenedores creados para que se visualice su dirección IP y se vea que se inician de forma automática.
7. Prueba de funcionamiento de que se ha limitado la memoria de los contenedores de forma adecuada.
8. Salida de la instrucción `iptables` que muestra la regla de SNAT que has configurado.
9. Comprobación que los contenedores tienen acceso al exterior.
10. Desde el host, utiliza `ssh -A`, para acceder al **router** y posteriormente a los contenedores.
11. Busca información sobre la configuración de ssh para definir distintos accesos. Configura el fichero `~/.ssh/config` en tu equipo para que puedas acceder directamente al **cliente1**.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## 3. Creación de las máquinas clientes

1. Crea una nueva máquina virtual llamada **cliente1** a partir de la plantilla **plantilla-cliente** que tenga un volumen de 5G. Tienes que tener en cuenta los siguientes aspectos:
	* Antes de crear la máquina virtual redimensiona su sistema de fichero para que ocupe el espacio completo del disco.
	* La máquina se conecta a la red **red_intra**.
	* La máquina tiene una configuración estática de red.
	* La máquina debe tener el hostname **cliente1-tunombre**.
2. Accede a **cliente1**, realiza una configuración estática de la red y comprueba si tiene acceso al exterior.

{% capture notice-text %}
## Entrega

1. Demostración de que el volumen de la máquina **cliente1** utiliza como imagen base el volumen de la plantilla **plantilla-cliente**.
2. Demostración que tanto el volumen de **cliente1**, cómo su sistema de ficheros tiene el tamaño indicado en el enunciado.
3. Muestra la dirección IP de **cliente1** y la puerta de enlace.
4. Demostración que tiene acceso al exterior.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


