---
title: Servidores Web, Base de Datos y DNS en nuestros escenario de trabajo
---

## Servidor DNS

Vamos a instalar un servidor dns en **apolo** que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor dns con autoridad sobre un subdominio de nuestro dominio principal `gonzalonazareno.org`, que se llamará `tu_nombre.gonzalonazareno.org`. A partir de este momento no será necesario la resolución estática en los servidores.

1. Determina la regla DNAT en `zeus` para que podamos hacer consultas DNS desde el exterior.
2. Configura de forma adecuada todas las máquinas para que usen como servidor DNS a **apolo**.
3. Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal `papion-dns`.
4. El servidor DNS se va a configurar en un principio de la siguiente manera:

    * El servidor DNS se llama `apolo.tu_nombre.gonzalonazareno.org` y va a ser el servidor con autoridad para la zona `tu_nombre.gonzalonazareno.org`.
    * El servidor debe resolver el nombre de todas las máquinas.
    * El servidor debe resolver los distintos servicios (virtualhost, servidor de base de datos, servido ldap, ...).
    * Vamos a usar vistas en bind9, para que el nombre de `zeus` se corresponda con una ip distinta según desde se realice la consulta. Determina cuantas vistas vamos a crear.
    * Vamos a crear las zonas de resolución inversas correspondientes al direccionamiento de las redes privadas.

## Servidor Web

En `hera` (Rocky)(Servidor que está en la DMZ) vamos a instalar un servidor web apache. Configura el servidor para que sea capaz de ejecutar código php (para ello vamos a usar un servidor de aplicaciones php-fpm). Investiga la reglas DNAT de cortafuegos que tienes que configurar en `zeus` para, cuando accedemos a la IP flotante/pública se acceda al servidor web.

## Servidor de base de datos

En `ares` (Ubuntu) vamos a instalar un servidor de base de datos mariadb (`bd.tu_nombre.gonzalonazareno.org`). 


{% capture notice-text %}
## Entrega

1. Entrega la configuración DNS de cada máquina.
2. Entrega la definición de las vistas y de las zonas.
3. Entrega el resultado de las siguientes consultas desde un cliente interno a nuestra red y otro externo:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `seuz`.
    * Una resolución de www.
    * Una resolución de bd.
    * Un resolución inversa de IP fija en cada una de las redes. (Esta consulta sólo funcionará desde una máquina interna).

4. Entrega una captura de pantalla accediendo a `www.tunombre.gonzalonazareno.org/info.php` donde se vea la salida del fichero `info.php`.
5. Entrega una prueba de funcionamiento donde se vea como se realiza una conexión a la base de datos desde `hera`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>