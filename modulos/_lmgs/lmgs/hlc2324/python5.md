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


## Estructuras alternativas anidadas

Anidar estructuras significa incluir unas estructuras dentro de otras.

{% capture notice-text %}

**Ejercicio**

Para hacer este ejercicio, vamos a aprender dos cosas:

1. Si tenemos una cadena, podemos calcular el número de caracteres que tiene usando la función **len**. Por ejemplo:

    ``` 
    cadena = "programa"
    print(len(cadena))
    8
    ```
2. El operador **in** nos permite averiguar si una cadena está dentro de otra. Devuelve **True** si la primera cadena está dentro de la segunda, y **False** en caso contrario. Por ejemplo:

    ```
    >>> cadena = "informática"
    >>> "info" in cadena
    True
    >>> "mati" in cadena
    False
    ```
El programa que queremos hacer es el siguiente:

El programa mostrará un mensaje indicando lo que hace.

* Solicitará el nombre del usuario.
* Contará el número de caracteres del nombre.
* Si el nombre tiene 7 caracteres o menos, sólo contará mostrará el numero de caracteres del nombre.
* Si el nombre tiene más de 7 caracteres, comprobará además si contiene algún espacio.
* En el caso de que contenga algún espacio dirá que el nombre es compuesto.
* Si no contiene ningún espacio, dirá que el nombre no es compuesto.

Escribe el programa y comprueba como funciona:

![ ](../lmgs/hlc2324/img/img4_p4.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Programa que pida dos números e indique si el primero es mayor que el segundo o no.

### Ejercicio 2

Programa que pida un número y diga si es positivo, negativo o 0.

### Ejercicio 3

Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

### Ejercicio 4

Escribe un programa que pide un mes (un número del 1 y al 12). Si se introduce un mes incorrecto se dará un error y terminará el programa. Si el mes es correcto se escribirá en pantalla el nombre del mes.

### Ejercicio 5

Escribe un programa que pide un mes (un número del 1 y al 12). Si se introduce un mes incorrecto se dará un error y terminará el programa. Si el mes es correcto se escribirá en pantalla los días que tiene dicho mes (suponemos que febrero tiene 28 días).

### Ejercicio 6

Escribe un programa que genere las siguientes salidas en su ejecución.

![ ](../lmgs/hlc2324/img/img5_p4.png)

### Ejercicio 7

Escribe un programa que genere las siguientes salidas en su ejecución.

![ ](../lmgs/hlc2324/img/img6_p4.png)

### Ejercicio 8

El programa comprobará si la palabra tiene 5 letras o menos, en cuyo caso mostrará la primera y la última letra.
En el caso de que tenga más de 5 letras, mostrará las 4 primeras letras por un lado y las 4 últimas letras por otro, aunque haya letras coincidentes en las 2 particiones.
El programa debe generar las siguientes salidas en su ejecución.

![ ](../lmgs/hlc2324/img/img7_p4.png)

## Ejercicio 9

Programa que pida dos números y muestre primero el mayor y luego el menor. Si son iguales, indica con un mensaje que los dos números son iguales.

## Ejercicio 10

Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
