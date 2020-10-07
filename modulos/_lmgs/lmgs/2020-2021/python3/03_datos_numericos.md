---
permalink: /lmgs/2020-2021/python3/datos_numericos.html
layout: single3
---

# Datos numéricos

<iframe width="560" height="315" src="https://www.youtube.com/embed/8ygasB-FXbM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Python3 trabaja con varios tipos numéricos, pero en este curso sólo vamos a utilizar dos:

* Enteros (int): Representan todos los números enteros (positivos, negativos y 0), sin parte decimal. 
* Reales (float): Sirve para representar los números reales, tienen una parte decimal y otra  decimal.

*Ejemplos*

	>>> entero = 7
	>>> type(entero)
	<class 'int'>
	>>> real = 7.2
	>>> type (real)
	<class 'float'>


## Operadores aritméticos

* `+`: Suma dos números
* `-`: Resta dos números
* `*`: Multiplica dos números
* `/`: Divide dos números, el resultado es `float`.
* `//`: División entera
* `%`: Módulo o resto de la división
* `**`: Potencia
* `+`, `-`: Operadores unarios positivo y negativo

## Funciones predefinidas que trabajan con números:

* `abs(x)`: Devuelve al valor absoluto de un número.
* `divmod(x,y)`: Toma como parámetro dos números, y devuelve una tupla con dos valores, la división entera, y el módulo o resto de la división.
* `hex(x)`: Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro.
* `bin(x)`: Devuelve una cadena con la representación binaria del número que recibe como parámetro.
* `pow(x,y): Devuelve la potencia de la base x elevado al exponente y. Es similar al operador `**`.
* `round(x,[y])`: Devuelve un número real (float) que es el redondeo del número recibido como parámetro, podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.

*Ejemplos*

	>>> abs(-7)
	7
	>>> divmod(7,2)
	(3, 1)
	>>> hex(255)
	'0xff'
	>>> pow(2,3)
	8
	>>> round(7.567,1)
	7.6

## Conversión de tipos

* `int(x)`: Convierte el valor a entero.
* `float(x)`: Convierte el valor a float.

Los valores que se reciben también pueden ser cadenas de caracteres (str).

*Ejemplos*

	>>> a=int(7.2)
	>>> a
	7
	>>> type(a)
	<class 'int'>
	>>> a=int("345")
	>>> a
	345
	>>> type(a)
	<class 'int'>
	>>> b=float(1)
	>>> b
	1.0
	>>> type(b)
	<class 'float'>
	>>> b=float("1.234")
	>>> b
	1.234
	>>> type(b)
	<class 'float'>

Por último si queremos convertir una cadena a entero, la cadena debe estar formada por caracteres numéricos, sino es así, obtenemos un error:

	a=int("123.3")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '123.3'

# Otras operaciones

Quizás eches en falta más operaciones que podemos realizar sobre los números. En el módulo `math` encontramos muchas de estas operaciones. Para utilizarlas vamos  a importar el módulo, por ejemplo para realizar una raíz cuadrada:

	>>> import math
	>>> math.sqrt(9)
	3.0



