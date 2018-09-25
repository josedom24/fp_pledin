---
title: "Ejercicio 1: Hacer peticiones HTTP: GET, HEAD y POST"
permalink: /serviciosgs/u03/ejercicio1.html
---

1. Utilizando el comando de linux HEAD visualiza la información de la cabeceras de los URL:

		http://dit.gonzalonazareno.org
		http://informatica.gonzalonazareno.org/proyectos/index.html
		http://josedom24.github.io/img/yo1.jpg

	Identifica todos los parámetros que puedas.

	Utiliza algún plugin de firefox  para identificar las cabeceras de las peticiones y de las respuestas.


2. Utilizando el método GET obtén el contenido de la página:

    	http://dit.gonzalonazareno.org/moodle/index.php
    	http://dit http://www.debian.org/index.html

	Comprueba con el plugin de firefox cuantas peticiones se realizan al acceder a estas páginas.


3. Envío de información al servidor, comprueba como se manda información al servidor mediante el método GET en la URL:

		http://playerone.josedomingo.org/ejget.php?valor=hola
		http://dit.gonzalonazareno.org/moodle/course/view.php?id=4

	Usando el comando GET manda tu nombre a la página: 

		http://playerone.josedomingo.org/ejget.php
        
	Usando el comando POST (que envia el contenido en el cuerpo) manda tu nombre a la página:

		http://playerone.josedomingo.org/ejpost.php
