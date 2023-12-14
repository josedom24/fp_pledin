---
permalink: /python/python2.html
layout: single3
---

# Tipos de datos, Operadores y Variables

En esta práctica vamos a estudiar cómo trabajar con los datos en el lenguaje Python, también veremos los distintos tipos que existen y las operaciones que podemos realizar con ellos.

## Trabajando con datos numéricos

{% capture notice-text %}

**Ejercicio**

Vamos a comenzar a usar Python desde el intérprete como si se tratase de una calculadora inteligente capaz de hacer cálculos matemáticos. Usando el interprete realiza los siguientes cálculos:

![ ](../lmgs/hlc2324/img/img1_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* Podemos trabajar con números **enteros (int)** (sin decimales) o con números **reales (float)** (con decimales) (utilizamos el punto para separar la parte entera de la parte decimal). 
* Podemos realizar las operaciones básicas de **suma(+), resta(-), multiplicación(*) y división(/)**.
* También podemos hacer operaciones un poco más complejas, por ejemplo la **potenciación(\*\*), división entera(//) y el resto de la división o módulo (%)**.
* Más adelante veremos que podemos hacer **más operaciones matemáticas**.

## Trabajando con cadenas de caracteres

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para trabajar con cadenas de caracteres:

![ ](../lmgs/hlc2324/img/img2_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* En estos ejemplos hemos escrito texto entrecomillado, este tipo de dato recibe el nombre de **cadenas de texto (strings)**. 
* En Python las cadenas de texto se pueden escribir entre **comillas dobles o entre comillas simples**.
* Para unir dos cadenas usamos la operación **concatenar (+)**.
* Podemos concatenar varias veces una cadena varias veces para ello usamos el operador **repetir (*)**.

## Trabajando con comparaciones

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para comparar números:

![ ](../lmgs/hlc2324/img/img3_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* Hemos comparado valores numéricos y Python no ha dicho si el resultado de las comparaciones es **cierto (True)** o **falso (False)**.
* A los valores **True y False**, se le llaman **datos lógicos o booleanos**.
* Estos valores se utilizan para comprobar si se cumple alguna condición en un determinado momento. 

## Tipos de datos y operadores

Hemos visto que los datos con los que podemos trabajar en un programa Python lo podemos dividir en los siguientes **tipos**:

* **Numéricos enteros (int)**.
* **Numéricos decimales (float)**.
* **Textos o cadenas de caracteres (strings)**.
* **Datos lógicos o booleanos (bool)**.

Python tiene más tipos de datos, pero por el momento, nos quedaremos con estos que son los más comunes cuando se empieza a programar.

También hemos visto que podemos hacer distintas operaciones con distintos **operadores**:

* **Operadores matemáticos**
* **Operadores de cadenas**
* **Operadores de comparación**

Resumen de operadores:

![ ](../lmgs/hlc2324/img/img4_p2.png)

## Variables

En muchas ocasiones necesitamos "recordar" un dato (numérico, texto o lógico). Para poder recordarlo podemos guardarlo en la memoria del ordenador dándole un **nombre** y **asignándole el valor a dicho nombre**.
Este es el concepto de **variable**, se trata de **un nombre al cual se le asigna un valor**. Este valor puede ser directo o como resultado de una operación.

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para trabajar con variables:

![ ](../lmgs/hlc2324/img/img5_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* Las **variables** son un almacén donde guardar una información y que en cualquier momento podemos recuperarla para volver a utilizarla. Los nombres de las variables deben cumplir lo siguiente:
    * No deben se palabras reservadas de Python.
    * Deben comenzar por una letra.
    * No pueden contener espacios ni caracteres extraños.
    * Python hace distinción entre mayúsculas y minúsculas.

* En los lenguajes de programación, **el símbolo = debe entenderse como una asignación**, no como una igualdad matemática.
* En Python, las variables **no es necesario declararlas ni indicar qué tipo de información va a contener**, basta con asignarles un valor y nada más.

## Entrada y salida de información 

La instrucción **print** la usaremos para mostrar mensajes por pantalla.

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para trabajar con la instrucción print:

![ ](../lmgs/hlc2324/img/img6_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* Observa que cuando se le pasan varios argumentos separados por comas, la función print al mostrar estos valores,  introduce un espacio entre ellos para que se visualicen mejor.

Al igual que la función print sirve para mostrar información, disponemos de la función **input** para introducir datos en el programa para que puedan ser procesados. Estos datos se almacenan en una variable y se utilizan cuando el programa los necesita en función de las tareas que deba llevar a cabo.

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para trabajar con la instrucción input:

![ ](../lmgs/hlc2324/img/img7_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


* La función input devuelve una cadena de texto.
* En este ejemplo podemos comprobar que el valor de n es el texto '12', sin embargo, el valor de v es el número 12.
* La conversión de n en un valor numérico podemos hacer de varias formas distintas:
    * v = int(n), si queremos convertirla a un número entero.
    * v = float(n), si queremos convertirla a un número real.

Para que la conversión de una cadena de texto a entero o float, se realice correctamente, si usamos las funciones int() o float() los valores deben ser del tipo correspondiente.

{% capture notice-text %}

**Ejercicio**

En este ejercicio vamos a usar el interprete de Python para trabajar con la instrucción input:

![ ](../lmgs/hlc2324/img/img8_p2.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

* Se produce **un error por ser n un valor inválido para convertirlo en un valor entero**.

Para terminar indicar que podemos convertir directamente el valor leído por la instrucción input, por ejemplo:

```python
edad = int(input("Indica tu edad:"))
precio = float(input("Indica el precio del producto:"))
```

{% capture notice-text %}

## ¿Qué tienes que entregar?

### Ejercicio 1

Escribe el siguiente programa y ejecútalo:

![ ](../lmgs/hlc2324/img/img9_p2.png)

### Ejercicio 2

Utilizando el interprete de Python3 calcula las siguientes operaciones:

![ ](../lmgs/hlc2324/img/img10_p2.png)

### Ejercicio 3

Utilizando el interprete de Python3 crea una variable llamada **n** y asígnale el valor 5 (n=5). Luego realiza en el orden que aparecen las siguientes operaciones y escribe el resultado obtenido (de izquierda a derecha y después hacia abajo):

![ ](../lmgs/hlc2324/img/img11_p2.png)

### Ejercicio 4

Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra. Escribe un programa que pida el precio de un artículo y que muestre el precio restándole el 15%.

### Ejercicio 5

Un alumno desea saber cual será su calificación final en una asignatura. Para ello escribe un programa que pida la calificación del examen, la calificación de las prácticas y la calificación de los ejercicios. Y muestra la nota final sabiendo que se calcula de la siguiente forma:
    * 50% de de la nota final es la nota del examen.
    * 30% de la nota final es la nota de las prácticas.
    * 20% de la nota final es la nota de los ejercicios.

### Ejercicio 6

Realiza un programa que pida una distancia en kilómetros y te muestre los metros a los que corresponde.

Ejemplo de ejecución:
![ ](../lmgs/hlc2324/img/img12_p2.png)
![ ](../lmgs/hlc2324/img/img13_p2.png)

### Ejercicio 7

Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.






**Entrega**

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
