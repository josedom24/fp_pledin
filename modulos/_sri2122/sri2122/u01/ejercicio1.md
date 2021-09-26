---
title: "Ejercicio 1: Playbook sencillo"
---

1. Prepara una máquina virtual en KVM que es la que vamos a configurar de forma automática con ansible.
2. Debes crear un playbook que realice las siguientes tareas de forma automática:
    * Crear un usuario en el servidor remoto que tenga tu nombre.
    * Descarga el fichero desde la url `https://wordpress.org/latest.zip`.
    * Descomprime ese fichero en el home del usuario creado anteriormente.
    * Instala el paquete mariadb.
    * Crea una base de datos que se llame *tunombre_wordpress*.
    * Crea un usuario que se llame *my_nombre* que tenga privilegios sobre la base de datos.
    * Clona el repositorio: `https://github.com/josedom24/ansible_ejemplos.git`en el home del usuario que hemos creado en el primer punto.

Para cada uno de estas tareas tienes que usar un módulo especifico de ansible.
Entrega la url del repositorio donde has guardado el playbook y también la salida de la ejecución del playbook.
