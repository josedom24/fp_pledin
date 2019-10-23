---
title: "Entrega: Ejercicios pseudocódigo"
permalink: /lmgs/u01/entrega.html
---

## Ejercicio 1

Calcular el perímetro y área de un pentágono. Para ello debes pedir por teclado la longitud del lado y del apotema. Debes validar la entrada para asegurarnos de que las medidas son números positivos.

## Ejercicio 2

Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.

## Ejercicio 3

Escribir un programa que le pregunte al usuario una cantidad de euros, una tasa de interés y un número de años y muestre como resultado la cantidad final a pagar. La fórmula a utilizar es:

	Cn = C * (1 + x/100) ^ n

Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

## Ejercicio 4

Realiza un programa que pida una nota numéricas enteras e imprima sus equivalentes en texto (0-2 => MD, 3-4 => I, 5 => Suf, 6 => B, 7-8 => Not, 9-10 => Sob, otro => Error)

## Ejercicio 5

Escribe un programa que lea una lista de diez números y determine cuántos son positivos, y cuántos son negativos.

## Ejercicio 6

Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.

	DIVISOR DE NÚMEROS
	Escriba el dividendo: 14
	Escriba el divisor: 5
	La división no es exacta. Cociente: 2 Resto: 4	

	DIVISOR DE NÚMEROS
	Escriba el dividendo: 20
	Escriba el divisor: 4
	La división es exacta. Cociente: 5

## Ejercicio 7

Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2020
	Para llegar al año 2020 faltan 5 años.
    
    COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 1997
	Desde el año 1997 han pasado 18 años.
    
    COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2015
	¡Son el mismo año!
    
## Ejercicio 8

Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

	COMPARADOR DE TRES NÚMEROS
	Escriba un número: 6
	Escriba otro número: 6
	Escriba otro número más: 6
	Ha escrito tres veces el mismo número.

    COMPARADOR DE TRES NÚMEROS
	Escriba un número: 6
	Escriba otro número: 6.5
	Escriba otro número más: 6
	Ha escrito uno de los números dos veces.
    
    COMPARADOR DE TRES NÚMEROS
	Escriba un número: 4
	Escriba otro número: 5
	Escriba otro número más: 6
	Los tres números que ha escrito son distintos.

## Ejercicio 9

Escriba un programa que pida un número entero mayor que cero (debes validarlo) y que escriba sus divisores.

Notas:

* Un número es divisible por otro cuando el resto de su división es cero (``numero % divisor = 0``).
* Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores (o iguales) que la mitad del número. Es decir, no hace falta probar todos los números entre 1 y el propio número, sino únicamente hasta la mitad. Si se hace así, no hay que olvidarse de añadir el propio número a la lista de divisores.

Ejemplo:

	DIVISORES
	Escriba un número mayor que cero: -5
	¡Le he pedido un número entero mayor que cero!

	DIVISORES
	Escriba un número entero mayor que cero: 200
	Los divisores de 200 son 1 2 4 5 8 10 20 25 40 50 100 200

# Ejercicio 10

Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? -1
	¡Imposible!

	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? 4
	Escriba un número: 6
	Escriba un número más grande que 6: 10
	Escriba un número más grande que 6: 3
	¡3 no es mayor que 6!
	Escriba un número más grande que 6: 9
	Gracias por su colaboración

