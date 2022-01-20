---
title: "Práctica: Contenedores LXC"
---

## Ejercicio 1

Crea la siguiente infraestructura con contenedores LXC:

1. Un contenedor LXC llamado `router`. Este contenedor se creará a partir de la plantilla Debian Bullseye. Este contenedor tendrá dos interfaces de red: la primera conectada a una red pública (bridge `br0`). Por esta interfaz el contenedor tendrá acceso a internet. Además estará conectada la bridge de un red muy aislada que crearás con `virsh` y tendrá como dirección IP la 10.0.0.1.
2. Un contenedor LXC llamado `servidor_web`. Este contenedor se creará a partir de la plantilla Ubuntu Focal Fossa. Este contenedor estará conectado a la red muy aislada con la dirección IP 10.0.0.2.

Los dos contenedores deben tener las siguientes características:

* Se deben auto arrancar cuando se encienda el host.
* Deben tener una limitación de memoria RAM de 512M. El contenedor `router` debe usar dos CPU y el contenedor `servidor_web` una CPU.

Servicios que debemos instalar en los contenedores (si quieres lo puedes hacer con ansible):

* Los dos contenedores deben estar configurados para acceder por SSH con el usuario `root` con tu clave privada. El usuario `root` no tiene contraseña.
* El contenedor `router` debe hacer SNAT para que el contenedor `servidor_web` tenga acceso a internet.
* El contenedor `servidor_web` tiene un servidor web (apache2 o nginx). El servidor web sirve los ficheros del directorio `/var/www/pagina`. En este directorio se monta el directorio `/opt/pagina` del host y es donde tendrá los ficheros de la página web.
* El contenedor `router` debe hacer DNAT para que podamos acceder a la página web alojada en el contenedor `servidor_web`.


~~## Ejercicio 2~~

~~Explica los pasos necesarios para configurar Vagrant para que utilice LXC como proveedor y una vez configurado el sistema crea un `Vagrantfile` que construya un escenario similar al del ejercicio anterior. No hace falta configurarlo.~~

{% capture notice-text %}
Describe los pasos principales para realizar cada uno de los ejercicios, centrándonos en los aspectos relacionados con LXC y mostrando pruebas de funcionamiento donde se vean cada uno de los aspectos que se piden.

Estos ejercicios lo corregiremos en clase y deberás mostrar al profesor su funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>