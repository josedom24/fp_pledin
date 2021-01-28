---
title: "Introducción a docker"
permalink: /iawgs/u06/curso/01_introduccion.html
---

## Introducción a docker

Docker es una tecnología de virtualización "ligera" cuyo elemento básico es la utilización de contenedores en vez de máquinas virtuales y cuyo objetivo principal es el despliegue de aplicaciones encapsuladas en dichos contenedores.

Docker está formado por varios componentes:

* **Docker Engine**: Es un demonio que corre sobre cualquier distribución de Linux y que expone una API externa para la gestión de imágenes y contenedores. Con ella podemos crear imágnenes, subirlas y bajarla de un registro de docker y ejecutar y gestionar contenedores.
* **Docker Client**: Es el cliente de línea de comandos (CLI) que nos permite gestionar el Docker Engine. El cliente docker se puede configurar para trabajar con con un Docker Engine local o remoto, permitiendo gestionar tanto nuestro entorno de desarrollo local, como nuestro entorno de producción.
* **Docker Registry**: La finalidad de este componente es almacenar las imágenes generadas por el Docker Engine. Puede estar instalada en un servidor independiente y es un componente fundamental, ya que nos permite distribuir nuestras aplicaciones. Es un proyecto open source que puede ser instalado gratuitamente en cualquier servidor, pero, como hemos comentado, el proyecto nos ofrece **Docker Hub**.

* [Introducción a docker](https://raw.githubusercontent.com/albertomolina/beamer-focus/main/intro-docker.pdf)

## Instalación de docker

En debian vamos a instalar la versión de la comunidad:

    # apt install docker.io

Si queremos usar el cliente de docker con un usuario sin privilegios:

    usermod -aG docker usuario

volvemos acceder con el usuario al sistema, y comprobamos que ya podemos usar el cliente docker con el usuario sin privilegios, por ejemplo, podemos comprobar la versión que hemos instalado:

    $ docker --version
    Docker version 18.09.1, build 4c52b90

## El "Hola Mundo" de docker

Vamos a comprobar que todo funciona creando nuestro primer contendor desde la imagen `hello-world`:

    $ docker run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    0e03bdcc26d7: Pull complete 
    Digest:     sha256:31b9c7d48790f0d8c50ab433d9c3b7e17666d6993084c002c2ff1ca09b96391d
    Status: Downloaded newer image for hello-world:latest

    Hello from Docker!
    This message shows that your installation appears to be working     correctly.

    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
     3. The Docker daemon created a new container from that image which runs    the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which  sent it
        to your terminal.

    To try something more ambitious, you can run an Ubuntu container with:
     $ docker run -it ubuntu bash

    Share images, automate workflows, and more with a free Docker ID:
     https://hub.docker.com/

    For more examples and ideas, visit:
     https://docs.docker.com/get-started/

Pero, ¿qué es lo que está sucediendo al ejecutar esa orden?:

* Al ser la primera vez que ejecuto un contenedor basado en esa imagen, la imagen `hello-word` se descarga desde el repositorio que se encuentra en el registro que vayamos a utilizar, en nuestro caso DockerHub.
* Muestra el mensaje de bienvenida que es la consecuencia de crear y arrancar un contenedor basado en esa imagen.

Si listamos los contenedores que se están ejecutando (`docker ps`):

    $docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

Comprobamos que este contenedor no se está ejecutando. **Un contenedor ejecuta un proceso y cuando termina la ejecución, el contendor se para.**

Para ver los contendores que no se están ejecutando:

    $ docker ps -a
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
    372ca4634d53        hello-world         "/hello"            8 minutes ago       Exited (0) 8 minutes ago                       elastic_johnson

Para eliminar el contendor podemos identificarlo con su `id`:

    $ docker rm 372ca4634d53

 o con su nombre:

    $ docker rm elastic_johnson