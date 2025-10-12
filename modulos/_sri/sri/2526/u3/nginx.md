---
title: "Introducción al servidor web Nginx"
---

## Introducción a Nginx

**Nginx** (pronunciado *engine-x*) es un servidor web libre y de código abierto diseñado para ser **ligero, rápido y eficiente**.
Además de servir contenido estático, puede funcionar como **proxy inverso**, **balanceador de carga**, **servidor de correo** o **gateway** para aplicaciones web.

Se caracteriza por su:

* **Alto rendimiento**: utiliza un modelo de ejecución asíncrono basado en eventos, capaz de manejar miles de conexiones simultáneas.
* **Bajo consumo de recursos**: su arquitectura evita crear un proceso por conexión.
* **Versatilidad**: combina funciones de servidor web y proxy en una misma herramienta.
* **Configuración modular y clara**, mediante bloques jerárquicos.

El servicio se denomina `nginx` y se gestiona con `systemctl`.
El puerto predeterminado para HTTP es el **80**, y para HTTPS el **443**.

## Instalación y estructura de ficheros

En sistemas basados en Debian/Ubuntu, Nginx se instala con:

```bash
sudo apt update
sudo apt install nginx
```

La configuración se encuentra en el directorio `/etc/nginx/`, con la siguiente estructura:

| Archivo / Directorio | Descripción                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------- |
| `nginx.conf`         | Archivo principal de configuración global.                                                   |
| `conf.d/`            | Fragmentos de configuración adicionales cargados por defecto.                                |
| `sites-available/`   | Archivos de configuración de sitios web disponibles.                                         |
| `sites-enabled/`     | Enlaces simbólicos a los sitios activos.                                                     |
| `snippets/`          | Fragmentos reutilizables de configuración (por ejemplo, cabeceras comunes o parámetros TLS). |
| `/var/www/`          | Directorio raíz para los contenidos servidos.                                                |
| `/var/log/nginx/`    | Registros de acceso y error.                                                                 |


## Servidores virtuales (Server Blocks)

En Nginx, los sitios web se configuran mediante **bloques `server`**, equivalentes a los *Virtual Hosts* de Apache.
Cada bloque define un conjunto de directivas que determinan cómo se atienden las peticiones.

**Ejemplo básico:**

```nginx
server {
    listen 80;
    server_name ejemplo.com www.ejemplo.com;

    root /var/www/ejemplo;
    index index.html index.htm;

    access_log /var/log/nginx/ejemplo_access.log;
    error_log /var/log/nginx/ejemplo_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Tras crear el archivo en `/etc/nginx/sites-available/ejemplo`, se activa con:

```bash
sudo ln -s /etc/nginx/sites-available/ejemplo /etc/nginx/sites-enabled/
sudo systemctl reload nginx
```

Para desactivar un sitio:

```bash
sudo rm /etc/nginx/sites-enabled/ejemplo
sudo systemctl reload nginx
```

En Nginx, cuando se definen varios **bloques `server`** que escuchan en el mismo puerto (por ejemplo, el 80 para HTTP o el 443 para HTTPS), el servidor debe saber **cuál utilizar por defecto** cuando recibe una petición que **no coincide con ningún `server_name`** configurado.

Para marcar un bloque como predeterminado, se añade la palabra clave `default_server` en la directiva `listen`:

```nginx
server {
    listen 80 default_server;
    server_name _;
    root /var/www/html;
}
```

* `default_server` indica que este bloque se utilizará **si ninguna otra definición de servidor coincide** con la petición.
* El valor de `server_name` `_` (guion bajo) se emplea convencionalmente para representar un nombre “vacío” o genérico.


## Registros de acceso y error

**Nginx** también mantiene registros detallados de actividad y errores, que resultan clave para supervisar el funcionamiento del servidor. Por defecto, los logs se encuentran en el directorio `/var/log/nginx/`.

Los dos ficheros principales para el VirtualHost default son:

| Archivo      | Descripción                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `access.log` | Registra todas las peticiones atendidas por Nginx. Incluye IP, fecha, método, recurso solicitado, código de estado y tamaño de la respuesta. |
| `error.log`  | Registra errores en la ejecución del servidor o en la configuración.                                                                         |

Cada bloque `server` puede definir sus propios ficheros de registro:

```nginx
server {
    listen 80;
    server_name ejemplo.com;
    root /var/www/ejemplo;

    access_log /var/log/nginx/ejemplo_access.log;
    error_log /var/log/nginx/ejemplo_error.log warn;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

El parámetro opcional (`warn`, `error`, `info`, `debug`) determina el nivel de detalle del log de errores.

Para ver los lgos tenemos algunos comandos básicos:

```bash
# Mostrar las últimas entradas
sudo tail /var/log/nginx/access.log
sudo tail /var/log/nginx/error.log

# Seguimiento en tiempo real
sudo tail -f /var/log/nginx/error.log
```

Para ver todos los mensajes gestionados por *systemd*:

```bash
sudo journalctl -u nginx
```

## Mapear URL a ubicaciones del sistema de ficheros

La directiva `location` permite asociar rutas de URL con directorios o recursos del sistema de ficheros.
Es la base del manejo de peticiones en Nginx.

**Ejemplo:**

```nginx
server {
    listen 80;
    server_name ejemplo.com;

    location /imagenes/ {
        alias /srv/recursos/imagenes/;
        autoindex on;
    }
}
```

En este caso, al acceder a `http://ejemplo.com/imagenes/`, se servirán los ficheros del directorio `/srv/recursos/imagenes/`.

## Opciones de directorio y listados

Nginx no utiliza bloques `<Directory>` como Apache, pero se pueden controlar comportamientos similares dentro de los bloques `location`.

Para permitir el **listado de directorios**, se usa la directiva `autoindex on`.

**Ejemplo:**

```nginx
location /descargas/ {
    root /var/www/;
    autoindex on;
    autoindex_exact_size off;
    autoindex_localtime on;
}
```

Esto mostrará el listado de archivos disponibles en `/var/www/descargas/`.


En **Nginx**, **no existe una directiva equivalente a `Options FollowSymLinks`**, porque el servidor **siempre sigue los enlaces simbólicos** de forma predeterminada, **si el usuario del proceso tiene permisos** para acceder al destino del enlace.

Es decir:

* Si el usuario que ejecuta Nginx (habitualmente `www-data`) puede leer el archivo o directorio al que apunta el enlace simbólico, Nginx servirá el contenido sin problema.
* Si no tiene permisos, devolverá un error **403 Forbidden**.


## Redirecciones

Nginx permite redirigir peticiones hacia otras rutas o sitios mediante la directiva `return` o `rewrite`.

**Redirección permanente (301):**

```nginx
server {
    listen 80;
    server_name viejo.ejemplo.com;
    return 301 http://nuevo.ejemplo.com$request_uri;
}
```

**Redirección temporal (302):**

```nginx
location /mantenimiento/ {
    return 302 /aviso.html;
}
```

**Reescritura de URL con expresiones regulares:**

```nginx
location /blog/ {
    rewrite ^/blog/(.*)$ /articulos/$1 permanent;
}
```

## Autenticación básica

Nginx permite habilitar **autenticación HTTP básica** mediante el módulo `auth_basic`.

**Ejemplo de configuración:**

```nginx
location /privado/ {
    auth_basic "Zona restringida";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
```

El archivo `.htpasswd` se genera con la utilidad `htpasswd` (del paquete `apache2-utils`):

```bash
sudo htpasswd -c /etc/nginx/.htpasswd usuario1
```

Al acceder al directorio `/privado/`, el navegador solicitará usuario y contraseña.

**Nota:** Al igual que en Apache, las credenciales se envían codificadas en Base64, por lo que se recomienda utilizar HTTPS para proteger la comunicación.


Perfecto.
Aquí tienes el apartado **“Control de acceso”** reescrito para Nginx, manteniendo el mismo estilo formal que el resto de tus apuntes, e incluyendo tanto el **control por IP/red** como el **control por autenticación de usuario**.

## Control de acceso

Nginx permite restringir el acceso a los recursos del servidor mediante dos mecanismos principales:

1. **Control por dirección IP o red**, usando las directivas `allow` y `deny`.
2. **Control por autenticación de usuario**, mediante el módulo `auth_basic`.

Ambos pueden combinarse dentro de bloques `location`, `server` o `http`, lo que ofrece un control granular sobre quién puede acceder a determinadas rutas o servicios.

Las directivas `allow` y `deny` se utilizan para **permitir o denegar el acceso** según la dirección IP del cliente.

**Ejemplo básico:**

```nginx
location /admin/ {
    allow 192.168.1.0/24;
    allow 10.0.0.5;
    deny all;
}
```
* `allow 192.168.1.0/24;` → permite el acceso a todos los clientes de la red local 192.168.1.0/24.
* `allow 10.0.0.5;` → permite el acceso a una IP específica.
* `deny all;` → deniega el acceso al resto de clientes.

El orden de las directivas es importante: Nginx evalúa las reglas **en el orden en que aparecen**.

### Combianción entre control de acceso por IP y control de usuarios

Podemos combinar el control de acceso por IP y por usuario autentificado.
Por ejemplo, exigir autenticación **solo** a usuarios provenientes de redes externas:

```nginx
location /panel/ {
    # Permitir libre acceso desde la red local
    allow 192.168.1.0/24;

    # Denegar todo lo demás por defecto
    deny all;

    # Exigir autenticación solo a quienes no estén en la red local
    satisfy any;
    auth_basic "Acceso restringido";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
```
* `satisfy any;` permite el acceso si **se cumple al menos una de las condiciones**:
  o bien el cliente está autorizado por IP (`allow`), o bien proporciona credenciales válidas (`auth_basic`).
* Si se usa `satisfy all;`, se requeriría cumplir **ambas condiciones simultáneamente**.


## Archivos de inclusión (`conf.d` y `snippets`)

Nginx carga automáticamente todos los archivos con extensión `.conf` ubicados en `/etc/nginx/conf.d/`.
Estos fragmentos se usan para definir configuraciones comunes a varios sitios (por ejemplo, cabeceras de seguridad, compresión o límites de carga).

También pueden utilizarse **fragmentos reutilizables** en `/etc/nginx/snippets/`, que luego se incluyen con la directiva `include`.

**Ejemplo:**

Archivo `/etc/nginx/snippets/seguridad.conf`:

```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
```

Uso en un sitio:

```nginx
server {
    listen 80;
    include snippets/seguridad.conf;
    ...
}
```
## Módulos comunes útiles

Nginx incluye la mayoría de sus módulos compilados por defecto, aunque algunos pueden habilitarse al compilar el servidor o mediante paquetes específicos.
Los más utilizados en la administración de sitios web son los siguientes:

| Módulo                      | Función principal                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **ngx_http_rewrite_module** | Reescritura de URLs y redirecciones mediante expresiones regulares (`rewrite`, `return`). |
| **ngx_http_proxy_module**   | Configura Nginx como proxy inverso o balanceador de carga (`proxy_pass`).                 |
| **ngx_http_headers_module** | Permite modificar o añadir cabeceras HTTP (`add_header`).                                 |
| **ngx_http_ssl_module**     | Activa soporte para HTTPS/TLS.                                                            |

Ejemplo de proxy inverso:

```nginx
server {
    listen 80;
    server_name ejemplo.com;

    root /var/www/ejemplo;

    # Proxy inverso
    location /app/ {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
