---
title: "Práctica (1 / 2): Servidores Web, Base de Datos y DNS en nuestros escenario de OpenStack"
---

## Servidor DNS

Vamos a instalar un servidor dns en **nami** que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor DNS con autoridad sobre un subdominio de nuestro dominio principal `gonzalonazareno.org`, que se llamará `tu_nombre.gonzalonazareno.org`.

Hay que tener en cuenta los siguientes aspectos:

1. El servidor DNS se va a configurar de la siguiente manera:
    * El servidor DNS se llama `nami.tu_nombre.gonzalonazareno.org` y va a ser el servidor con autoridad para la zona `tu_nombre.gonzalonazareno.org`.
    * El servidor debe resolver el nombre de todas las máquinas.
    * En la siguiente parte de la práctica instalaremos un servidor web que llamaremos `www` en **zoro** y una base de datos que llamaremos `bd` en **sanji**.
    * Vamos a usar vistas en bind9, para que el nombre de `luffy` se corresponda con una ip distinta según desde se realice la consulta. Vamos a crear dos vistas, una para cuando se hacen consultas desde la **red_intra** y otra para cuando se hacen consultas desde la **red_dmz**.
    * Vamos a crear las zonas de resolución inversas correspondientes al direccionamiento de las redes privadas (`192.168.0.0/24` y `172.16.0.0/16`).
2. Configura como servidor DNS de nuestras máquinas a **nami**:
    * En los contenedores no hay problema ya que el direccionamiento es estático.
    * En `zoro` también podemos hacer el cambio de manera estática (investiga como hacer el cambio en Rocky Linux). 
    * En `luffy`: tenemos instalado `systemd-resolved`. Investiga como cambiar el servidor DNS cuando tenemos este sistema de resolución funcionando.
3. Para que podamos usar los nombres cortos (por ejemplo, para hacer `ssh zoro`) es necesario que el parámetro `search` del fichero `/etc/resolv.conf` este configurado con nuestro nombre de dominio. Investiga como hacer el cambio del parámetro `search` en las distintas máquinas.

{% capture notice-text %}
## Entrega

1. Entrega la configuración DNS de cada máquina: donde se compruebe que el servidor que están utilizando es **nami** y que tienes configurado de manera adecuada el parámetro `search`.
2. Entrega la definición de las vistas y de las zonas.
3. Entrega el resultado de las siguientes consultas desde **sanji**:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `luffy`.
    * Una resolución de `www`.
    * Una resolución de `bd`.
    * Un resolución inversa de IP fija en cada una de las redes.
4. Entrega el resultado de las siguientes consultas desde **zoro**:
    * La dirección IP de `luffy`.
5. Desde `luffy` entrega la salida de `ping zoro` y `ssh samji` para comprobar que funcionan los nombres cortos en la resolución.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
