---
title: Introducción al balanceo de carga con HAProxy
---

Un **Balanceador de carga** es un dispositivo de hardware o software que se pone al frente de un conjunto de servidores que atienden una aplicación y, tal como su nombre lo indica, asigna o balancea las solicitudes que llegan de los clientes a los servidores usando algún algoritmo (round robin, conexiones mínimas, ...).
Ejemplos: apache2, nginx, haproxy, . . .

[HAProxy](https://www.haproxy.org/) es un software que nos permite balancear carga entre varios servidores. Se suele usar para balancear servicios web, pero puede balancear cualquier servicio que funcione bajo protocolo TCP.

Vamos a usar los ficheros del directorio `taller_balanceador_de_carga` del repositorio [taller_http](https://github.com/josedom24/taller_http) para crear el escenario, con las siguientes máquinas:

* `frontned`: Será a la máquina que realizará el balanceo de carga. En ella instalaremos `HAProxy` y accedermos con el nombre `www.example.org`.
* `backend1` y `backend2`: Los dos servidores web entre los que vamos a balancear la carga. Cada uno tiene un fichero `index.html` para que veamos bien el balanceo.

## Configuración de HAProxy

Una vez levantado el escenario accede a `frontend` y vamos a configurar el HAProxy. Para ello añade la siguiente configuración en el fichero `/etc/haproxy/haproxy.cfg` y luego reinicia el servicio:

```
frontend servidores_web
	bind *:80 
	mode http
	stats enable
	stats uri /ha_stats
	stats auth cda:cda
	default_backend servidores_web_backend

backend servidores_web_backend
	mode http
	balance roundrobin
	server backend1 10.10.10.11:80 check
	server backend2 10.10.10.22:80 check
```

* La sección `frontend` representa al balanceador de carga:
    * `bind`: identifica desde que red se va a responderm este caso se va a escuchar en todas las interfaces en el puerto 80.
    * `mode`: Se va a balancear la carga usando el protocolo http.
    * `stats enable`:: Se va a ofrecer estadística en la URL `/ha_stats` y el usuario y contraseña de la autentificación para acceder a la estadística se configura en el parámetro `stats auth`.
    * `default_backend`:y que va a balancear en los servidores definido en el `default_backend`.
* La sección `backend` define los servidores entre los que se va a balancear, el tipo de balanceo y el modo.
	* `mode`: Indica el modo de balanceo en nuestro caso http.
	* `balance`: Indica el algoritmo de balanceo, en nuestro caso **roundrobin**.
	* `server`: Para cada servidor se indica el nombre, la ip y el puerto y con el parámetro `check` se indica que se va a comprobar si está funcionando para mandarle peticiones.


## Acceso a HAProxy

Vamos a configurar la resolución estática para acceder a la IP del servidor `frontend` con el nombre `www.example.org`. Cada petición que se haga se mandará a los nodos `backend1` y `backend2` alternativamente.

Puedes ver las estadísticas de acceso, accediendo a `http://www.example.org/ha_stats` y poniendo como credenciales el usuario y contraseña que has definido en el parámetro `stats auth`.

## Controlando HAProxy

Podemos acceder a las estadísticas y controlar a que nodos se está balanceado la carga utilizando la herramienta`hatop`:

```bash
apt install hatop
```

Y conectamos a un socket unix donde escucha HAProxy:

```
hatop -s /run/haproxy/admin.sock
```

Podemos ver los `frontend` y `backend` que tenemos definido, además podemos las peticiones que se están balanceado en cada nodo. Podemos activar o desactivar un nodo del backend, para ello lo seleccionamos y pulsamos F10 para desactivar y F9 para activar.

Más detalles en [Opciones de configuración HAPproxy 2.6](https://docs.haproxy.org/2.6/configuration.html).
