---
title: "Ejercicio 2: Creación de máquinas virtuales con virt-manager"
---

## ¿Qué vas a aprender en este ejercicio?

* A crear máquinas virtuales usando `virt-manager`.
* Gestionar las máquinas virtuales usando `virt-manager`.
* Ver los detalles de la definición de una máquina virtual usando `virt-manager`.
* A crear máquinas virtuales con el sistema operativo Windows y dispositivos paravirtualizados.

## Recursos para realizar este ejercicio

* Capítulo 4 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## ¿Qué tienes que hacer?

1. Instala `virt-manager`.
2. Crea una máquina virtual Linux con la herramienta `virt-mamager`, con las siguientes características:
	* Nombre: **linux_tu_nombre**.
	* Tamaño de disco: 15 Gb.
	* Memoria: 2 Gb
	* Número de CPUs: 2
	* No es necesario entorno gráfico.
3. Accede a la máquina creada en el taller anterior con `virt-manager`.
4. Instala un servidor ssh en la máquina virtual (si no lo tiene instalado por defecto) y accede a la máquina usando ssh.
5. Accede a la pestaña **Repaso** en la vista detalle de la máquina. Accede a la definición XML de la maquina.
6. Comprueba las características de la máquina: memoria, CPUs, discos, interfaces de red,...
7. Crea una máquina virtual con el sistema operativo Windows, asegurándote configurar el disco y la interfaz de red con el controlador VirtIO.

