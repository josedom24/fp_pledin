---
title: "Clase 1: Introducción a Linux Containers (LXC)"
---

## ¿Qué vas a aprender en esta clase?

* Conocer el concepto de contenedores. Y la diferencia entre contenedores de sistemas y de aplicaciones.
* Crear y gestionar contenedores LXC.

## Recursos

* [Introducción a Linux Containers (LXC)](lxc.html)


## ¿Qué tienes que hacer?

1. Instala LXC.
2. Crea un contenedor LXC con la última distribución de Ubuntu. Lista los contenedores. Inicia el contenedor y comprueba la dirección IP que ha tomado. ¿Tiene conectividad al exterior?. Sal del contenedor y ejecuta un `apt update` en el contenedor sin estar conectado a él.
3. Modifica la configuración del contenedor, y limita el uso de memoria a 512M y que use una sola CPU.
4. Comprueba que se ha creado un bridge llamado `lxcbr0` donde está conectado el contenedor. Cambia la configuración del contenedor para desconectar de este bridge y conectarlo a la red `red-nat` que creaste en el taller anterior. Toma de nuevo direccionamiento y comprueba de nuevo la dirección IP, y que sigue teniendo conectividad al exterior.
