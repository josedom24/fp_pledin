---
title: "Práctica (2 / 2): Escenario en OpenStack"
---

## Instalación de los contenedores

En **máquina1 (luffy)** vamos a crear dos contenedores en un red interna, para ello:

* Crea en **máquina1 (luffy)** un linux bridge llamado `br-intra` (no lo hagas con `virsh` ya que se configura una reglas de cortafuego muy estrictas) y asigna una dirección IP estática `192.168.0.1`. Esta será la IP de **máquina1 (luffy)** conectada a este switch virtual y será la puerta de enlace de los contenedores. Tienes que tener en cuenta que la imagen de Debian 12 Bookworm de OpenStack tiene **netplan** para la configuración de las redes, por lo tanto tienes que configurar el bridge usando el fichero de configuración de netplan, para ello te puede ser útil esta [página](https://fabianlee.org/2022/09/20/kvm-creating-a-bridged-network-with-netplan-on-ubuntu-22-04/). No olvides poner la mtu a 1442 al crear el bridge.
* Instala LXC y crea dos contenedores con la distribución **Ubuntu 22.04**. Estos contenedores serán la **máquina3 (nami)** y la **máquina4 (sanji)**.
* Configura de forma permanente la regla SNAT para que los contenedores tengan acceso a internet.
* Conecta los contenedores al bridge `br-intra` y configúralo de forma estática con las siguientes direcciones: **máquina3 (nami)** la `192.168.0.2` y **máquina4 (sanji)** la `192.168.0.3`. Su DNS será el `172.22.0.1`.
* Para que la red de OpenStack funcione de forma adecuada las imágenes que usamos tienen configurado la mtu (*Unidad máxima de transferencia*) a 1442 bytes. Tenemos que adecuar los contenedores a este tamaño de trama. Para ello introduce en la configuración de los contenedores la línea: `lxc.net.0.mtu = 1442`.
* Configura los contenedores para que se auto inicien al reiniciar la instancia. 
* Los contenedores tendrán características parecidas a las instancias anteriormente:
	* Debes actualizar los paquetes de la distribución instalada.
	* El dominio utilizado será del tipo `tunombre.gonzalonazareno.org`. Por lo tanto configura de manera adecuada el hostname y el FQDN.
	* Para acceder a los contenedores vamos a usar ssh.
	* Crea dos usuarios: 
		* Un usuario sin privilegios. Se puede llamar como quieras (el nombre de usuario que usaste en las instancias) y accederás a los contenedores usando tu clave ssh privada.
		* Un usuario `profesor`, que puede utilizar `sudo` sin contraseña. Copia de las claves públicas de todos los profesores en los contenedores para que puedan acceder con el usuario `profesor`.
	* Cambia la contraseña al usuario `root`.

{% capture notice-text %}
## Entrega

1. El fichero de configuración de uno de los contenedores.
2. La salida del comando `sudo lxc-ls -f`.
3. Prueba de funcionamiento de qué los FQDN están bien configurados en los dos contenedores.
4. Prueba de funcionamiento de que se pueden acceder a los contenedores por ssh.
5. Prueba de funcionamiento de que los contenedores tienen acceso a internet accediendo a un nombre de dominio, para comprobar que funciona el DNS.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Finalmente comprueba que todo el escenario está funcionando después de reiniciar la **máquina1 (luffy)**.
