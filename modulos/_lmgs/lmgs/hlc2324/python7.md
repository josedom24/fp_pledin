---
permalink: /python/python7.html
layout: single3
---

# Estructura repetitiva: while

La instrucción while ejecuta una secuencia de instrucciones mientras una condición sea verdadera.
```
while <condición>:
    <instrucciones>
```
* Al ejecutarse esta instrucción, la condición es evaluada. Si la condición resulta verdadera, se ejecuta una vez la secuencia de instrucciones que forman el cuerpo del ciclo. Al finalizar la ejecución del cuerpo del ciclo se vuelve a evaluar la condición y, si es verdadera, la ejecución se repite. Estos pasos se repiten mientras la condición sea verdadera.
* Se puede dar la circunstancia que las instrucciones del bucle no se ejecuten nunca, si al evaluar por primera vez la condición resulta ser falsa.
* Si la condición siempre es verdadera, al ejecutar esta instrucción se produce un ciclo infinito. A fin de evitarlo, las instrucciones del cuerpo del ciclo deben contener alguna instrucción que modifique la o las variables involucradas en la condición, de modo que ésta sea falsificada en algún momento y así finalice la ejecución del ciclo.

{% capture notice-text %}

**Ejemplo 1**

Escribir en pantalla del 1 al 10.

![ ](../lmgs/hlc2324/img/img1_p7.png)

* Podemos observar como se inicializa la variable que vamos a imprimir antes del while.
* La última instrucción en el bloque while incrementa la variable, de este modo llegará el momento que la variable sea mayor que 10 y la condición no se cumpla.

**Ejemplo 2**

Pedir por teclado un número y se muestra su cuadrado. El programa termina cuando se introduce el 0.

![ ](../lmgs/hlc2324/img/img2_p7.png)

* En este caso, pedimos el número antes del while, ya que la condición de salida va a preguntar por el número.
* Al final del bucle, vuelvo a preguntar por el número, de esta manera es posible que valga 0 que es la condición de salida.

**Ejemplo 3**

Realiza un programa que pida una contraseña. Mientras la contraseña sea incorrecta, me da un error y vuelve a pedir la contraseña. Cuando se acierta, me informa de que he adivinado la contraseña.

![ ](../lmgs/hlc2324/img/img3_p7.png)


{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Realizar un programa con while que muestre los números del  1 al 20, su cuadrado y su cubo. La salida del programa será:

![ ](../lmgs/hlc2324/img/img6_p6.png)

### Ejercicio 2

Escribe un programa que vaya pidiendo números. Nos ira informando si el número es par o impar. el programa termina al introducir un 0.

![ ](../lmgs/hlc2324/img/img4_p7.png)

### Ejercicio 3

Realizar un programa que vaya pidiendo números, hasta que se introduzca el 0 (dicho de otra manera mientras el número introducido sea distinto de 0 sigo pidiendo números). Al finalizar me dirá cuántos números he introducido y la suma de todos. Nota: Si el primer número que meto es 0, me dirá que he metido 0 números.

![ ](../lmgs/hlc2324/img/img5_p7.png)

![ ](../lmgs/hlc2324/img/img6_p7.png)

### Ejercicio 4

Realiza un programa que pida cadena de caracteres hasta que se introduzca la cadena "*". Por cada cadena introducida me saldrá la longitud. Al finalizar me mostrará la cantidad de cadenas con más de 5 caracteres, la cantidad de cadenas con menos o igual de 5 caracteres.

![ ](../lmgs/hlc2324/img/img7_p7.png)

### Ejercicio 5

Hacer un programa de login. El programa pedirá un nombre de usuario y una contraseña. Si el usuario es **pepe** y la contraseña **asdasd** el programa terminará dando un mensaje de bienvenida. Mientras no aciertes el usuario o la contraseña, el programa dará un error y volverá a pedir el usuario y la contraseña. Al finalizar el programa el programa nos dirá el número de intentos que has realizado.

![ ](../lmgs/hlc2324/img/img8_p7.png)

### Ejercicio 6

Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.

![ ](../lmgs/hlc2324/img/img9_p7.png)

![ ](../lmgs/hlc2324/img/img10_p7.png)

![ ](../lmgs/hlc2324/img/img11_p7.png)


### Ejercicio 7

Realiza un programa que vaya pidiendo las notas de los alumnos de una asignatura, cada vez que introducimos una nota nos pregunta "¿Quieres introducir otra nota (S/N)?". Si podemos "S" nos pedirá otra nota. Cuando pongamos "N" nos dirá el número de alumnos de la clase y la nota media obtenida.

![ ](../lmgs/hlc2324/img/img12_p7.png)

### Ejercicio 8

Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
Recuerda que 2 elevado a 3 es 2 * 2 * 2.

### Ejercicio 9

Realizar un programa que genere un número aleatorio del 1 al 100. El objetivo es acertar ese número, por lo tanto me irá pidiendo números hasta que lo acierte. Al final me dirá en cuantos intentos lo he acertado.

![ ](../lmgs/hlc2324/img/img13_p7.png)

### Ejercicio

Vamos a mejorar el ejercicio anterior, para que cuando introduzca un número me diga si el que el ha generado es mayor o menor, de esta forma me ayudará a acertar el número más fácilmente.

![ ](../lmgs/hlc2324/img/img14_p7.png)













Escribe un programa que pida un número inicial a otro final y muestre los números que van desde el inicial hasta el final. Si el valor inical es mayoor que el ginal se dará un mensaje de error y se terminará el programa. Ejemplo de salida:

![ ](../lmgs/hlc2324/img/img7_p6.png)
![ ](../lmgs/hlc2324/img/img8_p6.png)

### Ejercicio 3

Realiza un programa parecido al anterior, pero en este caso si el valor inicial es mayor que el final, también se mostrarán los números que hay desde el inicial al final, por ejemplo:

![ ](../lmgs/hlc2324/img/img9_p6.png)

### Ejercicio 4

Hacer un programa que nos pida por teclado un número y nos muestre la tabla de multiplicar, por ejemplo:

![ ](../lmgs/hlc2324/img/img10_p6.png)

### Ejercicio 5

Realiza un programa que nos pida 10 números. Al finalizar, nos indicara cuantos de ellos son positivos, cuantos negativos y cuantos 0. Ejemplo de salida:

![ ](../lmgs/hlc2324/img/img11_p6.png)

### Ejercicio 6

Realizar un programa que muestre todos los divisores de un número. si el número no es positivo se dará un error y se terminará el programa. Ejemplo:

![ ](../lmgs/hlc2324/img/img12_p6.png)

### Ejercicio 7

Realiza un programa que pida por teclado 10 números y finalmente muestre la siguiente información:

* La cantidad de números pares introducidos.
* La suma de todos los números pares.
* La cantidad de números impares introducidos.
* El producto de todos los números impares.

![ ](../lmgs/hlc2324/img/img13_p6.png)

### Ejercicio 8

Realiza un programa que nos pida por teclado cuantas cadenas de caracteres vamos a introducir. A continuación iremos introduciendo cadenas, y al finalizar el programa nos mostrará la siguiente información:

* Cuantas cadenas tenían más de 5 caracteres.
* Cuantas cadenas tenía al menos un espacio.
* La suma de la cantidad de caracteres de cada una de las cadenas introducidas.

![ ](../lmgs/hlc2324/img/img14_p6.png)

### Ejercicio 9

Vamos a realizar un programa que nos pida por teclado la cantidad de multiplicaciones que nos va a preguntar. A continuación va generando multiplicaciones (igual que el ejercicio 4 del boletín anterior).

* Genera dos números del 1 al 10 de forma aleatoria.
* Por ejemplo si se ha generado el 4 y el 7, muestra por pantalla la cadena "4 x 7 =".
* Pide al usuario que introduzca el resultado.
* Indica al usuario si el resultado que ha puesto es correcto o no es correcto.

Esto se repite tantas veces como le hayamos indicado. Al final nos dirá cuantas multiplicaciones hemos acertado.

![ ](../lmgs/hlc2324/img/img15_p6.png)

### Ejercicio 10

Hacer un ejercicio, que nos pida por teclado el número de alumnos que hay en una clase. A continuación nos irá pidiendo la nota que ha sacado en un examen. Al finalizar no dirá cuantos alumnos han aprobado, cuantos alumnos han suspendido y la nota media de la clase.

![ ](../lmgs/hlc2324/img/img16_p6.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
