---
title: "Ejercicios peticiones a API web con curl"
permalink: /lmgs/u09/curl.html
---

## API restful swapi

[swapi](https://swapi.dev/) es una API restful que ofrece información sobre Star Wars. No es necesario a autentificarte y la documentación la obtienes en la dirección: [https://swapi.dev/documentation](https://swapi.dev/documentation).

1. Muestra información del personaje que tiene el código 1:

	"curl https://swapi.dev/api/people/1/"

2. Realiza la petición HTTP para obtener todos los personajes de la saga:

		curl "https://swapi.dev/api/people/"

	Como hay tantos personajes la respuesta esta páginada, es decir, te devuelve un conjunto de personajes por página, si te fijas al en el json, te indica la dirección de la siguiente página (`next`), a dirección de la página anterior (`previous`) y la cantidad de personajes (`count`):

		...
		"previous" : null,
   		"count" : 82,
   		"next" : "http://swapi.dev/api/people/?page=2"
		...

	Por la tanto ahora si queremos ver la siguiente página de personajes, hago una petición a (**cuidado que hay que usar https, aunque ponga http**):

		curl "https://swapi.dev/api/people/?page=2"

	Y veamos donde están las siguientes páginas:

		...
		"next" : "http://swapi.dev/api/people/?page=3",
	   "previous" : "http://swapi.dev/api/people/?page=1",
   		"count" : 82
		...

{% capture notice-text %}

* Ejercicio 1: Muestra la información de Yoda (este persona está en la segunda página de personajes).
* Ejercicio 2: Muestra todas las películas de la saga. Haz otra petición para mostrar información de la pélicula "El Retorno del Jedi".

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## API restful Redmine

La documentación de la API restful de Redmine está en [https://www.redmine.org/projects/redmine/wiki/Rest_api](https://www.redmine.org/projects/redmine/wiki/Rest_api).
Utilizando el comando `curl` realiza peticiones a las API web de las distintas aplicaciones para obtener la siguiente información:

1. Programa que muestre el nombre de los proyectos públicos de la aplicación redmine de nuestro ciclo. Utiliza la respuesta XML.

		curl "https://dit.gonzalonazareno.org/redmine/projects.xml"

	Si quiero la respuesta en XML, si la quiero en json:

		curl "https://dit.gonzalonazareno.org/redmine/projects.json"

2. Programa que muestre el nombre de los proyectos de la aplicación redmine de nuestro ciclo. Para ello necesitas autentificarte con la API key. Utiliza la respuesta XML. 

	Lo primero que hacemos es guardar nuestra API KEY en una variable de entorno:

		export key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

		curl "https://dit.gonzalonazareno.org/redmine/projects.xml?key=$key"

	Si queremos la respuesta en json:

	curl "https://dit.gonzalonazareno.org/redmine/projects.json?key=$key"

{% capture notice-text %}

* Ejercicio 1: Obtén información del proyecto 1ºASIR. Tendrás que hacer dos peticiones una para obtener el id del proyecto, y otra para obtener información de dicho proyecto.
* Ejercicio 2: Obtén información de las tareas que tienes asignadas en el proyecto 1ª ASIR.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
