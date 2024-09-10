---
title: "Ejercicio 4: Creación de máquinas virtuales con virt-manager"
---

## ¿Qué vas a aprender en este ejercicio?

* A crear máquinas virtuales usando `virt-manager`.
* Gestionar las máquinas virtuales usando `virt-manager`.
* Ver los detalles de la definición de una máquina virtual usando `virt-manager`.
* A crear máquinas virtuales con el sistema operativo Windows y dispositivos paravirtualizados.

## Recursos para realizar este ejercicio

* Capítulo 4 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## Duración

* 2 horas

## ¿Qué tienes que hacer?

1. Instala `virt-manager`.
2. Accede a la máquina creada en el taller anterior con `virt-manager`.
3. Instala un servidor ssh en la máquina virtual (si no lo tiene instalado por defecto) y accede a la máquina usando ssh.
4. Accede a la pestaña **Repaso** en la vista detalle de la máquina. Accede a la definición XML de la maquina.
5. Comprueba las características de la máquina: memoria, CPUs, discos, interfaces de red,...
6. Crea una máquina virtual con el sistema operativo Windows, asegurándote configurar el disco y la interfaz de red con el controlador VirtIO.

