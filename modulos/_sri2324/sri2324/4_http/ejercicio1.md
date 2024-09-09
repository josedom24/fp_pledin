---
title: "Ejercicio 1: Peticiones HTTP"
---

## ¿Qué vas a aprender en este ejercicio?

* Repasar los conceptos aprendidos en el estudio del protocolo HTTP. 
* Realizar peticiones HTTP con curl
* Utilizar las herramientas de desarrollo de los navegadores web para analizar las peticiones y respuestas HTTP.

## ¿Qué tienes que hacer?

Veamos algunas opciones de la herramienta `curl` para realizar peticiones HTTP:

* Petición GET: `curl <url>`.
* Petición GET y seguir redirección: `curl -L <url>`.
* Petición HEAD: `curl -I <url>`
* Petición POST con envío de información: `curl -X POST -d "campo1=valor1&campo2=valor" <url>`

Ejercicios que tienes que realizar:

1. Realiza una petición para ver las cabeceras de la URL `https://dit.gonzalonazareno.org`.
	¿Qué código de estado devuelve? ¿Qué significa? ¿En qué cabecera se encuentra la URL a la que hay que acceder para obtener el recurso?
2. Realiza una petición GET a `https://dit.gonzalonazareno.org`. ¿Qué tipo de redirección devuelve?. Realiza una petición a la URL `https://dit.gonzalonazareno.org` para seguir la redirección.
3. Utiliza las herramientas de un navegador web (En firefox: Herramientas para desarrolladores -> Red ) para ver las cabeceras de la URL `https://dit.gonzalonazareno.org/gestiona/`.
	¿Cuántas peticiones se han realizado para mostrar la página?. Fíjate en la petición a `https://dit.gonzalonazareno.org/gestiona/`: identifica las cabeceras más importantes de las peticiones y de las respuestas.
4. Obtén la información del cuerpo de la respuesta de la URL: `https://dit.gonzalonazareno.org/gestiona/`.
5. Usando el método GET manda tu nombre a la página `http://www2.gonzalonazareno.org/josedom/resultado.php`.
6. Usando el método POST (que envía el contenido en el cuerpo) manda tu nombre a la misma página.

