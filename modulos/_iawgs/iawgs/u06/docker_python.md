---
title: "Práctica: Implantación de aplicaciones web Python en docker"
permalink: /iawgs/u06/docker_python.html
--- 

## Tarea 1: Ejecución de una aplicación web Python en docker (1)

* Queremos ejecutar en un contenedor docker la aplicación web escrita en python: Gestion IESGN ([https://github.com/jd-iesgn/iaw_gestionGN](https://github.com/jd-iesgn/iaw_gestionGN)).
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu, que ejecute la aplicación con python y que sea servido por un servidor web apache2.
* Crea un contenedor a partir de la imagen anterior.
* Crea la base de datos y añade los datos de prueba de la base de datos (Utiliza el fichero `datos.json`).
* La base de datos debe estar guardada en un volumen.
* Comprueba que la aplicación está funcionando. Usuario: `admin` contraseña: `asdasd1234`.

{% capture notice-text %} 
* Describe los pasos más importantes para realizar la tarea. Muestra los ficheros de configuración que has usado. (3 puntos).
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Ejecución de una aplicación web Python en docker (2)

Realiaza las modificaciones necesarias para crear una imagen de la aplicación web que cumpla las siguientes características:

* Es necesario tener un contenedor con mariadb donde vamos a crear la base de datos y los datos de la aplicación. 
* El contenedor mariadb debe tener un volumen para guardar la base de datos.
* Realiza la imagen docker de la aplicación a partir de la imagen oficial [python](https://hub.docker.com/_/python/) que encuentras en docker hub. 
* Crea un script con `docker compose` que levante el escenario con los dos contenedores.
* Comprueba que la aplicación está funcionando.

{% capture notice-text %} 
* Describe los pasos más importantes para realizar la tarea. Muestra los ficheros de configuración que has usado. (4 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Ejecución de una aplicación python en docker (3)

* En este caso queremos usar un contenedor que utilice nginx para servir la aplicación python. Puedes crear la imagen desde una imagen base debian o ubuntu o desde la imagen oficial de nginx.
* Vamos a crear otro contenedor que sirva `uwsgi` o `gunicorn`.
* Crea un script con `docker compose` que levante el escenario con los tres contenedores.

{% capture notice-text %} 
* Documenta el proceso que has realizado para crear el escenario. Entrega el script de docker compose y realiza alguna prueba de funcionamiento. (4 puntos).
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Tarea 4: Ejecución de un CMS python en docker 

* A partir de una imagen base (que no sea una imagen con el CMS), genera una imagen que despliegue un CMS python: [django CMS](https://www.django-cms.org/en/). 
* Crea un contenedor y comprueba que el CMS está funcionando.

{% capture notice-text %} 
* Explica los pasas más importantes en la creación y puesta en marcha del contenedor con el CMS (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Ejecución de un CMS en docker (2)

Modifica la imagen creada para que el contenedor que se crea tenga que enlazar con un contenedor mariadb o postgreSQL.

{% capture notice-text %} 
* Explica los pasos más importantes en la creación y puesta en marcha del contenedor con el CMS (2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
