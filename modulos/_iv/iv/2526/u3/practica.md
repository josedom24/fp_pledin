---
title: "Práctica: Escenario en OpenStack"
---


Para nombrar las máquinas se van a utilizar los siguientes nombres: **ra, anubis, isis, horus**. Estos nombres pertenecen a la mitología griega.

Además el dominio será un subdominio de la forma `tunombre.gonzalonazareno.org`. De esta forma tendremos:

* Máquina 1: Instancia en OpenStack con **Debian 13** que se llama `ra.tunombre.gonzalonazareno.org`.
* Máquina 2: Instancia en OpenStack con **Rocky Linux 10** que se llama `anubis.tunombre.gonzalonazareno.org`.
* Máquina 3: Contenedor LXC con **Ubuntu 24.04** que se llama `isis.tunombre.gonzalonazareno.org`.
* Máquina 4: Contenedor LXC con **Ubuntu 24.04** que se llama `horus.tunombre.gonzalonazareno.org`.

Todas las operaciones que realices sobre recursos de OpenStack lo tienes que hacer usando OSC.

## Escenario

![os](img/os.drawio.png)


## Creación de la infraestructura de red

* Crea un nuevo router llamado **RouterProyecto** conectado a la red externa.
* Crea una red NAT que se llame **Red_Proyecto**, con las siguientes características:
	* Está conectada al router que has creado en el punto anterior.
	* Direccionamiento: `10.0.200.0/24`
	* Con DHCP y DNS (`172.22.0.1`).
	* La puerta de enlace de los dispositivos conectados a esta red será el `10.0.200.1`.
* Crea una red interna que se llame **Red_Intra**, con las siguientes características:
	* Direccionamiento: `172.16.0.0/16`
	* **Sin DHCP**.
	* **Deshabilitamos la puerta de enlace.** Esto es para que *cloud-init* no configure la puerta de enlace en las instancias conectada a esta red.
	* La puerta de enlace de los dispositivos conectados a esta red será el `172.16.0.1`.

{% capture notice-text %}
## Entrega

1. Las instrucciones para crear el router y las redes.
2. Una captura de pantalla donde se vea la Topología de Red en Horizon que has creado.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Instalación de las instancias de OpenStack

### Configuración de las instancias

Las dos instancias que vamos a crear se van a configurar con `cloud-init` de la siguiente manera:

* Deben actualizar los paquetes de la distribución de la instancia.
* El dominio utilizado será del tipo `tunombre.gonzalonazareno.org`. Por lo tanto en la configuración con `cloud-init` habrá que indicar el hostname y el FQDN.
* Se crearán dos usuarios: 
	* Un usuario sin privilegios. Se puede llamar como quieras (pero el nombre será el mismo en todas las máquinas) y accederás a las máquinas usando tu clave ssh privada.
	* Un usuario `profesor`, que puede utilizar `sudo` sin contraseña. Copia mi clave pública en las instancias para que puedan acceder con el usuario `profesor`.
* Cambia la contraseña al usuario `root`.

### Creación de las instancias

#### máquina1 (ra)

* Crea una instancia sobre un volumen de 15Gb (el volumen se crea durante la creación de la instancia), usando una imagen de **Debian 13**. Elige el sabor `vol.medium`. Y configúrala con `cloud-init` como se ha indicado anteriormente.
* Está instancia estará conectada a las dos redes. Recuerda que en la red **Red_Intra** debe tomar la dirección `172.16.0.1` (puerta de enlace las máquinas conectadas a esta red). Asigna a la instancia una IP flotante.
* Deshabilita la seguridad de los puertos en las dos interfaces de red para que funcione de manera adecuada el NAT.
* Configura de forma permanente la regla SNAT para que las máquinas de la **Red_Intra** tengan acceso a internet.

#### maquina2 (anubis)

* Crea un volumen de 15Gb con la imagen **Rocky Linux 10**.
* Crea la instancia a partir de este volumen. Elige el sabor `vol.medium`. Y configúrala con `cloud-init` como se ha indicado anteriormente.
* Esta instancia estará conectada a la red **Red_Intra**, a la dirección `172.16.0.200`.
* Deshabilita la seguridad de los puertos en la interfaz de red para que funcione de manera adecuada el NAT.
* Comprueba que tiene acceso a internet.

{% capture notice-text %}
## Entrega

1. Las instrucciones para crear y configurar las máquinas.
2. Los ficheros `cloud-config.yaml` que has usado para crear las instancias.
3. La IP flotante de la **máquina1 (ra)**.
4. Una captura de pantalla donde se vea la Topología de Red en Horizon que has creado.
5. Prueba de funcionamiento de qué los FQDN están bien configurados en las dos máquinas.
6. Prueba de funcionamiento de que se pueden acceder a todas las máquinas por ssh.
7. Prueba de funcionamiento de que las máquinas tienen acceso a internet accediendo a un nombre de dominio, para comprobar que funciona el DNS.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Instalación de los contenedores

En **máquina1 (ra)** vamos a crear dos contenedores en un red interna, para ello:

* Vamos a crear una red virtual **Red_DMZ**, para ello crea en **máquina1 (ra)** un linux bridge llamado `br-dmz` y asigna una dirección IP estática `192.168.0.1`. Esta será la IP de **máquina1 (ra)** conectada a este switch virtual y será la puerta de enlace de los contenedores. Tienes que tener en cuenta que la imagen de Debian 13 de OpenStack tiene **netplan** para la configuración de las redes, por lo tanto tienes que configurar el bridge usando el fichero de configuración de netplan. **No olvides poner la mtu a 1442 al crear el bridge.**
* Instala LXC y crea dos contenedores con la distribución **Ubuntu 24.04**. Estos contenedores serán la **máquina3 (isis)** y la **máquina4 (horus)**.
* Configura de forma permanente la regla SNAT para que los contenedores tengan acceso a internet.
* Conecta los contenedores al bridge `br-dmz` y configúralo de forma estática con las siguientes direcciones: **máquina3 (isis)** la `192.168.0.2` y **máquina4 (horus)** la `192.168.0.3`. Su DNS será el `172.22.0.1`.
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
