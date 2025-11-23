---
tittle: "Tarea - Docker"
---

Queremos implantar distintas aplicaciones web con Docker en nuestro VPS. Utilizaremos nuestro servidor web `nginx` que tenemos instalado en el VPS como **proxy inverso**. 

Vamos a ir realizando distintos ejercicios:

## Ejercicio 1

Instala la versión **1.43** de la aplicación `mediawiki` puedes usar la [documentación](https://hub.docker.com/_/mediawiki) de la imagen de Docker Hub. Guarda en un **volumen Docker** el directorio `/var/www/html/images` para no perder las imágenes que subas a la wiki. Además tienes que guardar en otro volumen el directorio `/var/www/data` que es el directorio donde se encuentra la base de datos SQLite.

Durante la instalación elije **SQLite**, pon tu nombre al título de la wiki. Cuando termina la instalación te puedes bajar el fichero de configuración `LocalSettings.php`. Elimina el contenedor y vuelve a crearlo pero montando el fichero `LocalSettings.php` en el fichero del contenedor `/var/www/html/LocalSettings.php` (tienes que usar un **bind mount**)-

Configura el proxy inverso para acceder con HTTPS a la aplicación utilizando el nombre `wiki.tudominio.algo`. Accede a la aplicación, configúrala y realiza alguna modificación para que se vea tu nombre.

Ahora vamos a actualizar la aplicación: vamos a instalar la **última** versión de la aplicación `mediawiki`, para ello borra el contenedor y crear uno nuevo desde la imagen de la última versión, con los mismos puntos de montaje.

Para terminar la actualización debes ejecutar en el contenedor el siguiente comando:

```
php /var/www/html/maintenance/update.php --quick
```

Comprueba que la aplicación sigue funcionando sin ningún problema.

{% capture notice-text %}
## Entrega

1. El comando para crear el contenedor de `mediawiki` con la versión 1.43. Muestra la lista de contenedores que se están ejecutando.
2. Captura de pantalla accediendo a la aplicación donde se ve la versión que se está instalando. Y otra captura donde sea vea la aplicación configurada donde aparece tu nombre.
3. Muestra el listado de volúmenes para ver el volumen donde se ha guardado los datos de la aplicación.
4. El comando para crear el contenedor con la última versión. Muestra la lista de contenedores que se están ejecutando.
5. Captura de pantalla donde se comprueba que la aplicación sigue funcionando y se sigue viendo tu nombre.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio 2

Ahora vamos a instalar la aplicación mediawiki para que que guarde la información en una base de datos mariaDB. Elimina el contador del ejercicio 1.

Crea una red definida por el usuario para conectar los contenedores: 

* Crea un contenedor con mariaDB y configúralo de manera adecuada para que cree una base d e datos y un usuario con contraseña. Guarda en un **bind mount** el directorio donde se guarda la base de datos para que el contenedor sea persistente.
* Crea un contenedor mediawiki (con la úlrima versión) configurado para que conecte de manera adecuada a la base de datos que hemos creado. En esta ocasión sólo tienes que guardar en un **bind mount** el directorio `/var/www/html/images`, ya uqe no tenemos base de datos SQLite. Recuerda que al terminar la instalación tendrás que montar con un bind mount el fichero `LocalSettings.php`.

Escribe un artículo en la wiki donde subas una imagen. Comprueba posteriormente que si eliminas los contenedores y los vuelves a crear con las mismas características, el artículo con la imagen siguen existiendo.

{% capture notice-text %}
## Entrega

1. El comando para crear la red, el contenedor de mariaDB y el de mediawiki.
2. Captura de pantalla accediendo a la aplicación donde se ve la versión que se está instalando. Y otra captura donde sea vea la aplicación configurada donde aparece tu nombre y el artículo que has escrito.
3. Muestra como has borrado los contenedores y lo has vuelto a crear.
4. Captura de pantalla donde se comprueba que la aplicación sigue funcionando, se sigue viendo tu nombre y el artículo que has escrito.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio 3

Ahora vamos a utilizar Docker Compose para gestionar el ciclo de vida de la aplicación mediawiki. Para ello, elimina los contenedores que tienes creado.
Define en un fichero `docker-compose.yaml` el escenario para crear los dos contenedores, teniendo en cuenta que tienes en los bind mount la información persiste de la mediawiki y de la base de datos, así como el fichero de configuración `LocalSettings.php`.

Inicia el escenario, con el comando `docker compose`, comprueba que los contenedores están funcionando, con `docker compose`.
Accede a la página web y comprueba que la aplicación sigue funcionando, se sigue viendo tu nombre y el artículo que has escrito.

{% capture notice-text %}
## Entrega

1. El contenido del fichero `docker-compose.yaml`.
2. El comando y la salida de la instrucción para iniciar el escenario.
3. El comando y la salida de la instrucción para listar los contenedores en ejecución.
4. Captura de pantalla donde se comprueba que la aplicación sigue funcionando, se sigue viendo tu nombre y el artículo que has escrito.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
