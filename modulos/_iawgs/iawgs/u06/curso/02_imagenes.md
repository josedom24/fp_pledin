---
title: "Imágenes docker"
permalink: /iawgs/u06/curso/imagenes.html
---

## Registros de imágenes: Docker Hub

Las imágenes son la base de Docker. Nuestros contenedores se iniciarán a partir de ellas. Podemos pensar en ellas como plantillas de solo lectura, que se crea incorporando los requisitos necesarios para cumplir el objetivo para el cual fue creada.

Un registro es...

Docker Hub ...
El nombre de las imágenes...

## Gestión de imágenes


## ¿Cómo se organizan las imágenes?

Las imágenes están hechas de **capas ordenadas**. Puedes pensar en una capa como un conjunto de cambios en el sistema de archivos. Cuando tomas todas las capas y las apilas, obtienes una nueva imagen que contiene todos los cambios acumulados. 

Si tienes muchas imágenes basadas en capas similares, como Sistema Operativo base o paquetes comunes, entonces todas éstas capas comunes será almacenadas solo una vez.

Cuando un nuevo contenedor es creado desde una imagen, todas las capas de la imagen son únicamente de lectura y una delgada capa lectura-escritura es agregada arriba. Todos los cambios efectuados al contenedor específico son almacenados en esa capa. 

El contenedor no puede modificar los archivos desde su capa de imagen (que es sólo lectura). Creará una copia del fichero en su capa superior, y desde ese punto en adelante, cualquiera que trate de acceder al archivo obtendrá la copia de la capa superior. 

Por lo tanto cuando creamos un contenedor ocupa muy poco de disco duro, porque las capas de la imagen desde la que se ha creado se comparten con el contenedor:

Veamos el tamaño de nuestra imagen `ubuntu`:

    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ubuntu              latest              f63181f19b2f        7 days ago          72.9MB

Si creamos un contenedor interactivo:

    $ docker run -it --name contenedor1 ubuntu /bin/bash 

Nos salimos, y a continuación visualizamos los contenedores con la opción `-s` (size):

    $ docker ps -a -s
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                       PORTS               NAMES               SIZE
    a2d1ce6990d8        ubuntu              "/bin/bash"              8 seconds ago       Exited (130) 5 seconds ago                       contenedor1         0B (virtual 72.9MB)

Nos damos cuenta que el tamaño real del contenedor es 0B y el virtual, el que comparte con la imagen son los 72,9MB que es el tamaño de la imagen ubuntu.

Si a continuación volvemos a acceder al contenedor y creamos un fichero:

    $ docker start contenedor1
    contenedor1
    $ docker attach contenedor1
    root@a2d1ce6990d8:/# echo "00000000000000000">file.txt

Y volvemos a ver el tamaño, vemos que ha crecido con la creación del fichero:

    $ docker ps -a -s
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES               SIZE
    a2d1ce6990d8        ubuntu              "/bin/bash"              56 seconds ago      Exited (0) 2 seconds ago                        contenedor1         52B (virtual 72.9MB)

## Creación de instancias desde imágenes

Si navegas un poco por las distintas imágenes que encuentras en el registro de Docker HUB, te darás cuenta, que existen dos tipos de imágenes según la utilidad que nos ofrecen.

* Ejecutaremos contenedores de distintos sistemas operativos (Ubuntu, CentOs, Debian, Fedora....).
* Ejecutaremos contenedores que tengan servicios asociados (Apache, MySQL, Tomcat....).

Normalmente las imágenes de sistemas operativos genéricos, no tienen definida el proceso que debe ejecutar el contenedor. Por ello cuando creamos un contenedor a partir de ellos indicamos el comando:

    $ docker run ubuntu /bin/echo 'Hello world'

Sin embargo las imágenes que nos ofrecen alguna aplicación en concreto y nos ofrecen algún servicio (web, base de datos,...) tienen definido el proceso que tienen que ejecutar al crear el contenedor. Por ejemplo, como ya hemos visto al crear un contenedor de la imagen `httpd:2.4` ese contenedor ejecuta una servidor web sin que nosotros lo hayamos indicado:

    $ docker run -d --name my-apache-app -p 8080:80 httpd:2.4