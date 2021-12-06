---
title: Introducción a HAProxy
---

Vamos a desarrollar un escenario usando vagrant y ansible para trabajar con HAProxy, para ello vamos a utilizar el repositorio 
[vagrant_ansible_haproxy](https://github.com/josedom24/vagrant_ansible_haproxy). Al levantar el escenario y configurarlo con ansible, se realizan las siguientes tareas:

* En el nodo `backend1` y `backend2` instala wordpress.
* En el nodo `frontend` instala HAProxy pero sin configurar.
* Las credenciales para entrar en la administración son usuario `admin`, contraseña `admin`.
* Una vez configurado el HAProxy, se accedera a la aplicación usando la URL: `http://www.example.org/wordpress/`, por lo tanto hay que configurar resolución estática para que `www.example.org` apunte a la ip del nodo `frontend`.

Realiza los siguientes pasos:

### Configuración de HAProxy

Una vez levantado el escenario accede a `frontend` y vamos a configurar el HAProxy. Para ello añade la siguiente configuración en el fichero `/etc/haproxy/haproxy.cfg`:

```
frontend servidores_web
	bind *:80 
	mode http
	stats enable
	stats uri /ha_stats
	stats auth  cda:cda
	default_backend servidores_web_backend

backend servidores_web_backend
	mode http
	balance roundrobin
	server backend1 10.0.0.10:80 check
	server backend2 10.0.0.11:80 check
```

* La sección `frontend` representa al balanceador de carga, que va a escuchar n todas las interfaces en el puerto 80, en modo `http`, que va a ofrecer estadística en la URL  `/ha_stats` y que va a balancear en los servidores definido en el `default_backend`.
* La sección `backend` define los servidores entre los que se va a balancear, el tipo de balanceo y el modo.

### Acceso a HAProxy

Vamos a configurar la resolución estática para acceder a la IP del servidor `frontend` con el nombre `www.example.org`. Cada petición que se haga se mandará a los nodos `backend1` y `backend2` alternativamente.

Puedes ver las estadisticas de acceso, accediendo a `http://www.example.org/ha_stats` y poniendo como credenciales el usuario y contraseña que has definido en el parámetro `stats auth`.

### Controlando HAProxy

Podemos acceder a las estadisticas y controlar a que nodos se está balanceado la carga utilizando la herramienta`hatop`:

```bash
apt install hatop
```

Y conectamos a un socket unix donde escucha HAProxy:

```
hatop -s /run/haproxy/admin.sock
```

Podemos ver los `frontend` y `backend` que tenemos definido, además podemos las peticiones que se están balanceado en cada nodo. Podemos activar o desactivar un nodo del backend, para ello lo seleccionamos y pulsamos F10 para desactivar y F9 para activar.

## ¿Funciona el balanceo de carga?

El balanceo de carga funciona, ¿pero funciona de forma adecuada el Wordpress?:

* ¿Qué pasa si escribo un artículo en wordpress? ¿Se ven en los dos nodos? ¿Las base de datos están sincronizadas?
* ¿Qué pasa si subo una imagen a un artículo? ¿Esa imagen es accesible en los dos nodos?
* ¿Puedo acceder a la zona de administracion? ¿Cómo se gestiona las sesiones cuando balanceamos?

En el último tema del curso crearemos un cluster de forma adecuada para que mi wordpress funcione de manera adecuada: sistemas de archivos distribuidos, base ded datos replicadas, ...


