---
title: "Práctica: Virtualización en Linux y servidor DHCP (Parte 2)"
---

## Descripción

Vamos as seguir trabajando con el escenario que hemos construido en la práctica anterior. En esta práctica vamos instalar y configurar servicios en las máquinas creadas, en concreto un servidor dhcp y un servidor web.

## 1. Instalación del servidor DHCP 

1. Instala un servidor DHCP en el contenedor **servidorDHCP** con las siguientes características:
	* Rango de direcciones: `192.168.200.10` - `192.168.200.200`.
	* Máscara de red: `255.255.255.0`
	* Duración de la concesión: 30 minutos
	* Puerta de enlace: `192.168.200.1`
	* Servidor DNS: `172.22.0.1`
2. Configura la máquina **cliente1** para que tome configuración de red dinámica y puedas probar que realmente está funcionando el servidor.
3. Conecta una máquina Windows a la **red_intra** y comprueba que también toma direccionamiento dinámico.

{% capture notice-text %}
## Entrega

1. Contenido de los ficheros de configuración que has modificado en el servidor DHCP.
2. Una captura de pantalla donde se vea la ip que ha tomado de forma dinámica el **cliente1** y el cliente windows.
3. Una captura de pantalla donde se comprueba que los dos clientes tienen conectividad al exterior.
4. El contenido del fichero de concesiones en el servidor dhcp para comprobar que se han concedido esas direcciones IP.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## 2. Reserva para el servidor web

Actualmente el servidor web **servidorWeb** tiene una configuración de red estática. Vamos a configurar una reserva para esta máquina:

1. Configura de forma adecuada el servidor dhcp para que ofrezca al servidor Web la misma IP (**reserva**) que habíamos configurado de forma estática.
2. Modifica la configuración de red del servidor Web para que tome la configuración de red de forma dinámica.

{% capture notice-text %}
## Entrega

1. Contenido del ficheros de configuración que has modificado en el servidor DHCP.
2. Una captura de pantalla donde se vea la ip que ha tomado de forma dinámica el servidor web.
3. ¿Las reservas se guardan en el fichero de concesión del servidor dhcp?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## 3. Instalación del servidor Web

Para ello sigue los siguientes pasos:

1. Instala el servidor `apache2` en el contenedor **servidorWeb**.
2. Crea en tu host un directorio en `/srv/web` con un fichero `index.html`.
3. Monta ese directorio en el directorio `/var/www/html` del contenedor **servidorWeb**.
4. Configura en el **router** una regla de DNAT para que podamos acceder al servidor Web desde el exterior. (**La configuración debe ser persistente.**)

{% capture notice-text %}
## Entrega

1. Captura de pantalla donde se vea que has montado el directorio indicado en el contenedor.
2. Captura de pantalla donde se vea el acceso al servidor web desde el exterior.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## 4. Script de creación de clientes

Escribe un script llamado `crear_cliente.sh` que va a automatizar la tarea de crear máquinas clientes a partir de la plantilla **plantilla-cliente**. Este script creará una nueva máquina con el nombre que le indiquemos, con nuevo volumen con el tamaño que le indiquemos y conectada a la red que le indiquemos. La nueva máquina se debe iniciar.

Por lo tanto el script recibe los siguientes argumentos en la línea de comandos:

* **Nombre**: nombre de la nueva máquina.
* **Tamaño del volumen**: Tamaño del volumen que tendrá la nueva máquina.
* **Nombre de la red** a la que habrá que conectar la máquina.

Para comprobar que funciona:

1. Crea un nuevo cliente llamado **cliente2** que tenga un volumen de 10G y que esté conectado a la **red_intra**. La instrucción que debes ejecutar será:

	```
	sh crear_clientes.sh cliente2 10G red_intra
	```
2. Comprueba que la máquina está funcionando, y que ha tomado direccionamiento de red de forma dinámica.

{% capture notice-text %}
## Entrega

1. La url del repositorio GitHub donde se encuentra el script.
2. Una comprobación de que el tamaño del disco de la máquina creada es el adecuado.
3. Una vez creado el **cliente2**, pruebas de funcionamiento del direccionamiento que ha tomado y de que tiene acceso al exterior.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## 5. Configuración de un nuevo ámbito

En este último punto vamos a modificar nuestra infraestructura para que el servidor dhcp reparta otro direccionamiento para las máquinas conectadas a otra red, para ello realiza los siguientes puntos:

1. Crea una **red muy aislada**, que se llame **red_intra2** que creará el puente `br-intra2`. Esta red se tiene que iniciar cada vez que encendemos el host.
2. Conecta la máquina **router** a esta red, y configura la nueva interfaz con la dirección `172.16.0.1\16`.
3. Conecta el contenedor **servidorDHCP** a esta red, y configura la nueva interfaz con la dirección `172.16.0.2\16`.
4. Configura la máquina **router** para que haga SNAT y permita que que las máquinas conectadas a esta red tengan acceso al exterior.
5. Configura el nuevo ámbito en el servidor dhcp con las siguientes características.
	* Rango de direcciones: `172.16.0.3` - `172.22.255.254`.
	* Máscara de red: `255.255.0.0`
	* Duración de la concesión: 1 hora
	* Puerta de enlace: `172.16.0.1`
	* Servidor DNS: `172.22.0.1`
6. Para comprobar que funciona el nuevo ámbito, utiliza el script para crear el **otro_cliente** con un volumen de 6G y conectada a la **red_intra2**.

{% capture notice-text %}
## Entrega

1. Contenido del ficheros de configuración que has modificado en el servidor DHCP.
2. Una vez creado el **otro_cliente**, pruebas de funcionamiento del direccionamiento que ha tomado y de que tiene acceso al exterior.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



