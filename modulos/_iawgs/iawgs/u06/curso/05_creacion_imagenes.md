---
title: "Creación de imágenes en docker"
permalink: /iawgs/u06/curso/creacion_imagenes.html
---

## Creación de imágenes en docker

Hasta ahora hemos creado contenedores a partir de las imágenes que encontramos en Docker Hub. Estas imágenes las han creado otras personas.

Para crea un contenedor que sirva nuestra aplicación, tendremos que crear una imagen personaliza, es lo que llamamos "dockerizar" una aplicación.

![docker](img/build.png)

* [Creación de una nueva imagen a partir de un contenedor](creacion_imagenes_contenedor.html)
* [Creación de imágenes con fichero Dockerfile](creacion_imagenes_dockerfile.html)
* [Creación automática de imágenes en Docker Hub](creacion_imagenes_dockerhub.html)

Una vez que hemos visto cómo crear imágnes docker, podemos estudiar el proceso de puesta en producción de aplicaciones web usandos docker:

* [Ciclo de vida de nuestras aplicaciones con docker](ciclo_vida.html)

**El ciclo de vida de una aplicación docker** lo podría resumir en:

* Paso 1:Desarrollo de nuestra aplicación
* Paso 2: Creación de la imagen Docker
* Paso 3: Probamos nuestra aplicación en el entorno de desarrollo o prueba
* Paso 4: Distribuimos nuestra imagen
* Paso 5:Implantación de la aplicación en el entorno de producción
* Paso 6: Modificación de la aplicación, volviendo al paso 2.

## Ejercicio: Despliegue de páginas estáticas con docker

## Ejercicios

1. Create una cuenta en Docker Hub