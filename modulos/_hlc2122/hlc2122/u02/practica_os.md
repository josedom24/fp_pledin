---
title: Instalación y configuración inicial de los servidores OpenStack
---
En esta tarea se va a crear el escenario de trabajo que se va a usar durante todo el curso, que va a constar inicialmente de 4 instancias con nombres relacionados .......

Imágen

Pasos a realizar:

1. Creación de la red interna:
    * Nombre: "red interna de <nombre de usuario>"
    * Direccionamiento: 10.0.1.0/24
    * DHCP y DNS (192.168.202.2)
2. Creación de la red DMZ:
    * Nombre: "red DMZ de <nombre de usuario>"
    * Direccionamiento: 10.0.2.0/24
    * DHCP y DNS (192.168.202.2)
3. Creación de las instancias
    * Máquina 1
        * Debian 11 sobre volumen de 10GB con sabor m1.mini
        * Accesible directamente a través de la red externa y con una IP flotante
        * Conectada a la red interna y a la red DMZ, de la que será la puerta de enlace
    * Máquina 2
        * Ubuntu 20.04 sobre volumen de 10GB con sabor m1.mini
        * Conectada a la red interna
        * Dirección: 10.0.1.101
        * Accesible indirectamente a través de dulcinea
    * Máquina 3:
        * Debian 11 sobre volumen de 10GB con sabor m1.mini
        * Conectada a la red interna
        * Dirección: 10.0.1.102
        * Accesible indirectamente a través de dulcinea
    * Máquina 4:
        * Rocky 8 sobre volumen de 10GB con sabor m1.mini
        * Conectada a la red DMZ
        * Dirección: 10.0.2.200
        * Accesible indirectamente a través de dulcinea
4. Configuración de NAT en Dulcinea (Es necesario deshabilitar la seguridad en todos los puertos de dulcinea) Para que todas las máquinas tengan acceso a internet.
5. Definición de contraseña en todas las instancias (para poder modificarla desde consola en caso necesario).
6. Configuración de ssh en tu cliente para acceder a todas las instancias.
7. Creación del usuario `profesor` en todas las instancias. Usuario que puede utilizar `sudo` sin contraseña.
8. Copia de las claves públicas de todos los profesores en las instancias para que puedan acceder con el usuario `profesor`.
9. Realiza una actualización completa de todos los servidores.
10. Nombrar de forma adecuada: FQDN todas las máquinas. Hacerlo con el `cloud-init` y un fichero `cloud-config.yaml`.
10. Hasta que no esté configurado el servidor DNS, incluye resolución estática en las cuatro instancias tanto usando nombre completo como hostname.
    
