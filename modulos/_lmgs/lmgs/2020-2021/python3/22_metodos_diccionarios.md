---
permalink: /lmgs/2020-2021/python3/metodos_diccionarios.html
layout: single3
---

# Métodos principales de diccionarios

## Métodos de eliminación

`clear()`: Elimina los elementos de un diccionario.

	>>> dict1 = {'one': 1, 'two': 2, 'three': 3}
	>>> dict1.clear()
	>>> dict1
	{}

## Métodos de agregado y creación

`copy()`: Como hemos explicado anteriormente nos permite copiar diccionarios.

	>>> dict1 = {'one': 1, 'two': 2, 'three': 3}
	>>> dict2 = dict1.copy()

`update()`: Nos permite añadir elementos a un diccionario a partir de los elementos de otro diccionario.

	>>> dict1 = {'one': 1, 'two': 2, 'three': 3}
	>>> dict2 = {'four':4,'five':5}
	>>> dict1.update(dict2)
	>>> dict1
	{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

## Métodos de retorno

`get()`: Nos devuelve el valor de un elemento de un diccionario indicando la clave. Además podemos indicar el valor devuelto si no existe el elemento.

	>>> dict1 = {'one': 1, 'two': 2, 'three': 3}
	>>> dict1.get("one")
	1
	>>> dict1.get("four")
	>>> dict1.get("four","no existe")
	'no existe'

`pop()`: Nos devuelve el valor de un elemento de un diccionario a partir de la cale y elimina dicho elemento. También podemos indicar el valor devuelto si no existe el elemento buscado.

	>>> dict1.pop("one")
	1
	>>> dict1
	{'two': 2, 'three': 3}
	>>> dict1.pop("four")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'four'
	>>> dict1.pop("four","no existe")
	'no existe'

## Recorrido de diccionarios

El método `keys()` nos devuelve las claves de un diccionario, por lo tanto podemos recorrer las claves de la siguiente manera:

	>>> for clave in dict1.keys():
	...    print(clave)
	one
	two
	three

El método `values()` nos devuelve los valores de un diccionario, por lo tanto podemos recorrer los valores de la siguiente manera:

	>>> for valor in dict1.values():
	...    print(valor) 
	1
	2
	3

Finalmente el método `items()` nos devuelve la clave y el valor correspondiente de los elemento de un diccionario, por lo tanto podemos recorrer ambos:

	>>> for clave,valor in dict1.items():
	...   print(clave,"->",valor)
	one -> 1
	two -> 2
	three -> 3
