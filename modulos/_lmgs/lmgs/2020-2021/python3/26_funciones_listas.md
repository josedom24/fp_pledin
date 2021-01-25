---
permalink: /lmgs/2020-2021/python3/funciones_listas.html
layout: single3
---

# Funciones que reciben listas o diccionarios

Tantos las listas como los diccionarios son tipos de datos mutables, por lo tanto cuando la pasamos como parámetros a una función al cambiar el parámetro formal podemos estar cambiando el parámetro real.

Por tanto al trabajar con listas o diccionarios como parámetro de funciones, podemos hacer dos versiones de estas funciones:

1. Una función que modifica la lista o el diccionario. Estas funciones no tienen `return`, por lo que no devuelve nada (`None`).
2. Una función que no modifica la lista o diccionario original, y que devuelven una nueva lista o diccionario modificado. Estas funciones si tienen que tener `return` para devolver la lista o diccionario modificado.

## Ejemplo 1: Función que recibe una lista y la modifica

Vamos a hacer una función que elimine todas las apariciones de una lista, modificando la lista original:

    def eliminar_elemento_lista(lista,elem):
        while elem in lista:
            lista.remove(elem)

En el programa principal creamos una lista, y vemos que cuando usamos la función la lista se modifica:

    milista = [2,4,5,2,3]
    eliminar_elemento_lista(milista,2)
    print(milista)

El resultado de este programa será:

    [4,5,3]

La lista `milista` se ha modificado.

## Ejemplo 2: Función que recibe una lista y devuelve otra lista modificada

Vamos a hacer una función que elimine todas las apariciones de una lista, pero no modifica la lista original, devuelve otra lista con los elementos eliminados:

    def eliminar_elemento_lista(lista,elem):
        aux=lista.copy()
        while elem in aux:
            aux.remove(elem)
        return aux

En el programa principal creamos una lista, y vemos que cuando usamos la función la lista original no se modifica, y necesitamos otra variable para guardar la lista modificada.

    milista = [2,4,5,2,3]
    otralista=eliminar_elemento_lista(milista,2)
    print(otralista)
    print(milista)

El resultado de este programa será:

    [4,5,3]
    [2,4,5,2,3]

La lista `milista` no se ha modificado, en la lista `otralista` tenemos el resultado de eliminar el elemento en la lista orginal.

