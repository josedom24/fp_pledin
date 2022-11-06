---
title: "Creación de instancias desde OSC"
---

Realiza los siguientes pasos:

1. Instala el cliente de línea de comando de OpenStack cómo se muestra en [Instalación y uso básico de OpenStack client (OSC)](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo1/osc.md).
2. Descarga de Horizon tu fichero de credenciales, cargálo y ejecuta la instrucción `openstack server list` para visualizar tus instancias.
3. Vamos a crear una instancia y la vamos a configurar con [**cloud-init**](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/cloudinit.md), para ello crea un fichero `cloud-config.yaml` con el siguiente contenido:

	```yaml
	#cloud-config
	package_update: true
	package_upgrade: true
	preserve_hostname: false
	fqdn: test1.gonzalonazareno.org
	hostname: test1
	# Crear un usuario y añadir clave pública ssh
	users:
	  - name: jose
	    sudo: ALL=(ALL) NOPASSWD:ALL
	    shell: /bin/bash
	    passwd: asdasd
	
	    ssh_authorized_keys:
	      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmjoVIoZCx4QFXvljqozXGqxxlSvO7V2aizqyPgMfGqnyl0J9YXo6zrcWYwyWMnMdRdwYZgHqfiiFCUn2QDm6ZuzC4Lcx0K3ZwO2lgL4XaATykVLneHR1ib6RNroFcClN69cxWsdwQW6dpjpiBDXf8m6/qxVP3EHwUTsP8XaOV7WkcCAqfYAMvpWLISqYme6e+6ZGJUIPkDTxavu5JTagDLwY+py1WB53eoDWsG99gmvyit2O1Eo+jRWN+mgRHIxJTrFtLS6o4iWeshPZ6LvCZ/Pum12Oj4B4bjGSHzrKjHZgTwhVJ/LDq3v71/PP4zaI3gVB9ZalemSxqomgbTlnT
	chpasswd:
	  list: |
	    root:asdasd
	  expire: False
	 ```

	 Modifica el fichero e indica un nombre a la máquina, crea otro usuario y cambia las contraseñas. 

	 Este fichero actualizará la paquetería de la instancia, configurará el FQDN de la instancia, creará un nuevo usuario y cambiará la contraseña del usuario `root`.

4. Siguiendo el apartado [Gestión de instancia con OpenStack client (OSC)](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/osc_nova.md), visualiza con el OSC los flavors disponibles, imágenes disponibles, claves disponibles, reglas de cortafuegos,...
5. Crea una nueva instancia usando el comando que encontrarán en la sección [Configuración de instancias con cloud-init](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo1/osc.md).
6. Añade una IP flotante a la instancia para ello puedes usar los comandos que encuentras en [Gestión de instancia con OpenStack client (OSC)](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/osc_nova.md).
7. Accede por ssh (recuerda usar el usuario que has creado con cloud-init) a la instancia.

