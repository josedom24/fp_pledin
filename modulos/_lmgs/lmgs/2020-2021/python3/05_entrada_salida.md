---
permalink: /lmgs/2020-2021/python3/entrada_salida.html
layout: single3
---

# Entrada y salida estándar

## Función input

Nos permite leer por teclado información. Devuelve una cadena de caracteres y puede tener como argumento una cadena que se muestra en pantalla.

*Ejemplos*

	>>> nombre=input("Nombre:")
	Nombre:jose
	>>> nombre
	'jose'
	>>> edad=int(input("Edad:"))
	Edad:23
	>>> edad
	23
	
## Función print

Nos permite escribir en la salida estándar. Podemos indicar varios datos a imprimir, que por defecto serán separado por un espacio. Podemos también imprimir varias cadenas de texto utilizando la concatenación.

*Ejemplos*

	>>> print(1,2,3)
	1 2 3
	
	>>> print("Hola son las",6,"de la tarde")
	Hola son las 6 de la tarde
	
    >>> print("Hola son las "+str(6)+" de la tarde")
	Hola son las 6 de la tarde

## Formateando cadenas de caracteres
	
Con la función `print` Podemos indicar el formato con el que se va a mostrar los datos, por ejemplo:

	>>> print("%d %f %s" % (2.5,2.5,2.5))
	2 2.500000 2.5
	
	>>> print("El producto %s cantidad=%d precio=%.2f"%("cesta",23,13.456))
	El producto cesta cantidad=23 precio=13.46	




