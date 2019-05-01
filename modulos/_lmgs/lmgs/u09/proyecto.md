---
title: "Proyecto 3ª evaluación: Utilización de API web"
permalink: /lmgs/u09/proyecto.html
---

## Objetivo

El objetivo fundamental del proyecto es la realización de una página web alojada en Heroku y creada con el web framework python Flask, que utilizando algún servicio web proporcione una funcionalidad original.

## Proceso

El proceso de realización del proyecto tendrá las siguientes etapas:

* Estudio y búsqueda de uno o varios servicios web (API Restful). Se tendrá en cuenta que tipo de autentificación nos ofrece, así cómo el tipo de los datos que nos devuelve. 
* Una vez que se ha elegido la API con la que se va a trabajar, se entregará un "anteproyecto" explicando los objetivos y funcionalidades del proyecto. El profesor lo valorará y el alumno podrá empezar la implementación. 
* Codificación del proyecto: El alumno empezará a construir la página web alojada en Heroku. Al mismo tiempo todos los cambios que vaya realizando se registrarán en un repositorio GitHub.
* Una vez concluido el proyecto se mostrará su funcionamiento al profesor.

## Pre-evaluación del proyecto

Para hacer una estimación de la nota que puedes sacar en el proyecto vamos a ver distintos tipos de proyectos que se pueden hacer:

* Aplicación que consume información de un servicio web: **Nota: 5**
* Aplicación que consume de dos servicios web: **Nota: 6**
* Aplicación que consume y modifica un servicio web: **Nota: 7**
* Aplicación que consume de un servicio web y modifica otro servicio web: **Nota: 8**
* Aplicación que consume y modifica varios servicios web: **Nota: 9**

Todas las aplicaciones deben tener hoja de estilo y tener un HTML válido. Se valorará de forma positiva la innovación que se consiga en la construcción de la aplicación.

## ¿Qué debe entregar el alumno?

### Fase 0: Anteproyecto

Es el enunciado del proyecto que se debe entregar antes de comenzar la etapa de codificación se tendrán que indicar los siguientes apartados:

* Nombre del proyecto:
* Objetivos, descripción y funcionalidad del proyecto:
* URL del repositorio GitHub:
* URL de la página web:

* ¿Cuántas API web vas a usar en el proyecto?: 
	* URL de la API(s) utilizada(s):
	* Lenguaje(s) de marcas que utiliza(n) la(s) API:
	* ¿Qué tipo de autentificación tiene(n) la(s) API utilizada(s)?:
	* ¿Qué métodos vas a usar en las llamada a la API?, es decir, ¿vas a consumir información del servicio web (métodos GET)?, o también, ¿vas a modificar los recursos del servicio web (métodos POST, PUT, DELETE,...)?:

### Fase 1: Consultas a la API

Debes entregar al menos tres peticiones a la API que vayas a realizar en el proyecto. Si la API utiliza autentificación oauth realiza las pruebas utilizando el simulador de peticiones que suelen tener estas APIS.

### Fase 2: Petición con python

Entrega un programa python (que funcione en la terminal) que haga una de las tres peticiones que has mostrado en la fase anterior.

### Fase 3: Diseño de la aplicación

Explica cada una de las rutas que va a tener la aplicación web:

* Nombre de la ruta
* ¿Se accede con get o con post?
* ¿Qué se hace en esa ruta?

### Fase 4: Aplicación web en heroku

Muestra al profesor y entrega una captura de pantalla donde se vea la página web escrita en flask (con la hoja de estilo) desplegada en heroku.

### Fase 5: Peticiones y formularios

Muestra al profesor y entrega una captura de pantalla donde se vea el funcionamiento de algún formulario en tu aplicación y la realización de alguna petición a algún servicio web en el mismo.

### Fase 6: Termina la aplicación

## Evaluación final

La evaluación final del proyecto se realizará teniendo en cuenta los siguientes aspectos:

* Puntuación técnica del proyecto (teniendo en cuenta la valoración del apartado **Pre-evaluación del proyecto**) (70%).
* Asistencia a clase y participación activa en el proyecto: Es importante hablar, preguntar, discutir con el profesor acerca de tu proyecto. Sería muy importante que desde el primer momento el profesor supiera que vas a hacer, que problemas tienes, por donde vas, ... En este punto también se tendrá en cuenta los puntos que hemos indicado que debes enseñar al profesor.(20%).
* Corrección del proyecto: Se valorará el repositorio GitHub entregado (debe tener un fichero `README.md` explicando de forma clara el contenido del repositorio), además la corrección se realizará de la aplicación web ejecutándose en Heroku. Se valorará la originalidad del proyecto, la facilidad de uso y la funcionalidad del mismo.(10%).