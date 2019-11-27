---
title: "Entrega: Ejercicios python3"
permalink: /lmgs/u02/entrega.html
---

## Ejercicio 1

Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2020
	Para llegar al año 2020 faltan 5 años.
    
    COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 1997
	Desde el año 1997 han pasado 18 años.
    
    COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2015
	¡Son el mismo año!


## Ejercicio 2

Juego de las multiplicaciones

**Apartado 1**

Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.

Para generar números al azar puedes utilizar el siguiente código:

    from random import randint
    a = randint(2, 10)

Ejemplos:    

    ¿Cuánto es 7 x 8? 56
    ¡Respuesta correcta!
    
    ¿Cuánto es 4 x 9? 35
    ¡Respuesta incorrecta!


**Apartado 2**

Amplie el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.

	
	Número de preguntas: 0
	El número de preguntas debe ser al menos 1	
	
	Número de preguntas: 2	
	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!

**Apartado 3**

Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado.
Ayuda: La nota se calcula con la fórmula Nota=Correctas / Total * 10.

	Número de preguntas: 2	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 5.0	

	
	Número de preguntas: 3	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	
	¿Cuánto es 2 x 3? 6
	¡Respuesta correcta!	

	Ha contestado correctamente 2 preguntas
	Le corresponde una nota de 6.7	

	Número de preguntas: 1	
	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 10.0
	¡Enhorabuena!


NOTA: **Tienes que entregar sólo el código del apartado 3.**

## Ejercicio 3

Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas) y podrá responder una de las siguientes opciones:
	
* La segunda cadena es una subcadena de la primera
* La segunda cadena no es una subcadena de la primera

Ejemplo:

	Cadena 1: Java es un lenguaje de programación
	Cadena 2: LENGUAJE
	Respuesta:
	La segunda cadena es una subcadena de la primera

## Ejercicio 4

Escribe una programa que pida una cadena de caracteres y diga si *no* tiene caracteres repetidos.

## Ejercicio 5

Tenemos la siguiente variable definida en nuestro programa:

	temperaturas='''
		Utrera,29,12
		Dos Hermanas,32,14
		Sevilla,30,15
		Alcalá de Guadaíra,31,14
	'''

En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas de dichas poblaciones durante un día.

Realiza un programa que muestre el nombre de las poblaciones y la temperatura media. Además el programa te debe pedir el nombre de una población y nos debe dar la temperatura máxima y mínima (si la población no existe se debe dar une error.)

**Ayuda: Puede venir muy bien utilizar los métodos `splitlines` y `split` de cadenas.**

## Ejercicio 6

Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones: 

* Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
* Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
* Eliminar: Me pide una cadena, y la elimina de la lista.

El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.

	Dígame cuántas palabras tiene la lista: 4
	Dígame la palabra 1: Carmen
	Dígame la palabra 2: Alberto
	Dígame la palabra 3: Benito
	Dígame la palabra 4: Carmen
	La lista creada es: Carmen, Alberto, Benito, Carmen
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
	La lista es ahora: Alberto, David, Benito, David

	3
	Palabra a eliminar: David
	La lista es ahora: Alberto, Benito	
	0
	Adiós!!!