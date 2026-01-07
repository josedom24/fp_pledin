---
title: Creación de imágenes a partir de un Dockerfile
---
Aunque podemos crear nuevas [imágenes a partir de contenedores](https://github.com/josedom24/curso_docker_ies/blob/main/modulo5/contenedor.md), ese método no es adecuado y tiene algunas limitaciones:

* **No se puede reproducir la imagen**. 
* **No podemos configurar el proceso que se ejecutará en el contenedor creado desde la imagen**.
* **No podemos cambiar la imagen de base**. 

Por todas estas razones, el método preferido para la creación de imágenes es el uso de ficheros `Dockerfile` y el comando `docker build`. Con este método vamos a tener las siguientes ventajas:

* **Podremos reproducir la imagen fácilmente** ya que en el fichero `Dockerfile` tenemos todas y cada una de las órdenes necesarias para la construcción de la imagen. Si además ese `Dockerfile` está guardado en un sistema de control de versiones como git podremos, no sólo reproducir la imagen si no asociar los cambios en el `Dockerfile` a los cambios en las versiones de las imágenes creadas.
* **Podremos configurar el proceso que se ejecutará por defecto en los contenedores creados a partir de la nueva imagen**.
* Si queremos cambiar la imagen de base esto es extremadamente sencillo con un `Dockerfile`, únicamente tendremos que modificar la primera línea de ese fichero tal y como explicaremos posteriormente.

## El fichero Dockerfile

Un fichero `Dockerfile` es un conjunto de instrucciones que serán ejecutadas de forma secuencial para construir una nueva imagen docker. 
Las instrucciones que cambian el sistema de fichero crearán **una nueva capa**.

La primera línea a añadir a un Dockerfile es una directiva `# syntax=docker/dockerfile:1` que se utiliza para especificar la versión del formato del Dockerfile que se va a utilizar. Es opcional, pero recomendable.

Las principales instrucciones que podemos usar:

* **FROM**: Sirve para especificar la imagen sobre la que vamos a construir la nueva.
* **RUN**: Ejecuta una orden creando una nueva capa.  Ejemplo: `RUN apt update && apt install -y git`. En este caso es muy importante que pongamos la opción `-y` porque en el proceso de construcción no puede haber interacción con el usuario.
* **WORKDIR**: Establece el directorio de trabajo dentro de la imagen que estoy creando, las siguientes instrucciones se ejecutarán en este directorio.
* **COPY**: Para copiar ficheros desde mi equipo a la imagen. Esos ficheros deben estar en el mismo contexto (carpeta o repositorio). Su sintaxis es `COPY [--chown=<usuario>:<grupo>] src dest`. 
* **ADD**: Es similar a COPY pero tiene funcionalidades adicionales como especificar URLs  y tratar archivos comprimidos.
* **LABEL**: Sirve para añadir metadatos a la imagen mediante clave=valor.
* **EXPOSE**: Nos da información acerca de qué puertos tendrá abiertos el contenedor cuando se cree uno en base a la imagen que estamos creando. Es meramente informativo.  
* **ENV**: Para establecer variables de entorno dentro del contenedor. Puede ser usado posteriormente en las órdenes RUN añadiendo $ delante de el nombre de la variable de entorno. 
* **ENTRYPOINT**: Para establecer el ejecutable que se lanza siempre  cuando se crea el contenedor  con `docker run`. El comando no se puede cambiar al crear el contenedor.
* **CMD**: Para establecer el ejecutable por defecto (salvo que se sobreescriba desde la orden `docker run`).

Para una descripción completa sobre el fichero `Dockerfile`, puedes acceder a la [documentación oficial](https://docs.docker.com/engine/reference/builder/).

## Construyendo imágenes con docker build

El comando `docker build` construye la nueva imagen leyendo las instrucciones del fichero `Dockerfile` y la información de un **entorno**, que para nosotros va a ser un directorio.

La creación de la imagen es ejecutada por el *docker engine*, que recibe toda la información del entorno, por lo tanto es recomendable guardar el `Dockerfile` en un directorio vacío y añadir los ficheros necesarios para la creación de la imagen. El comando `docker build` ejecuta las instrucciones de un `Dockerfile` línea por línea y va mostrando los resultados en pantalla.

Para terminar indicar que la creación de imágenes intermedias generadas por la ejecución de cada instrucción del `Dockerfile`, es un **mecanismo de caché**, es decir, si en algún momento falla la creación de la imagen, al corregir el `Dockerfile` y volver a construir la imagen, los pasos que habían funcionado anteriormente no se repiten ya que tenemos a nuestra disposición las imágenes intermedias, y el proceso continúa por la instrucción que causó el fallo.

## Ejemplo de  Dockerfile

Vamos a crear un directorio (a este directorio se le llama **contexto**) donde vamos a crear un `Dockerfile` y un fichero `index.html`:

```bash
cd build
~/build$ ls
Dockerfile  index.html
```

El contenido de `Dockerfile` es:

```Dockerfile
# syntax=docker/dockerfile:1
FROM debian:stable-slim
RUN apt-get update  && apt-get install -y  apache2 
WORKDIR /var/www/html
COPY index.html .
CMD apache2ctl -D FOREGROUND
```

Para crear la imagen uso el comando `docker build`, indicando el nombre de la nueva imagen (opción `-t`) y indicando el directorio **contexto**.

```bash
$ docker build -t josedom24/myapache2:v2 .
...
```
> Nota: Pongo como directorio el `.` porque estoy ejecutando esta instrucción dentro del directorio donde está el `Dockerfile`.


Una vez terminado, podríamos ver que hemos generado una nueva imagen:

```bash
$ docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
josedom24/myapache2       v2                  3bd28de7ae88        43 seconds ago      195MB
...
```

Si usamos el parámetro `--no-cache` en `docker build` haríamos la construcción de una imagen sin usar las capas cacheadas por haber realizado anteriormente imágenes con capas similares.

En este caso al crear el contenedor a partir de esta imagen no hay que indicar el proceso que se va a ejecutar, porque ya se ha indicando en el fichero `Dockerfile`:

```bash
$ docker run -d -p 8080:80 --name servidor_web josedom24/myapache2:v2 
```            

No utilizar la etiqueta `latest` al indicar la imagen base, ya que está va cambiando con el tiempo y si volvemos a crear la imagen dentro de un tiempo, es posible que estemos usando una imagen base diferente.

{% capture notice-text %}
## Ejercicio

1. Crea un fichero `index.html` y guardálo en un directorio con el fichero `dockerfile` que hemos visto en el ejemplo.
2. Crea una nueva imagen con `docker build`.
3. Comprueba la imagen con `docker images`.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Distribución de imágenes

Una vez que hemos creado nuestra imagen personalizada, es la hora de distribuirla para desplegarla en el entorno de producción. Para ello vamos a tener varias posibilidades:


1. Utilizar la secuencia de órdenes `docker commit` /` docker save` / `docker load`. En este caso la distribución se producirá a partir de un fichero.
2. Utilizar la pareja de órdenes `docker commit` / `docker push`. En este caso la distribución se producirá a través de DockerHub.

En este curso nos vamos a ocupar  únicamente de las dos primeras ya que la tercera se limita a copiar el sistema de ficheros sin tener en cuenta la información de las imágenes de las que deriva el contenedor (capas, imagen de origen, autor etc..) y además si tenemos volúmenes o bind mounts montados los obviará.

### Distribución a partir de un fichero

1. Guardar esa imagen en un archivo .tar usando el comando `docker save`:

    ```bash    
    $ docker save josedom24/myapache2:v1 > myapache2.tar
    ```

2. Distribuir el fichero `.tar`.

3. Si me llega un fichero .tar puedo añadir la imagen a mi repositorio local:

    ```bash
    $ docker load -i myapache2.tar          
    6a30654d94bc: Loading layer [=============================================>]  132.4MB/132.4MB
    Loaded image: josedom24/myapache2:v1
    ```

### Distribución usando Docker Hub

1. Autentificarme en Docker Hub usando el comando `docker login`.

    ```bash
    $ docker login 
    Login with your Docker ID to push and pull images from Docker Hub...
    Username: josedom24
    Password: 
    ...
    Login Succeeded
    ```

2. Distribuir ese fichero subiendo la nueva imagen a DockerHub mediante `docker push`. Nota: El nombre de la imagen tiene que tener como primera parte el nombre del usuario de DockerHub que estamos usando.

    ```bash
    $ docker push josedom24/myapache2:v2
    The push refers to repository [docker.io/josedom24/myapache2:v2]
    6a30654d94bc: Pushed 
    4762552ad7d8: Mounted from library/debian 
    latest: digest: sha256:25b34b8342ac8b73058aa07ec935dcf5d33db7544da9a216050e1d2077a size: 741
    ```

3. Ya cualquier persona puede bajar la imagen usando `docker pull`.

{% capture notice-text %}
## Ejercicio

1. Darte de alta en Docker Hub.
2. Si es necesario vuelve a generar la imagen con este formato de nombre: `<tu_usuario_docker_hub>/<nimbre_imagen>:<etiqueta>`
3. Sube la imagen a Docker Hub.
4. Descarga la imagen desde Docker Hub en otra máquina donde tengas instalado Docker.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
