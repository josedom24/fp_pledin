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

{% capture notice-text %}
## Entrega

Seguimos trabajando con el contenedor del ejercicio anterior.

1. Conecta el contenedor a la red `default` de libvirt y comprueba el direccionamiento, y que puedes hacerle ping desde una máquina virtual conectada a la misma red.
2. Crea otro contenedor con otro sistema operativo y conéctalo a `br0`. Comprueba el direccionamiento y que puedes hacerle ping desde el host.
3. Conecta los dos contenedores a un red muy aislada, sin desconectarlos de las redes en las que están conectados. Configura sus interfaces de red y prueba su conectividad por la nueva red.
4. Crea en el host el directorio `/opt/web`, crea el fichero `index.html` y monta este directorio en el directorio `/srv/www` del contenedor.
5. Instala apache2 en el contenedor y comprueba que se puede acceder a la página web.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>