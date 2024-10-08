---
title: "Utilización de OpenStack"
---

## Contenido

1. Introducción a OpenStack
* [Presentación: Introducción al Cloud Computing](http://iesgn.github.io/emergya/curso/u1/presentacion)
* [Presentación: Introducción a OpenStack](http://iesgn.github.io/emergya/curso/u1/presentacion_openstack)
2. Uso básico de OpenStack desde Horizon
    * **Glance**
        * [Administración de imágenes](http://iesgn.github.io/emergya/curso/u3/imagenes)
    * **Nova**
        * [Conceptos previos](http://iesgn.github.io/emergya/curso/u3/conceptos_previos)
        * [Trabajo con claves ssh](http://iesgn.github.io/emergya/curso/u3/claves_ssh)
        * [Creación de instancias a partir de una imagen](http://iesgn.github.io/emergya/curso/u3/instancias1)
        * [Operaciones sobre la instancia](http://iesgn.github.io/emergya/curso/u3/operaciones)
        * [Instantaneas de instancias](http://iesgn.github.io/emergya/curso/u3/instantaneas)
        * [Redimensión y reconstrucción de instancias](http://iesgn.github.io/emergya/curso/u3/redimension)
    * **Cinder**
        * [Conceptos previos de volúmenes](http://iesgn.github.io/emergya/curso/u4/conceptos_previos)
        * [Creación de volúmenes, asociación a instancias](http://iesgn.github.io/emergya/curso/u4/volumen)
        * [Operaciones sobre volúmenes](http://iesgn.github.io/emergya/curso/u4/operaciones)
        * [Creación de instancia ejecutadas sobre volúmenes](http://iesgn.github.io/emergya/curso/u4/instancias_volumen)
        * [VÍDEO: Crear una instancia desde volumen](https://youtu.be/4rgZM06BSrI)
    * **Neutron**
        * [Introducción a la virtualización de redes](http://iesgn.github.io/emergya/curso/u5/intro)
        * [Conceptos previos de neutron](http://iesgn.github.io/emergya/curso/u5/conceptos_previos)
        * [Gestión de redes con horizon](http://iesgn.github.io/emergya/curso/u5/neutron)
        * [Puertos de red](http://iesgn.github.io/emergya/curso/u5/puertos)
        * [Eliminación de la infraestructura de red creada](http://iesgn.github.io/emergya/curso/u5/borrar)
3. Uso básico de Openstack desde la línea de comandos
    * [VÍDEO: openstackclient. Instalación y uso básico](https://youtu.be/qjvWtvgo8FU)
    * [VÍDEO: Deshabilitar seguridad de un puerto](https://youtu.be/jqfILWzHrS0)
    * [Gestión de imágenes con OpenStack client (OSC)](osc_glance.html)
    * [Gestión de instancia con OpenStack client (OSC)](osc_nova.html)
    * [Gestión de volúmenes con OpenStack client (OSC)](osc_cinder.html)
    * [Gestión de redes con OpenStack client (OSC)](osc_neutron.html)
4. Metadatos y cloud-init
    * [cloud-init](https://raw.githubusercontent.com/albertomolina/beamer-focus/main/cloud-init.pdf)
    * [VÍDEO: OpenStack. Uso del servicio de metadatos](https://youtu.be/8xLF28rKNI0)
    * [VÍDEO: cloud-init](https://youtu.be/YIhlg_cGrYQ)
    * [VÍDEO: Utilización de cloud-init. Ejemplo](https://youtu.be/eWbAg4fenVo)
    * [Ejemplo de cloud-config.yml](cloud-config.yml)

## Ejercicios

* [Ejercicio 1: Primeros pasos para el uso de OpenStack. Configuración del cliente VPN.](ejercicio1.html)
* [Ejercicio 2: Infraestructura de red router-nat desde horizon](ejercicio2.html)
* [Ejercicio 3: Infraestructura de red router-nat desde OSC](ejercicio3.html)

## Práctica
* [Práctica: Instalación y configuración inicial de los servidores OpenStack](practica_os.html)
* [Práctica: Instalación y configuración inicial de los servidores KVM/Libvirt](practica_kvm.html)


## Enlaces de interes

* [OpenStack](https://www.openstack.org/)
