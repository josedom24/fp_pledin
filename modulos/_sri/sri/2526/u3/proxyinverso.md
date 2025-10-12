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

Apache2 puede actuar como proxy inverso mediante el módulo `mod_proxy` y sus submódulos especializados. Para habilitar la funcionalidad básica de proxy inverso:

```bash
sudo a2enmod proxy proxy_http
sudo systemctl reload apache2
```

Ejemplo de *VirtualHost* configurado como proxy inverso:

```apache
<VirtualHost *:80>
    ServerName proxy.example.org

    ProxyPreserveHost On
    ProxyPass "/" "http://interno.example.org/"
    ProxyPassReverse "/" "http://interno.example.org/"

    ErrorLog ${APACHE_LOG_DIR}/proxy_error.log
    CustomLog ${APACHE_LOG_DIR}/proxy_access.log combined
</VirtualHost>
```

* `ProxyPass` redirige las peticiones al servidor interno.
* `ProxyPassReverse` reescribe las cabeceras `Location` de las respuestas (para que el cliente vea la URL pública).
* `ProxyPreserveHost On` mantiene la cabecera `Host` original del cliente, útil para aplicaciones que dependen del dominio.


### Publicar una aplicación en una ruta

Si queremos ofrecer el servicio interno en una subruta, por ejemplo `/web/`:

```apache
ProxyPass "/web/" "http://interno.example.org/"
ProxyPassReverse "/web/" "http://interno.example.org/"
```

El cliente accederá a `http://proxy.example.org/web/`, mientras Apache reenviará las peticiones a `http://interno.example.org/`.


### Problemas habituales

| Situación                                     | Causa                                       | Solución                               |
| --------------------------------------------- | ------------------------------------------- | -------------------------------------- |
| Las redirecciones apuntan al servidor interno | Falta `ProxyPassReverse`                    | Añadir `ProxyPassReverse`              |
| Recursos no cargan (rutas absolutas en HTML)  | Rutas absolutas en `/` o uso de IP interna  | Usar rutas relativas o reescribir HTML |
| La aplicación necesita el `Host` original     | Cabecera `Host` sustituida por la del proxy | Usar `ProxyPreserveHost On`            |


## Nginx como proxy inverso

Nginx tiene soporte nativo para proxy inverso y balanceo, sin necesidad de módulos adicionales.
Las directivas relacionadas comienzan con el prefijo `proxy_`.

Veamos la configuración básica:

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

El archivo `/etc/nginx/proxy_params` contiene los parámetros estándar para reenviar cabeceras del cliente al servidor interno:

```nginx
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

**Significado:**

| Cabecera            | Propósito                                      | Variable                     |
| ------------------- | ---------------------------------------------- | ---------------------------- |
| `Host`              | Nombre del host solicitado por el cliente      | `$http_host`                 |
| `X-Real-IP`         | IP real del cliente                            | `$remote_addr`               |
| `X-Forwarded-For`   | Cadena de IPs de los proxys intermedios        | `$proxy_add_x_forwarded_for` |
| `X-Forwarded-Proto` | Protocolo de conexión del cliente (HTTP/HTTPS) | `$scheme`                    |


### Publicar una aplicación en una ruta

Para acceder a un backend bajo una subruta:

```nginx
location /web/ {
    proxy_pass http://interno.example.org/;
    include proxy_params;
}
```

El cliente accederá a `http://proxy.example.org/web/`, mientras Nginx reenviará internamente a `http://interno.example.org/`.


### Reescritura de redirecciones

Cuando el servidor interno envía una redirección (`Location: http://interno.example.org/...`), Nginx debe reemplazar esa dirección por la pública.
Esto se logra con la directiva `proxy_redirect`:

```nginx
proxy_redirect http://interno.example.org/ /;
```

Similar al uso de `ProxyPassReverse` en Apache2.

