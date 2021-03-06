---
title: "Práctica: Proxy, proxy inverso y balanceadores de carga"
permalink: /serviciosgs/u08/practica_proxy_lb.html
---

## Proxy

En esta práctica vamos a instalar un proxy `squid` para configurar nuestro cliente para que acceda a internet por medio de este proxy.

Vamos a usar el fichero [Vagrantfile](doc/squid/Vagrantfile) para crear el escenario: un ordenador llamado `proxy` donde instalaremos squid y un cliente interno (`cliente_int`).

{% capture notice-text %}
* **Tarea 1**: Instala squid en la máquina `squid` y configúralo para que permita conexiones desde la red donde este tu ordenador.
* **Tarea 2**: Prueba que tu ordenador está navegando a través del proxy (HTTP/HTTPS) configurando el proxy de dos maneras diferentes:

    * Directamente indicándolo en el navegador.
    * Configurando el proxy del sistema en el entorno gráfico (tienes que indicar en el navegador que vas a hacer uso del proxy del sistema).

Muestra el contenido del fichero ´/var/log/squid/access.log` para comprobar que está funcionando el proxy.

* **Tarea 3**: Configura squid para que pueda ser utilizado desde el cliente interno. En el cliente interno configura el proxy desde la línea de comandos (con una variable de entorno). Fíjate que no hemos puesto ninguna regla SNAT y podemos navegar (protocolo HTTP), pero no podemos hacer ping o utilizar otro servicio.
* **Tarea 4**: Con squid podemos filtrar el acceso por url o dominios, realiza las configuraciones necesarias para implementar un filtro que funcione como lista negra (todo el acceso es permitido menos las url o dominios que indiquemos en un fichero.)
* **Tarea 5**: Realiza las configuraciones necesarias para implementar un filtro que funcione como lista blanca (todo el acceso es denegado menos las url o dominios que indiquemos en un fichero.)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Balanceador de carga

En esta práctica vamos a hacer uso de vagrant para crear este escenario:


![haproxy](img/haproxy.jpg)

Para ello descarga este [fichero](doc/haproxy/vagrant.zip), descomprímelo en un directorio y crea el escenario vagrant.

### Configurar y evaluar balanceo de carga con dos servidores Apache

Instala HAproxy en `balanceador` y configuralo de la siguiente manera:

    balanceador:~# cd /etc/haproxy
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
        bind 172.22.x.x:80 #aquí pon la dirección ip del balanceador
        mode http
        stats enable
        stats auth  cda:cda
        balance roundrobin
        server uno 10.10.10.11:80 maxconn 128
        server dos 10.10.10.22:80 maxconn 128

Define (en la sección `listen`) un "proxy inverso" de nombre `granja_cda` que:

* trabajará en modo `http` (la otra alternativa es el modo tcp, pero no analiza las peticiones/respuestas HTTP, sólo retransmite paquetes TCP)
* atendiendo peticiones en el puerto 80 del balanceador
* con balanceo `round-robin`
* que repartirá las peticiones entre dos servidores reales (de nombres uno y dos) en el puerto 80 de las direcciones `10.10.10.11` y `10.10.10.22`
* adicionalmente, habilita la consola Web de estadísticas, accesible con las credenciales `cda:cda`

Más detalles en [Opciones de configuración HAPproxy 1.8](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html).

Inicia HAproxy en balanceador: Antes de hacerlo es necesario habilitar en ``/etc/default/haproxy`` el arranque de HAproxy desde los scripts de inicio, estableciendo la variable ``ENABLED=1``

Por último, desde la máquina cliente abrir en un navegador web la URL `http://172.22.x.x` y recargar varias veces para comprobar como cambia el servidor real que responde las peticiones.

{% capture notice-text %}
* **Tarea 1**: Entrega capturas de pantalla que el balanceador está funcionando.
* **Tarea 2**: Entrega una captura de pantalla donde se vea la página web de estadísticas de haproxy (abrir en un navegador web la URL `http://172.22.x.x/haproxy?stats`, pedirá un usuario y un password, ambos `cda`).
* **Tarea 3**: Desde uno de los servidores (apache1 ó apache2), verificar los logs del servidor Apache. En todos los casos debería figurar como única dirección IP cliente la IP interna de la máquina balanceador `10.10.10.1`. ¿Por qué?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


### Configurar la persistencia de conexiones Web (sticky sessions)

En los servidores internos hay una aplicación PHP para trabajar con sesiones, puedes encontrar el fichero `sesion.php` con el siguiente contenido:

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
* acceder la misma URL desde el navegador en modo texto lynx (o desde una pestaña de "incógnito" del Navegador para forzar la creación de una nueva sesión)::

        cliente:~# lynx -accept-all-cookies http://172.22.x.x/sesion.php

{% capture notice-text %}
* **Tarea 4**:Verificar la estructura y valores de las cookies PHPSESSID intercambiadas. En la primera respuesta HTTP (inicio de sesión), se establece su valor con un parámetro HTTP SetCookie en la cabecera de la respuesta. Las sucesivas peticiones del cliente incluyen el valor de esa cookie (parámetro HTTP Cookie en la cabecera de las peticiones)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Proxy inverso

### Opción 1

Para hacer esta práctica puedes utilizar el escenario del ejercicio anterior.

En este caso queremos instalar dos servidores web en el `apache1` y en `apache2`, estos servidores deben servir una web completa (con hoja de estilo, imágenes,...) busca alguna plantilla (debe tener algunas páginas html para probar los enlaces).

Configura en el ordenador `balanceador` (tienes que detener haproxy) un proxy inverso para acceder a las aplicaciones de dos formas distintas:

### Opción 2

En una máquina instala docker e instala con docker-compose dos aplicaciones:  [joomla](https://hub.docker.com/_/joomla) y [nextcloud](https://hub.docker.com/_/nextcloud). Instala un proxy inverso para acceder a las aplicaciones de dos formas distintas:

{% capture notice-text %}
* **Tarea 1**: Para que se acceda a la primera aplicación con la URL `www.app1.org` y a la segunda aplicación con la URL `www.app2.org`.
* **Tarea 2**: Para que se acceda a la primera aplicación con la URL `www.servidor.org\app1` y a la segunda aplicación con la URL `www.servidor.org\app2`.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>