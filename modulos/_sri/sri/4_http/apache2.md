---
title: "Configuración básica de Apache2"
---

## Mapear URL a ubicaciones de un sistema de ficheros

* **Alias**: La directiva [Alias](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#alias) nos permite que el servidor sirva ficheros desde cualquier ubicación del sistema de archivo aunque esté fuera del directorio indicado en el *DocumentRoot*. Ejemplo:

	```
	Alias "/image" "/ftp/pub/image"
	<Directory "/ftp/pub/image">
	    Require all granted
	</Directory>
	```
	
	Cuando accedamos a la ruta `image` se estarán sirviendo los ficheros que se encuentran en `/ftp/pub/image`. como este directorio no tiene los permisos de apache2 definidos tenemos que definirlos con una directiva `Directory`. 
	
* **Opciones de directorio**: Todos los directorios servidos por el servidor web tienen definida una serie de opciones. Para ello usamos la directiva [Options](http://httpd.apache.org/docs/2.4/mod/core.html#options). Veamos las opciones que tiene el directorio `/var/www` definido en el fichero `/etc/apache2/apache2.conf` (recuerda que la directiva `Directory` afecta al directorio indicado y a todos sus subdirectorios):

	```
	<Directory /var/www/>
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>
	```
	
	* `Indexes`: Si no existe un fichero con un nombre por defecto (`index.html`, `index.php`,...) muestra la lista de ficheros y directorios que hay en el *DocumentRoot*.
	* `FollowSymLinks`: El servidor web servirá el contenido de un fichero o directorio apuntado por un enlace simbólico que este en el *DocumentRoot*.

	Existen más opciones que no vamos a estudiar en este curso. Si defino una sección `Directory` para un subdirectorio podremos quitar opciones usando el signo `-` y añadirle usando el símbolo `+`.

* **Redirecciones**: La directiva [Redirect](http://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirect) nos permite crear redirecciones temporales o permanentes. La directiva `redirect` es usada para pedir al cliente que haga otra petición a una URL diferente. Normalmente la usamos cuando el recurso al que queremos acceder **ha cambiado de localización**.

	Ejemplos de redirección temporal (302):

	```
	Redirect "/service" "http://www.pagina.com/service"
	Redirect "/one" "/two"
	```

	Ejemplos de redirecciones permanentes (301):

	```
	Redirect permanent "/one" "http://www.pagina2.com/two"
	Redirect 301 "/otro" "/otra"
	```

	También se puede usar la directiva `RedirectMatch` para trabajar con expresiones regulares:

	```
	RedirectMatch "(.*)\.gif$" "http://www.pagina2.org/$1.jpg"
	```
	Por ejemplo, para al entrar en una página se redireccione a un subdirectorio:

	```
	RedirectMatch ^/$ https://openstack.gonzalonazareno.org/horizon/
	```
	
## Control de acceso, autentificación y autorización

### Control de acceso

El **Control de acceso** en un servidor web nos permite determinar desde donde podemos acceder a los recursos del servidor.

**No lo vamos a utilizar, pero nos podemos encontrar directivas de control de acceso para la versión Apache 2.2**: En **apache2.2** se utilizan las siguientes directivas: [order](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#order), [allow](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#allow) y [deny](http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html#deny). La directiva [satisfy](http://httpd.apache.org/docs/2.2/mod/core.html#satisfy) controla como el se debe comportar el servidor cuando tenemos autorizaciones de control de acceso (allow, deny,...) y tenemos autorizaciones de usuarios (require).

En **apache2.4** se utilizan las siguientes directivas: [Require](https://httpd.apache.org/docs/2.4/es/mod/mod_authz_core.html#require), [RequireAll](https://httpd.apache.org/docs/2.4/es/mod/mod_authz_core.html#requireall), [RequireAny](https://httpd.apache.org/docs/2.4/es/mod/mod_authz_core.html#requireany) y [RequireNone](https://httpd.apache.org/docs/2.4/es/mod/mod_authz_core.html#requirenone).

Veamos algunos ejemplos:

* El acceso es permitido: `Require all granted`.
* El acceso es denegado: `Require all denied`.

Otros ejemplos:

```
Require user userid [userid] ...
Require group group-name [group-name] ...
Require valid-user
Require ip 10 172.20 192.168.2
Require host dominio
```

###  Autentificación básica

El servidor web Apache puede acompañarse de distintos módulos para proporcionar diferentes modelos de autenticación.
La primera forma que veremos es la más simple. Usamos para ello el módulo de autenticación básica que viene instalada "de serie" con cualquier Apache: [mod_auth_basic](http://httpd.apache.org/docs/2.4/es/mod/mod_auth_basic.html). La configuración que tenemos que añadir en el fichero de definición del Virtual Host a proteger podría ser algo así:

  ```bash
  <Directory "/var/www/miweb/privado">
    AuthUserFile "/etc/apache2/claves/passwd.txt"
    AuthName "Palabra de paso"
    AuthType Basic
    Require valid-user
  </Directory>
  ```

El método de autentificación básica se indica en la directiva [AuthType](http://httpd.apache.org/docs/2.4/es/mod/core.html#authtype).  

* En ``Directory`` escribimos el directorio a proteger, que puede ser el raíz de nuestro Virtual Host o un directorio interior a este. 
* En [AuthUserFile](http://httpd.apache.org/docs/2.4/es/mod/mod_authn_file.html#authuserfile) ponemos el fichero que guardará la información de usuarios y contraseñas que debería de estar, como en este ejemplo, en un directorio que no sea visitable desde nuestro Apache. Ahora comentaremos la forma de generarlo. 
* Por último, en [AuthName](http://httpd.apache.org/docs/2.4/es/mod/core.html#authname) personalizamos el mensaje que aparecerá en la ventana del navegador que nos pedirá la contraseña.
* Para controlar el control de acceso, es decir, que usuarios tienen permiso para obtener el recurso utilizamos las siguientes directivas: [AuthGroupFile](http://httpd.apache.org/docs/2.4/es/mod/mod_authz_groupfile.html#authgroupfile), [Require user](http://httpd.apache.org/docs/2.4/es/mod/core.html#require), [Require group](http://httpd.apache.org/docs/2.4/es/mod/core.html#require).

El fichero de contraseñas se genera mediante la utilidad ``htpasswd``. Su sintaxis es bien sencilla. Para añadir un nuevo usuario al fichero operamos así:

    $ htpasswd /etc/apache2/claves/passwd.txt carolina
    New password:
    Re-type new password:
    Adding password for user carolina

Para crear el fichero de contraseñas con la introducción del primer usuario tenemos que añadir la opción ``-c`` (create) al comando anterior. Si por error la seguimos usando al incorporar nuevos usuarios borraremos todos los anteriores, así que cuidado con esto. Las contraseñas, como podemos ver a continuación, no se guardan en claro. Lo que se almacena es el resultado de aplicar una [función hash](http://es.wikipedia.org/wiki/Hash):

    josemaria:rOUetcAKYaliE
    carolina:hmO6V4bM8KLdw
    alberto:9RjyKKYK.xyhk

Para denegar el acceso a algún usuario basta con que borremos la línea correspondiente al mismo. No es necesario que le pidamos a Apache que vuelva a leer su configuración cada vez que hagamos algún cambio en este fichero de contraseñas.

 La principal ventaja de este método es su sencillez. Sus inconvenientes: lo incómodo de delegar la generación de nuevos usuarios en alguien que no sea un administrador de sistemas o de hacer un front-end para que sea el propio usuario quien cambie su contraseña. Y, por supuesto, que dichas contraseñas viajan en claro a través de la red. Si queremos evitar esto último podemos usa HTTPS.

**Cómo funciona este método de autentificación**

Cuando desde el cliente intentamos acceder a una URL que esta controlada por el método de autentificación básico:

1. El servidor manda una respuesta del tipo 401 *HTTP/1.1 401 Authorization Required* con  una cabecera *WWW-Authenticate* al cliente de la forma:

    ```bash
    WWW-Authenticate: Basic realm="Palabra de paso"
    ```

2. El navegador del cliente muestra una ventana emergente preguntando por el nombre de usuario y contraseña y cuando se rellena se manda una petición con una cabecera *Authorization*

    ```bash
    Authorization: Basic am9zZTpqb3Nl
    ```

En realidad la información que se manda es el nombre de usuario y la contraseña en base 64, que se puede decodificar fácilmente con cualquier [utilidad](http://www.base64decode.org/).

Existe otro tipo de autentificación llamada **digest** que añade más seguridad a la transmisión de las credenciales. En la actualidad se recomienda usar https para el envío de credenciales por lo que con la autentificación básica es suficiente.

### Políticas de autentificación y control de acceso

¿Cómo se debe comportar el servidor cuando tenemos restricciones de acceso y usuarios autentificados?. Podemos indicar políticas de autentificación y control de acceso usando las siguientes directivas: `RequireAll`, `RequireAny` y `RequireNone`:

* `RequireAll`: Todas las condiciones dentro del bloque se deben cumplir para obtener el acceso.
* `RequireAny`: Al menos una de las condiciones en el bloque se debe cumplir.
* `RequireNone`: Ninguna de las condiciones se deben cumplir para permitir el acceso.

Ejemplo:

```
<RequireAny>
    <RequireAll>
        Require user root
        Require ip 123.123.123.123
    </RequireAll>
    <RequireAll>
        <RequireAny>
            Require group sysadmins
            Require group useraccounts
            Require user anthony
        </RequireAny>
        <RequireNone>
            Require group restrictedadmin
            Require host bad.host.com
        </RequireNone>
    </RequireAll>
</RequireAny>
```

## Configuración de apache mediante fichero `.htaccess`

Un fichero `.htaccess` (hypertext access), también conocido como archivo de configuración distribuida, es un fichero especial, popularizado por el Servidor HTTP Apache que nos permite definir diferentes directivas de configuración para cada directorio (con sus respectivos subdirectorios) sin necesidad de editar el archivo de configuración principal de Apache.

Para permitir el uso de los ficheros `.htaccess` o restringir las directivas que se pueden aplicar usamos la directiva [AllowOverride](http://httpd.apache.org/docs/2.4/mod/core.html#allowoverride), que puede ir acompañada de una o varias opciones: `All`: Se permiten todas las directivas; `None`: No se permite el uso de ficheros `.htaccess` (valor por defecto para `/var/www`). Se pueden limitar las directivas que se pueden usar indicando el grupo: `AuthConfig`, `FileInfo`, `Indexes`, `Limit`, ...

## Módulos en apache2

Los módulos añaden nuevas funcionalidades a nuestro servidor web apache2. Hay muchos módulos que están habilitados desde que instalamos el servidor, y otros que están instalados pero no habilitados. También podemos instalar nuevos módulos que no están instalados (`apt search libapache2-mod`).

Los módulos disponibles y sus configuraciones se encuentran en el directorio `/etc/apache2/mods-available`. Si un módulo está habilitado existirá uno o varios enlaces simbólicos en el directorio `/etc/apache2/mods-enabled` a los ficheros del directorio anterior. Para habilitar un módulo podemos usar `a2enmod` y para deshabilitarlo podemos usar `a2dismod`.



## Configuración adicional

Es posible tener ficheros de configuración adicional del servidor apache2 en el directorio `/etc/apache2/conf-available`. si la configuración está activa existirá un enlace simbólico en el directorio `/etc/apache2/conf-enabled` a los ficheros del directorio anterior. Para activar una configuración podemos usar el comando `a2enconf` y para desactivarlo, el comando `a2disconf`.
