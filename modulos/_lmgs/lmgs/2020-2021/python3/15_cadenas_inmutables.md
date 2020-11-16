---
permalink: /lmgs/2020-2021/python3/cadenas_inmutables.html
layout: single3
---

# Las cadenas de caracteres son inmutables

Cuando creamos una variable de tipo cadena de caracteres, estamos creando un **objeto** de la **clase** `str`. Una clase especifica lo que podemos guardar en un tipo de datos y las operaciones que pueden realizar, cada vez que creamos una variable de una determinada clase, creamos un objeto, que además de guardar información (en nuestro caso los caracteres de la cadena) puede realizar distintas operaciones que llamamos **métodos**.

Nosotros ya hemos usado un método de la clase `str`. El método `upper()` nos permite convertir la cadena a mayúsculas.

## ¿Qué significa que las cadenas de caracteres son inmutables?

No podemos cambiar los caracteres de una cadena de la siguiente forma:

	>>> cadena = "informática"
	>>> cadena[2]="g"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

Esto implica que al usar un método la cadena original no cambia, el método devuelve otra cadena modificada. Veamos un ejemplo:

    >>> cadena = "informática"
    >>> cadena.upper()
    'INFORMÁTICA'
    >>> cadena
    'informática'

Si queremos cambiar la cadena debemos modificar su valor con el operador de asignación:

    >>> cadena = cadena.upper()
    >>> cadena
    'INFORMÁTICA'

