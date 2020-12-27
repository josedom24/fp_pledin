---
permalink: /lmgs/2020-2021/python3/funciones_recursivas.html
layout: single3
---

# Funciones recursivas

En la unidad anterior hemos visto como crear una función para calcular el factorial de un número:

Veamos un ejemplo de definición de función:

	>>> def factorial(n):
	...   """Calcula el factorial de un número"""
	...   resultado = 1
	...   for i in range(1,n+1):
	...     resultado*=i
	...   return resultado

El factorial de un número también puede ser calculado de forma recursiva: el factorial del 0 o del 1 es 1, y el factorial de un número es igual al número multiplicado por el factorial del número menos 1.

Una función recursiva es aquella que al ejecutarse hace llamadas a ella misma. Por lo tanto tenemos que tener "un caso base" que hace terminar el bucle de llamadas. Veamos un ejemplo:

    def factorial(num):
        if num==0 or num==1:
            return 1
        else:
            return num * factorial(num-1)

Y para utilizar la función:

	>>> factorial(5)
	120


## Otro ejemplo: Mostrar los elementos de una lista

Podemos tener una función que reciba una lista y muestre sus elementos:

    def mostrar_lista(lista):
        for elem in lista:
            print(elem)

La versión recursiva de esta función sería:

    def mostrar_lista(lista):
        if len(lista)!=0:
            print(lista[0])
            mostrar_lista(lista[1:])
    