---
title: "Ejercicio 2: Implementación de un cortafuego perimetral"
permalink: /seguridadgs/u03/ejercicio2.html
---

Vamos a realizar los primeros pasos para implementar un cortafuegos que protege la red interna.

## Esquema de red

Vamos a utilizar dos máquinas en openstack, que vamos a crear con la receta heat: [escenario2.yaml](escenario2.yaml). La receta heat ha deshabilitado el cortafuego que nos ofrece openstack (todos los puertos de todos los protocolos están abiertos). Una máquina (que tiene asignada una IP flotante) hará de cortafuegos, y la otra será una máquina de la red interna 192.168.100.0/24.

## Limpieza de las reglas previas

    iptables -F
    iptables -t nat -F
    iptables -Z
    iptables -t nat -Z

## Vamos a permitir ssh al cortafuegos

Cómo estamos conectado a la máquina por ssh, vamos a permitir la conexión ssh desde la red 172.22.0.0/16, antes de cambiar las políticas por defecto a DROP, para no perder la conexión:

    iptables -A INPUT -s 172.22.0.0/16 -p tcp -m tcp --dport 22 -j ACCEPT
    iptables -A OUTPUT -d 172.22.0.0/16 -p tcp -m tcp --sport 22 -j ACCEPT

## Política por defecto

    iptables -P INPUT DROP
    iptables -P OUTPUT DROP
    iptables -P FORWARD DROP

Comprobamos que el equipo no puede acceder a ningún servicio ni de Internet ni de la red local, ya que la política lo impide.

## Activar el bit de forward

El primer paso común es habilitar el bit de forward mediante la instrucción:

    echo 1 > /proc/sys/net/ipv4/ip_forward

Para habilitar el forward de forma permanente, habilitamos la línea `net.ipv4.ip_forward=1` del fichero `/etc/sysctl.conf` y ejecutando posteriormente `sysctl -p /etc/sysctl.conf`.

## SNAT

Hacemos SNAT para que los equipos de la LAN puedan acceder al exterior:

    iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o eth0 -j MASQUERADE

## Permitimos el ssh desde el cortafuego a la LAN

    iptables -A OUTPUT -p tcp -o eth1 -d 192.168.100.0/24 --dport 22 -j ACCEPT
    iptables -A INPUT -p tcp -i eth1 -s 192.168.100.0/24 --sport 22 -j ACCEPT

## Permitimos tráfico para la interfaz loopback

    iptables -A INPUT -i lo -p icmp -j ACCEPT
    iptables -A OUTPUT -o lo -p icmp -j ACCEPT

## Peticiones y respuestas protocolo ICMP

    iptables -A OUTPUT -o eth0 -p icmp -j ACCEPT
    iptables -A INPUT -i eth0 -p icmp -j ACCEPT

Si queremos permitir también los ping a la LAN:

    iptables -A OUTPUT -o eth1 -p icmp -j ACCEPT
    iptables -A INPUT -i eth1 -p icmp -j ACCEPT

## Reglas forward

Aunque ya hemos configurado SNAT, como hemos puesto la política por defecto FORWARD a DROP, los equipos de la LAN están incomunicadas, ya que no permitimos que ningún paquete pase por el cortafuego. Por lo tanto ahora tenemos que ir configurando los pares de reglas (forward en ambas direcciones) para ir permitiendo distintos protocolos, puertos,... a la LAN.

## Permitir hacer ping desde la LAN

Actualmente estamos permitiendo que desde la LAN se pueda hacer ping al cortafuego, pero para que la LAN haga ping al exterior los paquetes ICMP tiene que estar permitidos que pasen por el cortafuego:

    iptables -A FORWARD -o eth0 -i eth1 -s 192.168.100.0/24 -p icmp -j ACCEPT
    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p icmp -j ACCEPT
    
## Consultas y respuestas DNS desde la LAN

    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p udp --dport 53 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p udp --sport 53 -j ACCEPT


## Permitimos la navegación web desde la LAN

    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --dport 443 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p tcp --sport 443 -j ACCEPT

Podemos comprobar que está haciendo resolución DNS y navegación web desde la máquina de la LAN instalando un servidor web apache2.


## Permitimos el acceso a nuestro servidor web de la LAN desde el exterior

En un primer momento tenemos que permitir que la consulta pase por el cortafuegos:

    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --sport 80 -j ACCEPT

Y necesitamos configurar una regla DNAT:

    iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.200.10

## Configuración en un solo paso

Editamos un fichero y añadimos todas las reglas anteriores:

    # Limpiamos las tablas
    iptables -F
    iptables -t nat -F
    iptables -Z
    iptables -t nat -Z
    # Establecemos la política
    iptables -P INPUT DROP
    iptables -P OUTPUT DROP
    iptables -P FORWARD DROP

    # SNAT
    echo 1 > /proc/sys/net/ipv4/ip_forward
    iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o eth0 -j MASQUERADE

    # DNAT
    iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.200.10

    # Reglas INPUT/OUTPUT

    iptables -A OUTPUT -p tcp -o eth1 -d 192.168.100.0/24 --dport 22 -j ACCEPT
    iptables -A INPUT -p tcp -i eth1 -s 192.168.100.0/24 --sport 22 -j ACCEPT

    iptables -A INPUT -i lo -p icmp -j ACCEPT
    iptables -A OUTPUT -o lo -p icmp -j ACCEPT

    iptables -A OUTPUT -o eth0 -p icmp -j ACCEPT
    iptables -A INPUT -i eth0 -p icmp -j ACCEPT

    iptables -A OUTPUT -o eth1 -p icmp -j ACCEPT
    iptables -A INPUT -i eth1 -p icmp -j ACCEPT

    # Reglas FORWARD

    iptables -A FORWARD -o eth0 -i eth1 -s 192.168.100.0/24 -p icmp -j ACCEPT
    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p icmp -j ACCEPT

    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p udp --dport 53 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p udp --sport 53 -j ACCEPT

    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p tcp --sport 80 -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --dport 443 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p tcp --sport 443 -j ACCEPT

    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p tcp --dport 80 -j ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --sport 80 -j ACCEPT

{% capture notice-text %}
## Ejercicios

1. Permite realizar conexiones ssh desde los equipos de la LAN
2. Instala un servidor de correos en la máquina de la LAN. Permite el acceso desde el exterior y desde el cortafuego al servidor de correos. Para probarlo puedes ejecutar un `telnet` al puerto 25 tcp.
3. Permite poder hacer conexiones ssh desde exterior a la LAN
4. Modifica la regla anterior, para que al acceder desde el exterior por ssh tengamos que conectar al puerto 2222, aunque el servidor ssh este configurado para acceder por el puerto 22.
5. Permite hacer consultas DNS sólo al servidor `192.168.202.2`. Comprueba que no puedes hacer un `dig @1.1.1.1`.
6. ¿Tendría resolución de nombres y navegación web el cortafuego? ¿Sería necesario? ¿Tendrían que estar esas de reglas de forma constante en el cortafuego?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>