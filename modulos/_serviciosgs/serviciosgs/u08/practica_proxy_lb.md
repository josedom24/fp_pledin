---
title: "Práctica: Proxy, proxy inverso y balanceadores de carga"
permalink: /serviciosgs/u08/practica_proxy_lb.html.html
---

**(12 tareas - 15 puntos)**
{: .notice--warning}

## Proxy

En esta práctica vamos a instalar un pequeño proxy llamado `tinyproxy` para que podamos comprobar como funciona este tipo de servicio.

{% capture notice-text %}
* **Tarea 1 (1 puntos)**: Instala tinyproxy en una máquina y configúralo para que permita conexiones desde la red dopnde este tu ordenador.
* **Tarea 2 (1 puntos)**: Prueba que tu ordenador está navegando a través del proxy (HTTP/HTTPS) configurando el proxy de tres maneras diferentes:

    * Directamente indicándolo en el navegador.
    * Configurando el proxy del sistema en el entorno gráfico (tienes que indicar en el navegador que vas a hacer uso del proxy del sistema).
    * Configurando el proxy desde la línea de comandos (tienes que indicar en el navegador que vas a hacer uso del proxy del sistema).

    Muestra el contenido del fichero ´/var/log/tinyproxy.log` para comprobar que está funcionando el proxy.
* **Tarea 3 (2 puntos)**: Con tinyproxy podemos filtrar el acceso por url o dominios, realiza las configuraciones necesarias para implementar un filtro que funcione como lista negra (todo el acceso es permitido menos las url o dominios que indiquemos.)
* **Tarea 4 (2 puntos)**: Realiza las configuraciones necesarias para implementar un filtro que funcione como lista blanca (todo el acceso es denegado menos las url o dominios que indiquemos.)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Proxy inverso

...

* Para que se acceda a la primera aplicación con la URL `www.servidor.org\app1` y a la segunda aplicación con la URL `www.servidor.org\app2`.
* Para que se acceda a la primera aplicación con la URL `www.app1.org` y a la segunda aplicación con la URL `www.app2.org`.

{% capture notice-text %}
* **Tarea 5 (1 punto)**: Configura apache2 como proxy inverso para acceder a los servidores internos de la primera forma.
* **Tarea 6 (1 punto)**: Configura apache2 como proxy inverso para acceder a los servidores internos de la segunda forma.
* **Tarea 7 (1 punto)(Obligatorio)**: Configura nginx como proxy inverso para acceder a los servidores internos de la primera forma.
* **Tarea 8 (1 punto)**: Configura nginx como proxy inverso para acceder a los servidores internos de la segunda forma.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Balanceador de carga

En primer lugar, construye con KVM con vagrant la siguiente infraestructura:

![haproxy](img/haproxy.png)

Modifica el contenido de los ficheros `index.html` para que indiquen a que servidor se está accediendo:
En apache1:

    apache1:~# nano /var/www/html/index.html
     ...
     <h1> Servidor por APACHE_UNO </h1>
     ...
            

 En apache2:

    apache2:~# nano /var/www/html/index.html
    ...
     <h1> Servidor por APACHE_DOS </h1>
     ...

### Configurar y evaluar balanceo de carga con dos servidores Apache

Instala HAproxy en balanceador y configurarlo de la siguiente manera:

    balanceador:~# cd /etc/haproxy
    balanceador:/etc/haproxy/# mv haproxy.cfg haproxy.cfg.original
    balanceador:/etc/haproxy/# nano haproxy.cfg        
    global
        daemon
        maxconn 256
        user    haproxy
        group   haproxy
        log     127.0.0.1       local0
        log     127.0.0.1       local1  notice     
    defaults
        mode    http
        log     global
        timeout connect 5000ms
        timeout client  50000ms
        timeout server  50000ms        
    listen granja_cda 
        bind 193.147.87.47:80
        mode http
        stats enable
        stats auth  cda:cda
        balance roundrobin
        server uno 10.10.10.11:80 maxconn 128
        server dos 10.10.10.22:80 maxconn 128

Define (en la sección listen) un "proxy inverso" de nombre granja_cda que:

* trabajará en modo http (la otra alternativa es el modo tcp, pero no analiza las peticiones/respuestas HTTP, sólo retransmite paquetes TCP)
* atendiendo peticiones en el puerto 80 del balanceador
* con balanceo round-robin
* que repartirá las peticiones entre dos servidores reales (de nombres uno y dos) en el puerto 80 de las direcciones 10.10.10.11 y 10.10.10.22
* adicionalmente, habilita la consola Web de estadísticas, accesible con las credenciales cda:cda

Más detalles en [Opciones de configuración HAPproxy 1.5](http://cbonte.github.io/haproxy-dconv/configuration-1.5.html).

Inicia HAproxy en balanceador: Antes de hacerlo es necesario habilitar en ``/etc/default/haproxy`` el arranque de HAproxy desde los scripts de inicio, estableciendo la variable ``ENABLED=1``

Por último, desde la máquina cliente abrir en un navegador web la URL http://172.22.x.x y recargar varias veces para comprobar como cambia el servidor real que responde las peticiones.

{% capture notice-text %}
* **Tarea 9 (1 puntos)**: Muestra al profesor y entrega capturas de pantalla que el balanceador está funcionando.
* **Tarea 10 (1 punto)**: Entrega una captura de pantalla donde se vea la página web de estadísticas de haproxy (abrir en un navegador web la URL `http://172.22.x.x/haproxy?stats`, pedirá un usuario y un password, ambos `cda`).
* **Tarea 11 (1 punto)**: Desde uno de los servidores (apache1 ó apache2), verificar los logs del servidor Apache. En todos los casos debería figurar como única dirección IP cliente la IP interna de la máquina balanceador [10.10.10.1]. ¿Por qué?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


### Configurar la persistencia de conexiones Web (sticky sessions)

En los servidores internos vamos a crear una aplicación PHP para trabajar con sesiones, vamos a crear el fichero `sesion.php` con el siguiente contenido:

    <?php
         header('Content-Type: text/plain');
         session_start();
         if(!isset($_SESSION['visit']))
         {
                 echo "This is the first time you're visiting this server";
                 $_SESSION['visit'] = 0;
         }
         else
                 echo "Your number of visits: ".$_SESSION['visit'];             

         $_SESSION['visit']++;              

         echo "\nServer IP: ".$_SERVER['SERVER_ADDR'];
         echo "\nClient IP: ".$_SERVER['REMOTE_ADDR'];
         echo "\nX-Forwarded-for: ".$_SERVER['HTTP_X_FORWARDED_FOR']."\n";
         print_r($_COOKIE);
    ?>

Vamos a añadir las opciones de persistencia de conexiones HTTP (sticky cookies) al fichero de configuración::
   
Contenido a incluir: (añadidos marcados con ``<- aquí``)::

    global
         daemon
         maxconn 256
         user    haproxy
         group   haproxy
         log     127.0.0.1       local0
         log     127.0.0.1       local1  notice         

     defaults
         mode    http
         log     global
         timeout connect 10000ms
         timeout client  50000ms
         timeout server  50000ms            

     listen granja_cda 
         bind 172.22.x.x:80 #aquí pon la dirección ip del balanceador
         mode http
         stats enable
         stats auth  cda:cda
         balance roundrobin
         cookie PHPSESSID prefix                               # <- aquí
         server uno 10.10.10.11:80 cookie EL_UNO maxconn 128   # <- aquí
         server dos 10.10.10.22:80 cookie EL_DOS maxconn 128   # <- aquí

El parámetro cookie especifica el nombre de la cookie que se usa como identificador único de la sesión del cliente (en el caso de aplicaciones web PHP se suele utilizar por defecto el nombre PHPSESSID). Para cada “servidor real” se especifica una etiqueta identificativa exclusiva mediante el parámetro cookie. Con esa información HAproxy reescribirá las cabeceras HTTP de peticiones y respuestas para seguir la pista de las sesiones establecidas en cada “servidor real” usando el nombre de cookie especificado (PHPSESSID):

* conexión cliente -> balanceador HAproxy : cookie original + etiqueta de servidor
* conexión balanceador HAproxy -> servidor : cookie original

Reiniciamos el balanceador y realizamos las siguientes acciones:

* desde el navegador web acceder varias veces a la URL `http://172.22.x.x/sesion.php`(comprobar el incremento del contador [variable de sesión])
* acceder la misma URL desde el navegador en modo texto lynx (o desde una pestaña de "incógnito"’’" del Navegador para forzar la creación de una nueva sesión)::

    cliente:~# lynx -accept-all-cookies http://172.22.x.x/sesion.php


* **Tarea 12 (2 puntos)**:Verificar la estructura y valores de las cookies PHPSESSID intercambiadas. En la primera respuesta HTTP (inicio de sesión), se establece su valor con un parámetro HTTP SetCookie en la cabecera de la respuesta. Las sucesivas peticiones del cliente incluyen el valor de esa cookie (parámetro HTTP Cookie en la cabecera de las peticiones)

