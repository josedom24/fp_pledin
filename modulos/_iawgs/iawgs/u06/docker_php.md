---
title: "Práctica: Implantación de aplicaciones web PHP en docker"
permalink: /iawgs/u06/docker_php.html
---

## Tarea 1: Ejecución de una aplicación web PHP en docker (1)

* Queremos ejecutar en un contenedor docker la aplicación web escrita en PHP: bookMedik ([https://github.com/evilnapsis/bookmedik](https://github.com/evilnapsis/bookmedik)).
* Es necesario tener un contenedor con mysql donde vamos a crear la base de datos y los datos de la aplicación. El script para generar la base de datos y los registros lo encuentras en el repositorio y se llama `schema.sql`. Debes crear un usuario con su contraseña en la base de datos. La base de datos se llama `bookmedik` y se crea al ejecutar el script.
* Ejecuta el contenedor mysql y carga los datos del script `schema.sql`. Para más [información](https://gist.github.com/spalladino/6d981f7b33f6e0afe6bb).
* El contenedor mysql debe tener un volumen para guardar la base de datos.
* Crea una imagen docker con la aplicación desde una imagen base de debian o ubuntu. Ten en cuenta que el fichero de configuración de la base de datos (`core\controller\Database.php`) lo tienes que configurar utilizando las variables de entorno del contenedor mysql.
* La imagen la tienes que crear en tu máquina con el comando `docker build`.
* Crea un contenedor a partir de la imagen anterior, enlazado con el contenedor mysql, y comprueba que está funcionando (Usuario: **admin**, contraseña: **admin**)
* El contenedor que creas debe tener un volumen para guardar los logs de apache2.

{% capture notice-text %} 
* Creación del contenedor mysql y carga de los datos (1 punto).
* Creación de la imagen docker bookmedik (2 puntos).
* Creación del contenedor con la aplicación web. (1 punto).
* Comprueba que si borramos el contenedor mysql y volvemos a crear otro, los datos no se han perdido porque se han guardado en un volumen. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Ejecución de una aplicación web PHP en docker (2)

* Realiza la imagen docker de la aplicación a partir de la imagen oficial [PHP](https://hub.docker.com/_/php/) que encuentras en docker hub. Lee la documentación de la imagen para configurar una imagen con apache2 y php, además seguramente tengas que instalar alguna extensión de php.
* Crea esta imagen en docker hub.
* Crea un script con docker compose que levante el escenario con los dos contenedores.


{% capture notice-text %} 
* Documenta como has creado el Dockerfile para crear la imagen, entrega la URL del repositorio github donde has guardado el contexto para a creación de la imagen (2 puntos).
* Docuementa el uso de docker compose, entrega el script que has desarrollado. (1 punto)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Ejecución de una aplicación PHP en docker (3)

* En este caso queremos usar un contenedor que utilice nginx para servir la aplicación PHP. Puedes crear la imagen desde una imagen base debian o ubuntu o desde la imagen oficial de nginx.
* Vamos a crear otro contenedor que sirva php-fpm.
* Y finalmente nuestro contenedor con la aplicación.
* Crea un script con docker compose que levante el escenario con los tres contenedores.

A lo mejor te puede ayudar el siguiente enlace: [Dockerise your PHP application with Nginx and PHP7-FPM](http://geekyplatypus.com/dockerise-your-php-application-with-nginx-and-php7-fpm/)


{% capture notice-text %} 
* Documenta el proceso que has realizado para crear el escenario. Entrega el script de docker compose y realiza alguna prueba de funcionamiento. (3 puntos).
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Tarea 4: Ejecución de un CMS en docker (1)

* A partir de una imagen base (que no sea una imagen con el CMS), genera una imagen que despliegue un CMS PHP (que no sea wordpress). El contenedor que se crea a partir de esta imagen se tendrá que enlazar con un contenedor mysql o postgreSQL.
* Crea los volúmenes necesarios para que la información que se guarda sea persistente.

{% capture notice-text %} 
* Elige un CMS PHP y crea la imagen que despliega la aplicación. Crea los contenedores necesarios para servir el CMS. Entrega una prueba de funcionamiento.
* Elimina los contenedores, vuelve a crearlos y demuestra que la información no se ha perdido.
	(2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Ejecución de un CMS en docker (2)

Busca una imagen oficial de un CMS PHP en docker hub (distinto al que has instalado en la tarea anterior, ni wordpress), y crea los contenedores necesarios para servir el CMS, siguiendo la documentación de docker hub.

{% capture notice-text %} 
Explica el proceso que has seguido para realizar la tarea, pon alguna prueba de funcionamiento. ¿Se ha creado algún volumen para que la información sea persistente?
	(2 puntos)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
