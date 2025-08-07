---
title: "Clase 1: Instalación y creación de una máquina virtual con virt-manager"
---

## ¿Qué vas a aprender en esta clase?

* A realizar la instalación del sistema de virtualización QEMU/libivrt/virt-manager.
* A trabajar con la conexión privilegiada a libvirt.
* A instalar una máquina virtual Linux con virt-manager.

## Teoría

*  La **virtualización** utiliza el software para imitar las características del hardware y crear un sistema informático virtual.
* Tenemos distintos tipos de virtualización. Nosotros vamos a usar un **hipervisor** de tipo 1 usando virtualización completa o por hardware.
* **Hipervisor**: Software de virtualización.
* **Virtualización completa o por hardware**: el hipervisor emula completamente el hardware físico, permitiendo que los sistemas operativos invitados se ejecuten sin modificaciones, como si estuvieran en una máquina física real. El hipervisor utiliza extensiones de virtualización del procesador (como Intel VT-x o AMD-V) para mejorar el rendimiento y aislar los sistemas invitados, proporcionando acceso directo al hardware cuando es posible. Esto permite ejecutar múltiples sistemas operativos independientes en el mismo hardware físico de manera eficiente y segura.
* **Virtualización con hipervisores de tipo 1 (bare-metal)**: En este caso, el hipervisor se ejecuta directamente sobre el hardware físico del host, sin un sistema operativo subyacente. Para esto, la CPU debe contar con extensiones de virtualización, como **Intel VT-x** o **AMD-V**. Este enfoque ofrece un **rendimiento cercano al de una máquina física**.  
    * **Ejemplos:** VMware ESXi, Microsoft Hyper-V, Xen, KVM (aunque se ejecuta dentro de Linux, convierte el kernel en un hipervisor).  
* **Virtualización con hipervisores de tipo 2 (hosteados)**: Aquí, el hipervisor se ejecuta sobre un sistema operativo anfitrión, que gestiona el acceso al hardware. Este enfoque introduce una capa adicional que **reduce el rendimiento en comparación con los hipervisores de tipo 1**.  
    * **Ejemplos:** VMware Workstation, VirtualBox, Parallels Desktop, VMware Player.  

 


* Capítulo 2 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)


## ¿Qué tienes que hacer?

1. Realiza la instalación de QEMU/libvirt.
2. Configura tu usuario sin privilegios para que puedas hacer conexiones privilegiadas sin usar el usuario `root`. Para probarlo: Ejecuta el comando `list` de `virsh` realizando una conexión privilegiada con tu usuario sin privilegios (no uses el `root`).

