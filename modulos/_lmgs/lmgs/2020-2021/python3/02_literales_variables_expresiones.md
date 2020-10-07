---
permalink: /lmgs/2020-2021/python3/literales_variables_expresiones.html
layout: single3
---

# Literales, variables y expresiones

<iframe width="560" height="315" src="https://www.youtube.com/embed/CNtCxItLpao" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Literales

Los literales nos permiten representar valores. Estos valores pueden ser de diferentes tipos, de esta manera tenemos diferentes tipos de literales:

**Literales numéricos**

* Para representar números enteros utilizamos cifras enteras (Ejemplos: 3, 12, -23).
* Para los números reales utilizamos un punto para separar la parte entera de la decimal (12.3, 45.6). Podemos indicar que la parte decimal es 0, por ejemplo 10., o la parte entera es 0, por ejemplo .001.

**Literales cadenas**

Nos permiten representar cadenas de caracteres. Para delimitar las cadenas podemos usar el carácter ' o el carácter ". También podemos utilizar la combinación ''' cuando la cadena ocupa más de una línea. Ejemplos.

	'hola que tal!'
	"Muy bien"
	'''Podemos \n
	ir al cine'''

El carácter `\n` es el retorno de carro (los siguientes caracteres se escriben en una nueva línea).

## Variables

Una variables es un identificador que referencia a un valor. Para que una variable referencia a un valor se utiliza el operador de asignación `=`.

El nombre de una variable, ha de empezar por una letra o por el carácter guión bajo, seguido de letras, números o guiones bajos. 
	
    >>> var = 5
	>>> var
    5

Hay que tener en cuanta que python distingue entre mayúsculas y minúsculas en el nombre de una variable, pero se recomienda usar sólo minúsculas.

## Expresiones

Una expresión es una combinación de variables, literales, operadores, funciones y expresiones, que tras su evaluación o cálculo nos devuelven un valor de un determinado tipo. 

Veamos ejemplos de expresiones:

	a + 7
	(a ** 2) + b
