---
permalink: /python/python6.html
layout: single3
---

# Estructura repetitiva: for

La estructura **for** nos permite ejecutar una bloque de instrucciones un número determinado de veces, desde un valor inicial, hasta un valor final y con un posible incremento. Para ello vamos a usar el tipo de datos **range** que nos permite generar listas de números. Vamos a usar **for** para crear **bucles** de instrucciones donde sabemos a priori el número de **iteraciones** que hay que realizar.

{% capture notice-text %}

**Ejemplo 1**

Escribir en pantalla del 1 al 10.

![ ](../lmgs/hlc2324/img/img1_p6.png)

**Ejemplo 2**

Escribir en pantalla de 10 al 1.

![ ](../lmgs/hlc2324/img/img2_p6.png)

**Ejemplo 3**

Escribir los número pares desde el 2 al 10.

![ ](../lmgs/hlc2324/img/img3_p6.png)


{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Contadores

Un contador es una variable entera que la utilizamos para contar cuando ocurre un suceso. Un contador:

* Se **inicializa** a un valor inicial.

		cont = 0;

* Se **incrementa**, cuando ocurre el suceso que estamos contado se le suma 1.

		cont = cont + 1;

* Otra forma de incrementar el contador:

        cont += 1


{% capture notice-text %}

**Ejemplo 4**

Introducir 5 número y contar los números pares.

![ ](../lmgs/hlc2324/img/img4_p6.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Acumuladores

Un acumulador es una variable numérica que permite ir acumulando operaciones. Me permite ir haciendo operaciones parciales. Un acumulador:

* Se **inicializa** a un valor inicial según la operación que se va a acumular: a 0 si es una suma o a 1 si es un producto.
* Se **acumula** un valor intermedio.
		
		acum  =  acum + num;

{% capture notice-text %}

**Ejemplo 5**

Introducir 5 número y sumar los números pares.

![ ](../lmgs/hlc2324/img/img5_p6.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Realizar un programa que muestre los números del  1 al 20, su cuadrado y su cubo. La salida del programa será:

![ ](../lmgs/hlc2324/img/img6_p6.png)

### Ejercicio 2

Escribe un programa que pida un número inicial a otro final y muestre los números que van desde el inicial hasta el final. Si el valor inicial es mayor que el final se dará un mensaje de error y se terminará el programa. Ejemplo de salida:

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
