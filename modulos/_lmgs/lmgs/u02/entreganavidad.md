---
title: "Entrega "
permalink: /lmgs/u02/entreganavidad.html
---

1. Juego Mastermind. El juego consiste en que el ordenador piensa en 4 dígitos no repetidos (se guardan en una cadena de caracteres). Luego se va pidiendo al usuario número de 4 dígitos para acertar el que ha generado de forma aleatoria. La respuesta del programa será la siguiente:

	* Si acertamos un dígito y está en la misma posición contará un acierto
	* Si acertamos un dígito pero no está en la mismo posición contará una coincidencia.

	Cuando acertemos el número nos dirá en los intentos que lo hemos adivinado.

	Ejemplo:

		Bienvenido/a al Mastermind!
		Tenes que adivinar un numero de 4 cifras distintas
		Que código propones?: 1234
		Tu propuesta ( 1234 ) tiene 0 aciertos y  1 coincidencias.
		Propone otro código: 5678
		Tu propuesta ( 5678 ) tiene 0 aciertos y  1 coincidencias.
		Propone otro código: 1590
		Tu propuesta ( 1590 ) tiene 1 aciertos y  1 coincidencias.
		Propone otro código: 2960
		Tu propuesta ( 2960 ) tiene 2 aciertos y  1 coincidencias.
		Propone otro código: 0963
		Tu propuesta ( 0963 ) tiene 1 aciertos y  2 coincidencias.
		Propone otro código: 9460
		u propuesta ( 9460 ) tiene 1 aciertos y  3 coincidencias.
		Propone otro código: 6940
		Felicitaciones! Adivinaste el código en 7 intentos.

2. Escribe un programa para jugar al ahorcado.

	* Un jugador introduce una palabra secreta y otro jugador tratará de adivinarla.
	* La pantalla se limpia y aparece la horca vacía, el número de intentos y la palabra a acertar, donde cada letra se sustituye por un asterisco.

		```
		EL JUEGO DEL AHORCADO

		  +---+
		  |	  |
		  	  |
		  	  |
		  	  |
		  	  |
		  ======

		Palabra a acertar :********
		Fallos : 0
		Letras utilizadas :

		Introduce una letra ( '*' para resolver ):
		```
	Reglas del juego:

	* El jugador puede cometer como máximo 6 fallos. Por cada fallo aparecerá un elemento más en la horca: cabeza, tronco, brazo izquierdo, brazo derecho,
pierna izquierda y pierna derecha.
	* Cada letra acertada aparecerá en la lista de letras utilizadas y se sustituirá en la posición que corresponda en la palabra a acertar.
	* Una letra ya utilizada contará siempre como fallo (Esté o no en la palabra a acertar)
	* No se permite el uso de vocales
	* El jugador puede intentar resolver la palabra a acertar en cualquier momento tecleando la tecla `*`, tras lo cual se solicitará la palabra.
	* El juego termina cuando el número de fallos es igual a 6 o cuando el jugador acierta la palabra, solicitando la resolución de la misma.
	* Cualquier otro carácter que se introduzca: numero o signo de puntuación, contará como fallo.
	* En un momento cualquiera el programa mostrará:

		```
		EL JUEGO DEL AHORCADO

		   +---+
		   |   |
		   o   |
		  /|   |
		       |
		       |
		   ======

		Palabra a acertar :y**t*p***t*
		Fallos : 3
		Letras utilizadas : y n m p t b 

		Introduce una letra ( '*' para resolver ):
		```

	* Se obtendrá mayor puntuación en el ejercicio si se estructura adecuadamente el código mediante el uso de funciones.
	* Para que no se desplacen los caracteres a posiciones no deseadas, utiliza el triple apóstrofe con el print, por ejemplo:

		```
		>>> print('''
		  +---+
		  |	  |
		  o	  |
		 /|	  |
		  	  |
		  	  |
		  ======
		''')
		```

	* Para limpiar la pantalla se puede utilizar (en GNU/Linux):
		```
		import os
		os.system ('clear')
		```


