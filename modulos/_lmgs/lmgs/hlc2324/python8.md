---
permalink: /python/python8.html
layout: single3
---

# Boletín de ejercicios


{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Escribe el siguiente programa, arreglando los errores que tiene para que se pueda ejecutar:

```python
 Este programa verifica si un número es par o impar y luego muestra los primeros cinco números primos.

# Solicitar al usuario que ingrese un número
numero = intinput("Ingrese un número: "

# Determinar si el número es par o impar
if numero % 2 = 0
    print(numero "es un número par.")
else
    print(numero, "es un número impar.")

# Encontrar los primeros cinco números primos
primos = []
for i in range(2, 20)
    es_primo = True
    for j in range(2, i):
        if i % j = 0:
            es_primo = False
            break
    if es_primo=True
        primos.append(i)

# Mostrar los primeros cinco números primos
print("Los primeros cinco números primos son:" primos[:5])
```

### Ejercicio 2

Escribe un programa en Python que calcule el índice de masa corporal (IMC) de una persona. El IMC se calcula utilizando la fórmula:

IMC=peso / altura**2

El programa debe solicitar al usuario que ingrese su peso en kilogramos y su altura en metros. Luego, calculará el IMC y mostrará un mensaje indicando si la persona está por debajo del peso saludable (IMC menor a 18.5), dentro del rango de peso saludable (IMC entre 18.5 y 24.9), o en sobrepeso (IMC igual o mayor a 25).

### Ejercicio 3

Escribe un programa en Python que ayude a un estudiante a calcular su calificación final en un curso. El programa debe solicitar al usuario que ingrese las calificaciones obtenidas en tres evaluaciones parciales y la calificación obtenida en el examen final del curso. Luego, calculará la calificación final a partir de las calificaciones parciales y el examen final, donde las evaluaciones parciales cuentan un 30% cada una y el examen final cuenta un 40%. Finalmente, mostrará la calificación final del estudiante.

### Ejercicio 4

Escribe un programa en Python que calcule el perímetro y el área de un rectángulo. El programa debe solicitar al usuario que ingrese la longitud y la anchura del rectángulo. Luego, calculará el perímetro sumando los cuatro lados del rectángulo y el área multiplicando la longitud por la anchura. Finalmente, el programa mostrará el perímetro y el área del rectángulo.

### Ejercicio 5

Escribe un programa en Python que ayude a un cajero automático a dispensar dinero en efectivo. Suponemos que el usuario tiene en el banco una cantidad (saldo) de 500€. El programa debe solicitar al usuario que introduzca la cantidad que desea retirar. 
Luego, verificará si la cantidad es un valor válido:
* Es múltiplo de 10 y
* no excede el saldo disponible en la cuenta. 

Si la cantidad es válida, el programa mostrará la cantidad que has solicitado y el saldo que te queda en el banco. En caso contrario, mostrará un mensaje de error indicando que la cantidad no es válida. 

### Ejercicio 6

Realiza un programa Python que comprueba si una cadena introducida por teclado es pentavocálica. Una cadena pentavocálica es aquella que tiene al menos una vez todas las vocales.

Debes probar las vocales minúsculas y mayúsculas.
Se introduce la cadena, y el programa te dice si es pentavocálica o no.

### Ejercicio 7

Escribe un programa en Python que determine el tipo de triángulo basado en las longitudes de sus lados. El programa solicitará al usuario que ingrese las longitudes de los tres lados del triángulo. 

Primero verifica si la longitud de los lados corresponde a un triangulo, para ello la suma de cualquiera de dos lados debe ser mayor que el otro lado.
Si no cumple esa condición dará un mensaje de error.

Luego, determinará y mostrará el tipo de triángulo según las siguientes condiciones:

* Si todos los lados son iguales, el triángulo es equilátero.
* Si dos lados son iguales, el triángulo es isósceles.
* Si todos los lados son diferentes, el triángulo es escaleno.


### Ejercicio 8

Escribe un programa en Python que calcule el costo total de una compra en un supermercado. 

El programa debe solicitar cuántos productos has comprado. A continuación por cada producto, pedirá lo que vale y la cantidad que ha comprado. Irá calculando el costo total de la compra sumando el precio de cada artículo multiplicado por su cantidad correspondiente. 
El programa debe mostrar el costo total de la compra.


### Ejercicio 9

Vamos a mejorar el ejercicio 5. Vamos a realizar un programa que simule un cajero automática. El usuario al principio tiene 500€.
El programa pedirá elegir entre tres opciones:

"Ingresar (I), Retirar (R), Terminar(T)"

* Si pulsamos la I, nos pedirá una cantidad, que debe ser múltiplo de 10 y lo sumará al saldo.
* Si pulsamos la R, nos pedirá una cantidad, que debe ser múltiplo de 10 y menor que el saldo y lo restará al saldo.
* Si pulsamos la T el programa se terminará.

A continuación se mostrará el saldo,y se volverá a preguntar hasta que se introduzca la opción de salir.

![ ](../lmgs/hlc2324/img/img1_p8.png)

### Ejercicio 10

El método `count` de las cadenas de caracteres en python devuelve el número de ves que aparece una cadena dentro de otra.

Por ejemplo, si queremos saber cuantas "a" tiene la palabra "Abracadabra", podríamos ejecutar:

```python
cadena = "Abracadabra"
cantidad = cadena.count("a")
print(cantidad)
```

Escribe un programa en Python que solicite al usuario que ingrese cadenas de caracteres una tras otra. El programa continuará pidiendo cadenas hasta que el usuario introduzca un asterisco *. Por cada cadena, el programa mostrará la cadena y el número de caracteres que tiene. Al final el programa mostrará.

* La cantidad de cadenas que has introducido.
* La cantidad de espacios que has introducido.
* La cantidad de palabras que tienen una "a".

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
