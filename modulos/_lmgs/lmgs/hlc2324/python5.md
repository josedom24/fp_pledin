---
permalink: /python/python5.html
layout: single3
---

# Más programas con estructura alternativa

{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

* El exponente sea positivo, sólo tienes que imprimir la potencia.
* El exponente sea 0, el resultado es 1.
* El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

### Ejercicio 2

Realiza un programa  que pida dos números ‘nota’ y ‘edad’ y una cadena ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

### Ejercicio 3

Escribe un programa que pide un mes (un número del 1 y al 12) y un año. Si se introduce un mes incorrecto se dará un error y terminará el programa. Si el mes es correcto se escribirá en pantalla los días que tiene dicho mes. Para poner los días de febrero tienes que comprobar lo siguiente: si el año no es bisiesto, febrero tiene 28 días y si es bisiesto tiene 29 años. Una año es bisiesto si es divisible entre 4.

### Ejercicio 4

Hacer un programa que genere aleatoriamente una multiplicación, nos pida el resultado y nos diga si hemos acertado o no. Para ello:

* Genera dos números del 1 al 10 de forma aleatoria.
* Por ejemplo si se ha generado el 4 y el 7, muestra por pantalla la cadena "4 x 7 =".
* Pide al usuario que introduzca el resultado.
* Indica al usuario si el resultado que ha puesto es correcto o no es correcto.

### Ejercicio 5

Escribir un programa que, a partir de la cantidad de mesas de un aula y la cantidad de alumnos inscritos para un curso, permita determinar si alcanzan los mesas existentes. De no ser así, informar además cuantos mesas sería necesario agregar. El usuario deberá ingresar por teclado tanto la cantidad de mesas que tiene el aula, como la cantidad de alumnos inscritos para el curso.

### Ejercicio 6

Realizar un programa que permita aplicar un descuento del 10% a la cantidad total de una compra si la forma de pago empleada es de contado. El usuario deberá ingresar la cantidad de la compra realizada y la forma de pago. Si la forma de pago es CONTADO deberá aplicar el descuento y escribir el total con el descuento. Si la forma de pago es TARJETA se deberá mostrar un mensaje informando que para dicha forma de pago no tiene descuento y mostrará la cantidad de la compra sin descuento. Si introducimos otro tipo de pago nos dará un mensaje que indicara que el modo de pago no es válido.

### Ejercicio 7

Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

### Ejercicio 8

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

### Ejercicio 9

Haz una calculadora básica pida al usuario dos números, a y b; y un operador (cadena de caracteres),

* Si operador es "+" entonces debemos ver el resultado de a + b
* Si operador es "-" entonces debemos ver el resultado de a * b
* Si operador es "*" entonces debemos ver el resultado de a - b
* Si operador es "/" entonces debemos ver el resultado de a / b 
* Si se indica otro operador se mostrará un mensaje de error.

### Ejercicio 10

En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículos y 5% si compra hasta 20 artículos pero más de 10. Dado el precio unitario de un artículo y la cantidad adquirida, muestre lo que debe pagar el cliente.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
