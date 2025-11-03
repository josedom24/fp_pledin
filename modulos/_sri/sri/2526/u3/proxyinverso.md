---
title: "Proxy inverso con Apache2 y Nginx"
---

## Introducción al proxy inverso

Un **proxy inverso** es un tipo de servidor que actúa como intermediario entre los **clientes externos** y uno o varios **servidores internos** (*backends*).
Cuando un cliente realiza una petición (normalmente por HTTP o HTTPS), el proxy la recibe, la reenvía al servidor interno y devuelve la respuesta al cliente como si procediera del propio proxy.

Este mecanismo se utiliza principalmente para:

* **Proteger** los servidores internos, que no son accesibles directamente desde el exterior.
* **Centralizar el acceso** a varias aplicaciones internas bajo un único dominio.
* **Distribuir carga** entre varios backends (balanceo).
* **Terminar conexiones HTTPS** (TLS termination).
* **Añadir cabeceras o filtros** de seguridad, compresión o autenticación.
* **Reescribir rutas o redirecciones** para adaptarlas al espacio público.

**Esquema general:**

```
Cliente (HTTP/HTTPS)
        │
        ▼
 Proxy inverso (80/443)
        │
        ▼
Servidor interno (p.ej. 10.0.0.2:8080)
```

## Apache2 como proxy inverso

Apache2 puede actuar como proxy inverso mediante el módulo `mod_proxy` y sus submódulos especializados (por ejemplo, `mod_proxy_http` para HTTP).
Para habilitar esta funcionalidad:

```bash
sudo a2enmod proxy proxy_http
sudo systemctl reload apache2
```

### Proxy desde la raíz (`/`)

Configuración básica en un *VirtualHost* para redirigir todas las peticiones entrantes (`/`) a un servidor interno:

```apache
<VirtualHost *:80>
    ServerName proxy.example.org

    ProxyPass "/" "http://interno.example.org/"
    ProxyPassReverse "/" "http://interno.example.org/"

    ErrorLog ${APACHE_LOG_DIR}/proxy_error.log
    CustomLog ${APACHE_LOG_DIR}/proxy_access.log combined
</VirtualHost>
```

**Explicación de las directivas:**

* `ProxyPass`: redirige las solicitudes entrantes hacia el servidor interno (`backend`).
* `ProxyPassReverse`: reescribe las cabeceras de respuesta (`Location`, `Content-Location`) para que las URLs devueltas sean las públicas.

### Problema de redirecciones

Cuando el backend responde con una redirección HTTP (cabecera `Location`), suele incluir su propio dominio interno, por ejemplo:

```
Location: http://interno.example.org/login
```

El cliente, al recibir esa cabecera, intentará acceder directamente a la dirección interna, que no es accesible desde el exterior.

**Solución:**

`ProxyPassReverse` reescribe esas cabeceras, reemplazando la URL interna por la pública, de modo que el cliente vea:

```
Location: http://proxy.example.org/login
```

Esto garantiza que las redirecciones funcionen correctamente desde el exterior.


### Proxy inverso usando una ruta

También es posible publicar una aplicación interna bajo una **subruta** específica del dominio público:

```apache
ProxyPass "/web/" "http://interno.example.org/"
ProxyPassReverse "/web/" "http://interno.example.org/"
```

El cliente accederá a `http://proxy.example.org/web/`, mientras Apache reenviará internamente las peticiones a `http://interno.example.org/`.

Este enfoque permite ofrecer varios servicios desde el mismo dominio (por ejemplo `/api/`, `/web/`, `/admin/`).

### Envío de cabeceras

Cuando Apache actúa como proxy inverso, puede **modificar, añadir o conservar cabeceras HTTP** para transmitir al servidor interno información sobre la petición original del cliente.

#### Propósito del envío de cabeceras

El envío de cabeceras adicionales permite que el backend conozca:

* el **dominio público** al que accedió el cliente (`Host`);
* la **IP real** del cliente, no la del proxy;
* el **protocolo original** (`http` o `https`);
* y los **proxys intermedios** por los que pasó la solicitud.

Esto es esencial para:

* registrar correctamente la IP de los usuarios;
* generar redirecciones o URLs correctas desde el backend;
* aplicar reglas de autenticación o seguridad dependientes del dominio o protocolo.

#### Conservación y envío de cabeceras

Para controlar el envío de cabeceras, Apache usa el módulo `mod_headers`.
Podemos conservar el `Host` original y añadir cabeceras adicionales como sigue:

```apache
# Conservar el dominio solicitado por el cliente
ProxyPreserveHost On

# Añadir cabeceras informativas al backend
RequestHeader set X-Real-IP "%{REMOTE_ADDR}s"
RequestHeader add X-Forwarded-For "%{REMOTE_ADDR}s"
RequestHeader set X-Forwarded-Proto "http"
RequestHeader set X-Forwarded-Host "%{HTTP_HOST}s"
```

**Cabeceras comunes y su propósito:**

| Cabecera            | Propósito                                        |
| ------------------- | ------------------------------------------------ |
| `Host`              | Dominio solicitado originalmente                 |
| `X-Real-IP`         | IP real del cliente                              |
| `X-Forwarded-For`   | Lista de IPs de proxies intermedios              |
| `X-Forwarded-Proto` | Protocolo del cliente (HTTP o HTTPS)             |
| `X-Forwarded-Host`  | Host solicitado originalmente (similar a `Host`) |

Estas cabeceras ayudan a que el servidor interno tenga una visión completa del contexto real de la solicitud, especialmente útil cuando hay varios niveles de proxy o balanceo de carga.


## Nginx como proxy inverso

Nginx incorpora de forma nativa la funcionalidad de proxy inverso y balanceo de carga, sin módulos adicionales.

### Proxy desde la raíz (`/`)

Configuración básica:

```nginx
server {
    listen 80;
    server_name proxy.example.org;

    location / {
        proxy_pass http://interno.example.org/;
        include proxy_params;
    }

    access_log /var/log/nginx/proxy_access.log;
    error_log /var/log/nginx/proxy_error.log;
}
```

El archivo `/etc/nginx/proxy_params` contiene los parámetros estándar de reenvío de cabeceras (se detalla más adelante).

### Problema de redirecciones

Al igual que en Apache, las redirecciones del backend pueden apuntar a la URL interna.
Para corregirlo, se utiliza la directiva `proxy_redirect`:

```nginx
proxy_redirect http://interno.example.org/ /;
```

Esto reescribe las cabeceras `Location` y `Refresh` en las respuestas del backend, sustituyendo las rutas internas por las del proxy público.

### Proxy inverso usando una ruta

Para ofrecer un servicio interno bajo una ruta específica (por ejemplo `/web/`):

```nginx
location /web/ {
    proxy_pass http://interno.example.org/;
    include proxy_params;
}
```

El cliente accede a `http://proxy.example.org/web/`, mientras Nginx redirige las peticiones internamente al backend.

### Envío de cabeceras

Nginx envía automáticamente varias cabeceras al backend para conservar información sobre el cliente.
Estas se definen en `/etc/nginx/proxy_params` (archivo incluido en la mayoría de configuraciones):

```nginx
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

**Cabeceras estándar:**

| Cabecera            | Propósito                                   | Variable                     |
| ------------------- | ------------------------------------------- | ---------------------------- |
| `Host`              | Host solicitado por el cliente              | `$http_host`                 |
| `X-Real-IP`         | IP real del cliente                         | `$remote_addr`               |
| `X-Forwarded-For`   | Cadena de IPs de los proxies intermedios    | `$proxy_add_x_forwarded_for` |
| `X-Forwarded-Proto` | Protocolo usado por el cliente (HTTP/HTTPS) | `$scheme`                    |

Estas cabeceras permiten que el servidor interno conozca el contexto de la solicitud original y genere respuestas coherentes (por ejemplo, URLs correctas en redirecciones o registros de auditoría con la IP real del usuario).


## Resumen comparativo

| Aspecto                        | Apache2                            | Nginx                                 |
| ------------------------------ | ---------------------------------- | ------------------------------------- |
| Módulos necesarios             | `mod_proxy`, `mod_proxy_http`      | Nativo                                |
| Reescritura de redirecciones   | `ProxyPassReverse`                 | `proxy_redirect`                      |
| Proxy en subruta               | `ProxyPass /ruta/ http://...`      | `location /ruta/ { proxy_pass ...; }` |
| Conserva cabecera `Host`       | `ProxyPreserveHost On`             | `proxy_set_header Host $http_host`    |
| Envío de cabeceras del cliente | `RequestHeader set/add ...`        | `proxy_set_header ...`                |
| Archivo de configuración común | `/etc/apache2/sites-available/...` | `/etc/nginx/proxy_params`             |

