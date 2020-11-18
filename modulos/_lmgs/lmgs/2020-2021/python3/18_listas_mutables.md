---
permalink: /lmgs/2020-2021/python3/listas_mutables.html
layout: single3
---

# Las listas son mutables

Al igual que las cadenas el tipo de datos lista es una **clase**, cada vez que creamos una variable de la clase lista estamos creando un **objeto** que además de guardar un conjunto de datos, posee un conjunto de **métodos** que nos permiten trabajar con la lista.

## ¿Qué significa que las listas son mutables?

Los elementos de las listas se pueden modificar:

	>>> lista1 = [1,2,3]
	>>> lista1[2]=4
	>>> lista1
	[1, 2, 4]
	>>> del lista1[2]
	>>> lista1
	[1, 2]

Esto también ocurre cuando usamos los métodos, es decir, los métodos de las listas modifican el contenido de la lista, por ejemplo si usamos el método `append()` para añadir un elemento a la lista:

    >>> lista1.append(3)
    >>> lista1
	[1, 2, 3]

Como vemos la lista `lista1` se ha modificado.

### ¿Cómo se copian las listas?

Para copiar una lista en otra no podemos utilizar el operador de asignación:

	>>> lista1 = [1,2,3]
	>>> lista2 = lista1
	>>> lista1[1] = 10
	>>> lista2
	[1, 10, 3]

El operador de asignación no crea una nueva lista, sino que nombra con dos nombres distintos a la misma lista, por lo tanto la forma más fácil de copiar una lista en otra es:

	>>> lista1 = [1,2,3]
	>>> lista2=lista1[:]
	>>> lista1[1] = 10
	>>> lista2
	[1, 2, 3]

