---
permalink: /lmgs/2020-2021/python3/cadenas_caracteres.html
layout: single3
---

# Tipo de datos cadenas de caracteres

Como vimos en una unidad anterior, las cadenas de caracteres (`str`): Me permiten guardar secuencias de caracteres.

Además de las operaciones que ya hemos estudiado:

* Concatenación: `+`:  El operador `+` me permite unir datos de tipos secuenciales, en este caso dos cadenas de caracteres.
* Repetición: `*`:  El operador `*` me permite repetir un dato de un tipo secuencial, en este caso de cadenas de caracteres.
* Indexación: Puedo obtener el dato de una secuencia indicando la posición en la secuencia. En este caso puedo obtener el carácter de la cadena indicando la posición (**empezando por la posición 0**).
* Para obtener la longitud de una cadena (número de caracteres que tiene), utilizamos la función `len`.

Tenemos más operaciones que podemos realizar:

## Otras operaciones con cadenas de caracteres

* Las cadenas de caracteres se pueden recorrer:

        >>> cadena = "informática"
        >>> for caracter in cadena:
        ...    print(caracter,end="")
        ...
        informática

* Operadores de pertenencia: Se puede comprobar si un elemento (subcadena) pertenece o no a una cadena de caracteres con los operadores `in` y `not in`.

        >>> "a" in cadena
        True
        >>> "b" in cadena
        False
        >>> "a" not in cadena
        False

* Slice (rebanada): Puedo obtener una subcadena de la cadena de caracteres. Se indica el carácter inicial, y el carácter final, además podemos indicar opcionalmente un salto. Si no se indica el carácter inicial se supone que es desde el primero, sino se indica el carácter final se supone que es hasta el final. Por último podemos usar salto negativo para empezar a contar desde el final.

Como resumen de las distintas posibilidades podemos indicar:

* `cadena[start:end]` 	  # Elementos desde la posición start hasta end-1
* `cadena[start:]`    	  # Elementos desde la posición start hasta el final
* `cadena[:end]`      	  # Elementos desde el principio hasta la posición end-1
* `cadena[:]` 	 	  # Todos Los elementos	    
* `cadena[start:end:step]` # Igual que el anterior pero dando step saltos.

Veamos algunos ejemplos:

        >>> cadena[2:5]
        'for'
        >>> cadena[2:7:2]
        'frá'
        >>> cadena[:5]
        'infor'
        >>> cadena[5:]
        'mática'
        >>> cadena[-1:-3]
        ''
        >>> cadena[::-1]
        'acitámrofni'

## Conversión de tipos

Podemos convertir cualquier número en una cadena de caracteres utilizando la función `str`:

        >>> cad = str(7.8)
        >>> type(cad)
        <class 'str'>
        >>> print(cad)
        7.8