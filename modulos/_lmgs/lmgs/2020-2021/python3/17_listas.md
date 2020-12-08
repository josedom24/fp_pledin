---
permalink: /lmgs/2020-2021/python3/listas.html
layout: single3
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/cUIjTbk0wgg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Tipo de datos secuencia: listas

En Python tenemos varios tipos de datos que nos permiten guardar conjuntos de informaciones. En esta unidad vamos a estudiar las **Listas**. Las listas (`list`) me permiten guardar un conjunto de datos que se pueden repetir y que pueden ser de distintos tipos. Además esta estructura es dinámica, en cualquier momento de la ejecución del programa puedo añadir o eliminar elementos de la lista.

## Construcción de una lista 

Para crear una lista puedo usamos los caracteres `[` y `]`:

	>>> lista1 = []
	>>> lista2 = ["a",1,True]

## Operaciones básicas con listas

Las listas son secuencias, a las que podemos realizar las siguientes operaciones. Vamos a ver distintos ejemplos partiendo de la siguiente lista:

	lista = [1,2,3,4,5,6]

* Las listas se pueden recorrer:
	
		>>> for num in lista:
		...   print(num,end="")
		123456

	Con la instrucción `for` podemos recorrer más de una listas, utilizando la función `zip`. Veamos un ejemplo:

		>>> lista2 = ["a","b","c","d","e"]
		>>> for num,letra in zip(lista,lista2):
		...     print(num,letra)
		...
		1 a
		2 b
		3 c
		4 d
		5 e
		
* Operadores de pertenencia: Se puede comprobar si un elemento pertenece o no a una lista con los operadores `in` y `not in`.

		>>> 2 in lista
		True
		>>> 8 not in lista
		True

* Concatenación: El operador `+` me permite unir datos de tipos listas:

		>>> lista + [7,8,9]
		[1, 2, 3, 4, 5, 6, 7, 8, 9]

* Repetición: El operador `*` me permite repetir un dato de una lista:

		>>> lista * 2
		[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

* Indexación: Puedo obtener el dato de una secuencia indicando la posición en la secuencia.

		>>> lista[3]
		4

    Cada elemento tiene un índice, empezamos a contar por el elemento en el índice 0. Si intento acceder a un índice que corresponda a un elemento que no existe obtenemos una excepción `IndexError`.

		>>> lista1[12]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module
		IndexError: list index out of range	

	Se pueden utilizar índices negativos:

		>>> lista[-1]
		6
	
* Slice (rebanada): Puedo obtener una subsecuencia de los datos de una lista. Funciona de forma similar como en las cadenas, veamos algunos ejemplos:

		>>> lista[2:4]
        [3, 4]
        >>> lista[1:4:2]
        [2, 4]
        >>> lista[:5]
        [1, 2, 3, 4, 5]
        >>> lista[5:]
        [6, 1, 2, 3, 4, 5, 6]
        >>> lista[::-1]
        [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]


## Funciones predefinidas que trabajan con listas

	>>> lista1 = [20,40,10,40,50]
	>>> len(lista1)
	5
	>>> max(lista1)
	50
	>>> min(lista1)
	10
	>>> sum(lista1)
	150
	>>> sorted(lista1)
	[10, 20, 30, 40, 50]
	>>> sorted(lista1,reverse=True)
	[50, 40, 30, 20, 10]

## Listas multidimensionales

A la hora de definir las listas hemos indicado que podemos guardar en ellas datos de cualquier tipo, y evidentemente podemos guardar listas dentro de listas. 

	>>> tabla = [[1,2,3],[4,5,6],[7,8,9]]
	>>> tabla[1][1]
	5

	>>> for fila in tabla:
	...   for elem in fila:
	...      print(elem,end="")
	...   print()
	 
	123
	456
	789
