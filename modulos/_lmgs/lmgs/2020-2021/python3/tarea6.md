---
permalink: /lmgs/2020-2021/python3/tarea6.html
layout: single3
---

# Ejercicios de listas

## Ejercicio 1

Pedir cadenas de caracteres y guardarlas en una lista (el programa pedirá al principio cuantas cadenas se van a introducir). A continuación se pide otra cadena, y hay que eliminar de la lista todas las apariciones de esta segunda cadena. Si se ha quitado algún elemento se muestra la lista, sino se informa que la segunda cadena no estaba en la lista.

## Ejercicio 2

Crear una lista con 10 número aleatorios (del 1 al 100). A continuación se muestra la lista. El programa seguirá mostrando el siguiente menú:

```
1. Sumar
2. Máximo
3. Media
4. Salir
Opción:
```

Al elegir una opción se realiza la operación:

* Sumar: Muestra la suma de los números
* Máximo: Muestra el máximo de la lista
* Medía: Muestra la Media

El menú se va repitiendo hasta que elegimos la opción 4 (Salir).

## Ejercicio 3

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

## Ejercicio 4

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

## Ejercicio 5

Vamos a crear un programa que tenga el siguiente menú:

1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3. Longitud de la lista: te muestra el número de elementos de la lista.
4. Eliminar el último número: Muestra el último número de la lista y lo borra.
5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
8. Mostrar números: Muestra los números de la lista
9. Salir

Nota: Utilizar todos los métodos de las listas que sean necesarios.