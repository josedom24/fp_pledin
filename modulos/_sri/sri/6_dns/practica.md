---
title: Servidores Web, Base de Datos y DNS en nuestros escenario de OpenStack
---

## Servidor DNS

Vamos a instalar un servidor dns en **thor** que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor dns con autoridad sobre un subdominio de nuestro dominio principal `gonzalonazareno.org`, que se llamará `tu_nombre.gonzalonazareno.org`.

Hay que tener en cuenta los siguientes aspectos:

1. El servidor DNS se va a configurar en un principio de la siguiente manera:

    * El servidor DNS se llama `thor.tu_nombre.gonzalonazareno.org` y va a ser el servidor con autoridad para la zona `tu_nombre.gonzalonazareno.org`.
    * El servidor debe resolver el nombre de todas las máquinas.
    * El servidor debe resolver los distintos servicios (virtualhost, servidor de base de datos, servidor ldap, ...).
    * Vamos a usar vistas en bind9, para que el nombre de `odin` se corresponda con una ip distinta según desde se realice la consulta. Determina cuantas vistas vamos a crear y que nombres se van a crear en cada vista.
    * Vamos a crear las zonas de resolución inversas correspondientes al direccionamiento de las redes privadas (`192.168.0.0/24` y `172.16.0.0/16`).

    Realiza pruebas desde los otros equipos para comprobar que tu servidor DNS funciona de manera adecuada en las redes locales.
3. Será necesario realizar consultas desde el exterior (ya que vamos a hacer una delegación del subdominio). Determina la regla DNAT en `odin` para que podamos hacer consultas DNS desde el exterior. Prueba hacer una consulta desde tu anfitrión usando la IP flotante de `odin`.
4. Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal `dns.gonzalonazareno.org`. Ahora prueba, desde tu anfitrión a resolver tus nombres pero preguntando al DNS de nuestra red (`172.22.0.1`).
5. Quewremos que el servidor DNS que has configurado también pueda resolver los nombres de los dNS de los compañeros. Para ello lo vamos a configurar como **servidor DNS forward/caché**, de tal manera que las consultas la realizará sobre nuestro servidor `172.22.0.1`. Para configurar el servidor como forwarder hay que modificar el parámetro en el fichero `named.conf.options`.
6. Por último vamos a configurar los equipos de nuestro escenario para que usen por defecto el servidor DNS de thor, para ello: modifica la configuración de la subred en las redes que estás usando en tu escenario de OpenStack para que el servidor DNS principal sea **thor** (`192.168.0.2`) y modifica la configuración de los contenedores para que usen **thor** como DNS.
7. Para que podamos usar los nombres cortos (por ejemplo, para hacer `ssh hela`) es necesario que el parámetro `search` del fichero `/etc/resolv.conf` este configurado con nuestro nombre de dominio. Como no podemos enviar esa información con el servidor DHCP de las redes de OpenStack, vamos a configurar los clientes DHCP de las máquinas para que autoconfiguren el parámetro `search`, para ello modifica el fichero `//etc/dhcp/dhclient.conf` y añade la siguiente línea:

        prepend domain-search "tu_nombre.gonzalonazareno.org";

    Toma de nuevo configuración dinámica y comprueba en el fichero `/etc/resolv.conf` si se ha configurado de manera adecuada el parámetro `search`.

## Servidor Web

En `hela` vamos a instalar un servidor web apache. Configura el servidor para que sea capaz de ejecutar código php. Investiga las reglas DNAT de cortafuegos que tienes que configurar en `odin` para, cuando accedemos a la IP flotante/pública se acceda al servidor web. Instala un CMS WordPress que debe ser accesible con el nombre `www.tu_nombre.gonzalonazareno.org`.

## Servidor de base de datos

En `loki` vamos a instalar un servidor de base de datos mariadb (`bd.tu_nombre.gonzalonazareno.org`). A este servidor de base de datos se debe permitir el acceso desde todas las máquinas del escenario.

{% capture notice-text %}
## Entrega

1. Entrega la configuración DNS de cada máquina.
2. Entrega la definición de las vistas y de las zonas.
3. Entrega el resultado de las siguientes consultas desde una máquina interna a nuestra red y otro externo:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `odin`.
    * Una resolución de www.
    * Una resolución de bd.
    * Un resolución inversa de IP fija en cada una de las redes. (Esta consulta sólo funcionará desde una máquina interna).
4. Desde `odin` entrega la salida de `ping hela` y `ssh loki` para comprobar que funcionan los nombres cortos en la resolución.
5. Entrega el contenido del fichero de configuración de Wordpress (`wp-config.php`) para comprobar el nombre de la base de datos que has configurado.
6. Entrega una captura de pantalla accediendo a `www.tunombre.gonzalonazareno.org` donde se vea el Wordpress.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
