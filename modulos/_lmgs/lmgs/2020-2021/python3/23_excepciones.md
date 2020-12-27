---
permalink: /lmgs/2020-2021/python3/excepciones.html
layout: single3
---

# Excepciones

## Errores sintácticos y errores de ejecución

Los errores sintácticos se producen cuando tenemos algo mal escrito en nuestro código fuente. Veamos un ejemplo de error sintáctico:

	>>> while True print('Hello world')
	  File "<stdin>", line 1
	    while True print('Hello world')
	                   ^
	SyntaxError: invalid syntax

Una excepción o un error de ejecución se produce durante la ejecución del programa. Las excepciones se puede manejar para que no termine el programa. Veamos algunos ejemplos de excepciones:

	>>> 4/0
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero	

	>>> a+4
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'a' is not defined	

	>>> "2"+2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: Can't convert 'int' object to str implicitly

Hemos obtenido varias excepciones: ˋZeroDivisionErrorˋ, ˋNameErrorˋ y ˋTypeErrorˋ. Puedes ver la [lista de excepciones](https://docs.python.org/3.4/library/exceptions.html#bltin-exceptions) y su significado.

## Manejando excepciones

Veamos un ejemplo simple como podemos tratar una excepción:

	>>> while True:
	...   try:
	...     x = int(input("Introduce un número:"))
	...     break
	...   except ValueError:
	...     print ("Debes introducir un número")

1. Se ejecuta el bloque de instrucciones de `try`.
2. Si no se produce la excepción, el bloque de `except` no se ejecuta y continúa la ejecución secuencia.
3. Si se produce una excepción, el resto del bloque `try` no se ejecuta, si la excepción que se ha produce corresponde con la indicada en `except` se salta a ejecutar el bloque de instrucciones `except`.
4. Si la excepción producida no se corresponde con las indicadas en `except` se pasa a otra instrucción `try`, si finalmente no hay un manejador nos dará un error y el programa terminará.

Un bloque `except` puede manejar varios tipos de excepciones, si quiero controlar varios tipos de excepciones puedo poner varios bloques `except`. Teniendo en cuenta que en el último, si quiero no indico el tipo de excepción:

	>>> try:
	...   print (10/int(cad))
	... except ValueError:
	...   print("No se puede convertir a entero")
	... except ZeroDivisionError:
	...   print("No se puede dividir por cero")
	... except:
	...   print("Otro error")

Se puede utilizar también la clausula `else`:

	>>> try:
	...   print (10/int(cad))
	... except ValueError:
	...   print("No se puede convertir a entero")
	... except ZeroDivisionError:
	...   print("No se puede dividir por cero")
	... else:
	...   print("Otro error")

Por último indicar que podemos indicar una clausula `finally` para indicar un bloque de instrucciones que siempre se debe ejecutar, independientemente de la excepción se haya producido o no.

	>>> try:
	...     result = x / y
	... except ZeroDivisionError:
	...     print("División por cero!")
	... else:
	...     print("El resultado es", result)
	... finally:
	...     print("Terminamos el programa")

