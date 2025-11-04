---
title: "Introducción a los contenedores Docker"
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

{% capture notice-text %}
## Ejercicio

1. Instala docker en una máquina y configúralo para que se pueda usar con un usuario sin privilegios.
2. Ejecuta un contenedor a partir de la imagen `hello-word`. Comprueba que nos devuelve la salida adecuada. Comprueba que no se está ejecutando. Lista los contenedores que están parado. Borra el contenedor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejecución simple de contenedores

Con el comando `run` vamos a creamos un contenedor indicando la imagen. También podemos indicar el comando que queremos ejecutar, **si no lo indicamos se ejecutara el comando por defecto que viene definido en la imagen.** En el siguiente ejemplo, crearemos un contenedor desde la imagen `ubuntu` que se descargará al ser la primera vez que la usamos:

```bash
$ docker run ubuntu echo 'Hello world' 
...
Hello world
```

Comprobamos que el contenedor ha ejecutado el comando que hemos indicado y se ha parado ejecutando `docker ps -a`. 
Para ver las imágenes que tenemos descargada en nuestro registro local: `docker images`.

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

{% capture notice-text %}
## Ejercicio

1. Crea un contenedor interactivo desde una imagen debian. Instala un paquete (por ejemplo `nano`). Sal de la terminal, ¿sigue el contenedor corriendo? ¿Por qué?. Vuelve a iniciar el contenedor y accede de nuevo a él de forma interactiva. ¿Sigue instalado el `nano`?. Sal del contenedor, y bórralo. Crea un nuevo contenedor interactivo desde la misma imagen. ¿Tiene el `nano` instalado?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
