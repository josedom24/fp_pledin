---
permalink: /lmgs/2020-2021/python3/metodos_listas.html
layout: single3
---

# Métodos principales de listas

## Métodos de inserción: append, extend, insert

`append()`: añade un elemento a la lista:

	>>> lista = [1,2,3]
	>>> lista.append(4)
	>>> lista
	[1, 2, 3, 4]

`extend()`: Une dos listas:

	>>> lista2 = [5,6]
	>>> lista.extend(lista2)
	>>> lista
	[1, 2, 3, 4, 5, 6]	

`insert()`: Añade un elemento en un posición indicada de la lista:

	>>> lista.insert(1,100)
	>>> lista
	[1, 100, 2, 3, 4, 5, 6]

## Métodos de eliminación: pop, remove

`pop()`: elimina un elemento de la lista y lo devuelve. Se puede indicar el índice del elemento que queremos obtener como parámetro, sino se indica se devuelve y elimina el último:

	>>> lista.pop()
	6
	>>> lista
	[1, 100, 2, 3, 4, 5]

	>>> lista.pop(1)
	100
	>>> lista
	[1, 2, 3, 4, 5]

`remove()`: Elimina el elemento de la lista indicado por la posición:

	>>> lista.remove(3)
	>>> lista
	[1, 2, 4, 5]

## Métodos de ordenación: reverse, sort, 

`reverse()`: Modifica la lista invirtiendo los elementos:

	>>> lista.reverse()
	>>> lista
	[5, 4, 2, 1]

`sort()`: Modifica la lista ordenando los elementos, se puede indicar el sentido de la ordenación:

	>>> lista.sort()
	>>> lista
	[1, 2, 4, 5]

	>>> lista.sort(reverse=True)
	>>> lista
	[5, 4, 2, 1]

	>>> lista=["hola","que","tal","Hola","Que","Tal"]
	>>> lista.sort()
	>>> lista
	['Hola', 'Que', 'Tal', 'hola', 'que', 'tal']


## Métodos de búsqueda: count, index

`count()`: devuelve el número de apariciones de un elemento en la lista:

	>>> lista.count(5)
	1

`index()`: Nos devuelve la posición de la primera aparición del elemento indicado. Se puede indicar la posición inicial y final de búsqueda:

	>>> lista.append(5)
	>>> lista
	[5, 4, 2, 1, 5]
	>>> lista.index(5)
	0
	>>> lista.index(5,1)
	4
	>>> lista.index(5,1,4)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: 5 is not in list

Si no encuentra el elemento nos da una **excepción**.

