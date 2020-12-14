---
title: "Implementación de un cortafuegos perimetral con iptables"
permalink: /seguridadgs/u03/perimetral_iptables.html
---

Vamos a realizar los primeros pasos para implementar un cortafuegos que protege la red interna.

## Esquema de red

Vamos a utilizar dos máquinas en openstack, que vamos a crear con la receta heat: [escenario2.yaml](escenario2.yaml). La receta heat ha deshabilitado el cortafuego que nos ofrece openstack (todos los puertos de todos los protocolos están abiertos). Una máquina (que tiene asignada una IP flotante) hará de cortafuegos, y la otra será una máquina de la red interna 192.168.100.0/24.

Puedes usar también las máquinas de tu escenario OpenStack (dulcinea y los clientes de la red interna).

## Limpieza de las reglas previas

    iptables -F
    iptables -t nat -F
    iptables -Z
    iptables -t nat -Z

## Vamos a permitir ssh al cortafuegos

Cómo estamos conectado a la máquina por ssh, vamos a permitir la conexión ssh desde la red 172.22.0.0/16, antes de cambiar las políticas por defecto a DROP, para no perder la conexión:

**Mejora: Vamos a limitar el estado de las conexiones.**

    iptables -A INPUT -s 172.22.0.0/16 -p tcp -m tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -d 172.22.0.0/16 -p tcp -m tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

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

**Mejora: Vamos a limitar el estado de las conexiones.**

    iptables -A OUTPUT -p tcp -o eth1 -d 192.168.100.0/24 --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A INPUT -p tcp -i eth1 -s 192.168.100.0/24 --sport 22 -m state --state ESTABLISHED -j ACCEPT

## Permitimos tráfico para la interfaz loopback

    iptables -A INPUT -i lo -p icmp -j ACCEPT
    iptables -A OUTPUT -o lo -p icmp -j ACCEPT

## Peticiones y respuestas protocolo ICMP

**Mejora: sólo permitimos el ping**

    iptables -A OUTPUT -o eth0 -p icmp -m icmp --icmp-type echo-reply -j ACCEPT
    iptables -A INPUT -i eth0 -p icmp -m icmp --icmp-type echo-request -j ACCEPT

Si queremos permitir también los ping a la LAN:

    iptables -A OUTPUT -o eth1 -p icmp -m icmp --icmp-type echo-request -j ACCEPT
    iptables -A INPUT -i eth1 -p icmp -m icmp --icmp-type echo-reply -j ACCEPT

## Reglas forward

Aunque ya hemos configurado SNAT, como hemos puesto la política por defecto FORWARD a DROP, los equipos de la LAN están incomunicadas, ya que no permitimos que ningún paquete pase por el cortafuego. Por lo tanto ahora tenemos que ir configurando los pares de reglas (forward en ambas direcciones) para ir permitiendo distintos protocolos, puertos,... a la LAN.

## Permitir hacer ping desde la LAN

Actualmente estamos permitiendo que desde la LAN se pueda hacer ping al cortafuego, pero para que la LAN haga ping al exterior los paquetes ICMP tiene que estar permitidos que pasen por el cortafuego:

**Mejora: sólo permitimos el ping**

    iptables -A FORWARD -o eth0 -i eth1 -s 192.168.100.0/24 -p icmp -m icmp --icmp-type echo-request -j ACCEPT
    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p icmp -m icmp --icmp-type echo-reply -j ACCEPT
    
## Consultas y respuestas DNS desde la LAN

**Mejora: Vamos a limitar el estado de las conexiones.**

    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p udp --dport 53 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p udp --sport 53 -m state --state ESTABLISHED -j ACCEPT


## Permitimos la navegación web desde la LAN

**Mejora: Vamos a limitar el estado de las conexiones.**<br/>
**Mejora: Uso de multiport para indicar los dos puertos**<br/>
**Mejora: Dejas navegar sólo unas horas**<br/>



    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp -m multiport --dport 80,443 -m state --state NEW,ESTABLISHED -m time \
    --timestart 12:00 --timestop 12:30 -j ACCEPT
    iptables -A FORWARD -o eth1 -i eth0 -d 192.168.100.0/24 -p tcp -m multiport --sport 80,443 -m state --state ESTABLISHED -m time \
    --timestart 12:00 --timestop 12:30 -j ACCEPT
    
Podemos comprobar que está haciendo resolución DNS y navegación web desde la máquina de la LAN instalando un servidor web apache2.


## Permitimos el acceso a nuestro servidor web de la LAN desde el exterior

**Mejora: Vamos a limitar el estado de las conexiones.**<br/>
**Mejora: Limitamos el número de conexiones al servidor web**<br/>

En un primer momento tenemos que permitir que la consulta pase por el cortafuegos:

    iptables -A FORWARD -i eth0 -o eth1 -d 192.168.100.0/24 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -m connlimit --connlimit-above 15 -j REJECT --reject-with tcp-reset
    iptables -A FORWARD -i eth1 -o eth0 -s 192.168.100.0/24 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT

Y necesitamos configurar una regla DNAT:

    iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.200.10

