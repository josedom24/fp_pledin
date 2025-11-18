---
tittle: "Tarea - Docker"
---

Queremos implantar distintas aplicaciones web con Docker en nuestro VPS. Utilizaremos nuestro servidor web `nginx` que tenemos instalado en el VPS como **proxy inverso**. 

Vamos a ir realizando distintos ejercicios:

## Ejercicio 1

Instala la versión **1.43** de la aplicación `mediawiki` puedes usar la [documentación](https://hub.docker.com/_/mediawiki) de la imagen de Docker Hub. Guarda en un **volumen Docker** el directorio `/var/www/html/images`. En ese directorio está la base de datos SQLite.

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

