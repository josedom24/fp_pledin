---
title: "Dispositivos virtualizados. virtio"
---

Virtio ofrece los denominados dispositivos paravirtualizados para
procesos de E/S, que permiten el acceso privilegiado a recursos del
anfitrión. Los dispositivos virtio más habituales son utilizados para
dispositivos de bloque, interfaces de red, *memory balloning* y
generadores de números aleatorios.

La inclusión de dispositivos virtio permite que el sistema de
virtualización KVM compita en rendimiento con sistemas
paravirtualizados.

Es necesario que el kérnel del sistema operativo del huésped incluya
soporte para estos dispositivos paravirtualizados, en el caso del
kérnel linux este soporte se realiza a través de los siguientes
componentes:

```
CONFIG_BLK_MQ_VIRTIO
CONFIG_VIRTIO_VSOCKETS
CONFIG_VIRTIO_VSOCKETS_COMMON
CONFIG_NET_9P_VIRTIO
CONFIG_VIRTIO_BLK
CONFIG_SCSI_VIRTIO
CONFIG_VIRTIO_NET
CONFIG_VIRTIO_CONSOLE
CONFIG_HW_RANDOM_VIRTIO
CONFIG_DRM_VIRTIO_GPU
CONFIG_VIRTIO
CONFIG_VIRTIO_MENU
CONFIG_VIRTIO_PCI
CONFIG_VIRTIO_PCI_LEGACY
CONFIG_VIRTIO_PMEM
CONFIG_VIRTIO_BALLOON
CONFIG_VIRTIO_MEM
CONFIG_VIRTIO_INPUT
CONFIG_VIRTIO_MMIO
CONFIG_VIRTIO_MMIO_CMDLINE_DEVICES
CONFIG_RPMSG_VIRTIO
CONFIG_VIRTIO_FS
CONFIG_CRYPTO_DEV_VIRTIO
```

## Dispositivos virtio en Windows

El sistema operativo Windows no ofrece soporte nativo para
dispositivos virtio (a pesar de que Microsoft ama a Linux), pero el
proyecto [virtio-win](https://github.com/virtio-win) que es ajeno a
Microsoft, proporciona controladores para estos dispositivos.

El proyecto Fedora ofrece una ISO-9660 para poder agregar estos
controladores de forma sencilla durante la instalación de una máquina
virtual con Windows: [virtion-win.iso](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso).

## Dispositivos de bloque

En lugar de emular un dispositivo IDE o SATA, es mucho más eficiente
utilizar un dispositivo virtio para los dispositivos de bloque, por
ejemplo:

```
<disk type='file' device='disk'>
  <driver name='qemu' type='qcow2'/>
  <source file='disco.qcow2'/>
  <target dev='vda' bus='virtio'/>
</disk>
```

## Dispositivos de red

Es posible emular dispositivos de red Fast-Ethernet (`rtl-8139`) o
Gigabit Ethernet (`e1000`), pero se consigue un rendimiento mucho
mayor con dispositivos de red virtio:

```
<interface type='bridge'>
  <mac address='52:54:00:5c:55:0b'/>
  <source bridge='br0'/>
  <model type='virtio'/>
</interface>
```

## *Memory Balloning*

Mecanismo que permite modificar al vuelo la cantidad de memoria que se
proporciona a la máquina virtual en función de las necesidades del
anfitrión (como si de un globo que se infla o desinfla se tratase, de
ahí el nombre).

El dispositivo no necesita parámetros adicionales:

```
<memballoon model='virtio'>
</memballoon>
```

## Dispositivo de números aleatorios

La generación de números aleatorios es un problema habitual en las
máquinas virtuales, que carecen inicialmente de dispositivos físicos
que los proporcionen, como sí tienen las máquinas físicas a través de
dispositivos específicos en sus placas base. Virtio permite la
utilización de estos dispositivos en máquinass virtuales, evitando
tener que usar otras soluciones de software menos eficaces.

`rng:` Random Number Generator

```
<rng model='virtio'>
  <backend model='random'>/dev/urandom</backend>
</rng>
```