---
permalink: /lmgs/2020-2021/python3/solucion_boletin1.html
layout: single3
---

# Análisis y diseño de problemas. Ejercicios resueltos

## Ejercicio 1

Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

### Análisis

* Definición del problema: Tenemos que pedir un nombre por teclado y luego escribir un mensaje de saludo.
* Datos/Variables de entrada: nombre (Cadena)
* Datos/Variables de salida: saludo (Cadena)

### Diseño
 1. Leer nombre
 2. saludo = "Hola " y el nombre
 3. Escribir saludo

- - -

## Ejercicio 2

Calcular el perímetro y área de un rectángulo dada su base y su altura.

### Análisis

* Definición del problema: Tenemos que leer la base y la altura del triangulo y calcular el perí­metro y el área. 
`perimetro = 2*pi*radio`
`area=pi*radio al cuadrado`
* Datos/Variables de entrada: radio (real)
* Datos/Variables de salida:  perímetro(real) y área(real)

### Diseño

1. Leer base y altura
2. Calcular perí­metro. perí­metro=2*pi*radio
3. Calcular área. área= pi*radio al cuadrado
4. Mostrar perí­metro y área

- - -

## Ejercicio 3

Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

### Análisis

* Definición del problema: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. En un triángulo rectángulo el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.
* Datos/Variables de entrada: cateto1(real), cateto2(real)
* Datos/Variables de salida:  hipotenusa(real)

### Diseño

1. Leer la longitud de los catetos
2. Calcular hipotenusa (igual a la raí­z cuadrada de la suma de los cuadrados de los catetos).
3. Mostrar la hipotenusa

- - -

## Ejercicio 4

Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

### Análisis

* Definición del problema: Tenemos que leer dos números, calcular la suma, resta, multiplicación y división.
* Datos/Variables de entrada: numero1(entero), numero2(entero)
* Datos/Variables de salida:  suma(entero), resta(entero), multiplicación(entero), división(real)

### Diseño

1. Leer numero1,numero2
2. Calcular suma, resta, multiplicación y división
3. Mostrar suma,resta, multiplicación y división

- - -

## Ejercicio 5

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

### Análisis

* Definición del problema: Tenemos que leer una temperatura en grados Fahrenheit y devolverla en grados celsius.
`C = (F-32)*5/9)`
* Datos/Variables de entrada: Grados Fahrenheit (real)
* Datos/Variables de salida:  Frado Celsius (real)

### Diseño

1. Leer la temperatura en grados Fahrenheit
2. Calcular los grados celsius (C = (F-32)*5/9)
3. Mostrar grados celsius

- - - 

## Ejercicio 6

Calcular la media de tres números pedidos por teclado

### Análisis

* Definición del problema: Tenemos que leer tres números y calcular la media. Suma de los tres números partido 3.
* Datos/Variables de entrada: numero1 (real),numero2 (real),numero3 (real)
* Datos/Variables de salida:  media (real)

### Diseño

1. Leer numero1,numero2,numero3
2. Calcular la media. media = (numero1+numero2+numero3)/3
3. Mostrar media

- - - 

## Ejercicio 7

Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

### Análisis

* Definición del problema: Tenemos que leer una cantidad de minutos, y calcular cuantas horas y minutos son. Si divido los minutos totales entre 60, la división entera será las horas y el módulo (el resto de la división) serán los minutos restantes.
* Datos/Variables de entrada: minutos_totales (entero)
* Datos/Variables de salida:  horas (entero), minutos (entero)

### Diseño

1. Leer los minutos totales
2. Calcular a cuantas horas corresponde, división entera entre 60.
3. calcular los minutos restantes: resto de la división entre 60.
4. Mostrar horas y minutos

- - -

## Ejercicio 8

Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

### Análisis

* Definición del problema: El vendedor tiene un sueldo base mas una comisión del 10% por cada venta. Hace tres ventas.
* Datos/Variables de entrada: sueldo base (real), venta1 (real), venta2 (real), venta3 (real).
* Datos/Variables de salida:  comisiones (real),) sueldo total (real)

### Diseño

1. Leer sueldo base
2. Leer venta1, venta2 y venta3
3. Calcular las comisiones. Ir sumando el 10 % de cada venta. comision = 0,1 * venta1 + 0,1 * venta2 + 0,1 * venta3
4. Mostrar comisión
5. Mostrar sueldo total: sueldo_base+comisión

- - -

## Ejercicio 9

Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

### Análisis

* Definición del problema: Debemos preguntar cuanto dinero es la compra, calcular el 15% y restarlo al total.
* Datos/Variables de entrada: precio (real).
* Datos/Variables de salida:  precio final (real).

### Diseño

1. Leer el precio
2. Calcular precio final = precio - 15% del precio
3. Mostrar precio final

- - -

## Ejercicio 10

Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final.

### Análisis

* Definición del problema: Hay que leer las notas parciales, la nota del examen final y la nota del trabajo final. Posteriormente se calculan los porcentajes y se suman.
* Datos/Variables de entrada:  parcial1 (real), parcial2 (real), parcial3 (real), nota_examen (real), nota_trabajo (real)
* Datos/Variables de salida:  nota_final (real)

### Diseño

1. Leer parcial1, parcial2, parcial3, nota_examen, nota_trabajo
2. Calculamos la nota final. 55% de la media de las notas parciales más el 30% de la nota del examen mas 15% de la nota del trabajo.
`nota_final = 0,55 * ((parcial1 + parcial2 + parcial3)/3) + 0,3 * nota_examen + 0,15 * nota_trabajo`
3. Mostrar nota_final

- - -

## Ejercicio 11

Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

### Análisis

* Definición del problema: Se piden dos números y se calcula el valor absoluto de la diferencia.
* Datos/Variables de entrada:  numero1 (entero), numero2 (entero).
* Datos/Variables de salida:  distancia (entero)

### Diseño

1. Leer los dos números.
2. Calcular distancia (valor absoluto de la diferencia). 
3. Mostrar distancia.

- - -

## Ejercicio 12

Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

### Análisis

* Definición del problema: Se piden dos puntos (cada punto está representado por dos coordenadas) y se calcula la distancia entre ellos. Para calcular la distancia se utiliza la formula que hemos mostrado.
* Datos/Variables de entrada: cuatro coordenadas (x1,y1) (x2,y2) (entero).
* Datos/variables de salida: distancia (real).

## Diseño

1. Leer las cuatro coordenadas.
2. Calcular distancia: raíz cuadrada de (x2-x1)^2 + (y2-y1)^2
3. Mostrar distancia 

- - -

## Ejercicio 13

Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

### Análisis

* Definición del problema: Se piden número y se muestra la raíz cuadrada y la cúbica. 
* Datos/Variables de entrada: numero (entero)
* Datos/variables de salida: raíz_cuadrada (real), raíz_cúbica(real).

## Diseño

1. Leer el número.
2. Calcular raíz cuadrada
3. Calcular raíz cúbica
4. Mostrar la raíz_cuadrada, raíz_cúbica

- - -

## Ejercicio 14

Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 

### Análisis

* Definición del problema: Se pide un número de dos cifras y se debe mostrar el número de unidades y de decenas
* Datos/Variables de entrada: numero (entero).
* Datos/variables de salida: decenas (real), unidades (entero).

## Diseño

1. Leer el número de dos cifras
2. Calcular decenas: división entera del número entre 10.
3. Calcular unidades: resto de dividir el número entre 10.
4. Mostrar decenas y unidades

- - -

## Ejercicio 15

Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

### Análisis

* Definición del problema: Se piden el valor de dos variables (el tipo puede ser el que queramos). Hay que intercambiar los valores de las variables.
* Datos/Variables de entrada: numero1 (entero), numero2 (entero).
* Necesito una variable auxiliar (aux). 
* Datos/variables de salida:  Las dos variables pero con los datos cambiados (entero)

## Diseño

1. Leer los dos números
2. Intercambio los valores. Asigno "numero1" en "aux", "numero2" en "numero1" y "aux" en "numero2"
3. Mostrar "numero1" y "numero2"

- - -

## Ejercicio 16

Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

### Análisis

* Definición del problema: Hay que saber la velocidad de cada vehículo, y la distancia entre ambos, sabemos que v=s/t, por lo tanto t=s/v, con esta formula calcularemos el tiempo que tardará el que está detrás (y va más rápido) en alcanzar al primero, siendo la velocidad la diferencia de velocidad.
* Datos/Variables de entrada: velocidad1, velocidad2 (real) y distancia (real).
* Datos/variables de salida: Tiempo en minutos (real)

### Diseño

1. Leer las dos velocidades y la distancia (no puedo controlar que v1 > v2).
2. Calcular tiempo: (v=s/t), por lo tanto t=s/v. Tiempo = distancia / (v1-v2)
3. El tiempo hay que pasarlo a minútos tiempo*60
4. Mostrar tiempo

- - -

## Ejercicio 17

Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

### Análisis

* Definición del problema: Tenemos que pedir la hora de salida (hora, minutos y segundos). Tengo que saber también el tiempo en segundo que ha tardado en llegar. Tenemos que calcular la hora de llegada.
* Datos/Variables de entrada: hora_salida (entero), minutos_salida (entero), segundos_salida (entero), segundos_viaje (entero).
* Datos/variables de salida: hora_llegada (entero), minutos_llegada (entero), segundos_llegada (entero)

### Diseño

1. Leer hora_salida,minutos_salida, segundos_salida
2. Leer segundos_viaje
3. Convierto la hora de salida a segundos (necesito una variable seginicial) 
`seginicial=hora_salida * 3600 + minuto_salida * 60 + segundos_salida`
4. Le sumo los segundos que he tardado(necesito una variable segfinal)
`segfinal=seginial+segundos_viaje
5. Convierto los segundos totales a hora, minuto y segundos
`horallegada = (segfinal / 3600)` División entera
`minllegada = ((segfinal % 3600) / 60)` División entera
`segllegada <- (segfinal % 3600) % 60`
6. Muestro hora_llegada,minutos_llegada, segundos_llegada

- - -

## Ejercicio 18

Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

### Análisis

* Definición del problema: Hay que pedir el nombre y los apellidos, y mostrar las iniciales. Las iniciales son la primera letra del nombre, primer apellido y segundo apellido.
* Datos/Variables de entrada: nombre (cadena), apellido1 (cadena), apellido2 (cadena)
* Datos/variables de salida: iniciales (cadena)

### Diseño

1. Leer nombre, apellido1, apellido2
2. Obtener primer carácter de cada cadena
3. Concatenar los caracteres en iniciales
4. Mostrar iniciales

- - -

## Ejercicio 19

Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

### Análisis

* Definición del problema: Se piden la cantidad de respuestas correctas, las respuestas incorrectas y las en blanco. Calculamos la nota: 5 puntos por respuesta correcta, -1 por incorrecta. `nota=5 * correctas - incorrectas
* Datos/Variables de entrada: correctas (entero), incorrectas (entero), en_blanco(entero).
* Datos/variables de salida: nota (entero)

### Diseño

Diseño
1. Leer correctas, incorrectas, en_blanco
2. Calcular nota: número de correctas * 5 + número de incorrectas * -1
3. Mostrar nota

- - -

## Ejercicio 20

Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

### Análisis

* Definición del problema: Se piden la cantidad de monedas que tenemos (de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos) y calculamos el dinero que tenemos (euros y céntimos).
* Datos/Variables de entrada: 2euros (entero), 1euro (entero), 50céntimos (entero), 20céntimos (entero), 10céntimos (entero)
* Datos/variables de salida: total_euros (entero), total_centimos (entero)

### Diseño

1. Leer el monedas de 2euros, 1euro, 50céntimos, 20céntimos o 10céntimos.
2. Calcular Euros (`sumar monedas de 2 euros * 2 + monedas de 1 euro`)
3. Calcular céntimos 
`monedas de 50c * 50 + monedas de 30c * 30 + moneda de 20c * 20 + moneda de 10c * 10`
4. Convertir céntimos a euros (división entera entre 100)
5. Mostrar total_euros, total_centimos

