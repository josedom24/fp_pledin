---
title: "Ejercicio: Configuración de ansible"
permalink: /lmgs/u07/ejercicio2.html
---

Ansible es un software que nos permite la configuración automática de nuestra infraestructura. Las tareas que se van a ejecutar de forma automática en nuestros servidores se escriben en playbook que son ficheros escrito en YAML.

El fichero [ansible.yaml](https://github.com/josedom24/lmgs_doc/raw/master/unidades/u9/fich/ansible.yaml) es un playbook para instalar mysql en un servidor. Crea distintas funciones en python que nos devuelvan la siguiente información:

* Cuantas tareas se ejecutan en el playbook.
* La lista de los nombres de las distintas tareas.
* En la primera tarea se realiza la instalación de paquetes. Devuelve el nombre de los paquetes que se instalan.
* Devuelve la contraseña que se va a asignar al root de mysql.
* Devuelve si esta receta tiene handlers (manejadores para reiniciar los servicios).

