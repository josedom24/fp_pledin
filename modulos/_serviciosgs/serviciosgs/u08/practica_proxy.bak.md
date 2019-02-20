# Práctica: Servidor proxy-cache, proxy inverso y balanceador de carga

```eval_rst
.. note::

	**(16 tareas - 30 puntos)(8 tareas obligatorias - 15 puntos)**

```

En primer lugar, construye con KVM o con vagrant la siguiente infraestructura:

```eval_rst
.. image:: img/esquema.png
```

## Proxy squid

Queremos instalar un servidor proxy/cache en nuestro **servidor 1**. Con ello vamos a poder controlar las páginas web a las que accedamos (desde el **servidor 2** y **servidor 3**), además de acelerar nuestra navegación.

Nos piden la configuración de un proxy/cache/filtro en nuestra infraestructura. Hemos elegido como proxy/cache squid3, y como filtro de contenido dansguardian. Tenemos que tener en cuenta las siguientes consideraciones:

1. El proxy/cache sólo admite conexiones de la red local.
2. Se quieren limitar las siguientes conexiones:
    * No se pueden bajar ficheros que se puedan instalar (``exe,msi,rar,zip,bin,iso``).
    * No tienen acceso a internet los fines de semana.
3. El control de las páginas permitidas se hará mediante listas negras usando dansguardians.
4. Por último tendremos instalado un programa para monitorizar el uso del proxy: sarg. Para visualizar la información generada por dicho programa accederemos a una página web llamada ``proxy.josedomingo.gonzalonazareno.org`` que sólo será accesible si ponemos el nombre de usuario y contraseña.
5. Finalmente queremos configurar la infraestrucutra para tener un proxy transparente.

```eval_rst
.. note::

    * **Tarea 1 (1 punto)(Obligatorio)**: Configura de forma manual el proxy. Muestra las capturas de pantalla.
    * **Tarea 2 (2 puntos)(Obligatorio)**: Muestra la configuración de squid para no permitir descargar ficheros ejecutables. Prueba de funcionamiento.
    * **Tarea 3 (2 puntos)(Obligatorio)**: Muestra la configuración de squid para no permitir el acceso los fines de semana. Prueba de funcionamiento.
    * **Tarea 4 (2 puntos)**: Filtra el dominio youtube.com en la lista negra y prueba que realmente no se puede acceder.
    * **Tarea 5 (2 puntos)**: Documenta la instalación de sarg, y muestra las estadísticas de acceso al proxy con sarg.
    * **Tarea 6 (3 puntos)**: Documenta la configuración del proxy transparente y haz una prueba de funcionamiento.
```

## Proxy inverso

```eval_rst
.. note::

    Seguimos trabajando con las mismas máquinas, pero en un ejercicio nuevo, por lo que si necesitas detener los servicios del ejercicio anterior lo puedes hacer.
```

En este caso queremos instalar dos servidor web en el **Servidor 2** y en **Servidor 3**, estos servidores deben servir una web completa (con hoja de estilo, imágenes,...) busca alguna plantilla.

En el **Servidor 1** vamos a instalar diferentes configuraciones de proxy inverso para que desde el exterior se puedan acceder a las páginas de los servidores conectados a la red interna. Los proxy inversos los vamos a configurar de dos maneras distintas:

* Para que se acceda al servidor de **Servidor 2** con la URL `www.servidor.org\pagina1` y al servidor **Servidor 3** con la URL `www.servidor.org\pagina2`.
* Para que se acceda al servidor de **Servidor 2** con la URL `www.pagina1.org` y al servidor **Servidor 3** con la URL `www.pagina2.org`.

```eval_rst
.. note::

    * **Tarea 7 (2 puntos)(Obligatorio)**: Configura apache2 como proxy inverso para acceder a los servidores internos de la primera forma.
    * **Tarea 8 (2 puntos)**: Configura apache2 como proxy inverso para acceder a los servidores internos de la segunda forma.
    * **Tarea 9 (2 puntos)(Obligatorio)**: Configura nginx como proxy inverso para acceder a los servidores internos de la primera forma.
    * **Tarea 10 (2 puntos)**: Configura nginx como proxy inverso para acceder a los servidores internos de la segunda forma.
    
```

## Balanceador de carga

```eval_rst
.. note::

    Seguimos trabajando con las mismas máquinas, pero en un ejercicio nuevo, por lo que si necesitas detener los servicios del ejercicio anterior lo puedes hacer.
```

Ajustar la configuración de las dos máquinas del cluster de balanceo (**Servidor 2** y **Servidor3**):

Deshabilitar la opción `KeepAlive` en el fichero de configuración ``/etc/apache2/apache2.conf`` para realizar la evaluación del rendimiento sin la opción de reutilización de conexiones, para ello en `/etc/apache2/apache2.conf`:
     
     ...
     KeepAlive Off
     ...            
    
```eval_rst
.. warning:: 

    Nota: este ajuste no es estrictamente necesario (y sería desaconsejable en un entorno de producción real), pero facilita las pruebas manuales dado que permite detectar inmediatamente el “cambio” de destino resultado del balanceo de carga manteniendo la opción por defecto, en las pruebas manuales desde el navegador sería necesario esperar 5 segundos (el time out de keep alive) antes de recargar la página y ver el efecto del reparto de carga
```
En el **Servidor 1** vamos a realizar diferentes configuraciones de servicios para que realicen el balanceo de carga entre los servidores web internos, por lo tanto al acceder desde el exterior a la ip del **Servidor 1** se irá mostrando alternativamente las páginas de **Servidor 2** y **Servidor 3**.


```eval_rst
.. note::

    * **Tarea 11 (2 puntos)(Obligatorio)**: Configura apache2 como balanceador de carga.
    * **Tarea 12 (2 puntos)(Obligatorio)**: Configura ngninx como balanceador de carga.

```

### Balanceo de carga con haproxy

Instala haproxy en **Servidor 1**. Lo primero es configurar HAproxy en balanceador (de momento sin soporte de sesiones persistentes)::

     servidor1:~# cd /etc/haproxy
     servidor1:/etc/haproxy/# mv haproxy.cfg haproxy.cfg.original
     servidor1:/etc/haproxy/# nano haproxy.cfg        

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
         server uno 10.0.0.X:80 maxconn 128
         server dos 10.0.0.Y:80 maxconn 128

Define (en la sección listen) un "proxy inverso" de nombre `granja_cda` que:

* trabajará en modo http (la otra alternativa es el modo tcp, pero no analiza las peticiones/respuestas HTTP, sólo retransmite paquetes TCP)
* atendiendo peticiones en el puerto 80 del balanceador
* con balanceo round-robin
* que repartirá las peticiones entre dos servidores reales (de nombres uno y dos) en el puerto 80 de las direcciones 10.0.0.X y 10.0.0.Y
* adicionalmente, habilita la consola Web de estadísticas, accesible con las credenciales `cda`:`cda`

Más detalles en [Opciones de configuración HAPproxy 1.5](http://cbonte.github.io/haproxy-dconv/configuration-1.5.html)

Para iniciar HAproxy es necesario habilitar en ``/etc/default/haproxy`` el arranque de HAproxy desde los scripts de inicio, estableciendo la variable ``ENABLED=1``

Desde la máquina cliente abrir en un navegador web la URL `http://172.22.x.x` y recargar varias veces para comprobar como cambia el servidor real que responde las peticiones.
```eval_rst
.. warning::

    Nota: Si no se ha deshabilitado la opción KeepAlive de Apache, es necesario esperar 5 segundos entre las recargas para que se agote el tiempo de espera para cerrar completamente la conexión HTTP y que pase a ser atendida por otro servidor.
```

Desde la máquina cliente podemos abrir en un navegador web la URL `http://172.22.x.x/haproxy?stats` para inspeccionar las estadísticas del balanceador HAProxy (pedirá un usuario y un password, ambos `cda`).

```eval_rst
.. note::

    * **Tarea 13 (2 puntos)(Obligatorio)**: Muestra al profesor y entrega capturas de pantalla que el balanceador está funcionando.
    * **Tarea 14 (1 punto)**: Entrega una captura de pantalla donde se vea la página web de estadísticas de haproxy.
    * **Tarea 15 (1 punto)**:Desde uno de los servidores (**Servidor 2** ó **Servidor 3**), verificar los logs del servidor Apache. En todos los casos debería figurar como única dirección IP cliente la IP interna de la máquina balanceador [10.0.0.1]. ¿Por qué?
```

### Configurar la persistencia de conexiones Web (sticky sessions)

Vamos a añadir las opciones de persistencia de conexiones HTTP (sticky cookies) al fichero de configuración. Para ello vamos a modificar las tres últimas líneas del fichero de configuración:
        
        ...
        cookie PHPSESSID prefix                               
        server uno 10.0.0.X:80 cookie EL_UNO maxconn 128   
        server dos 10.0.0.Y:80 cookie EL_DOS maxconn 128   

El parámetro `cookie` especifica el nombre de la cookie que se usa como identificador único de la sesión del cliente (en el caso de aplicaciones web PHP se suele utilizar por defecto el nombre `PHPSESSID`). Para cada "servidor real" se especifica una etiqueta identificativa exclusiva mediante el parámetro `cookie`. Con esa información HAproxy reescribirá las cabeceras HTTP de peticiones y respuestas para seguir la pista de las sesiones establecidas en cada "servidor real" usando el nombre de cookie especificado (PHPSESSID):

* conexión cliente -> balanceador HAproxy : cookie original + etiqueta de servidor
* conexión balanceador HAproxy -> servidor : cookie original

En los servidores web **Servidor 2** y **Servidor 3** vamos a configurar apache2 para que puedan ejecutar php y vamos a crear el fichero `sesion.php` con el siguiente contenido:

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

Para realizar la comprobación de que la sesión se mantiene aunque estemos balanceando, en la máquina cliente, arrancar el sniffer de red whireshark y ponerlo en escucha sobre el interfaz eth0 (fijar como filtro la cadena http para que solo muestre las peticiones y respuestas HTTP).
    
* desde el navegador web del cliente acceder varias veces a la URL `http://172.22.x.x/sesion.php` (comprobar el incremento del contador [variable de sesión])
* acceder la misma URL desde otro navegador (o desde una pestaña de "incógnito") para forzar la creación de una nueva sesión:
    
Detener la captura de tráfico en wireshark y comprobar las peticiones/respuestas HTTP capturadas.


```eval_rst
.. note::

    * **Tarea 16 (2 puntos)**:Verificar la estructura y valores de las cookies PHPSESSID intercambiadas. En la primera respuesta HTTP (inicio de sesión), se establece su valor con un parámetro HTTP SetCookie en la cabecera de la respuesta. Las sucesivas peticiones del cliente incluyen el valor de esa cookie (parámetro HTTP Cookie en la cabecera de las peticiones)
```

   