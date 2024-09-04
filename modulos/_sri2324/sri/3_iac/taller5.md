---
title: "Taller 5: Vagrant + Ansible"
---

## ¿Qué vas a aprender en este taller?

* Configuración de ansible para automatizar la configuración de máquinas vagrant.

## Recursos para realizar el taller

### Acceder por ssh a una máquina vagrant sin usar el comando `vagrant ssh`.

Como se explicó anteriormente, el comando `vagrant ssh` realiza una conexión ssh utilizando la red de mantenimiento que siempre es la que corresponde a la interfaz `eth0`. Pero, ¿puedo hacer una conexión directamente usando el comando `ssh`? La respuesta es sí, pero debemos saber algunos datos:

* Suponemos que queremos acceder a una máquina que hemos llamado `nodo1`.
* ¿Cuál es la IP de la máquina a la que quiero acceder? Podemos averiguarlo accediendo a la máquina o desde el host ejecutando `vagrant ssh nodo1 -c "hostname -I"`
* ¿Cómo se llama el usuario con el que vamos a acceder? Todas las máquinas vagrant tienen un usuario sin privilegio llamado `vagrant`.
* ¿Dónde se encuentra la clave privada que corresponde a la clave pública que se ha introducido en la máquina? Si nos situamos en el directorio donde está el `Vagranfile`, se encuentra en `.vagrant/machines/nodo1/libvirt/private_key`.

Por lo tanto:

```
$ vagrant ssh nodo1 -c "hostname -I"
192.168.121.166

$ ssh -i .vagrant/machines/nodo1/libvirt/private_key  vagrant@192.168.121.166
```

Podríamos usar la IP de eth0, o cualquier otra IP accesible de otra interfaz de la máquina.

## ¿Qué tienes que hacer?

1. Utilizando el escenario que puedes obtener en el directorio **Taller5** del repositorio [taller_ansible_vagrant](https://github.com/josedom24/taller_ansible_vagrant), crea el escenario con vagrant.

2. Tenemos una sola máquina, accede a ella y averigua la IP que ha tomado la interfaz de red.

3. Si tuviéramos que acceder por ssh a dicha máquina utilizaríamos el usuario `vagrant` y necesitaríamos la clave privada que corresponde a la clave pública que se ha inyectado en la máquina al crearse. La clave privada la podemos encontrar en el directorio donde tenemos el fichero `Vagrantfile`, en el directorio `.vagrant/machines/default/libvirt/private_key`. El directorio se llama `default` porque tenemos una única máquina, si el escenario tuviera más de una máquina habría un directorio con el nombre de cada máquina.

2. Ya tenemos las credenciales para acceder a la máquina. Ahora vamos a estudiar el **inventario** del playbook de ansible que encontramos en el directorio `ansible`. Vamos a estudiar el fichero `hosts`:

	* `ansible_ssh_host`: Dirección IP del equipo, debes poner la que ha tomado tu máquina.
	* `ansible_ssh_user`: `vagrant`
	* `ansible_ssh_private_key_file`: `../.vagrant/machines/default/libvirt/private_key`

3. Comprueba que tienes conectividad con la máquina.
5. Ejecuta el playbook que instala un servidor web en la máquina.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Entrega una captura de pantalla donde se vea que se ha finalizado la ejecución del playbook.
2. Captura de pantalla donde se vea el acceso desde el navegador al servidor web.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


