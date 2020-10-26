---
permalink: /lmgs/2020-2021/python3/estructura_for.html
layout: single3
---

# Estructuras de control repetitivas: for

La estructura `for` nos permite recorrer los elementos de una secuencia (lista, tupla, cadena de caracteres,...). sin embargo en esta unidad vamos a a prender a usar `for` de forma similar a la instrucción `Para` de pseudocódigo, es decir, ejecutar una secuencia de instrucciones un número determinado de veces, desde un valor inicial, hasta un valor final y con un posible incremento. Para ello vamos a usar el tipo de datos `range` que nos permite generar listas de números. Vamos a usar `for` para crear bucles de instrucciones donde sabemos a priori el número de iteraciones que hay que realizar.

## Ejemplos

### Ejemplo 1

Escribir en pantalla del 1 al 10.

    for var in range(1,11):
        print(var," ",end="")

### Ejemplo 2

Escribir en pantalla de 10 al 1.

    for var in range(10,0,-1):
        print(var," ",end="")

### Ejemplo 3

Escribir los número pares desde el 2 al 10.

    for var in range(2,11,2):
        print(var," ",end="")