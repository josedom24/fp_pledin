---
title: "Práctica: Implantación de aplicaciones web PHP en docker"
---

Imaginemos que el equipo de desarrollo de nuestra empresa ha desarrollado una aplicación PHP que se llama BookMedik ([https://github.com/evilnapsis/bookmedik](https://github.com/evilnapsis/bookmedik)).

Queremos crear una imagen Docker para implantar dicha aplicación.

Tenemos que tener en cuenta los siguientes aspectos:

**Contenedor mariadb**

* Es necesario que nuestra aplicación guarde su información en un contenedor docker **mariadb**.
*  El script para generar la base de datos y los registros lo encuentras en el repositorio y se llama `schema.sql`. Debes crear un usuario con su contraseña en la base de datos. La base de datos se llama `bookmedik` y se crea al ejecutar el script.
* Ejecuta el contenedor **mariadb** y carga los datos del script `schema.sql`. Para más [información](https://gist.github.com/spalladino/6d981f7b33f6e0afe6bb).
* El contenedor **mariadb** debe tener un volumen para guardar la base de datos.

**Contenedor bookmedik**

* Vamos a crear tres versiones de la imagen que nos permite implantar la aplicación PHP.
* La imagen debe crear las variables de entorno necesarias con datos de conexión por defecto.
* Al crear un contenedor a partir de estas imágenes se ejecutará un script bash que realizará las siguientes tareas:
    * Modifique el fichero `core\controller\Database.php` para que lea las variables de entorno. Para obtener las variables de entorno en PHP usar la función `getenv`. [Para más información](http://php.net/manual/es/function.getenv.php).
    * Inicialice la base de datos con el fichero `schema.sql`.
    * Ejecute el servidor web.
* El contenedor que creas debe tener un volumen para guardar los logs del servidor web.
* La imagen la tienes que crear en tu entorno de desarrollo con el comando `docker build`.

## Tarea 1: Creación de una imagen docker con una aplicación web desde una imagen base

* Vamos a crear una imagen que se llame `usuario/bookmedik:v1`.
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu.

{% capture notice-text %} 
* Entrega la url del repositorio GitHub donde tengas los ficheros necesarios para hacer la construcción de la imagen.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Despliegue en el entorno de desarrollo

*  Crea un script con `docker-compose` que levante el escenario con los dos contenedores.
* Recuerda que para acceder a la aplicación: Usuario: **admin**, contraseña: **admin**.

{% capture notice-text %} 
* Entrega la url del repositorio GitHub donde hayas añadido el fichero `docker-compose.yml`.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Creación de una imagen docker con una aplicación web desde una imagen PHP

* Vamos a crear una imagen que se llame `usuario/bookmedik:v2`.
* Realiza la imagen docker de la aplicación a partir de la imagen oficial [PHP](https://hub.docker.com/_/php/) que encuentras en docker hub. Lee la documentación de la imagen para configurar una imagen con apache2 y php, además seguramente tengas que instalar alguna extensión de php.
* Modifica el fichero docker-compose.yml` para probar esta imagen.

{% capture notice-text %} 
* Entrega la url del repositorio GitHub donde tengas los ficheros necesarios para hacer la construcción de la imagen.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
* Entrega la instrucción para ver los dos contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Ejecución de una aplicación PHP en docker con nginx (OPTATIVA)

* Vamos a crear una imagen que se llame `usuario/bookmedik:v3`.
* En este caso queremos usar un contenedor que utilice nginx para servir la aplicación PHP. Puedes crear la imagen desde una imagen base debian o ubuntu o desde la imagen oficial de nginx.
* Vamos a crear otro contenedor que sirva php-fpm.
* Para que funcione de forma adecuada el php-fpm tiene que tener acceso al directorio donde se encuentra la aplicación.
* Y finalmente nuestro contenedor con la aplicación.
* Crea un script con docker compose que levante el escenario con los tres contenedores.

A lo mejor te puede ayudar el siguiente enlace: [Dockerise your PHP application with Nginx and PHP7-FPM](http://geekyplatypus.com/dockerise-your-php-application-with-nginx-and-php7-fpm/)


{% capture notice-text %} 
* Entrega la url del repositorio GitHub donde tengas los ficheros necesarios para hacer la construcción de la imagen.
* Entrega una captura de pantalla donde se vea la imagen en el registro de tu entorno de desarrollo.
* Entrega la instrucción para ver los tres contenedores del escenario funcionando.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Puesta en producción de nuestra aplicación

* Elige una de las tres imágenes y súbela a Docker Hub.
* En tu VPS instala Docker y utilizando el `docker-compose.yml` correspondiente, crea un contenedor en ella de la aplicación.
* Configura el nginx de tu VPS para que haga de proxy inverso y nos permita acceder a la aplicación con `https://bookmedik.tudominio.xxx`.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega la configuración de nginx.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 6: Modificación de la aplicación

* En el entorno de desarrollo vamos a hacer una modificación de la aplicación. Por ejemplo modifica el fichero `core/app/view/login-view.php` y pon tu nombre en la línea `<h4 class="title">Acceder a BookMedik</h4>`.
* Vamos a trabajar con la primera imagen que construimos. Vuelve a crear la imagen con la etiqueta `v1_2`.
* Cambia el `docker-compose` para probar el cambio.
* Modifica la aplicación en producción.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
