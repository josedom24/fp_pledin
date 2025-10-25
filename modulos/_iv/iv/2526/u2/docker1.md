---
title: "Introducción a Docker"
---

## Instalación de Docker

Vamos a trabajar con [Moby](https://mobyproject.org/) que es la distribución Docker de la comunidad. En Debian 13:


```bash
$ apt install docker.io
$ docker --version
Docker version 26.1.5+dfsg1, build a72d7cd
```

Para manejar Docker con un usuario sin privilegio, debemos añadir el usuario al grupo `docker`, y reiniciar la sesión:

```bash
$ sudo usermod -aG docker $USER
```

## El "Hola Mundo" de docker

Vamos a comprobar que todo funciona creando nuestro primer contenedor desde la imagen `hello-world`:

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete 
Digest: sha256:56433a6be3fda188089fb548eae3d91df3ed0d6589f7c2656121b911198df065
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
...
```
¿Qué ha ocurrido?

1. El cliente Docker a conectado con el servidor Docker.
2. **Todos los contenedores se construyen a partir de una imagen**. Como la imagen `hello-world` no la teníamos en nuestro **registro local**se ha descragado del **registro público DockerHub**. El próximo contenedor que se cree a partir de esta imagen, no será necesario descargarla.
3. Se crea el nuevo contenedor que ejecuta un proceso, en este caso, mostrar el mensaje que jas visto. **Un contenedor ejecuta un proceso y cuando termina la ejecución, el contenedor se para.**

Si listamos los contenedores que se están ejecutando (`docker ps`), **no verás ninguno porque el contenedor está parado.**.
Para ver todos los contenedores, incluso los parados:

```bash
$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
f88fe68a16fc   hello-world   "/hello"   1 minutes ago   Exited (0) 1 minutes ago             interesting_greider
```

Para eliminar el contenedor: `docker rm interesting_greider`.

## Ejecución simple de contenedores

Con el comando `run` vamos a creamos un contenedor indicando la imagen. También podemos indicar el comando que queremos ejecutar, **si no lo indicamos se ejecutara el comando por defecto que viene definido en la imagen.** En el siguiente ejemplo, crearemos un contenedor desde la imagen `ubuntu` que se descargará al ser la primera vez que la usamos:

```bash
$ docker run ubuntu echo 'Hello world' 
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
4b3ffd8ccb52: Pull complete 
Digest: sha256:66460d557b25769b102175144d538d88219c077c678a49af4afca6fbfc1b5252
Status: Downloaded newer image for ubuntu:latest
Hello world
```

Comprobamos que el contenedor ha ejecutado el comando que hemos indicado y se ha parado ejecutando `docker ps -a`. 
Para ver las imágenes que tenemos descargada en nuestro registro local:

```bash
$ $ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    97bed23a3497   3 weeks ago    78.1MB
hello-world   latest    1b44b5a3e06a   2 months ago   10.1kB
```

## Ejecutando un contenedor interactivo

Podemos acceder a un contenedor interactivamente, usando la opción `-i` para abrir una sesión interactiva y `-t` nos permite crear un pseudo-terminal que nos va a permitir interaccionar con el contenedor. Además con la opción `--name` indicamos un nombre del contenedor.

```bash
$  docker run -it --name contenedor1 ubuntu bash 
root@2bfa404bace0:/#
```

El contenedor se para cuando salimos de él. Para volver a conectarnos a él:

```bash
$ docker start contenedor1
contenedor1
$ docker attach contenedor1
root@2bfa404bace0:/#
```

Si el contenedor se está ejecutando podemos ejecutar comandos en él con el subcomando `exec`:

```bash
$ docker start contenedor1
contenedor1
$ docker exec contenedor1 ls -al
```

Con la orden `docker restart` reiniciamos el contenedor, lo paramos y lo iniciamos.

Para mostrar información de un contenedor ejecutamos `docker inspect`:

En realidad, todas las imágenes tienen definidas un proceso que se ejecuta, en concreto la imagen `ubuntu` tiene definida por defecto el proceso `bash`, por lo que podríamos haber ejecutado:

```bash
$ docker run -it --name contenedor1 ubuntu
```

## Creando un contenedor demonio

En esta ocasión usamos la opción `-d` (detach) del comando `run`, para que la ejecución del comando en el contenedor se haga en segundo plano.

```bash
$ docker run -d --name contenedor2 ubuntu bash -c "while true; do echo hello world; sleep 1; done"
7b6c3b1c0d650445b35a1107ac54610b65a03eda7e4b730ae33bf240982bba08
```

> NOTA: En la instrucción `docker run` hemos ejecutado el comando con `bash -c` que nos permite ejecutar uno o mas comandos en el contenedor de forma más compleja (por ejemplo, indicando ficheros dentro del contenedor).

* Comprueba que el contenedor se está ejecutando con `docker ps`
* Comprueba lo que está haciendo el contenedor (`docker logs contenedor2`)

Por último podemos parar el contenedor y borrarlo con las siguientes instrucciones:

```bash
$ docker stop contenedor2
$ docker rm contenedor2
```

Hay que tener en cuenta que un contenedor que esta ejecutándose no puede ser eliminado. Tendríamos que para el contenedor y posteriormente borrarlo. Otra opción es borrarlo a la fuerza:

```bash
$ docker rm -f contenedor2
```

## Configuración de contenedores con variables de entorno

Más adelante veremos que al crear un contenedor que necesita alguna configuración específica, lo que vamos a hacer es crear variables de entorno en el contenedor, para que el proceso que inicializa el contenedor pueda realizar dicha configuración.

Para crear una variable de entorno al crear un contenedor usamos el flag `-e` o `--env`:

```bash
$ docker run -it --name contenedor5 -e USUARIO=prueba ubuntu bash
root@91e81200c633:/# echo $USUARIO
prueba
```

## Creando un contenedor con un servidor web

Tenemos muchas imágenes en el registro público **docker hub**, por ejemplo podemos crear un servidor web con apache 2.4:

```bash
$ docker run -d --name my-apache-app -p 8080:80 httpd:2.4
```

Vemos que el contenedor se está ejecutando, además con la opción `-p` mapeamos un puerto del equipo donde tenemos instalado el docker, con un puerto del contenedor: Si accedemos a la ip del ordenador que tiene instalado docker al primer puerto indicado, se redigirá la petición a la ip del contenedor al segundo puerto indicado. **Nunca utilizamos directamente la ip del contenedor para acceder a él**. Para probarlo accede desde un navegador a **la ip del servidor con docker.

Para acceder al log del contenedor podemos ejecutar: `docker logs my-apache-app` o para visualizarlo en tiempo real la opción `logs -f`.

## Modificación del contenido servidor por el servidor web

Si consultamos la documentación de la imagen [`httpd`](https://hub.docker.com/_/httpd) en el registro docker Hub, podemos determinar que le servidor web que se ejecuta en el contenedor guardar sus ficheros (directorio *DocumentRoot*) en `/usr/local/apache2/htdocs/`. Vamos a crear un nu nuevo fichero `index.html` en ese directorio.

Lo podemos hacer de varias formas:

* Accediendo de forma interactiva al contenedor y haciendo la modificación:

    ```bash
    $ docker exec -it my-apache-app bash

    root@cf3cd01a4993:/usr/local/apache2# cd /usr/local/apache2/htdocs/
    root@cf3cd01a4993:/usr/local/apache2/htdocs# echo "<h1>Curso Docker</h1>" > index.html
    root@cf3cd01a4993:/usr/local/apache2/htdocs# exit
    ```

* Ejecutando directamente el comando de creación del fichero `index.html` en el contenedor:

    ```bash
    $ docker exec my-apache-app bash -c 'echo "<h1>Curso Docker</h1>" > /usr/local/apache2/htdocs/index.html'
    ```

* Copiando un fichero `index.html` dento del contenedor:

    ```
    $ echo "<h1>Curso Docker</h1>" > index.html
    $ docker cp index.html  my-apache-app:/usr/local/apache2/htdocs/
    ``

Independientemente de cómo hayamos creado el fichero, podemos volver a acceder al servidor web y comprobar que efectivamente hemos cambiado el contenido del `index.html`.

## Configuración de un contenedor con la imagen mariadb

En ocasiones es obligatorio el inicializar alguna variable de entorno para que el contenedor pueda ser ejecutado. Si miramos la [documentación](https://hub.docker.com/_/mariadb) en Docker Hub de la imagen mariadb, observamos que podemos definir algunas variables de entorno para la creación y configuración del contenedor (por ejemplo: `MARIADB_DATABASE`,`MARIADB_USER`, `MARIADB_PASSWORD`,...). Pero hay una que la tenemos que indicar de forma obligatoria, la contraseña del usuario `root` (`MARIADB_ROOT_PASSWORD`), por lo tanto:

```bash
$ docker run -d --name some-mariadb -e MARIADB_ROOT_PASSWORD=my-secret-pw mariadb
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED                STATUS              PORTS               NAMES
9c3effd891e3        mariadb             "docker-entrypoint.s…"   8 seconds ago       Up 7   seconds        3306/tcp            some-mariadb
```

Podemos ver que se ha creado una variable de entorno:

```bash
$ docker exec -it some-mariadb env
...
MARIADB_ROOT_PASSWORD=my-secret-pw
...
```

Y para acceder podemos ejecutar:

```bash
$ docker exec -it some-mariadb bash                                  
root@9c3effd891e3:/# mariadb -u root -p"$MARIADB_ROOT_PASSWORD" 
...

MariaDB [(none)]> 
```
Otra forma de hacerlo sería:

```bash
$ docker exec -it some-mariadb mariadb -u root -p
Enter password: 
...
MariaDB [(none)]> 
```

No hemos usado el parámetro `-p` para mapear los puertos de MariaDB, porque norlmanete no accedemos a las bases de datos desde el exterior.