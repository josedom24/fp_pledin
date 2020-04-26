---
title: "Ejercicios peticiones a API web con curl"
permalink: /lmgs/u09/curl.html
---

## API Redmine

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
