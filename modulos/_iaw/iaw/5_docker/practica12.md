---
title: "Práctica 1 (2 / 2): Implantación de aplicaciones web PHP en docker"
---

## Puesta en producción de nuestra aplicación

* Sube la iamgen que has generado a Docker Hub.
* En tu VPS instala Docker y utilizando el `docker-compose.yaml` para desplegar la aplicación.
* Configura el nginx de tu VPS para que haga de proxy inverso y nos permita acceder a la aplicación con `https://biblioteca.tudominio.xxx`.

{% capture notice-text %} 
* Entrega una captura de pantalla de Docker Hub donde se vea tu imagen subida.
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