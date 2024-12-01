---
title: "Taller 1: Trabajo con instancias en OpenStack"
---

## ¿Qué vas a aprender en este taller?

* Configurar el cliente de OpenStack.
* Gestionar imágenes de OpenStack.
* Crear instancias en OpenStack.

## Recursos para realizar este taller

* Capítulos 1,2 y 3 del [Curso OpenStack](https://github.com/josedom24/curso_openstack_ies).

## ¿Qué tienes que hacer?

1. Instala el cliente de OpenStack y configúralo con tu fichero de credenciales que debes bajar de Horizon. Los siguientes pasos los debes hacer con el cliente de OpenStack, puedes entrar en Horizon para comprobar si se ha realizado de forma correcta la acción realizada.
2. Muestra las claves públicas que tienes en tu proyecto OpenStack.
3. Muestra las reglas del grupo de seguridad *Default*.
4. Abre el puerto 443 en el grupo de seguridad *Default*.
5. CirrOS es una distribución mínima de Linux que fue diseñada para su uso como imagen de prueba en nubes como OpenStack. Sube a tu proyecto la imagen de CirrOS que puedes encontrar [aquí](https://download.cirros-cloud.net/0.6.2/cirros-0.6.2-x86_64-disk.img). Lista las imágenes a las que tienes acceso.
6. Lista los sabores que podemos usar para crear una instancia.
7. Crea una instancias Linux, con las siguientes características configuradas con *cloud-init*:
	* Al iniciarse se deben actualizar los paquetes.
	* Se debe instalar Apache2.
	* Se debe crear un usuario (con tu nombre) y contraseña.
	* Se debe configurar el fqdn a `maquina1.example.org`.
8. Muestra tus ips flotantes. Solicita una nueva y asígnala a la instancia.
9. Accede por ssh a la instancia que has creado.
10. Lista todas las instancias que tienes creada, y elimina la que has creado en el punto 7.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega comprobaciones de las instrucciones y sus salidas para cada uno de los puntos que tienes que hacer en el taller.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio voluntario

### Usar cloud-init con libvirt

Si tenemos una imagen cloud con *cloud-init* instalado, esta imagen se puede usar con distintos hipervisores, por ejemplo con KVM/libvirt. Siguiendo las instrucciones que encontrarás en el artículo [Run cloud-init locally with libvirt](https://cloudinit.readthedocs.io/en/latest/howto/launch_libvirt.html#launch-libvirt) crea una máquina virtual Debian 12 (Tendrás que bajar la imagen cloud de Debian 12) configurado con cloud-init con las mismas características que has configurado la instancia de OpenStack:

* Al iniciarse se deben actualizar los paquetes.
* Se debe instalar Apache2.
* Se debe crear un usuario (con tu nombre) y contraseña.
* Se debe configurar el fqdn a `maquina-cloud.example.org`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega un pequeño manual con las instrucciones y configuraciones que has realizado, y con las comprobaciones necesarias para comprobar que has realizado de forma correcta ele ejercicio.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>