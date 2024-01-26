---
title: "Práctica: Implantación de aplicaciones web PHP en docker"
---

Imaginemos que el equipo de desarrollo de nuestra empresa ha desarrollado una aplicación PHP que se llama Biblioteca([https://github.com/VidaInformatico/Sistema-de-biblioteca-basico-php-8-y-mysql](https://github.com/VidaInformatico/Sistema-de-biblioteca-basico-php-8-y-mysql)).

Queremos crear una imagen Docker para implantar dicha aplicación.

Tenemos que tener en cuenta los siguientes aspectos:

**Contenedor mariadb**

* Es necesario que nuestra aplicación guarde su información en un contenedor docker **mariadb**.
* en la creación del contenedor, usando variables de entorno, se creará una base de datos, un usuario y su contraseña.
* El contenedor **mariadb** debe tener un volumen para guardar la base de datos.

**Contenedor biblioteca**

* Vamos a crear dos versiones de la imagen que nos permite implantar la aplicación PHP.
* Antes de generar la imagen, modifica el fichero `Config/Config.php` para que lea las variables de entorno. Para obtener las variables de entorno en PHP usar la función `getenv`. [Para más información](http://php.net/manual/es/function.getenv.php).
* La imagen debe crear las variables de entorno necesarias con datos de conexión por defecto.
* Al crear un contenedor a partir de estas imágenes se ejecutará un script bash llamado `entrypint-docker.sh` que realizará las siguientes tareas:
    * Se asegura que el contenedor mariadb está funcionando. Por ejemplo, puedes hacer un bucle hasta que puedas conectar a la base de datos.
    * Inicialice la base de datos con el fichero `biblioteca.sql`.
    * Ejecute el servidor web.
* El contenedor que creas debe tener un volumen para guardar los logs del servidor web.
* La imagen debe tener activa el mod_rewrite de apache2.
* La imagen la tienes que crear en tu entorno de desarrollo con el comando `docker build`.

## Tarea 1: Creación de una imagen docker con una aplicación web desde una imagen base

* Vamos a crear una imagen que se llame `usuario/biblioteca:v1`.
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu.
* Está imagen debe tener apache2 instalado y todas las características indicadas anteriormente.

{% capture notice-text %} 
* Entrega el fichero `Dockerfile`.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Despliegue en el entorno de desarrollo

* Utiliza Compose para levantar el escenario con los dos contenedores.
* Recuerda que para acceder a la aplicación: Usuario: **admin**, contraseña: **admin**.

{% capture notice-text %} 
* Entrega el fichero `docker-compose.yaml`.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Creación de una imagen docker con una aplicación web desde una imagen PHP

* Vamos a crear una imagen que se llame `usuario/biblioteca:v2`.
* Realiza la imagen docker de la aplicación a partir de la imagen oficial [PHP](https://hub.docker.com/_/php/) que encuentras en docker hub. Lee la documentación de la imagen para configurar una imagen con apache2 y php, además seguramente tengas que instalar alguna extensión de php.
* Modifica el fichero `docker-compose.yaml` para probar esta imagen.

{% capture notice-text %} 
* Entrega los ficheros `Dockerfile` y `docker-compose.yaml`
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Puesta en producción de nuestra aplicación

* Elige una de las dos imágenes y súbela a Docker Hub.
* En tu VPS instala Docker y utilizando el `docker-compose.yaml` correspondiente, crea un contenedor en ella de la aplicación.
* Configura el nginx de tu VPS para que haga de proxy inverso y nos permita acceder a la aplicación con `https://biblioteca.tudominio.xxx`.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega la configuración de nginx.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Modificación de la aplicación

* En el entorno de desarrollo vamos a hacer una modificación de la aplicación. Por ejemplo modifica el fichero `Views/index.php` y pon tu nombre en la línea `<h1>Bienvenido</h1>`.
* Vuelve a crear la imagen con la etiqueta `vX_2` (X será 1 si has escogido la priemera versión, o 2 si has escogido la segunda).
* Cambia el `docker-compose.yaml` para probar el cambio.
* Modifica la aplicación en producción.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
