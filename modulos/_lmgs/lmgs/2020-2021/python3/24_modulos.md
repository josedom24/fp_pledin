---
permalink: /lmgs/2020-2021/python3/modulos.html
layout: single3
---


# Introducción a los módulos

* Módulo: Cada uno de los ficheros `.py` que nosotros creamos se llama módulo. Los elementos creados en un módulo (funciones, clases, ...) se pueden importar para ser utilizados en otro módulo. El nombre que vamos a utilizar para importar un módulo es el nombre del fichero.

Python tiene sus propios módulos, los cuales forman parte de su librería de módulos estándar, que podemos usar en nuestros programas. Para poder usarlos debemos importarlos.

## Importación de módulos

Podemos importar el módulo completo y posteriormente usar cualquier función definida, por ejemplo para realizar la raíz cuadrada importamos el módulo de funciones matemáticas `math`:

    >>> import math
    >>> math.sqrt(9)
    3.0

Pero si sólo quiero utilizar la función `sqrt` puedo importar sólo esa función (en este caso al utilizarla no hace falta utilizar el nombre del módulo):

    >>> from math import sqrt
    >>> sqrt(9)
    3.0

Veamos algunos módulos que ya hemos utilizado en algunos ejercicios:

## Algunos módulos de python

### Módulos matemáticos

* Módulo math: El módulo [math](https://docs.python.org/3.4/library/math.html) nos proporciones distintas funciones y operaciones matemáticas.

Ejemplo que hemos usado:

    >>> math.sqrt(9)

* Módulo fractions: El módulo [fractions](https://docs.python.org/3.4/library/fractions.html) nos permite trabajar con fracciones.
* Módulo random: El módulo [random](https://docs.python.org/3.4/library/random.html) nos permite generar datos pseudo-aleatorios.

Ejemplo que hemos usado:

    >>> random.randint(1,10)

### Módulos de hora y fecha

* Módulo time: El módulo [time](https://docs.python.org/3.6/library/time.html) nos permite trabajar con fechas y horas. 
El tiempo es medido como un número real que representa los segundos transcurridos desde el 1 de enero de 1970.

Ejemplo que hemos usado:

    >>> time.sleep(1)

* Módulo datetime: El módulo [datetime](https://docs.python.org/3.6/library/datetime.html) amplía las posibilidades del módulo time que provee funciones para manipular expresiones de tiempo.

### Módulo del sistema

* Módulo os: El módulo [os](https://docs.python.org/3.4/library/os.html#module-os) nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios.

Ejemplo:

    >>> os.system("clear")
