---
permalink: /lmgs/2020-2021/python3/tarea7.html
layout: single3
---

# Ejercicios

## Ejercicio 1

Queremos guardar el nombre de los artículos de un almacén y sus precios. Como estructura de datos vamos a usar dos listas: articulos, donde vamos a guardar el nombre de los artículos y precios donde vamos a guardar los precios. De tal forma que el artículo en la posición n de la lista artículos tendrá el precio correspondiente a la misma posición en la lista precios.

Realiza un programa que pida por teclado artículos y sus precios (el programa pedirá cuantos artículos se van a introducir), al finalizar dará la siguiente información:

* El precio medio de los arículos.
* El nombre de los articulos que valen más de 100 euros.
* Nos pedirá un nombre de un artículo y si exuste nos dará su precio, sino nos dará un error.

## Ejercicio 2

Repite el ejercicio 1 con la siguiente estructura de datos: vamos a usar una lista articulos donde vamos a guardar el nombre del artículo y su precio. De tal forma que las posiciones impares serán los nombres y las pares los precios. Ejemplo:

    articulos=["fregona",12,"cepillo",14,"recogerdor",23]

## Ejercicio 3

Repite el ejercicio 1 con la siguiente estructura de datos: vamos a usar una lista articulos donde vamos a guardar listas con dos elementos: el nombre del artículo y su precio. Ejemplo:

    articulos=[["fregona",12],["cepillo",14],["recogerdor",23]]

## Ejercicio 4

Realizar un programa que guarde en una lista los nombre y edades de los alumnos de una clase. El programa ira pidiendo por teclado el nombre (string) y la edad (int) hasta que se introduzca como nombre un “*”. Las posiciones pares (0,2,4,…) de la lista serán cadenas y las impares son enteros. Cuando terminemos de meter datos hay que mostrar la siguiente información:

* Los nombres de los alumnos con más edad.
* La media de edad de la clase
* Te pide por teclado un nombre y te dice la edad que tiene. Si hay varios alumnos con el mismo nombre te *muestra todos.
* Genera una nueva lista con los nombres y edades de los mayores de edad.

## Ejercicio 5

Repite el ejercicio 4, pero utilizando la siguiente estructura: una lista, en la cual cada elemento es una lista con dos elementos: el nombre y la edad. Por ejemplo:

    [ ["juan",18],["maría",21],["pablo",15] ]


## Ejercicio  6

Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

* Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos. Ejemplo: equipos = [["Sevilla","Betis"],["Madrid","Barcelona"],...]
* Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo. Ejemplo: resultados=[[3,0],[0,0],...]

El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

