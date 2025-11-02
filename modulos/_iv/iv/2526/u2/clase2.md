---
title: "Clase 2: Configuración de contenedores LXC"
---

## ¿Qué vas a aprender en esta clase?

* Configurar los contenedores LXC.
* Gestionar las redes a las que se conectan los contenedores.
* Añadir almacenamiento a los contenedores LXC.
* Tener una aproximación a la herramienta LXD.

## Recursos

* [Configuración de contenedores LXC](lxc2.html)

## Ejercicio

Vamos a realizar un ejercicio de Router/NAT con contenedores.

1. Crea un contenedor llamado **router** desde una plantilla de Debian 13. Configura su propiedad autostart.
2. Crea un contenedor llamado **servidorweb** desde una plantilla de Ubuntu 24.04. Configura su propiedad autostart.
3. Como hemos estudiado los contenedores lo podemos conectar a cualquier **Linux Bridge**. Podríamos crear redes con *libvirt* y conectarlos a los bridges de esas redes. Pero en esta ocasión, vamos a crear manualmente un bridge llamado `br-contenedores` (no lo hagas con `virsh` ya que se configura una reglas de cortafuego muy estrictas). Si conectamos los contenedores a ses bridge estarían conectados a una **red muy aislada**.
4. Conecta el contenedor **router** a **br0** y a **br-contenedores**. Configura las interfaces de red en el sistema operativo de forma adecuada.
5. Conecta el contenedor **servidorweb** a **br-contenedores**. Configura la interface de red en el sistema operativo de forma adecuada.
6. Configura el contenedor router para que haga de router y posibilite al contenedor **servidorweb** acceso a internet.
7. Instala en los contenedores el servidor SSH. Crea un usuario sin privilegios y configúralo para acceder con clave pública/privada. Accede por ssh al contenedor **servidorweb**.
8. Instala un servidor web en el contenedor **servidor web**.
9. Crea en el host el directorio `/opt/web`, crea el fichero `index.html` y monta este directorio en el directorio `/var/www/html` del contenedor.
10. Configura el contenedor **router** para acceder al servidor web desde el exterior. Comprueba el acceso y que si modificas el fichero `index.html` en el host se modificará directamente la página web,

{% capture notice-text %}
## Entrega

1. Direccionamiento y rutas de los dos contenedores.
2. Comprobación del acceso por SSH al contenedor **servidorweb**.
3. Captura de pantalla accediendo a la página web.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>