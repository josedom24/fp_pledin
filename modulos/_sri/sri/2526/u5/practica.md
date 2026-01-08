---
title: "Práctica: Protocolo DNS"
---

## Instalación del servidor DNS

Vamos a instalar un servidor dns en **isis** que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor DNS con autoridad sobre un subdominio de nuestro dominio principal `gonzalonazareno.org`, que se llamará `tu_nombre.gonzalonazareno.org`.

Hay que tener en cuenta los siguientes aspectos:

1. El servidor DNS se va a configurar de la siguiente manera:
    * El servidor DNS se llama `isis.tu_nombre.gonzalonazareno.org` y va a ser el servidor con autoridad para la zona `tu_nombre.gonzalonazareno.org`.
    * El servidor debe resolver el nombre de todas las máquinas.
    * Vamos a usar vistas en bind9, para que el nombre de `ra` se corresponda con una ip distinta según desde se realice la consulta. Vamos a crear dos vistas: una **interna**, para cuando se hacen consultas desde las máquinas de nuestro escenario y otra **externa** para cuando se hagan consultas desde el exterior. En este ejercicio **crea solo la vista interna**.
    * Vamos a crear las zonas de resolución inversas correspondientes al direccionamiento de las redes privadas (`192.168.0.0/24` y `172.16.0.0/16`).
2. Configura como servidor DNS de nuestras máquinas a **isis**:
    * En los contenedores no hay problema ya que el direccionamiento es estático.
    * En `anubis` también podemos hacer el cambio de manera estática (investiga como hacer el cambio en Rocky Linux). 
    * En `ra`: tenemos instalado `systemd-resolved`. Investiga como cambiar el servidor DNS cuando tenemos este sistema de resolución funcionando.
3. Para que podamos usar los nombres cortos (por ejemplo, para hacer `ssh anubis`) es necesario que el parámetro `search` del fichero `/etc/resolv.conf` este configurado con nuestro nombre de dominio. Investiga como hacer el cambio del parámetro `search` en las distintas máquinas.

{% capture notice-text %}
## Entrega

1. Entrega la configuración DNS de cada máquina: donde se compruebe que el servidor que están utilizando es **isis** y que tienes configurado de manera adecuada el parámetro `search`.
2. Entrega la definición de las vistas y de las zonas.
3. Entrega el resultado de las siguientes consultas desde **horus**:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `ra`.
    * Una resolución de `www`.
    * Una resolución de `bd`.
    * Un resolución inversa de IP fija en cada una de las redes.
4. Desde `ra` entrega la salida de `ping horus` y `ssh anubis` para comprobar que funcionan los nombres cortos en la resolución.


## Delegación de la zona

1. Será necesario realizar consultas desde el exterior (ya que vamos a hacer una delegación del subdominio). Por lo tanto tienes que realizar las siguientes tareas:
    * Determina la regla DNAT en `ra` para que podamos hacer consultas DNS desde el exterior. Prueba a hacer una consulta desde tu anfitrión usando la IP flotante de `ra`.
    * Crea una la vista **externa** para cuando se realizan consultas desde el exterior.
2. Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal `dns.gonzalonazareno.org`. Ahora prueba, desde tu anfitrión a resolver tus nombres pero preguntando al DNS de nuestra red (`172.22.0.1`).
3. Queremos que el servidor DNS que has configurado también pueda resolver los nombres de los DNS de los compañeros. Para ello lo vamos a configurar como **servidor DNS forward/caché**, de tal manera que las consultas la realizará sobre nuestro servidor `172.22.0.1`. Para configurar el servidor como forwarder hay que modificar el parámetro en el fichero `named.conf.options`.


{% capture notice-text %}
## Entrega

1. Entrega la definición de la nueva vista.
2. Entrega el resultado de las siguientes consultas desde la máquina anfitriona, preguntando a nuestro servidor DNS `172.22.0.1`:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `ra`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Servidor web

Instala un servidor web en **anubis**. Configura el DNS de forma correcta para que se pueda acceder a la página web (`www.tunombre.gonzalonazareno.org`) desde las máquinas del escenario y desde el exterior.

{% capture notice-text %}
## Entrega

1. Entrega el resultado de la consulta a `www.tunombre.gonzalonazareno.org` desde el exterior preguntando a nuestro servidor DNS `172.22.0.1`.
2. Entrega el resultado de la consulta a `www.tunombre.gonzalonazareno.org` desde una máquina interna.
3. Realiza una consulta a tu DNS preguntando por el nombre de un dns de un compañero, para comprobar si se está comportando como DNS fordward/caché.
4. Entrega una captura de pantalla accediendo a `www.tunombre.gonzalonazareno.org` donde se vea la página web desde  exterior y desde el interior.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
