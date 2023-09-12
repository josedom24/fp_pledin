---
title: "Taller 4: Gestión del almacenamiento en OpenStack"
---

## ¿Qué vas a aprender en este taller?

* Gestión de volúmenes.
* Asociación de una volumen a una instancia.
* Redimensión de volúmenes.
* Creación de instancia sobre volúmenes.

## Recursos para realizar este taller

* Capítulo 4 del [Curso OpenStack](https://github.com/josedom24/curso_openstack_ies).

## ¿Qué tienes que hacer?

Los siguientes pasos los debes hacer con el cliente de OpenStack, puedes entrar en Horizon para comprobar si se ha realizado de forma correcta la acción realizada.

1. Crea un volumen de 1Gb, y asócialo a una instancia de las que tienes creadas.
2. Accede a la instancia, formatea el volumen y móntalo en un directorio.
3. Redimensiona el volumen a 2Gb. Accede a la instancia y redimensiona el sistema de fichero.
4. Crea un volumen arrancable a partir de una imagen.
5. Crea una instancia cuyo disco sea el volumen creado anteriormente. Recuerda elegir un sabor de tipo **vol.XXXX**. Asóciale una IP flotante.
6. Accede a la instancia e instala nginx. Comprueba con un navegador web que está funcionando.
7. Elimina la instancia. Vuelve a crear una instancia con el mismo volumen y vuelve a comprobar que el servidor web sigue instalado. No se ha perdido la información.
{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Comandos OSC para crear y asociar el volumen.
2. Antes de redimensionar el volumen, la salida del comando `df -h` en la instancia donde hemos asociado el volumen.
3. Comando OSC para redimensionar el volumen. La salida del comando `df -h` en la instancia donde hemos asociado el volumen, después de redimensionar el sistema de ficheros.
5. Comando OSC para crear un volumen arrancable con una imagen.
6. Comando OSC para crear una instancia cuyo disco es el volumen.
7. Comprobación de que el servidor web sigue funcionando después de eliminar la instancia y volver a crear una instancia con el mismo volumen.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
