---
title: "Creación de imágenes en docker"
permalink: /iawgs/u06/curso/creacion_imagenes.html
---

## Creación de imágenes en docker

Hasta ahora hemos creado contenedores a partir de las imágenes que encontramos en Docker Hub. Estas imágenes las han creado otras personas.

Para crea un contenedor que sirva nuestra aplicación, tendremos que crear una imagen personaliza, es lo que llamamos "dockerizar" una aplicación.

## Creación de una nueva imagen a partir de un contenedor

La primera forma para personalizar las imágenes y distribuirlas es partiendo de un contenedor en ejecución. Para ello vamos a tener varias posibilidades:


1. Utilizar la secuencia de órdenes `docker commit` /` docker save` / `docker load`. En este caso la distribución se producirá a partir de un fichero.
2. Utilizar la pareja de órdenes `docker commit` / `docker push`. En este caso la distribución se producirá a través de DockerHub.
3. Utilizar la pareja de órdenes `docker export` / `docker import`. En este caso la distribución de producirá a través de un fichero.

En este curso nos vamos a ocupar  únicamente de las dos primeras ya que la tercera se limita a copiar el sistema de ficheros sin tener en cuenta la información de las imágenes de las que deriva el contenedor (capas, imagen de origen, autor etc..) y además si tenemos volúmenes o bind mounts montados los obviará.

![docker](img/build.png)

### Distribución a partir de un fichero

1. Arranca un contenedor a a partir de una imagen base

        $ docker  run -it --name contenedor debian bash

2. Realizar modificaciones en el contenedor (instalaciones, modificación de archivos,...)

        root@2df2bf1488c5:/# apt update && apt install apache2 -y

3. Crear una nueva imagen partiendo de ese contenedor usando `docker commit`. Con esta instrucción se creará una nueva imagen con las capas de la imagen base más la capa propia del contenedor. Al creala no vot a poner etiqueta, por lo que sera `latest`.

        $ docker commit contenedor josedom24/myapache2
        sha256:017a4489735f91f68366f505e4976c111129699785e1ef609aefb51615f98fc4

        $ docker images
        REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
        josedom24/myapache2       latest              017a4489735f        44 seconds ago      243MB
        ...
4. Guardar esa imagen en un archivo .tar usando el comando `docker save`:

        $ docker save josedom24/myapache2 > myapache2.tar

5. Distribuir el fichero .tar

6. Si me llega un fichero .tar puedo añadir la imagen a mi repositorio local:

        $ docker rmi josedom24/myapache2:latest 
        Untagged: josedom24/myapache2:latest
        Deleted: sha256:017a4489735f91f68366f505e4976c111129699785e1ef609aefb51615f98fc4
        Deleted: sha256:761d2ff599422097fcf3dd1a13f50b9bf924e453efee8617e29ba78602efcf21
    
        $ docker load -i myapache2.tar          
        6a30654d94bc: Loading layer [==================================================>]  132.4MB/132.4MB
        Loaded image: josedom24/myapache2:latest


### Distribución usando Docker Hub

Los tres primeros pasos son iguales, por lo tanto tenemos nuestra imagen ya creada después de ejecutar `docker commit`, los siguientes pasos serían:

4. Autentificarme en Docker Hub usando el comando `docker login`.

        $ docker login 
        Login with your Docker ID to push and pull images from Docker Hub...
        Username: usuario
        Password: 
        ...
        Login Succeeded

5. Distribuir ese fichero subiendo la nueva imagen a DockerHub mediante `docker push`.

        $ docker push josedom24/myapache2
        The push refers to repository [docker.io/josedom24/myapache2]
        6a30654d94bc: Pushed 
        4762552ad7d8: Mounted from library/debian 
        latest: digest: sha256:25b34b8342ac8b79610d3058aa07ec935dcf5d33db7544da9a216050e1d2077a size: 741

6. Ya cualquier persona puede bajar la imagen usando `docker pull`.


## Creación de imágenes con fichero Dockerfile

El método anterior tiene dos inconvenientes:

* **No se puede reproducir la imagen**. Si la perdemos tenemos que recordar toda la secuencia de órdenes que habíamos ejecutado desde que arrancamos el contenedor hasta que teníamos una versión definitiva e hicimos `docker commit`.
* **No podemos cambiar la imagen de base**. Si ha habido alguna actualización, problemas de seguridad, etc. con la imagen de base tenemos que descargar la nueva versión, volver a crear un nuevo contenedor basado en ella y ejecutar de nuevo toda la secuencia de órdenes.

Por lo que el método preferido para la creación de imágenes es el uso de ficheros `Dockerfile` y el comando `docker build`. Los pasos fundamentales serán:

1. Crear el fichero `Dockerfile`.
2. Construir la imagen usando la definición guardada en el fichero `Dockerfile` y el comando `docker build`.
3. Autentificarme en Docker Hub usando el comando `docker login`.
4. Distribuir ese fichero subiendo la nueva imagen a DockerHub mediante `docker push`.

Con este método vamos a tener las siguientes ventajas:

* **Podremos reproducir la imagen fácilmente** ya que en el fichero `Dockerfile` tenemos todas y cada una de las órdenes necesarias para la construcción de la imagen. Si además ese `Dockerfile` está guardado en un sistema de control de versiones como git podremos, no sólo reproducir la imagen si no asociar los cambios en el `Dockerfile` a los cambios en las versiones de las imágenes creadas.
* Si queremos cambiar la imagen de base esto es extremadamente sencillo con un `Dockerfile`, únicamente tendremos que modificar la primera línea de ese fichero tal y como explicaremos posteriormente.

### El fichero Dockerfile

Un fichero `Dockerfile` es un conjunto de instrucciones que serán ejecutadas de forma secuencial para construir una nueva imagen docker. Cada una de estas instrucciones crea una nueva capa en la imagen que estamos creando. 

Hay varias instrucción que podemos usar en la construcción de un `Dockerfile`, pero la estructura fundamental del fichero es:

* Indicamos imagen base: FROM
* Metadatos: MANTEINER, LABEL
* Instrucciones de construcción: RUN, COPY, ADD, WORKDIR
* Configuración: Variable de entornos, usuarios, puertos: USER, EXPOSE, ENV
* Instrucciones de arranque: CMD, ENTRYPOINT

Veamos las principales instrucciones que podemos usar:

* FROM: Sirve para especificar la imagen sobre la que voy a construir la mía. Ejemplo: FROM php:7.4-apache
* LABEL: Sirve para añadir metadatos a la imagen mediante clave=valor. Ejemplo: LABEL company=iesalixar
* COPY: Para copiar ficheros desde mi equipo a la imagen. Esos ficheros deben estar en el mismo contexto (carpeta o repositorio). Su sintaxis es `COPY [--chown=<usuario>:<grupo>] src dest`. Por ejemplo: `COPY --chown=www-data:www-data myapp /var/www/html`
* ADD: Es similar a COPY pero tiene funcionalidades adicionales como especificar URLs  y tratar archivos comprimidos.
* RUN: Ejecuta una orden creando una nueva capa. Su sintaxis es `RUN orden` / `RUN ["orden","param1","param2"]`. Ejemplo: `RUN apt update && apt install -y git`. En este caso es muy importante que pongamos la opción `-y` porque en el proceso de construcción no puede haber interacción con el usuario.
* WORKDIR: Establece el directorio de trabajo dentro de la imagen que estoy creando para posteriormente usar las órdenes RUN,COPY,ADD,CMD o ENTRYPOINT. Ejemplo: `WORKDIR /usr/local/apache/htdocs`
* EXPOSE: Nos da información acerca de qué puertos tendrá abiertos el contenedor cuando se cree uno en base a la imagen que estamos creando. Es meramente informativo.  Ejemplo: `EXPOSE 80`
* USER: Para especificar (por nombre o UID/GID) el usuario de trabajo para todas las órdenes RUN,CMD Y ENTRYPOINT posteriores. Ejemplos: `USER jenkins` / `USER 1001:10001`
* ARG: Para definir variables para las cuales los usuarios pueden especificar valores a la hora de hacer el proceso de build mediante el flag `--build-arg`. Su sintaxis es `ARG nombre_variable` o `ARG nombre_variable=valor_por_defecto`. Posteriormente esa variable se puede usar en el resto de la órdenes de la siguiente manera `$nombre_variable`. Ejemplo: `ARG usuario=www-data`. NO SE PUEDE USAR EN ENTRYPOINT Y CMD
* ENV: Para establecer variables de entorno dentro del contenedor. Puede ser usado posteriormente en las órdenes RUN añadiendo $ delante de el nombre de la variable de entorno. Ejemplo: `ENV WEB_DOCUMENT_ROOT=/var/www/html`.  NO  SE PUEDE USAR EN ENTRYPOINT Y CMD
* ENTRYPOINT: Para establecer el ejecutable que se lanza siempre  cuando se crea el contenedor  con `docker run`, salvo que se especifique expresamente algo diferente con el flag `--entrypoint`. Su síntaxis es la siguiente: `ENTRYPOINT <command>` / `ENTRYPOINT ["executable","param1","param2"]`. Ejemplo: `ENTRYPOINT ["a/usr/sbin/apache2ctl","-D","FOREGROUND"]`
* CMD: Para establecer el ejecutable por defecto (salvo que se sobreescriba desde la order docker run) o para especificar parámetros para un ENTRYPOINT. Si tengo varios sólo se ejecuta el último. Su sintaxis es CMD param1 param2 / CMD ["param1","param2"] / CMD["command","param1"]. Ejemplo: `CMD [“-c” “/etc/nginx.conf”]`  / `ENTRYPOINT [“nginx”]`. 

Ejemplo:

Si tenemos un fichero `Dockerfile`, que tiene las siguientes instrucciones:

    ENTRYPOINT ["http", "-v"]
    CMD ["-p", "80"]

Podemos crear un contenedor a partir de la imagen generada:

* `docker run centos:centos7`: Se creará el contenedor con el servidor web escuchando en el puerto 80.
* `docker run centos:centros7 -p 8080`: Se creará el contenedor con el servidor web escuchando en el puerto 8080.

### Construyendo imágenes con docker build

El comando `docker build` construye la nueva imagen leyendo las instrucciones del fichero `Dockerfile` y la información de un **entorno**, que para nosotros va a ser un directorio (aunque también podemos guardar información, por ejemplo, en un repositorio git).

La creación de la imagen es ejecutada por el *docker engine*, que recibe toda la información del entorno, por lo tanto es recomendable guardar el `Dockerfile` en un directorio vacío y añadir los ficheros necesarios para la creación de la imagen. El comando `docker build` ejecuta las instrucciones de un `Dockerfile` línea por línea y va mostrando los resultados en pantalla.

Tenemos que tener en cuenta que cada instrucción ejecutada crea una imagen intermedia, una vez finalizada la construcción de la imagen nos devuelve su id. Alguna imágenes intermedias se guardan en **caché**, otras se borran. Por lo tanto, si por ejemplo, en un comando ejecutamos `cd /scripts/` y en otra linea le mandamos a ejecutar un script (`./install.sh`) no va a funcionar, ya que ha lanzado otra imagen intermedia. Teniendo esto en cuenta, la manera correcta de hacerlo sería:

        cd /scripts/;./install.sh

Para terminar indicar que la creación de imágenes intermedias generadas por la ejecución de cada instrucción del `Dockerfile`, es un mecanismo de caché, es decir, si en algún momento falla la creación de la imagen, al corregir el `Dockerfile` y volver a construir la imagen, los pasos que habían funcionado anteriormente no se repiten ya que tenemos a nuestra disposición las imágenes intermedias, y el proceso continúa por la instrucción que causó el fallo.

Vamos a crear un directorio (**nuestro entorno**) donde vamos a crear un Dockerfile y un fichero `index.html`:

        cd build
        ~/build$ ls
        Dockerfile  index.html

El contenido de `Dockerfile` es:

        FROM debian:buster-slim
        MAINTAINER José Domingo Muñoz "josedom24@gmail.com"
        RUN apt update  && apt install -y  apache2 
        COPY index.html /var/www/html/index.html
        ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

Para crear la imagen uso el comando `docker build`, indicando el nombre de la nueva imagen (opción `-t`) y indicando el directorio contexto.

        $ docker build -t josedom24/myweb:v1 .
        ...

Una vez terminado, podríamos ver que hemos generado una nueva imagen:

        $ docker images
        REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
        josedom24/myweb           v1                  3bd28de7ae88        43 seconds ago      195MB
        ...

Y ya podríamos crear un nuevo contenedor o distribuir la imagen usando alguno de los métodos anteriormente estudiados.

### Buenas prácticas al crear DockerfilePermalink

* **Los contenedores deber ser "efímeros"**: Cuando decimos "efímeros" queremos decir que la creación, parada, despliegue de los contenedores creados a partir de la imagen que vamos a generar con nuestro Dockerfile debe tener una mínima configuración.
* **Uso de ficheros `.dockerignore`**: Como hemos indicado anteriormente, todos los ficheros del contexto se envían al *docker engine*, es recomendable usar un directorio vacío donde vamos creando los ficheros que vamos a enviar. Además, para aumentar el rendimiento, y no enviar al daemon ficheros innecesarios podemos hacer uso de un fichero `.dockerignore`, para excluir ficheros y directorios.
* **No instalar paquetes innecesarios**: Para reducir la complejidad, dependencias, tiempo de creación y tamaño de la imagen resultante, se debe evitar instalar paquetes extras o innecesarios Si algún paquete es necesario durante la creación de la imagen, lo mejor es desinstalarlo durante el proceso.
* **Minimizar el número de capas**: Debemos encontrar el balance entre la legibilidad del Dockerfile y minimizar el número de capa que utiliza.
* **Indicar las instrucciones a ejecutar en múltiples líneas**: Cada vez que sea posible y para hacer más fácil futuros cambios, hay que organizar los argumentos de las instrucciones que contengan múltiples líneas, esto evitará la duplicación de paquetes y hará que el archivo sea más fácil de leer. Por ejemplo:

        RUN apt-get update && apt-get install -y \
        git \
        wget \
        apache2 \
        php5






## Creación automática de imágenes en Docker Hub
## Ciclo de vida de nuestras aplicaciones con docker

Más concretamente **el ciclo de vida de una aplicación docker** lo podría resumir en:

* Paso 1:Desarrollo de nuestra aplicación
* Paso 2: Creación de la imagen Docker
* Paso 3: Probamos nuestra aplicación en el entorno de desarrollo o prueba
* Paso 4: Distribuimos nuestra imagen
* Paso 5:Implantación de la aplicación en el entorno de producción
* Paso 6: Modificación de la aplicación, volviendo al paso 2.

## Ejercicio: Despliegue de páginas estáticas con docker

## Ejercicios

1. Create una cuenta en Docker Hub