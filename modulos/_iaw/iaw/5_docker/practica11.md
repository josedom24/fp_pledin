---
title: "Práctica 1 (1 / 2): Implantación de aplicaciones web PHP en docker"
---

Imaginemos que el equipo de desarrollo de nuestra empresa ha desarrollado una aplicación PHP que se llama Biblioteca([https://github.com/VidaInformatico/Sistema-de-biblioteca-basico-php-8-y-mysql](https://github.com/VidaInformatico/Sistema-de-biblioteca-basico-php-8-y-mysql)).

Queremos crear una imagen Docker para implantar dicha aplicación.

Tenemos que tener en cuenta los siguientes aspectos:

* Es necesario que nuestra aplicación guarde su información en un contenedor docker **mariadb**.
* En la creación del contenedor de base de datos, usando variables de entorno, se creará una base de datos, un usuario y su contraseña.
* El contenedor **mariadb** debe tener un volumen para guardar la base de datos.
* Antes de generar la imagen, modifica el fichero `Config/Config.php` para que lea las variables de entorno. Para obtener las variables de entorno en PHP usar la función `getenv`. [Para más información](http://php.net/manual/es/function.getenv.php).
    Los cambios que tenemos que realizar para crear las constantes con el valor de las variables de entorno es la siguiente. Si tenemos en el fichero original:

    ```
    const base_url = "http://localhost/biblio/";
    ```
    Hay que sustituirlo por:

    ```
    define('base_url',getenv('BASE_URL'));
    ```
    Así con cada una de las variables.
* La imagen debe crear las variables de entorno necesarias con datos de conexión por defecto.
* Al crear un contenedor a partir de estas imágenes se ejecutará un script bash llamado `docker-entrypoint.sh` que realizará las siguientes tareas:
    * Se asegura que el contenedor mariadb está funcionando. Por ejemplo, puedes hacer un bucle hasta que puedas conectar a la base de datos.
    * Inicialice la base de datos con el fichero `biblioteca.sql`.
    * Ejecute el servidor web.
* El contenedor que creas debe tener un volumen para guardar los logs del servidor web.
* La imagen debe tener activa el mod_rewrite de apache2.
* Debemos configurar el apache2 para permitir el uso de ficheros `.htaccess`. Para ello necesitamos cambiar la configuración del fichero `/etc/apache2/apache2.conf`. Esto se puede hacer de varias formas:
    1. Copiando un fichero `apache2.conf` con la modificación hecha en la imagen.
    2. Que el script `docker-entrypoint.sh` modifique el fichero `apache2.conf` con la utilidad `sed` por ejemplo.
* La imagen la tienes que crear en tu entorno de desarrollo con el comando `docker build`.

## Creación de una imagen docker con una aplicación web desde una imagen base

* Vamos a crear una imagen que se llame `usuario/biblioteca:v1`.
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu o desde una imagen php.
* Está imagen debe tener apache2 instalado y todas las características indicadas anteriormente.

{% capture notice-text %} 
* Entrega el fichero `Dockerfile`.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Despliegue en el entorno de desarrollo

* Utiliza Docker Compose para levantar el escenario con los dos contenedores.
* Recuerda que para acceder a la aplicación: Usuario: **admin**, contraseña: **admin**.

{% capture notice-text %} 
* Entrega el fichero `docker-compose.yaml`.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
