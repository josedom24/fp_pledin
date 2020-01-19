---
title: "Configuración de openVPN basada en SSL/TLS"
permalink: /seguridadgs/u04/ejercicio2.html
---

## Acceso remoto

![remoto](img/remoto.jpg)

En este primer escenario vamos a establecer una VPN de acceso remoto. La autenticación será con
TLS utilizando certificados X.509 y la asignación de direcciones dinámica. Ejemplo de direccionamiento:

* Direcciones del servidor OpenVPN:
    * eth0: IP Pública, 80.80.80.1/24
    * eth1: Red Local interna, 192.168.1.1/24
    * Dirección virtual: 10.0.0.1/24
* Direcciones del cliente remoto:
    * IP Pública: 80.80.80.2/24
    * Dirección virtual: una de la red 10.0.0.0/24 que le asignará el servidor OpenVPN

Fichero de configuración del servidor: `/etc/openvpn/office.com`:

    #Dispositivo de túnel
    dev tun
        
    #Direcciones IP virtuales
    server 10.0.0.0 255.255.255.0 
    
    #subred local
    push "route 192.168.1.0 255.255.255.0"
    
    # Rol de servidor
    tls-server

    #Parámetros Diffie-Hellman
    dh /etc/openvpn/dh1024.pem

    #Certificado de la CA
    ca /etc/openvpn/ca.crt
    
    #Certificado local
    cert /etc/openvpn/server.crt

    #Clave privada local
    key /etc/openvpn/server.key
    
    #Activar la compresión LZO
    comp-lzo

    #Detectar caídas de la conexión
    keepalive 10 60

    #Nivel de información
    verb 3

En el servidor OpenVPN hay que activar el enrutamiento y copiar en el directorio `/etc/openvpn` los archivos `dh1024.pem`, `ca.crt`, `server.crt` y `server.key`.
En los clientes que quieran conectarse por acceso remoto a la VPN habrá que copiar el certificado
digital y la clave privada del usuario, así como el certificado de la CA a su propio directorio
`/etc/openvpn`.

Configuración del cliente: `/etc/openvpn/user1.conf`:

    #Dispositivo de túnel
    dev tun

    #Direcciones remota
    remote 80.80.80.1

    #Aceptar directivas del extremo remoto
    pull

    #Rol de cliente
    tls-client

    #Certificado de la CA
    ca /etc/openvpn/ca.crt

    #Certificado local
    cert /etc/openvpn/client1.crt

    #Clave privada local
    key /etc/openvpn/client1.key

    #Activar la compresión LZO
    comp-lzo

    #Detectar caídas de la conexión
    keepalive 10 60

    #Nivel de información
    verb 3

## Site to site

![site](img/site.jpg)

En este segundo escenario se va a establecer una VPN de sitio a sitio. La autenticación será basada en TLS utilizando certificados X.509. Ejemplo de direccionamiento:


* Las direcciones del servidor OpenVPN de la oficina central son:
    * eth0: IP Pública, 80.80.80.1/24
    * eth1: Red Local interna, 192.168.1.1/24
    * Dirección virtual: 10.0.0.1/24
* Las direcciones del servidor OpenVPN de la oficina remota son:
    * eth0: IP Pública, 80.80.80.2/24
    * eth1: Red Local interna, 192.168.2.1/24
    * Dirección virtual: 10.0.0.2/24

Los ficheros de configuración son similares a los del ejercicio anterior.

En este caso hay que activar el servicio de enrutamiento en ambos servidores y copiar el fichero de Diffie-Hellman, la clave privada y el certificado digital de cada servidor, así como el certificado de la CA, al directorio `/etc/openvpn` de cada equipo.