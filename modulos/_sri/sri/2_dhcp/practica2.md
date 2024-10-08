---
title: "Práctica (2 / 3): Virtualización en Linux y servidor DHCP (Parte 2)"
---

## Instalación del servidor Web

Para ello sigue los siguientes pasos:

1. Instala el servidor `apache2` en el contenedor **servidorWeb**.
2. Instala el servidor `nfs` en la máquina **servidorNAS**.
3. Crea en el **servidorNAS** un directorio `/srv/web` con un fichero `index.html` y compártelo con el contenedor **servidorWeb**.
3. Monta ese directorio en el directorio `/var/www/html` del contenedor **servidorWeb**.
4. Configura en el **router** una regla de DNAT para que podamos acceder al servidor Web desde el exterior. (**La configuración debe ser persistente.**)

{% capture notice-text %}
## Entrega

1. Configuración y demostración que has exportado un directorio desde el **servidorNAS**.
2. Demostración donde se vea que has montado el directorio indicado en el contenedor.
3. Demostración donde se vea el acceso al servidor web desde el exterior.
4. Cambia el contenido del fichero `index.html` en el **servidorNAS** y accede a la página para comprobar que se han producido los cambios,
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Script de creación de clientes

Escribe un script llamado `crear_cliente.sh` que va a automatizar la tarea de crear máquinas clientes a partir de la plantilla **plantilla-cliente**. Este script creará una nueva máquina con el nombre que le indiquemos, con un volumen con el tamaño que le indiquemos y conectada a la red que le indiquemos. El script cambiará el hostname de la máquina para poner el mismo nombre que hemos indicado como nombre de la máquina virtual. Se deben añadir las claves ssh necesarias para el acceso por ssh. La nueva máquina se debe iniciar. Utiliza la utilidad `virt-customize` para configurar la máquina antes de crearla.

Por lo tanto el script recibe los siguientes argumentos en la línea de comandos:

* **Nombre**: nombre de la nueva máquina y hostname.
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

1. Entrega el script que has diseñado.
2. Una comprobación de que el tamaño del disco (y de su sistema de fichero) de la máquina creada es el adecuado.
3. Una vez creado el **cliente2**, pruebas de funcionamiento del direccionamiento que ha tomado y de que tiene acceso al exterior.
4. Un acceso por ssh a **cliente2** donde se demuestre que no se pide contraseña.
5. Instala un cliente web de texto en **cliente2** y accede a la página web de **servidorWeb**.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>