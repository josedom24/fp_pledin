---
permalink: /python/python3.html
layout: single3
---

# Más programas con estructura secuencial

En esta práctica vamos a seguir haciendo programas python utilizando la estructura secuencial.

## Más funciones matemáticas

Por ejemplo, con la función `round` podemos redondear un número real. `round(x,[y])` devuelve un número real (float) que es el redondeo del número recibido como parámetro, podemos indicar un parámetro opcional que indica el número de decimales en el redondeo. Ejemplo:

```python
>>> num = 7 / 3
>>> print(num)
2.3333333333333335
>>> print(round(num,2))
2.33

Quizás eches en falta más operaciones que podemos realizar sobre los números. En el módulo math encontramos muchas de estas operaciones. Para utilizarlas vamos a importar el módulo, por ejemplo para realizar una raíz cuadrada:

```python
>>> import math
>>> math.sqrt(9)
3.0
```

Otra operación matemática es la generación de números aleatorios (al azar). Para ello usamos el módulo `random`, podemos usar varias funciones:

* `random.random()`: Genera un número decimal aleatorio entre 0 y 1.
* `random.randint(a,b)`: Genera un número entero aleatorio entre a y b.
* `random.uniform(a,b)`: Genera un número decimal aleatorio entre a y b.

Por ejemplo:

```python
>>> import random
>>> random.random()
0.19295156144040204
>>> random.randint(1,10)
6
>>> random.uniform(1,10)
3.555140411923311
```

## Más operaciones sobre cadenas de caracteres

* **Indexación**: Puedo obtener el dato de una secuencia indicando la posición en la secuencia. En este caso puedo obtener el carácter de la cadena indicando la posición (**empezando por la posición 0**).

```python
>>> cadena = "josé"
>>> cadena[0]
'j'
>>> cadena[3]
'é'
```

* Para obtener la **longitud de una cadena** (número de caracteres que tiene), utilizamos la función `len`:

```python
 >>> cadena = "josé"
>>> print(len(cadena))
4
```

* **Slice (rebanada)**: Puedo obtener una subcadena de la cadena de caracteres. Se indica el carácter inicial, y el carácter final. Si no se indica el carácter inicial se supone que es desde el primero, sino se indica el carácter final se supone que es hasta el final. 

```python
>>> cad="informática"
>>> print(cad[:4])
info
>>> print(cad[2:7])
formá
>>> print(cad[7:])
tica
```

{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Realizando previamente la asignación `palabra1='Informática'` y `palabra2='programación'`, obtén los resultados de estas expresiones:

![ ](../lmgs/hlc2324/img/img1_p3.png)

### Ejercicio 2

Realiza un programa cuya salida sea similar a la que se muestra en la imagen siguiente.

![ ](../lmgs/hlc2324/img/img2_p3.png)

### Ejercicio 3

Realiza un programa cuya salida sea similar a la que se muestra en la imagen siguiente.

![ ](../lmgs/hlc2324/img/img3_p3.png)

### Ejercicio 4

Realiza un programa cuya salida sea similar a la que se muestra en la imagen siguiente.

![ ](../lmgs/hlc2324/img/img4_p3.png)

### Ejercicio 5

Realiza un programa cuya salida sea similar a la que se muestra en la imagen siguiente.

![ ](../lmgs/hlc2324/img/img5_p3.png)

### Ejercicio 6



{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
