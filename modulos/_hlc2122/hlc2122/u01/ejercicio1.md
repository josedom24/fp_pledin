---
title: "Ejercicio 1: Uso básico de virsh"
---

Realiza las siguientes tareas con `virsh` conectándote a `qemu:///system`:

1. Crea una red virtual de tipo NAT llamada `red_interna` y direccionamiento `10.0.1.0/24`. esta rede debe ser de tipo `virtio`.
2. En lugar de instalar una máquina virtual, vamos a utilizar una imagen ya creada, haciendo algunas modificaciones previamente.
    * Descarga el fichero [debiantest.qcow2](https://cloud.josedomingo.org/index.php/s/9Jw3gNpekCzcBNj) que se corresponde con una imagen de Debian Bullseyes en formato qcow2 que podemos usar en libvirt/KVM.
    * Averigua los pasos que tienes que realizar para montar la imagen usando el módulo del kérnel `nbd` y la herramienta `qemu-nbd`.
    * Define una contraseña para el usuario `usuario` y/o copia tu clave pública ssh en el lugar adecuado.
    * Cambia el fichero `/etc/hostname` y `/etc/hosts` para cambiar el nombre de la máquina. El nombre debe ser del tipo *maquina_tu_nombre*.
    * Desmonta la imagen qcow2.
    * Crea un volumen en el "pool" por defecto que contenga esa imagen.
    * Define el dominio con el fichero XML de ejemplo conectada a la red que has creado.
    * Arranca el dominio y accede a la máquina virtual por ssh (tendrás que averiguar la dirección IP que tiene).

{% capture notice-text %}
## Entrega...

* El contenido del fichero xml y la instrucción para crear la red interna.
* Instrucciones para crear el volumen que contenga la imagen.
* Instrucción que permite montar la imagen para su modificación.
* Fichero XML de la definición del dominio.
* Pantallazo donde se vea un acceso a la máquina por ssh.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



