---
title: "Ejercicio: Provincias y poblaciones"
permalink: /lmgs/u04/ejercicio_python_1.html
---

Utilizando el fichero [provinciasypoblaciones.xml](xml/provinciasypoblaciones.xml.zip), crea distintas funciones en python, utilizando la libreria lxml, que realicen las siguientes tareas:

1. Función que devuelve una lista con los nombres de las provincias.
2. Función que devuelve una lista con todos las poblaciones.
3. Función que devuelve las provincias y el total de poblaciones que tiene cada uno. Piensa la estructura de datos que va a devolver la función.
4. Función que recibe el nombre de una provincia y devuelve la lista de poblaciones.
5. Función que recibe el nombre de una población y te devuelve la provincia donde se encuentra.
6. Función que recibe una lista distintos identificadores de provincias, y te devuelve las provincias que corresponden a cada identificador, y sus poblaciones.
7. Función que reciba el nombre de una provincia devuelva las "ciudades grandes" (atributo c="1").
8. Función que reciba una localidad y te devuelva si es "ciudad grande" (atributo c="1") o no de provincia. Si es "ciudad grande" de provincia te devuelve el nombre de la provincia.


Crea en otro fichero el programa principal que te muestre el siguiente menú:

1. Mostrar todas las provincias: Muestra por pantalla el nombre de todas las provincias.
2. Mostrar todas las poblaciones: Muestra por pantalla el nombre de todas las poblaciones.
3. Mostrar provincias y número de poblaciones: Muestra por pantalla el nombre de todas las provincias y la cantidad de poblaciones.
4. Mostrar las poblaciones: Lee una provincia por teclado y te muestra el nombre de las poblaciones. Si la provincia no existe te da un error.
5. Mostrar la provincia: Lee una población por teclado y te muestra el nombre de la provincia. Si la población no existe te da un error.
6. Información por identificador: Pide un conjunto de identificadores de provincias, y te muestra por pantalla las provincias correspondientes y sus poblaciones.
7. Ciudades grandes: Lee una provincia por teclado y te muestra las poblaciones grandes ("ciudades grandes"). Si la provincia no existe te da un error.
8. Es ciudad grande: Lee una población y si es ciudad grande te muestra el nombre de la provincia, sino te dice que no es una ciudad grande.

* [Solución](ejercicio1_xpath.py)