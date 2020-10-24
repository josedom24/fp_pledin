---
permalink: /lmgs/2020-2021/python3/tipo_booleano.html
layout: single3
---

# Tipo de datos booleano y expresiones lógicas

<iframe width="560" height="315" src="https://www.youtube.com/embed/nZ5I81gSxGk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Tipo booleano

El tipo booleano o lógico se considera en python3 como un subtipo del tipo entero. Se puede representar dos valores: verdadero o false (True, False).

## ¿Qué valores se interpretan como FALSO?

Cuando se evalúa una expresión, hay determinados valores que se interpretan como False:

* `False`
* Cualquier número 0. (0, 0.0)
* Cualquier secuencia vacía ([], (), '')
* Cualquier diccionario vacío ({})

## Operadores de comparación

Las expresiones lógicas utilizan operadores de comparación, me permiten comparar dos valores y devuelven un valor booleano, dependiendo de lo que este comparando.

* `==`: Igual que
* `!=`: Distinto que
* `>`: Mayor que
* `<`: Menor que
* `<=`: Menor o igual
* `>=`: Mayor o igual


## Operadores booleanos o lógicos

Los operadores booleanos se utilizan para operar sobre expresiones booleanas y se suelen utilizar en las estructuras de control alternativas (if, while):

* `x or y`: Si x es falso entonces y, sino x. Este operados sólo evalúa el segundo argumento si el primero es False.
* `x and y`: Si x es falso entonces x, sino y. Este operados sólo evalúa el segundo argumento si el primero es True.
* `not x`: Si x es falso entonces True, sino False.

