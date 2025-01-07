---
title: "Ejercicio 1: Resolución de nombres de dominios en sistemas Linux"
---

## ¿Qué vas a aprender en este ejercicio?

* Los distintos mecanismos que podemos usar en una distribución Linux para resolver nombres.
* Las distintas utilidades para realizar resoluciones de nombres.

## ¿Qué tienes que hacer?

1. Crea una máquina virtual con Vagrant usando el box `debian/bookworm64`. Realiza las siguientes tareas:
	* Instala la herramienta `dig` (paquete `dnsutils`).
	* Comprueba el servidor DNS que está utilizando el sistema. ¿Qué fichero tienes que comprobar?
	* ¿Qué mecanismos de resolución están configurado y en qué orden se van consultar?- ¿Qué fichero tienes que comprobar? ¿Qué base de datos nos interesa dentro de ese fichero?
	* Añade la siguiente resolución estática: `www.example.org` es la dirección IP 192.168.1.100. ¿En qué fichero has configurado está resolución?
	* Utiliza la herramienta `dig` para hacer una resolución de `www.example.org` para ello ejecuta:
		```
		dig www.example.org
		```
	Fíjate en la respuesta: `ANSWER SECTION`. ¿Por qué no ha salido la dirección que has puesto en la resolución estática?.
	¿Qué servidor DNs ha respondido?. Fíjate en la penúltima línea que empieza por `;; SERVER`.
	* Utiliza el comando que te permite realizar consultas usando el sistema NSS. ¿Qué dirección nos ofrece?. ¿Por qué?
	* Quita la resolución estática y vuelve a ejecutar el comando anterior. ¿Qué dirección nos ofrece? ¿Por qué?
	* En nuestra máquina vagrant se ha generado un fichero `/etc/resolv.conf` al crearse con el servidor DNS ofrecido por DHCP. Normalmente los sistemas tienen instalado un demonio que se encarga de actualizar este fichero. Instala el paquete `resolvconf`, y comprueba de nuevo el fichero `/etc/resolv.conf` (ahora te pone un comentario indicando que no edites el fichero que es generado por el demonio). Si no tiene un DNS configurado, reinicia la red para que `resolvconf` haga su trabajo. Vuelve a comprobar el contenido del fichero.

2. Vamos a trabajar con Multicast DNS. Realiza las siguientes tareas:
	* Instala `avahi` (paquetes `avahi-daemon avahi-utils`) en tu máquina virtual y en tu anfitriona.
	* Comprueba la nueva configuración de mecanismos de resolución y su orden en el fichero `/etc/nsswitch.conf`.
	* Utiliza la utilidad `getent ahosts` para realizar una resolución desde tu máquina virtual del nombre de tu anfitriona. Recuerda que el nombre será `nombre_host.local`.
	* Utiliza la herramienta `ping` para comprobar que hay conectividad desde la anfitriona a la máquina virtual usando su nombre multicast DNS.

3. systemd-resolved. Realiza las siguientes tareas:
	* en esta máquina no está instalado `systemd-resolved`, instálalo con `apt` y comprueba que está funcionando con `systemctl status`.
	* Accede al fichero `/etc/nsswitch.conf` y comprueba los nuevos mecanismos de resolución.
	* Accede al fichero `/etc/resolv.conf`. ¿Qué configuración DNS se ha configurado? (archivo "stub", DNS del sistema, o ha mantenido el `resolv.conf`). Comprueba que el nuevo `/etc/resolv.conf` es un enlace simbólico?. ¿Qué es el servidor DNS 127.0.0.53?
	* Usa el comando de `resolvectl` para que te muestre la configuración de resolución actual.
	* Añade de nuevo la resolución estática del ejercicio anterior, y usando `resolvectl` realiza una consulta a `ẁww.example.org`.
	* Vamos a comprobar la resolución del nombre local (mecanismo `myhostname`): con `resolvectl` realiza una consulta al nombre del equipo. También lo puedes hacer al `nombre_del_equipo.local`. Este nombre no es necesario que este en en `/etc/hosts`.
	* Ahora ejecuta la opción correspondiente al comando `resolvectl` para mostrar el servidor DNS que estamos utilizando.
	* Quita la resolución estática y usando `resolvectl` realiza una consulta a `ẁww.example.org`.
	* Prueba a realizar una resolución con el comando `getenv`. ¿Puedes seguir utilizando este comando? ¿Por qué?. Razona tu respuesta.
	* Prueba a hacer una consulta con `dig`. ¿Puedes seguir utilizando este comando? ¿Por qué?. Razona tu respuesta.