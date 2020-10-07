---
permalink: /lmgs/2020-2021/python3/variables.html
layout: single3
---

# Trabajando con variables

Una variables es un identificador que referencia a un valor. No hay que declarar la variable antes de usarla, el tipo de la variable será el mismo que el del valor al que hace referencia. Por lo tanto su tipo puede cambiar en cualquier momento:

	>>> var = 5
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>

## Creación, borrado y ámbito de variables

Como hemos comentado anteriormente para crear una variable simplemente tenemos que utilizar un operador de asignación, el más utilizado `=` para que referencia un valor. Si queremos borrar la variable utilizamos la instrucción `del`. Por ejemplo:

	>>> a = 5
	>>> a
	5
	>>> del a
	>>> a
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined

El ámbito de una variable se refiere a la zona del programa donde se ha definido y existe esa variable. Como primera aproximación las variables creadas dentro de funciones o clases tienen un ámbito local, es decir no existen fuera de la función o clase. Concretaremos cuando estudiamos estos aspectos más profundamente.

## Modificación del valor de una variable

En cualquier momento podemos cambiar el valor de una variable, asignándole un nuevo valor:

	>>> a = 5
	>>> a
	5
    >>> a = 8
    >>> a
    8

También podemos modificar el valor de una variable, por ejemplo si queremos incrementarla en uno, podríamos usar:

    >>> a = a + 1

Aunque también podemos utilizar otro operador de asignación:

    >>> a+=1

Otros operadores de asignación: `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`.


