---
title: "Gestión de peticiones en los servidores web"
--- 

## Módulos de Multiprocesamiento (MPMs) en Apache 2.4


Por defecto apache2 se configura con el MPM event, podemos ver el MPM que estamos utilizando con la siguiente instrucción::

	# apachectl -V
	...
	Server MPM:     event
	...

Para cambiar de MPM tenemos que desactivar el actual y activar el nuevo módulo::

	# a2dismod mpm_event
	# a2enmod mpm_prefork
	# service apache2 restart

	# apachectl -V
	...
	Server MPM:     prefork
	...

### Las directivas de configuración de los distintos MPM

En ``/etc/apache2/mods-availables/mpm_prefork.conf``::

Directivas de control de [prefork](https://httpd.apache.org/docs/2.4/mod/prefork.html>):

    StartServers              5
    MinSpareServers           5
    MaxSpareServers          10
    MaxRequestWorkers       150
    MaxConnectionsPerChild    0


En ``/etc/apache2/mods-availables/mpm_worker.conf``:

Directivas de control de [worker](https://httpd.apache.org/docs/2.4/mod/worker.html>):

    StartServers            2
    MinSpareThreads         25
    MaxSpareThreads         75
    ThreadLimit             64
    ThreadsPerChild         25
    MaxRequestWorkers       150
    MaxConnectionsPerChild  0

En ``/etc/apache2/mods-availables/mpm_event.conf``:

Directivas de control de [event](https://httpd.apache.org/docs/2.4/mod/event.html>):

    StartServers              2
    MinSpareThreads          25
    MaxSpareThreads          75
    ThreadLimit              64
    ThreadsPerChild          25
    MaxRequestWorkers       150
    MaxConnectionsPerChild    0

## Gestión de peticiones en nginx

### Procesos worker

La directiva `worker_processes` nos indica el número de procesos que van a responder peticiones. 
El valor de `worker_processes`, se suele definir al mismo número de CPUs que tenga el equipo, o como mucho, el doble. Esto se hace así porque, al ser un servidor web asíncrono, cada proceso se puede encargar de muchas peticiones y por lo tanto no tiene sentido tener más procesos que CPUs capaces de ejecutar código.

Para indicar un worker por cada core de la CPU:

    worker_processes auto;

* Comprueba la configuración por defecto de nginx y comprueba cuantos procesos worker se están ejecutando.

**Conexiones por proceso**

La opción `worker_connections` establece el número máximo de conexiones que cada proceso worker puede procesar a la vez. Es recomendable aumentar este valor si nuestra web tiene un elevado tráfico. El valor por defecto es de 768.

El número máximo de clientes que Nginx puede manejar viene determinado por multiplicar el valor indicado en `worker_processes` por el indicado en `worker_connections`.

Además podemos usar `multi_accept` con el fin de que un worker acepte todas las nuevas conexiones al mismo tiempo.

* Comprueba la configuración por defecto de nginx.

