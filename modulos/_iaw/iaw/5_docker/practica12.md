---
title: "Práctica 1 (2 / 2): Implantación de aplicaciones web PHP en docker"
---

## Puesta en producción de nuestra aplicación

* Sube la imagen que has generado a Docker Hub.
* En tu VPS instala Docker y utilizando el `docker-compose.yaml` para desplegar la aplicación.
* Configura el nginx de tu VPS para que haga de proxy inverso y nos permita acceder a la aplicación con `https://biblioteca.tudominio.xxx`.

Seguramente tendrás que cambiar el fichero `docker-compose.yaml` de desarrollo a producción (puede que cambie algún valor de alguna variable de entorno, el número del puerto,...). Para poder usar el mismo fichero `docker-compose.yml` en todos los entornos se suele parametrizar este fichero como se explica en esta [página](https://github.com/josedom24/curso_docker_ow/blob/main/contenido/modulo6/variables.md).

Parametriza el fichero `docker-compose.yaml` y crea dos ficheros distintos `.env` para el entorno de desarrollo y el entorno de producción. El fichero `.env` no se guarda en el repositorio git, por lo que es conveniente meterlo en el fichero `.gitignore`.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega el fichero `docker-compose.yaml` parametrizado y los ficheros `.env` de desarrollo y producción.
* Entrega la configuración de nginx.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Modificación de la aplicación

* En el entorno de desarrollo vamos a hacer una modificación de la aplicación. Por ejemplo modifica el fichero `Views/index.php` y pon tu nombre en la línea `<h1>Bienvenido</h1>`.
* Vuelve a crear la imagen con la etiqueta `v2`.
* Cambia el `docker-compose.yaml` para probar el cambio.
* Modifica la aplicación en producción.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
* Entrega una captura de pantalla donde se vea funcionando la aplicación, una vez que te has logueado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>