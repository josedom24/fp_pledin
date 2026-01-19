---
title: "Proyecto 2 - Escenario OpenStack"
---

## Objetivos del proyecto

* Realizar cambios a la infraestructura del escenario en OpenStack que themos montado.


## Entorno de trabajo

Partimos del escenario que hemos montado en la práctica:

* [Practica: Escenario en OpenStack](https://fp.josedomingo.org/iv/2526/u3/practica.html)

Y el servicio DNS que hemos configurado en la práctica:

* [Práctica: Protocolo DNS](https://fp.josedomingo.org/sri/2526/u5/practica.html)

## Desarrollo del proyecto

El proyecto consiste en tomar como base dicho escenario y configuración y realizar un proyecto donde podéis introducir distintas modificaciones.

Para realiza dichas modificaciones, hay que tener en cuenta los siguientes puntos:

* Si instala un servicio que tenga acceso desde el exterior estará en una de las máquinas de la **Red DMZ**.
* Todos los servicios internos estarán en máquinas de la **Red Interna**.
* Teniendo en cuenta lo anterior, el servidor web tendrás que cambiarlo de máquina.
* Puedes crear alguna otra máquina o contenedor, pero debe estar motivado. De principio con las máquinas que tenemos es suficiente.
* Todos los servicios que necesiten nombres se tendrán que dar de alta en el servidor DNS (**no usar direcciones IP**).
* Si el servicio es accesible desde el exterior habrá que dar de alta el nombre en la **vista externa**.
* Puedes añadir modificaciones sobre temas que hayas trabajado en los distintos módulos, pero también puedes aprovechar el proyecto para añadir modificaciones que impliquen temas que no se hayan estudiado en clase.

## ¿Qué tienes que hacer?

1. Se deberá realizar un cambio en el proyecto cada dos semanas.
2. Existirá una tarea en Redmine, donde se indicará la fecha de la siguiente modificación.
3. De cada modificación, se realizará un resumen del trabajo realizado en Redmine, y se describirá con detalle en la **Memoria del Proyecto** que se realizará en un pdf.
4. De cada modificación se entregará un vídeo explicando el trabajo que se ha realizado y comprobando el funcionamiento.
5. Cada entrega se calificará con una nota, la media de las notas de entrega junto a la nota de la presentación final servirán para calcular la nota final del proyecto.

