---
title: "Introducción al balanceo de carga con HAProxy"
---


Un **balanceador de carga** es un dispositivo —de hardware o software— que distribuye las solicitudes de los clientes entre varios servidores que ofrecen un mismo servicio. Su objetivo es optimizar el uso de recursos, mejorar el rendimiento y aumentar la disponibilidad del sistema.
Ejemplos de balanceadores de carga software: **Apache HTTPD (mod_proxy_balancer)**, **NGINX** y **HAProxy**.

[**HAProxy**](https://www.haproxy.org/) es un software libre y de alto rendimiento especializado en el **balanceo de carga** y **proxy inverso** para servicios basados en los protocolos **TCP** y **HTTP(S)**. Es ampliamente utilizado en entornos de producción por su estabilidad, eficiencia y extensas capacidades de monitorización.

## Escenario de trabajo

Para este laboratorio utilizaremos los ficheros del directorio `haproxy` del repositorio [taller_http](https://github.com/josedom24/taller_http), con las siguientes máquinas virtuales:

| Máquina    | Rol                            | Servicio principal | IP          | Notas                             |
| ---------- | ------------------------------ | ------------------ | ----------- | --------------------------------- |
| `frontend` | Balanceador de carga (HAProxy) | HAProxy            | 10.10.10.10 | Acceso mediante `www.example.org` |
| `backend1` | Servidor web                   | Apache o Nginx     | 10.10.10.11 | Contiene `index.html` distinto    |
| `backend2` | Servidor web                   | Apache o Nginx     | 10.10.10.12 | Contiene `index.html` distinto    |

El balanceador (`frontend`) recibirá las peticiones HTTP y las distribuirá entre `backend1` y `backend2` usando un algoritmo de balanceo.

## Instalación de HAProxy

En Debian 13 (Trixie), el paquete `haproxy` está disponible en los repositorios oficiales:

```bash
sudo apt update
sudo apt install haproxy
```

## Configuración básica

Edita el archivo principal de configuración de HAProxy:

```bash
sudo nano /etc/haproxy/haproxy.cfg
```

Puedes **borrar su contenido original** y **sustituirlo** por la siguiente configuración mínima funcional.

En entornos de laboratorio o pruebas es recomendable partir de un archivo limpio, ya que el fichero por defecto contiene ejemplos y comentarios que pueden confundir.
En servidores en producción, sin embargo, conviene conservar las secciones `global` y `defaults` existentes y añadir tus propias definiciones al final.

```haproxy
# =======================
# Configuración básica HAProxy
# =======================

global
    log /dev/log local0
    log /dev/log local1 notice
    daemon
    user haproxy
    group haproxy
    maxconn 2048
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    option  http-server-close
    timeout connect 5s
    timeout client  30s
    timeout server  30s
    retries 3
    maxconn 1024

frontend servidores_web
    bind *:80
    mode http
    default_backend servidores_web_backend

    # Panel de estadísticas
    stats enable
    stats uri /ha_stats
    stats refresh 10s
    stats auth admin:admin123

backend servidores_web_backend
    mode http
    balance roundrobin
    option httpchk GET /
    http-check expect status 200

    server backend1 10.10.10.11:80 check
    server backend2 10.10.10.12:80 check
```

### Explicación de los parámetros

#### Sección `global`

* **log**: define dónde se registrarán los logs (usa syslog).
* **daemon**: ejecuta HAProxy en segundo plano.
* **user / group**: mejora la seguridad al ejecutar con usuario sin privilegios.
* **maxconn**: número máximo de conexiones concurrentes.
* **stats socket**: crea un socket UNIX para administración (necesario para `hatop`).

#### Sección `defaults`

* Define valores por defecto que se aplican a todos los `frontend` y `backend`.
* **option httplog**: usa un formato de log detallado para HTTP.
* **option http-server-close**: mejora la gestión de conexiones HTTP/1.1.
* **timeout**: define tiempos de espera razonables para cliente, servidor y conexión.

#### Sección `frontend`

* **bind *:80**: escucha peticiones HTTP en el puerto 80 de todas las interfaces.
* **default_backend**: indica a qué backend se dirigirán las peticiones.
* **stats uri /ha_stats**: habilita estadísticas accesibles por web.
* **stats auth**: define usuario y contraseña para acceder al panel.

#### Sección `backend`

* **balance roundrobin**: distribuye las peticiones alternando entre los servidores.
* **option httpchk GET /**: realiza comprobaciones HTTP a la raíz `/`.
* **http-check expect status 200**: considera operativo un servidor solo si responde con código 200.
* **server backendX ... check**: define los servidores y activa las comprobaciones de salud.

## Verificación de la configuración

Antes de reiniciar el servicio, valida la configuración:

```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

Si la verificación devuelve `Configuration file is valid`, reinicia HAProxy:

```bash
sudo systemctl restart haproxy
```

Comprueba que el servicio está activo:

```bash
sudo systemctl status haproxy
```

## Acceso a la aplicación y estadísticas

Agrega una entrada en `/etc/hosts` de tu máquina cliente (o en cada backend para pruebas locales):

```
10.10.10.10   www.example.org
```

Ahora puedes acceder a:

* **Aplicación balanceada:** [http://www.example.org/](http://www.example.org/)
  (verás alternarse las respuestas de `backend1` y `backend2`)
* **Panel de estadísticas:** [http://www.example.org/ha_stats](http://www.example.org/ha_stats)
  Usuario: `admin`
  Contraseña: `admin123`

El panel muestra información en tiempo real sobre:

* Estado de cada servidor backend.
* Número de conexiones activas.
* Tiempos de respuesta y errores.
* Posibilidad de activar o desactivar nodos manualmente.

## Control y monitorización con HATop

[HATop](https://github.com/jhunt/hatop) es una interfaz en modo texto para supervisar y controlar HAProxy desde la terminal.

Instálalo con:

```bash
sudo apt install hatop
```

Conéctate al socket administrativo configurado en `/run/haproxy/admin.sock`:

```bash
sudo hatop -s /run/haproxy/admin.sock
```

Desde la interfaz puedes:

* Ver estadísticas en tiempo real.
* Activar o desactivar servidores backend (`F9` para activar, `F10` para desactivar).
* Observar el tráfico y el estado de los nodos.

