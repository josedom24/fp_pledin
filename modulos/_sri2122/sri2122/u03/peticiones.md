---
title: "Ejercicio: Hacer peticiones HTTP: GET, HEAD y POST"
---

Para realizar estos ejercicios utiliza el comando `curl`. Aprende sus distintas opciones para realizar las siguientes peticiones.

1. Realiza una petición con el método HEAD para visualizar la información de la cabeceras de los URL:

		https://dit.gonzalonazareno.org/moodle/index.php
		
	Identifica todos los parámetros que puedas.

	Utiliza algún plugin del navegador  para identificar las cabeceras de las peticiones y de las respuestas.

2. Realiza una petición GET obtén el contenido de la página:

		https://dit.gonzalonazareno.org/moodle/index.php
		
	Comprueba con el plugin del navegador cuantas peticiones se realizan al acceder a estas páginas. 
	

3. Envío de información al servidor, comprueba como se manda información al servidor mediante el método GET en la URL. ¿Qué pasa si envíamos otro identificador, por ejemplo el 4?:

		https://dit.gonzalonazareno.org/moodle/course/view.php?id=25

	Usando el método GET manda tu nombre a la página: 

		http://www2.gonzalonazareno.org/josedom/resultado.php
        
	Usando el método POST (que envía el contenido en el cuerpo) manda tu nombre a la página:

		http://www2.gonzalonazareno.org/josedom/resultado.php