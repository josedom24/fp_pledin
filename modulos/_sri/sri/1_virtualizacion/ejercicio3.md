---
title: "Ejercicio 3: Creación de máquinas virtuales desde la línea de comandos"
---

## ¿Qué vas a aprender en este taller?

* A crear máquinas virtuales usando `virt-install`.
* A acceder a las máquinas virtuales usando `virt-view`.
* A gestionar el ciclo de vida de las máquinas virtuales.
* A comprobar las características de las máquinas virtuales creadas.

## Recursos para realizar este taller

* Capítulo 3 del [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)

## Duración

* 2 horas

## ¿Qué tienes que hacer?

1. Crea una máquina virtual Linux con la herramienta `virt-install`, con las siguientes características:
	* Nombre: **linux_tu_nombre**.
	* Tamaño de disco: 15 Gb.
	* Memoria: 2 Gb
	* Número de CPUs: 2
	* No es necesario entorno gráfico.
2. Una vez creada accede a ella usando la herramienta `virt-viewer`.
3. Comprueba la dirección IP que ha tomado, el tamaño del disco y de la memoria.
4. Con `virsh`: lista las máquinas, para la máquina que has creado, vuelve a ejecutarla, reinicia la máquina,...
5. Con `virsh` muestra la definición XML de la máquina y fíjate en los elementos de la definición que se comentan en el apartado [Definición XML de una máquina virtual](https://github.com/josedom24/curso_virtualizacion_linux/blob/main/modulo3/xml.md).
6. Con `virsh` modifica el nombre de la máquina, el número de CPU y el tamaño de la memoria.

