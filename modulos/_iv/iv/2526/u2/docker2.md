---
title: "Imágenes Docker"
---

## Introducción a las imágenes Docker

* Una **imagen Docker** es una plantilla de solo lectura. Contiene, entre otras cosas, un sistema de ficheros. A partir de las imágenes **se crean los contenedores**. Si hacemos cambios en el contenedor ya lanzado, al detenerlo esto no se verá reflejado en la imagen.
* El **Registro docker** es un componente donde se almacena las imágenes generadas por el Docker Engine. Tenemos uno local y otro público que se llama **DokerHub**. Podemos instalar registros en servidores privados para tener guardadas nuestras imágenes.
* El nombre de una imagen suele estar formado por tres partes: `usuario/nombre:etiqueta`:
    * `usuario`: El nombre del usuario que la ha generado. Las **imáges oficiales** en Docker Hub no tienen nombre de usuario.
    * `nombre`: Nombre significativo de la imagen.
    * `etiqueta`: Nos permite versionar las imágenes. De esta manera controlamos los cambios que se van produciendo en ella. Si no indicamos etiqueta, por defecto se usa la etiqueta `latest`, por lo que la mayoría de las imágenes tienen una versión con este nombre.

## Gestión de imágenes

Para crear un contenedor es necesario usar una imagen que tengamos descargado en nuestro registro local. Por lo tanto al ejecutar `docker run` se comprueba si tenemos la versión indicada de la imagen y si no es así, se precede a su descarga.

Las principales instrucciones para trabajar con imágenes son:

* `docker images`: Muestra las imágenes que tenemos en el registro local.
* `docker pull`: Nos permite descargar la última versión de la imagen indicada.
* `docker rmi`: Nos permite eliminar imágenes. No podemos eliminar una imagen si tenemos algún contenedor creada a partir de ella.
* `docker search`: Busca imágenes en Docker Hub.
* `docker inspect`: nos da información sobre la imagen indicada:

En las imágenes además del sistema de fichero, se configura el proceso que se ejecuta en el contenedor sino indicamos ninguno. Esta información se guarda en parámetro `ENTRYPOINT`.

## Organización de las imágenes

* Una **capa** es un conjunto de archivos que representan **cambios** en un sistema de ficheros:

    * Instalación de un paquete
    * Copia de un archivo
    * Modificación de configuración

    Veremos más adelante que podemos crear una imagen y que cada cambio que hagamos sobre un sistema base formara una capa distinta.
    
* Todas esas capas son **de solo lectura** y se guardan en directorios distintos. 
* Docker usa un **union filesystem** para **apilar** esas capas una encima de otra para obtener un sistema de ficheros completo que es el que usará el contenedor.

    ```
    ┌──────────────────────────┐
    │ Capa 3: index.html       │
    ├──────────────────────────┤
    │ Capa 2: nginx instalado  │
    ├──────────────────────────┤
    │ Capa 1: Ubuntu base      │
    └──────────────────────────┘
    ```

* Se ahorra mucho espacio en disco (**aprovisionamiento ligero**) ya que podemos tener imágenes que compartan las mismas capas, esas capas sólo se guardan una vez.
* Cuando creamos un contenedor a partir de una imagen:
    * Docker monta las **capas de solo lectura** de la imagen.
    * Añade **encima** una **capa de escritura** exclusiva del contenedor de escritura y lectura donde se van guardando las modificaciones que realiza el contenedor en el sistema de arhivos (**parecido a la clonación ligada en las máquinas virtuales**). Resultado final:

    ```
    ┌─────────────────────────────────┐ ← Capa RW: cambios del contenedor
    │ Logs, configs, archivos nuevos  │
    ├─────────────────────────────────┤
    │ Capas de la imagen (RO)         │  ← Vista completa del sistema
    └─────────────────────────────────┘
    ```

* Si el contenedor escribe, borra o modifica algo, ese cambio se hace en la capa del contenedor de lectura/escritura.
* Cunado creamos un contenedor, ocupa muy poco espacio en disco. Ira ocupando conforme vaya modificando el sistema de ficheros en la capa del contenedor.
* Si borras el contenedor se pierde su capa, se pierden todos sus datos.
* No podemos borrar una imagen del que tengamos un contenedor creado, ya que utiliza sus capas para funcionar.

Veamos un ejemplo:

Veamos el tamaño de nuestra imagen `ubuntu`:

```bash
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
ubuntu       latest    97bed23a3497   3 weeks ago    78.1MB
```

Si creamos un contenedor interactivo:

```bash
$ docker run -it --name contenedor1 ubuntu
```

Nos salimos, y a continuación visualizamos los contenedores con la opción `-s` (size):

```bash
 docker ps -a -s
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS      NAMES          SIZE
de812a3f6b9b   ubuntu    "/bin/bash"              11 seconds ago   Exited (0) 9 seconds ago              contenedor1    5B (virtual 78.1MB)
```

Nos damos cuenta que el tamaño real del contenedor es 5B y el virtual, el que comparte con la imagen son los 78,1MB que es el tamaño de la imagen ubuntu.

Si a continuación volvemos a acceder al contenedor y creamos un fichero:

```bash
$ docker start contenedor1
root@a2d1ce6990d8:/# echo "00000000000000000">file.txt
```

Y volvemos a ver el tamaño, vemos que ha crecido con la creación del fichero:

```bash
$ docker ps -a -s
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS      NAMES          SIZE
de812a3f6b9b   ubuntu    "/bin/bash"              2 minutes ago    Exited (0) 12 seconds ago              contenedor1    79B (virtual 78.1MB)
```

Por todo lo que hemos explicado, ahora se entiende  que **no podemos eliminar una imagen cuando tenemos contenedores creados a a partir de ella**.

```
$ docker rmi ubuntu
Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container de812a3f6b9b is using its referenced image 97bed23a3497
```

## Creación de contenedores desde imágenes

Si navegas un poco por las distintas imágenes que encuentras en el registro de Docker Hub, te darás cuenta, que existen tres tipos de imágenes según la utilidad que nos ofrecen.

* Ejecutaremos contenedores de distintos sistemas operativos (Ubuntu, CentOs, Debian, Fedora....).
* Ejecutaremos contenedores con distintos lenguajes de programación (PHP, Java, Python,...)
* Ejecutaremos contenedores que tengan servicios asociados (Apache, MySQL, Tomcat....).
* Ejecutaremos contenedores que tengan servicios asociados y que tienen instalada alguna aplicación web (WordPress, Nextcloud,...)

Todas las imágenes tiene definidas un proceso que se ejecuta por defecto, pero en la mayoría de los casos podemos indicar un proceso al crear un contenedor.

## Ejemplo: Desplegando la aplicación mediawiki

La mediawiki en una aplicación web escrita en PHP que nos permite gestionar una wiki. En este ejemplo vamos a hacer un ejemplo simple de despliegue en contenedor usando la imagen [`mediawiki`](https://hub.docker.com/_/mediawiki) que encontramos en DockerHub. 

En concreto, si estudiamos la [documentación](https://hub.docker.com/_/mediawiki) de la imagen `mediawiki`, podemos ver las etiquetas disponibles para la imagen que corresponden a versiones distintas de la aplicación.

Ejemplo de creación de distintos contenedores con distintas versiones de mediawiki:

```bash
docker run -d -p 8080:80 --name mediawiki1 mediawiki
docker run -d -p 8081:80 --name mediawiki2 mediawiki:1.43
docker run -d -p 8082:80 --name mediawiki3 mediawiki:1.39
```
Podemos acceder a los distintos puestos que hemos indicado para acceder a cada contenedor y a las instalaciones de distintas versiones de la mediawiki.

**Nota: Puedes observar que la primera imagen que se baja, descargas todas las capas, sin embargo al descargar las otras versiones de la imagen, sólo se bajan las capas que difieren de la primera.**