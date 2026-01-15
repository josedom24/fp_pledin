---
title: "Practica: Despliegue de aplicaciones web con Docker"
---

Tienes que elegir entre realizar una imagen de una aplicación web escrita en PHP o en Python:

## Opción 1: Aplicación PHP

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
* Al crear un contenedor a partir de estas imágenes se ejecutará un script bash llamado `docker-entrypoint.sh` que realizará las siguientes tareas:
    * Se asegura que el directorio de la aplicación es del usuario `www-data`.
    * Ejecute el servidor web.
* El contenedor que creas debe tener un volumen para guardar los logs del servidor web.
* La imagen debe tener activa el mod_rewrite de apache2.
* Debemos configurar el apache2 para permitir el uso de ficheros `.htaccess`. Para ello necesitamos cambiar la configuración del fichero `/etc/apache2/apache2.conf`. Esto se puede hacer de varias formas:
    1. Copiando un fichero `apache2.conf` con la modificación hecha en la imagen.
    2. Que el script `docker-entrypoint.sh` modifique el fichero `apache2.conf` con la utilidad `sed` por ejemplo.
* La imagen la tienes que crear en tu entorno de desarrollo con el comando `docker build`.

### Creación de una imagen docker con una aplicación web desde una imagen base

* Vamos a crear una imagen que se llame `usuario/biblioteca:v1`.
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu o desde una imagen php.
* Está imagen debe tener apache2 instalado y todas las características indicadas anteriormente.

{% capture notice-text %} 
* Entrega el fichero `Dockerfile`.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Despliegue en el entorno de desarrollo

* Utiliza Docker Compose para levantar el escenario con los dos contenedores.
* Recuerda que para acceder a la aplicación: Usuario: **admin**, contraseña: **admin**.

{% capture notice-text %} 
* Entrega el fichero `docker-compose.yaml`.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Opción 2: Aplicación Python

Queremos desplegar en docker la aplicación escrita en python django: **Django Publicaciones** [django_publicaciones](https://github.com/josedom24/django_publicaciones). Si quieres puedes hacer un fork para modificar los ficheros del repositorio.

Tienes que tener en cuenta los siguientes aspectos:

* La aplicación debe guardar los datos en una base de datos mariadb persistente.
* La aplicación se podrá configurar para indicar los parámetros de conexión a la base de datos: usuario, contraseña, host y base de datos.
* Durante la construcción de la imagen se deberá clonar tu fork del repositorio para copiarlo al contenedor durante su construcción.
* La aplicación deberá tener creado un usuario administrador para el acceso, se deberán crear las variables de entornos necesarias como vimos en el ejemplo 5.

{% capture notice-text %}
1. Crea una imagen docker para poder desplegar un contenedor con la aplicación. La imagen la puedes hacer desde una imagen base o desde la imagen oficial de python.
2. Utiliza Compose para desplegar los contenedores necesarios. Configura los volúmenes que creas necesarios para que la aplicación sea persistente.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Puesta en producción de nuestra aplicación (Para la dos opciones)

* Sube la imagen que has generado a Docker Hub.
* En tu VPS instala Docker y utilizando el `docker-compose.yaml` para desplegar la aplicación.
* Configura el nginx de tu VPS para que haga de proxy inverso y nos permita acceder a la aplicación con `https://appdocker.tudominio.xxx`.

Seguramente tendrás que cambiar el fichero `docker-compose.yaml` de desarrollo a producción (puede que cambie algún valor de alguna variable de entorno, el número del puerto,...). Para poder usar el mismo fichero `docker-compose.yml` en todos los entornos se suele parametrizar este fichero como se explica en esta [página](https://github.com/josedom24/curso_docker_ow/blob/main/contenido/modulo6/variables.md).

Parametriza el fichero `docker-compose.yaml` y crea dos ficheros distintos `.env` para el entorno de desarrollo y el entorno de producción. El fichero `.env` no se guarda en el repositorio git, por lo que es conveniente meterlo en el fichero `.gitignore`.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega el fichero `docker-compose.yaml` parametrizado y los ficheros `.env` de desarrollo y producción.
* Entrega la configuración de nginx.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Modificación de la aplicación (Para la dos opciones)

* En el entorno de desarrollo vamos a hacer una modificación de la aplicación, para poner tu nombre en la página principal.
* Vuelve a crear la imagen con la etiqueta `v2`.
* Cambia el `docker-compose.yaml` para probar el cambio.
* Modifica la aplicación en producción.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
* Entrega un **vídeo** donde demuestres los distintos ejercicios que has hecho e la práctica. Graba la pantalla y ve explicando lo que has realizando y mostrando que funciona.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>