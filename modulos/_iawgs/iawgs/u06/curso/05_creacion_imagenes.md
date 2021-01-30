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