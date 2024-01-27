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

Escribe un programa que pida un número inicial a otro final y muestre los números que van desde el inicial hasta el final. Si el valor inical es mayoor que el ginal se dará un mensaje de error y se terminará el programa. Ejemplo de salida:

![ ](../lmgs/hlc2324/img/img7_p6.png)
![ ](../lmgs/hlc2324/img/img8_p6.png)

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
