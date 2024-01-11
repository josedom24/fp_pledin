---
permalink: /python/python4.html
layout: single3
---

# Estructura alternativa o condicional

Todos los lenguajes de programación disponen de estructuras que permiten evaluar expresiones cuyo resultado es **True** o **False** y dependiendo del resultado ejecutar un
determinado bloque de instrucciones u otro.
A este tipo de estructuras se le llaman **estructuras alternativas o condicionales**, evalúan una condición y cuando la condición resulta **True** ejecutan un determinado código y cuando resultan **False** pueden ejecutar otro bloque de código.
En Python estas estructuras vienen definidas con las palabras reservadas: **if, else y elif**.

## Alternativas simples

Al ejecutarse la instrucción **if** se evalúa la condición lógica. Si la condición lógica es **True** se ejecutan de manera secuencial el bloque de instrucciones . Si la condición es **False** no se ejecuta el bloque de instrucciones. Una vez ejecutado el **if** (opción verdadera o falsa) se continúa la ejecución de forma secuencial por la siguiente instrucción (bloque de instrucción no identado).

{% capture notice-text %}

**Ejercicio**

Escribe el siguiente programa y comprueba como funciona:

![ ](../lmgs/hlc2324/img/img1_p4.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Alternativas doble

Al ejecutarse la instrucción **if** se evalúa la condición lógica. Si la condición lógica es **True** se ejecutan de manera secuencial el primer bloque de instrucciones. Si la condición es **False** se ejecuta el segundo bloque de instrucción. Una vez ejecutado el **if** (opción verdadera o falsa) se continúa la ejecución de forma secuencial por la siguiente instrucción (bloque de instrucción no identado).

{% capture notice-text %}

**Ejercicio**

Escribe el siguiente programa y comprueba como funciona:

![ ](../lmgs/hlc2324/img/img2_p4.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Alternativa múltiple

En este caso tenemos varias opciones. Vamos preguntando por cada una de las opciones y según el valor de la expresión ejecutamos un bloque o otro. 

{% capture notice-text %}

**Ejercicio**

Escribe el siguiente programa y comprueba como funciona:

![ ](../lmgs/hlc2324/img/img3_p4.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>















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

Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

### Ejercicio 7

Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

### Ejercicio 8

Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

### Ejercicio 9

Crea un programa que genere e imprima un número decimal entre 0 y 1; un número entero entre 10 y 100; un número decimal entre 10 y 20.

### Ejercicio 10

Realiza un programa que genere 2 número aleatorios entre 1 y 6 simulando el lanzamiento de 2 dados. Debe mostrar los 2 números obtenidos y la suma de dichos números.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
