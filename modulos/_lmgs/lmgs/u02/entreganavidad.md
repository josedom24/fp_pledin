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

2. Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado. La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles.

	Por ejemplo:

		Cantidad total: 7,17 €
		Cantidad entregada: 100 €
		Cantidad a devolver: 92,83 €

		1  billete de 50 €
		2 billete de 20 €
		1 monedas de 2 €
		1 monda de 50 c
		1 moneda de 20 c
		1 moneda de 10 c
		1 moneda de 2 c
		1 moneda 1 c

3. Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones: 

	* Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
	* Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
	* Eliminar: Me pide una cadena, y la elimina de la lista.

	El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.

		Dígame cuántas palabras tiene la lista: 4
		Dígame la palabra 1: Carmen
		Dígame la palabra 2: Alberto
		Dígame la palabra 3: Benito
		Dígame la palabra 4: Carmen
		La lista creada es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
		Elige opción:
		1. Contar
		2. Modificar
		3. Eliminar	
		0. Salir	

		1
		Dígame la palabra a buscar: Carmen
		La palabra 'Carmen' aparece 2 veces en la lista.		

		2
		Sustituir la palabra: Carmen
		por la palabra: David
		La lista es ahora: ['Alberto', 'David', 'Benito', 'David']		

		3
		Palabra a eliminar: David
		La lista es ahora: ['Alberto', 'Benito']	

		0
		Adiós!!!

4. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

	* Lista de palabras que aparecen en las dos listas.
	* Lista de palabras que aparecen en la primera lista, pero no en la segunda.
	* Lista de palabras que aparecen en la segunda lista, pero no en la primera.
	* Lista de palabras que aparecen en ambas listas.

	Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

		Dígame cuántas palabras tiene la primera lista: 4
		Dígame la palabra 1: Carmen
		Dígame la palabra 2: Alberto
		Dígame la palabra 3: Benito
		Dígame la palabra 4: Carmen
		La primera lista es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
		Dígame cuántas palabras tiene la segunda lista: 3
		Dígame la palabra 1: Benito
		Dígame la palabra 2: Juan
		Dígame la palabra 3: Carmen
		La segunda lista es: ['Benito', 'Juan', 'Carmen']
		Palabras que aparecen en las dos listas: ['Carmen', 'Benito']
		Palabras que sólo aparecen en la primera lista: ['Alberto']
		Palabras que sólo aparecen en la segunda lista: ['Juan']
		Todas las palabras: ['Carmen', 'Benito', 'Alberto', 'Juan']	

5. Realizar un programa que guarde en una lista los nombre y edades de los alumnos de una clase. El programa ira pidiendo por teclado el nombre (string) y la edad (int) hasta que se introduzca como nombre un "\*". Las posiciones pares (0,2,4,...) de la lista serán cadenas y las impares son enteros. Cuando terminemos de meter datos hay que mostrar la siguiente información:

	* Los nombres de los alumnos con más edad.
	* La media de edad de la clase
	* Te pide por teclado un nombre y te dice la edad que tiene. Si hay varios alumnos con el mismo nombre te muestra todos.
	* Genera una nueva lista con los nombres y edades de los mayores de edad.

6. Repite el ejercicio 4, pero utilizando la siguiente estructura: una lista, en la cual cada elemento es una lista con dos elementos: el nombre y la edad. Por ejemplo:

	[ ["juan",18],["maría",21],["pablo",15] ]