---
title: "Taller 5: Trabajando con contenedores LXC"
---

## ¿Qué vas a aprender en este taller?

* Conocer el concepto de contenedores. Y la diferencia entre contenedores de sistemas y de aplicaciones.
* Crear y gestionar contenedores LXC.
* Configurar los contenedores LXC.
* Gestionar las redes a las que se conectan los contenedores.
* Añadir almacenamiento a los contenedores LXC.
* Tener una aproximación a la herramienta LXD.

## Recursos para realizar este taller

* Capítulo 8 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## ¿Qué tienes que hacer?

1. Instala LXC.
2. Crea un contenedor LXC con la última distribución de Ubuntu. Lista los contenedores. Inicia el contenedor y comprueba la dirección IP que ha tomado. ¿Tiene conectividad al exterior?. Sal del contenedor y ejecuta un `apt update` en el contenedor sin estar conectado a él.
3. Modifica la configuración del contenedor, y limita el uso de memoria a 512M y que use una sola CPU.
4. Comprueba que se ha creado un bridge llamado `lxcbr0` donde está conectado el contenedor. Cambia la configuración del contenedor para desconectar de este bridge y conectarlo a la red `red-nat` que creaste en el taller anterior. Toma de nuevo direccionamiento y comprueba de nuevo la dirección IP, y que sigue teniendo conectividad al exterior.
5. Añade una nueva interfaz de red al contenedor y conéctala a la red `red-externa` que creaste en el taller anterior. Toma direccionamiento en esta nueva interfaz y comprueba que esta en el direccionamiento del instituto.
6. Crea en el host el directorio `/opt/web`, crea el fichero `index.html` y monta este directorio en el directorio `/srv/www` del contenedor.
7. (Optativo)(**Te recomiendo que lo hagas en una máquina virtual limpia**). Instala LXD y crea un contenedor y una máquina virtual.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. La salida del comando para listar el contenedor creado. Un pantallzo donde se vea la IP que ha tomado. La instrucción que permite ejecutar el comando `apt update` sin estar conectado a él.
2. Pantallazos para demostrar que has limitado el uso de memoria y CPU en el contenedor.
3. Después de conectar el contenedor a la red `red-nat`, comprobación de la IP que ha tomado y de que tiene conectividad al exterior.
4. Después de conectar el contenedor a la red `red-externa`, comprobación de la nueva IP que ha tomado.
5. Indica la configuración que has hecho para montar el directorio `/opt/web`. Lista el directorio `/srv/www` del contenedor para comprobar que se ha montado de forma correcta.
6. (Optativo). Lista el contenedor y la máquina virtual creadas con LXD.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
