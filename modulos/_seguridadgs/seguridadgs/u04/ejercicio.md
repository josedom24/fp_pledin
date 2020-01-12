---
title: "Configuración de openVPN de acceso remoto con clave estática compartida"
permalink: /seguridadgs/u04/ejercicio.html
---

En esta ejercicio vamos a ver cómo configurar una VPN de acceso remoto utilizando OpenVPN, una solución libre que permite implementar VPNs basadas en SSL/TLS.

## El escenario

Supongamos que la siguiente figura representa la red de nuestra organización, en la que tenemos varios servidores internos que no queremos que sean accesibles desde Internet y, por tanto, están protegidos por el cortafuegos de nuestra red local. Sin embargo, uno de nuestros empleados debe conectarse de forma remota y utilizar estos servicios, pero debido a su criticidad no queremos abrir un puerto y que se conecte directamente desde Internet. En este escenario podemos utilizar OpenVPN para configurar de forma sencilla una VPN de acceso remoto, de forma que todo el tráfico entre el cliente y el servidor VPN viaje cifrado a través de Internet.

![vpn](img/vpn.jpg)

* Red interna: 192.168.100.0/24
* IP Cliente: 172.22.200.214
* IP Servidor: 172.22.200.249
* IP VPN punto a punto: 10.0.0.1 - 10.0.0.2

## Configuración

Para este ejemplo, tanto el router que conecta nuestra red local con Internet como el cliente VPN son máquinas Debian, pero la configuración es prácticamente igual con otros SOs.

Tras instalar OpenVPN en ambas máquinas (puede compilarse el código fuente o instalarse el paquete del repositorio), hay que decidir cómo se va a realizar la autenticación de los extremos y el cifrado. La forma más sencilla de configuración es usar una clave compartida (pre-shared key), mientras que el uso de certificados ofrece una solución más robusta. Veamos primero cómo sería la configuración usando la clave compartida. 

### Generación del secreto compartido

Lo primero que hay que hacer es generar la clave compartida en el servidor:

    $ openvpn --genkey --secret static.key

Esta orden nos genera la clave que utilizaremos para autenticar a los extremos de la VPN.

### Configuración del servidor

Tras mover el secreto compartido al directorio `/etc/openvpn` crearemos el archivo `/etc/openvpn/server.conf` con el siguiente contenido:

    dev tun
    ifconfig 10.0.0.1 10.0.0.2
    secret secreto.key

Las direcciones `10.0.0.1` y `10.0.0.2` de la directiva ifconfig son las que se asignarán a las interfaces virtuales del túnel: `10.0.0.1` para el servidor y `10.0.0.2` para el cliente. Puedes elegir las direcciones que prefieras, pero no deben coincidir con el direccionamiento utilizado en la red local.

A diferencia de otras soluciones más complejas como OpenSwan, basada en IPSec, OpenVPN utiliza un único puerto para todo el tráfico, por lo que la gestión en el cortafuegos es más sencilla. El puerto por defecto es el 1194 UDP (puede cambiarse este puerto con la directiva port nuevo_puerto), por lo que basta con que abrir este puerto para poder establecer la VPN.

### Configuración del cliente

Tras copiar a la máquina cliente el secreto compartido y moverlo al directorio `/etc/openvpn`, crearemos el archivo `/etc/openvpn/client.conf` con el siguiente contenido:

    remote 172.22.200.249
    dev tun
    ifconfig 10.0.0.2 10.0.0.1
    route 192.168.2.0 255.255.255.0 10.0.0.1
    secret secreto.key

La dirección `80.154.67.89` de la directiva remote es la IP pública del servidor VPN, necesaria para que el cliente comience el establecimiento de la VPN. La directiva `route` añadirá a la tabla de encaminamiento del cliente una entrada que permita acceder a los recursos de la red local remota (en el ejemplo `192.168.2.0/24`). Con esta configuración, el único tráfico que será cifrado y que se enviará a través del túnel, será el que vaya dirigido a la red local remota, mientras que el resto del tráfico se enviará sin cifrar de forma tradicional.

### Establecimiento de la VPN

Para establecer la VPN hay que arrancar OpenVPN en ambos extremos:

    $ openvpn --config /etc/openvpn/server.conf    (En el servidor)
    $ openvpn --config /etc/openvpn/client.conf    (En el cliente)

Una vez establecida la VPN, se habrá creado una interfaz virtual de tipo túnel en ambas máquinas, que simulan un enlace PPP:

    $ ifconfig
    ...
    tun0      Link encap:UNSPEC  direcciónHW 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00 
              Direc. inet:10.0.0.2  P-t-P:10.0.0.1  Másc:255.255.255.255
              ACTIVO PUNTO A PUNTO FUNCIONANDO NOARP MULTICAST
    ...

Y en la tabla de encaminamiento veremos las nuevas entradas que permiten el tráfico con la máquina `10.0.0.1` (el servidor VPN) y con la red local remota (`192.168.2.0`):

    $ route -n
    Tabla de rutas IP del núcleo
    Destino         Pasarela        Genmask         Indic Métric Ref    Uso Interfaz
    10.0.0.1      0.0.0.0         255.255.255.255 UH    0      0        0 tun0
    192.168.2.0    10.0.0.1      255.255.255.0   UG    0      0        0 tun0
    192.168.1.0     0.0.0.0         255.255.255.0   U     1      0        0 eth1
    0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth1

A partir de este momento, el cliente ya podría utilizar los recursos de la red local remota de forma segura, ya que todo el tráfico iría cifrado a través del túnel.