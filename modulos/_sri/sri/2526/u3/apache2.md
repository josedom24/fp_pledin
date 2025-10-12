---
title: "Introducción al servidor web Apache2"
---

## Introducción a Apache

**Apache HTTP Server** (habitualmente llamado *Apache2*) es un servidor web libre y de código abierto que implementa los protocolos **HTTP** y **HTTPS**.
Su función es recibir peticiones de los clientes (normalmente navegadores web) y responder con los recursos solicitados: páginas HTML, imágenes, ficheros, resultados de scripts, etc.

Apache se caracteriza por su:

* **Modularidad**: sus funciones están organizadas en módulos cargables según necesidad.
* **Flexibilidad**: permite un control muy fino de la configuración.
* **Portabilidad**: está disponible para la mayoría de sistemas operativos.

El servicio se denomina `apache2` y se gestiona con `systemctl`.
El puerto predeterminado para HTTP es el **80**, y para HTTPS el **443**.

## Instalación y estructura de ficheros

En sistemas basados en Debian/Ubuntu, la instalación se realiza mediante:

```bash
sudo apt update
sudo apt install apache2
```

La configuración de Apache se organiza en varios archivos y directorios bajo `/etc/apache2/`:

| Archivo / Directorio                | Descripción                                                          |
| ----------------------------------- | -------------------------------------------------------------------- |
| `apache2.conf`                      | Archivo principal de configuración global.                           |
| `ports.conf`                        | Define los puertos de escucha (`Listen 80`, `Listen 443`).           |
| `sites-available/`                  | Archivos de configuración de sitios web disponibles (Virtual Hosts). |
| `sites-enabled/`                    | Enlaces simbólicos a los sitios activos.                             |
| `mods-available/`                   | Módulos disponibles en el sistema.                                   |
| `mods-enabled/`                     | Módulos habilitados actualmente.                                     |
| `conf-available/` / `conf-enabled/` | Configuraciones adicionales opcionales.                              |

## Virtual Hosts (sitios virtuales)

Apache permite alojar **múltiples sitios web en el mismo servidor** mediante *Virtual Hosts*.
Cada sitio tiene su propia configuración, definida en un archivo dentro de `sites-available/`.

Ejemplo básico de un sitio virtual:

```apache
<VirtualHost *:80>
    ServerAdmin webmaster@ejemplo.com
    ServerName ejemplo.com
    ServerAlias www.ejemplo.com
    DocumentRoot /var/www/ejemplo

    ErrorLog ${APACHE_LOG_DIR}/ejemplo_error.log
    CustomLog ${APACHE_LOG_DIR}/ejemplo_access.log combined
</VirtualHost>
```

Para activarlo:

```bash
sudo a2ensite ejemplo.conf
sudo systemctl reload apache2
```

Para desactivar un virtualhost:
```bash
sudo a2dissite ejemplo.conf
sudo systemctl reload apache2
```

La activación de un sitio virtual crea un en lace simbólico en el directorio: `sites-enabled/`. Los ficheros de este directorio forman parte de la configuración del servidor. La desactivación borra el enlace simbólico.

## Registros de acceso y error

El servidor web **Apache2** genera información sobre su funcionamiento en ficheros de log (registros), que resultan fundamentales para el diagnóstico de problemas y el análisis de tráfico.

Normalmente guardamos los logs en el directorio `/var/log/apache2/`.

El el VirtualHost por defecto, los logs se almacenan en los ficheros:

| Archivo      | Descripción                                                                                                                                                       |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access.log` | Registra todas las peticiones HTTP recibidas por el servidor. Incluye dirección IP, fecha, método, recurso solicitado, código de estado y tamaño de la respuesta. |
| `error.log`  | Registra errores del servidor, como fallos de permisos, módulos, sintaxis en configuraciones o scripts CGI.                                                       |

Cada sitio virtual puede definir sus propios ficheros de log dentro de su bloque `<VirtualHost>`:

```apache
<VirtualHost *:80>
    ServerName ejemplo.com
    DocumentRoot /var/www/ejemplo

    ErrorLog ${APACHE_LOG_DIR}/ejemplo_error.log
    CustomLog ${APACHE_LOG_DIR}/ejemplo_access.log combined
</VirtualHost>
```

El parámetro `combined` indica el formato de log más habitual, que incluye agente de usuario y referencia (referer).
Otros formatos posibles son `common` o configuraciones personalizadas mediante la directiva `LogFormat`.

Pa var los logs tenemos algunos comandos útiles:

```bash
# Ver los últimos registros
sudo tail /var/log/apache2/access.log
sudo tail /var/log/apache2/error.log

# Seguir la salida en tiempo real
sudo tail -f /var/log/apache2/error.log
```

Cuando el servicio está integrado con *systemd*, también se pueden consultar los registros recientes con:

```bash
sudo journalctl -u apache2
```


## Mapear URL a ubicaciones del sistema de ficheros

La directiva `Alias` permite servir ficheros desde cualquier ubicación del sistema de archivos, incluso fuera del `DocumentRoot`.

**Ejemplo:**

```apache
Alias "/image" "/ftp/pub/image"

<Directory "/ftp/pub/image">
    Require all granted
</Directory>
```

Al acceder a `http://servidor/image/`, el servidor ofrecerá los ficheros almacenados en `/ftp/pub/image`.
Como este directorio no forma parte del árbol principal de publicación, es necesario definir explícitamente sus permisos mediante la directiva `<Directory>`.

## Opciones de directorio

Cada directorio gestionado por Apache tiene asociadas una serie de **opciones** que determinan su comportamiento.
Estas opciones se configuran con la directiva `Options`, dentro de un bloque `<Directory>`.

Ejemplo tomado del archivo `/etc/apache2/apache2.conf`:

```apache
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
```

**Significado de las opciones mostradas:**

| Opción           | Descripción                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| `Indexes`        | Si no existe un fichero índice (por ejemplo `index.html`), muestra el listado del contenido del directorio. |
| `FollowSymLinks` | Permite seguir enlaces simbólicos y servir el contenido al que apuntan.                                     |

Existen otras opciones posibles (como `ExecCGI`, `Includes`, `MultiViews`, etc.) que no se abordan en esta introducción.
Para subdirectorios, se pueden **añadir** o **quitar** opciones usando los signos `+` y `-`.
Ejemplo: `Options -Indexes +ExecCGI`

## Redirecciones

Apache permite redirigir peticiones hacia nuevas ubicaciones utilizando la directiva `Redirect`.
Esto es útil cuando los recursos cambian de ubicación o cuando se desea forzar el acceso a otra URL.

**Ejemplos de redirección temporal (código 302):**

```apache
Redirect "/service" "http://www.pagina.com/service"
Redirect "/old" "/new"
```

**Ejemplos de redirección permanente (código 301):**

```apache
Redirect permanent "/uno" "http://www.pagina2.com/dos"
Redirect 301 "/otro" "/otra"
```

También puede emplearse `RedirectMatch` para redirecciones basadas en expresiones regulares:

```apache
RedirectMatch "(.*)\.gif$" "http://www.pagina2.org/$1.jpg"
RedirectMatch ^/$ https://openstack.gonzalonazareno.org/horizon/
```
## Control de acceso

El control de acceso permite **restringir o permitir** el acceso a los recursos del servidor según distintos criterios, como direcciones IP, nombres de host o usuarios autenticados.

En Apache 2.4 y versiones posteriores, esto se gestiona mediante la directiva `Require`.

**Ejemplos:**

```apache
Require all granted        # Permitir acceso a todos
Require all denied          # Denegar acceso a todos
Require ip 192.168.1        # Permitir solo desde una red local
Require host dominio.com    # Permitir solo desde un dominio concreto
Require user usuario1       # Permitir a un usuario determinado
Require group grupo1        # Permitir a un grupo determinado
Require valid-user          # Permitir a cualquier usuario autenticado
```

**Nota:**: Las antiguas directivas `order`, `allow` y `deny` utilizadas en Apache 2.2 están obsoletas.

## Autenticación básica

Apache permite proteger el acceso a recursos mediante autenticación.
El método más sencillo es la **autenticación básica**, proporcionada por el módulo `mod_auth_basic`, que suele estar habilitado por defecto.

Ejemplo de configuración:

```apache
<Directory "/var/www/miweb/privado">
    AuthUserFile "/etc/apache2/claves/passwd.txt"
    AuthName "Zona restringida"
    AuthType Basic
    Require valid-user
</Directory>
```

**Descripción de las directivas:**

* `AuthType Basic`: especifica el tipo de autenticación.
* `AuthName`: define el mensaje mostrado al usuario.
* `AuthUserFile`: indica el fichero que contiene los usuarios y contraseñas.
* `Require valid-user`: permite el acceso únicamente a usuarios autenticados.

El archivo de contraseñas se crea con la herramienta `htpasswd`:

```bash
# Crear el fichero y añadir el primer usuario
htpasswd -c /etc/apache2/claves/passwd.txt carolina

# Añadir usuarios adicionales
htpasswd /etc/apache2/claves/passwd.txt jose
```

El fichero almacena los nombres de usuario junto con contraseñas cifradas mediante una función hash.
Para revocar el acceso a un usuario basta con eliminar su línea del fichero.

**Nota:**: Las credenciales se transmiten codificadas en Base64, pero **no cifradas**.
**Nota:**: Se recomienda combinar la autenticación básica con **HTTPS** para proteger la comunicación.

## Archivos `.htaccess`

Un archivo `.htaccess` (HyperText Access) es un fichero de configuración distribuida que permite aplicar directivas específicas en un directorio determinado, sin modificar los archivos principales de Apache.

Para habilitar su uso, se utiliza la directiva `AllowOverride` dentro del bloque `<Directory>` correspondiente:

```apache
<Directory /var/www/html>
    AllowOverride All
</Directory>
```

**Valores posibles de `AllowOverride`:**

| Valor                                           | Descripción                                                        |
| ----------------------------------------------- | ------------------------------------------------------------------ |
| `All`                                           | Permite todas las directivas posibles en `.htaccess`.              |
| `None`                                          | Desactiva completamente el uso de `.htaccess` (valor por defecto). |
| `AuthConfig`, `FileInfo`, `Indexes`, `Limit`, … | Permite únicamente grupos específicos de directivas.               |

El uso de `.htaccess` es útil cuando los usuarios no tienen acceso al archivo de configuración principal, aunque puede afectar al rendimiento del servidor si se abusa de él.

Perfecto.
Aquí tienes el siguiente apartado redactado con el mismo estilo formal que los anteriores, dedicado a **los módulos comunes útiles de Apache2**, con explicaciones claras sobre cómo se activan y una selección de los más relevantes (incluyendo `rewrite`, `proxy`, `headers`, `deflate`, `expires` y `ssl`).

## Módulos comunes útiles

El servidor web **Apache2** está construido sobre una arquitectura **modular**, lo que significa que la mayoría de sus funcionalidades se implementan a través de **módulos** (*modules*).
Cada módulo amplía las capacidades del servidor, y puede **activarse o desactivarse dinámicamente** según las necesidades del administrador.

En sistemas Debian/Ubuntu, los módulos disponibles se almacenan en el directorio `/etc/apache2/mods-available/`, y los que están activos aparecen como enlaces simbólicos en `/etc/apache2/mods-enabled/`.

Para habilitar o deshabilitar módulos se utilizan los comandos:

```bash
sudo a2enmod nombre_modulo     # Habilita el módulo
sudo a2dismod nombre_modulo    # Deshabilita el módulo
sudo systemctl reload apache2  # Aplica los cambios sin reiniciar
```

Veamos algunos ejemplos de módulos:

### `mod_rewrite`: Reescritura de URLs

El módulo **`mod_rewrite`** permite reescribir o redirigir URLs de forma flexible mediante **expresiones regulares**.
Es ampliamente utilizado para mejorar la legibilidad de las URLs, redirigir rutas antiguas, o aplicar reglas de acceso.

**Ejemplo de uso:**

```apache
<Directory /var/www/html>
    Options FollowSymLinks
    AllowOverride All
</Directory>
```

En un archivo `.htaccess` o en la configuración del sitio:

```apache
RewriteEngine On
RewriteRule ^productos/(.*)$ /tienda.php?item=$1 [L]
```

Esto convierte una petición como `/productos/camiseta` en una llamada interna a `/tienda.php?item=camiseta`.

### `mod_proxy`: Proxy directo e inverso

El módulo **`mod_proxy`** permite que Apache actúe como **servidor proxy**, reenviando peticiones hacia otros servidores o aplicaciones.
En combinación con submódulos como `mod_proxy_http`, `mod_proxy_balancer` o `mod_proxy_ftp`, puede configurarse como **proxy inverso** o **balanceador de carga**.

**Ejemplo (proxy inverso):**

```apache
<VirtualHost *:80>
    ServerName app.ejemplo.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8080/
    ProxyPassReverse / http://127.0.0.1:8080/
</VirtualHost>
```

Esto permite que Apache escuche en el puerto 80 y reenvíe las peticiones a una aplicación que corre internamente en el puerto 8080 (por ejemplo, un servicio Node.js o Python).

Para utilizarlo, deben activarse los módulos:

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl reload apache2
```

Perfecto.
Aquí tienes el apartado **“Configuración adicional”**, redactado con el mismo estilo formal y didáctico que los anteriores, e incluyendo un ejemplo práctico:

## Configuración adicional

Además de los ficheros de configuración principales y los sitios virtuales, **Apache2** permite definir fragmentos de configuración adicionales que pueden habilitarse o deshabilitarse de forma modular.
Estas configuraciones se almacenan en el directorio:

```
/etc/apache2/conf-available/
```

y las que estén activas aparecerán como **enlaces simbólicos** en:

```
/etc/apache2/conf-enabled/
```

Esto proporciona una forma flexible de **añadir parámetros globales o comunes** sin modificar directamente el archivo principal `apache2.conf`.

Para habilitar una configuración adicional se utiliza el comando:

```bash
sudo a2enconf nombre_configuracion
```

y para deshabilitarla:

```bash
sudo a2disconf nombre_configuracion
```

Después de realizar cualquier cambio, se recomienda recargar el servicio para aplicar la configuración:

```bash
sudo systemctl reload apache2
```

