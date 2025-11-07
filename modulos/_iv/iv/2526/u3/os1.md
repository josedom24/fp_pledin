---
title: "Instalación y uso básico de OpenStack client (OSC)"
---

Además de usar **Horizon** para interactuar con OpenStack, podemos usar un cliente de línea de comandos: *Openstack Client (OSC)*.

## Instalación de OpenStack Client

Para instalar el cliente de OpenStack podemos usar un entorno virtual de python3:

```
$ python3 -m venv os
(os)$ source os/bin/activate
(os)$ pip install python-openstackclient
```

O realizar la instalación con `apt`:

```
apt install python3-openstackclient
```

Ahora necesitamos el fichero de credenciales, para que nos podamos autentificar a nuestro proyecto de OpenStack, para descargar el fichero desde horizon escogemos la siguiente opción: **Tu usuario - Fichero OpenStack RC.**

Para cargar las variables de entorno que se definen en ese fichero podemos ejecutar:

```
$ source Proyecto\ de\ josedom-openrc.sh
Please enter your OpenStack Password for project Proyecto de josedom as user josedom: 
```

Y nos pide la contraseña de nuestro usuario que se guardará en otra variable de entorno. Una vez introducida la contraseña podremos usar el comando `openstack` para gestionar los recursos de nuestro proyecto. 

* Para ver tus máquinas: `openstack server list`.
* Para ver tus claves ssh: `openstack keypair list`.
* Para ver las imágenes: `opentack images list`.
* Para ver las redes: `openstack network list`.
* Para ver los sabores: `openstack flver list`.
* Para ver las reglas del grupo de seguridad **default**: `openstack security group rule list default`.

También podemos crear nuevos recursos con el CLI, por ejemplo para abrir el puerto 22 y poder acceder a las instancias por SSH, podemos ejecutar:

```
$ openstack security group rule create --protocol tcp --remote-ip 0.0.0.0/0 --dst-port 22 default
```

{% capture notice-text %}
## Ejercicio

1. Instala el cliente de OpenStack y configúralo con tu fichero de credenciales que debes bajar de Horizon. Los siguientes pasos los debes hacer con el cliente de OpenStack, puedes entrar en Horizon para comprobar si se ha realizado de forma correcta la acción realizada.
2. Muestra los distintos recursos como has estudiado en los apuntes.
3. Abre el puerto 443 en el grupo de seguridad `deafult`.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


