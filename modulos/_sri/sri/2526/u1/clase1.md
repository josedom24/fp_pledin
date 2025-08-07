---
title: "Clase 1: Instalación y creación de una máquina virtual con virt-manager"
---

## ¿Qué vas a aprender en esta clase?

* A realizar la instalación del sistema de virtualización KVM/QEMU; libivrt y virt-manager.
* A trabajar con la conexión privilegiada a libvirt.
* A instalar una máquina virtual Linux con virt-manager.

## Teoría

### Virtualización

*  La **virtualización** utiliza el software para imitar las características del hardware y crear un sistema informático virtual.
* Tenemos distintos tipos de virtualización. Nosotros vamos a usar un **hipervisor** de tipo 1 usando virtualización completa o por hardware.
* **Hipervisor**: Software de virtualización.
* **Virtualización completa o por hardware**: el hipervisor emula completamente el hardware físico, permitiendo que los sistemas operativos invitados se ejecuten sin modificaciones, como si estuvieran en una máquina física real. El hipervisor utiliza extensiones de virtualización del procesador (como Intel VT-x o AMD-V) para mejorar el rendimiento y aislar los sistemas invitados, proporcionando acceso directo al hardware cuando es posible. Esto permite ejecutar múltiples sistemas operativos independientes en el mismo hardware físico de manera eficiente y segura.
* **Virtualización con hipervisores de tipo 1 (bare-metal)**: En este caso, el hipervisor se ejecuta directamente sobre el hardware físico del host, sin un sistema operativo subyacente. Para esto, la CPU debe contar con extensiones de virtualización, como **Intel VT-x** o **AMD-V**. Este enfoque ofrece un **rendimiento cercano al de una máquina física**.  
    * **Ejemplos:** VMware ESXi, Microsoft Hyper-V, Xen, KVM (aunque se ejecuta dentro de Linux, convierte el kernel en un hipervisor).  
* **Virtualización con hipervisores de tipo 2 (hosteados)**: Aquí, el hipervisor se ejecuta sobre un sistema operativo anfitrión, que gestiona el acceso al hardware. Este enfoque introduce una capa adicional que **reduce el rendimiento en comparación con los hipervisores de tipo 1**.  
    * **Ejemplos:** VMware Workstation, VirtualBox, Parallels Desktop, VMware Player.

### QEMU/KVM, libvirt y virt-manager

* **QEMU** es un emulador genérico y de código abierto.

  * Permite ejecutar sistemas operativos de arquitecturas distintas (ej. ARM en x86\_64).
  * Puede usarse como solución de virtualización junto con **KVM**.
* **KVM (Kernel-based Virtual Machine)**:

  * Es un hipervisor de tipo 1 integrado en el kernel de Linux.
  * Requiere soporte de virtualización por hardware (Intel VT-x, AMD-V).
  * Se compone de:

    * `kvm.ko`: módulo principal del kernel.
    * `kvm-intel.ko` o `kvm-amd.ko`: módulos específicos por procesador.
* **QEMU + KVM**:

  * Permite ejecutar sistemas operativos sin modificar.
  * Ofrece un rendimiento cercano al nativo.
  * Cada máquina virtual dispone de hardware virtualizado: red, disco, gráficos, etc.

* **Dispositivos Paravirtualizados**: Al crear una VM, se definen dispositivos: RAM, CPU, disco, red, etc.
* **Por defecto**, los dispositivos son emulados por software.

  * Ejemplos: tarjeta de red Realtek 8139, disco con interfaz IDE.
  * Ventajas: alta compatibilidad con muchos sistemas operativos.
  * Desventajas:

    * Mayor uso de CPU.
    * Mayor latencia de E/S (peor rendimiento).
* **virtIO**: estándar de dispositivos paravirtualizados en KVM.

  * Diseñados para entornos virtualizados.
  * Mejoran rendimiento de red y almacenamiento.
  * Requieren soporte en el sistema operativo invitado.

    * **Linux**: compatibilidad nativa.
    * **Windows**: necesita instalación manual de controladores.


* **libvirt**: Es una **API de virtualización de código abierto**.
    * Proporciona una **interfaz unificada** para gestionar distintos hipervisores.
    * Incluye:
        * Un demonio: `libvirtd`.
        * Una API estable.
        * Herramientas para administración de máquinas virtuales.
    * Diseñada principalmente para hipervisores nativos de Linux: **KVM, LXC y Xen**.
    * También soporta otros hipervisores: **VMware ESXi, Microsoft Hyper-V**, etc.
    * Permite **abstraer** la complejidad de QEMU/KVM y otros hipervisores.
    * Tipos de conexiones:
        * **Conexión local no privilegiada a libvirt**: Esta conexión permite a un usuario sin privilegios gestionar máquinas virtuales en su propio entorno sin necesidad de permisos de root. En este modo los usuarios sin privilegios pueden gestionar máquinas virtuales, pero no tienen acceso a características avanzadas, por ejemplo la gestión de redes virtuales. URL de conexión: `qemu:///session`.
        * **Conexión local privilegiada a libvirt**: Este método permite a un usuario con permisos de superusuario administrar todas las máquinas virtuales del sistema. Es el modo más común en servidores o entornos de producción. URL de conexión: `qemu:///system`.
        * **Conexión remota a libvirt**: Este método permite administrar un hipervisor QEMU/KVM en otro equipo a través de la red. Se usa en entornos de gestión centralizada o administración remota. Se pueden usar varios protocolos para el acceso, pero el más común es SSH. URL de conexión: `qemu+ssh://<usuario>@<dirección  máquina remota>/system`.

* **virt-manager**: interfaz gráfica que accede a libvirt para crear y administrar VMs.


## Recursos

* Curso completo: [Introducción a la virtualización con KVM/libvirt usando virt-manager](https://github.com/josedom24/curso_kvm_ow/tree/main/curso1)
* En concreto los apartados:
  * Introducción a la virtualización con KVM/libvirt
  * Introducción a virt-manager
  * Creación de máquinas virtuales con virt-manager

## Ejercicio

1. Realiza la instalación de QEMU/KVM, libvirt y virt-manager. Apartado: [Instalación de virt-manager](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad02/clase2.md).
2. Siguiendo lo indicando en el apartado [Conexión local privilegiada a libvirt con virt-manager](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad02/clase3.md), comprueba que por defecto estamos usando **una conexión provilegiada a libviert**, y comprueba la red y el almacenamiento disponible. Estudia las características de la red *default* que tenemos a nuestra disposición.
3. Siguiendo el apartado [Creación de máquinas virtuales Linux](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase1.md) instala una máquina virtual con el sistema operativo Linux.
    * Si no tienes un fichero ISO para la instalación puedes probar [Creación de máquinas virtuales por red](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad07/clase2.md).
    * Una vez instalada la máquina comprueba las [Características de las máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase2.md).
    * Estudia las distintas operaciones para la [Gestión de máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase3.md).
    * Estudia los [Detalles de las máquinas virtuales](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase4.md).
    * Accede a la máquina virtual usando el protocolo SSH, tienes distintos métos de acceso en el apartado [Acceso a las máquinas virtuales desde el exterior](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad03/clase7.md).