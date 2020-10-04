---
permalink: /lmgs/2020-2021/python3/solucion_boletin1.html
layout: single3
---

# Análisis y diseño de problemas. Ejercicios resueltos

# Ejercicio 1

Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

## Análisis

* Definición del problema: Tenemos que pedir un nombre por teclado y luego escribir un mensaje de saludo.
* Datos/Variables de entrada: nombre (Cadena)
* Datos/Variables de salida: saludo (Cadena)

## Diseño
 1. Leer nombre
 2. saludo = "Hola " y el nombre
 3. Escribir saludo

# Ejercicio 2

## Análisis

* Definición del problema: Tenemos que leer la base y la altura del triangulo y calcular el perí­metro y el área. 
`perimetro = 2*pi*radio`
`area=pi*radio al cuadrado`
* Datos/Variables de entrada: radio (real)
* Datos/Variables de salida:  perímetro(real) y área(real)

## Diseño

1. Leer base y altura
2. Calcular perí­metro. perí­metro=2*pi*radio
3. Calcular área. área= pi*radio al cuadrado
4. Mostrar perí­metro y área

# Ejercicio 3

Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

## Análisis

* Definición del problema: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. En un triángulo rectángulo el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.
* Datos/Variables de entrada: cateto1(real), cateto2(real)
* Datos/Variables de salida:  hipotenusa(real)

## Diseño

1. Leer la longitud de los catetos
2. Calcular hipotenusa (igual a la raí­z cuadrada de la suma de los cuadrados de los catetos).
3. Mostrar la hipotenusa






Un alumno desea saber cual será su calificación final en la materia de Algoritmos
Dicha calificación se compone de los siguientes porcentajes:
* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final.

Análisis
Hay que leer las notas parciales, la nota del examen final 
y la nota del trabajo final. 
Posteriormente se calculan los porcentajes y se suman.
Datos de entrada: tres calificaciones parciales, nota examen final, 
					nota trabajo final (real).
Información de salida: nota final (real).
Variables: parcial,parcial2,parcial3,examen, trabajo, nota(real).

Diseño
1. Leer las notas parciales, del examen final y del trabajo.
2. Calculamos la nota 55% de la media de las notas parciales, 
   más el 30% de la nota del examen mas 15% de la nota del trabajo.
3. Mostrar nota final


Proceso CalcularNota
	Definir parcial1,parcial2,parcial3,examen,trabajo,nota como Real;
	Escribir "Dime la nota del parcial 1:";
	Leer parcial1;
	Escribir "Dime la nota del parcial 2:";
	Leer parcial2;
	Escribir "Dime la nota del parcial 3:";
	Leer parcial3;
	Escribir "Dime la nota del examen:";
	Leer examen;
	Escribir "Dime la nota del trabajo:";
	Leer trabajo;
	nota <- ((parcial1 + parcial2 + parcial3)/3)*0.55 + 0.3*examen + 0.15*trabajo;
	Escribir "Nota final:", nota;
FinProceso
Pide al usuario dos números y muestra la "distancia" entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

Análisis
Se piden dos números y se calcula el valor absoluto de la diferencia.
Datos de entrada: dos números (entero).
Información de salida: distancia (entero).
Variables: num1,num2(entero).

Diseño
1. Leer los dos números.
2. Mostrar distancia (valor absoluto de la diferencia)


Proceso CalcularDistancia
	Definir num1, num2 como Entero;
	Escribir "Dime el número1:";
	Leer num1;
	Escribir "Dime el número2:";
	Leer num2;
	Escribir "Distancia:", abs(num1-num2);
FinProceso
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
en el plano. Calcula y muestra la distancia entre ellos.

Análisis
Se piden dos puntos y se calcula la distancia entre ellos. 
Datos de entrada: dos puntos; cuatro coordenadas (x1,y1) (x2,y2) (entero).
Información de salida: distancia (real).
Variables: x1,y1,x2,y2(entero), distancia(real).

Diseño
1. Leer las cuatro coordenadas.
2. Calcular distancia: raíz cuadrada de (x2-x1)^2 + (y2-y1)^2
3. Mostrar distancia 


Proceso CalcularDistanciaEntrePuntos
	Definir x1,x2,y1,y2 como Entero;
	Definir distancia como Real;
	Escribir "Dime las coordenadas del punto 1:";
	Leer x1;
	Leer y1;
	Escribir "Dime las coordenadas del punto 2:";
	Leer x2;
	Leer y2;
	distancia <- raiz((x2-x1)^2 + (y2-y1)^2);
	Escribir "Distancia:", distancia;
FinProceso
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada 
y su raíz cúbica.
PSeInt no tiene ninguna función predefinida que permita calcular la raíz cúbica,
¿cómo se puede calcular?

Análisis
Se piden número y se muestra la raíz cuadrada y la cúbica. 
Datos de entrada: numero (entero).
Información de salida: raíz cuadrada, raíz cúbica(real).
Variables: num (entero).

Diseño
1. Leer el número.
2. Calcular raíz cuadrada: tenemos una función
3. Calcular raíz cúbica: es igual que elevar el número a 1/3
4. Mostrar las raíces


Proceso CalcularRaices
	Definir num como Entero;
	Escribir "Dime el número:";
	Leer num;
	Escribir "Raíz cuadrada:", raiz(num);
	Escribir "Raíz cúbica:", num ^ (1/3);
FinProceso 
Dado un número de dos cifras, diseÃ±e un algoritmo que permita obtener el 
número invertido. 

Análisis
Se pide un número de dos cifras y se debe mostrar el número de centenas 
y de unidades
Datos de entrada: el número (entero).
Información de salida: primera cifra, segunda cifra (enteros)
Variables: num, decenas, unidades (entero)

Diseño
1. Leer el número de dos cifras (en estos momentos no podemos determinar que el 
   número es de dos cifras)
2. Calcular decenas: división entera del número entre 10.
3. Calcular unidades: resto de dividir el número entre 10.
4. Mostrar decenas y unidades


Proceso CalcularDecenasUnidades
	Definir num,decenas,unidades como Entero;
	Escribir "Dime un número de dos cifras";
	Leer num;
	decenas <- trunc(num/10);
	unidades <- num % 10;
	Escribir "Primera cifra (decenas): ",decenas;
	Escribir "Segunda cifra (unidades): ",unidades;
FinProceso
Dadas dos variables numÃ©ricas A y B, que el usuario debe teclear, 
se pide realizar un algoritmo que intercambie los valores de ambas variables 
y muestre cuanto valen al final las dos variables.

Análisis
Se piden el valor de dos variables (el tipo puede ser el que queramos). 
Hay que intercambiar los valores de las variables
Datos de entrada: dos números en dos variables (entero).
Información de salida: Las dos variables pero con los datos cambiados (entero)
Variables: a,b (entero).

Diseño
1. Leer los dos números
2. Intercambio los valores. Necesito una variable auxiliar (aux). 
	 Asigno "a" en "aux", "b" en "a" y "aux" en "b"
3. Mostrar "a" y "b"


Proceso IntercambiarVariables
	Definir a,b,aux como Entero;
	Escribir "Introduce valor de la variable A:";
	Leer a;
	Escribir "Introduce valor de la variable B:";
	Leer b;
	aux <- a;
	a <- b;
	b <- aux;
	Escribir "Nuevo valor de A:", a;
	Escribir "Nuevo valor de B:", b;
FinProceso
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados 
por una distancia d. 
El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo 
para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
alcanzará el vehículo más rápido al otro.

Análisis
Hay que saber la velocidad de cada vehículo, y la distancia entre ambos
Hay que calcular el tiempo que tardará el que está detrás (y va más rápido) 
alcanzar al primero.
Datos de entrada: velocidad1, velocidad2 km/h (real) y distancia (real).
Información de salida: Tiempo en minutos (real)
Variables: velocidad1, velocidad2, distancia (real), tiempo (real).

Diseño
1. Leer las dos velocidades y la distancia (no puedo controlar que v1 > v2.
2. Calcular tiempo: (v=s/t), por lo tanto t=s/v. Tiempo = distancia / (v1-v2)
3. El tiempo hay que pasarlo a minútos
4. Mostrar tiempo


Proceso CalcularAdelantamiento
	Definir velocidad1,velocidad2,distancia,tiempo como Real;
	Escribir Sin Saltar "Dime la velocidad del coche 1 (km/h):";
	Leer velocidad1;
	Escribir Sin Saltar "Dime la velocidad del coche 2 (más pequeña)(km/h):";
	Leer velocidad2;
	Escribir Sin Saltar "Dime la distancia entre los coches (km):";
	Leer distancia;
	tiempo <- distancia / (velocidad1 - velocidad2);
	tiempo<- tiempo * 60;
	Escribir "Lo alcanza en ",tiempo, " minutos.";
FinProceso

Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la ciudad B.

Análisis
Tenemos que pedir la hora de salida (hora, minutos y segundos).
Tengo que saber también el tiempo en segundo que ha tardado en llegar. 
Tenemos que calcular la hora de llegada.
Datos de entrada: hora, minutos y segundos de salida (entero), 
segundos que tarda (entero).
Información de salida: hora, minutos y segundos de llegada (enteros)
Variables: horapartida, minpartida, segpartida, segviaje, horallegada, 
           minllegada, segllegada (enteros)

Diseño
1. Leer hora de salida
2. Leer segundos que tarda
3. Convierto la hora de salida a segundos (necesito una variable seginicial)
4 Le sumo los segundos que he tardado(necesito una variable segfinal)
5. Convierto los segundos totales a hora, minuto y segundos
6. Muestro la hora de llegada


Proceso CalcularHoraLlegada
	Definir horapartida, minpartida, segpartida, seginicial, segfinal,segviaje, horallegada, minllegada, segllegada Como Entero;
	Escribir Sin Saltar "Hora de salida:";
	Leer horapartida;
	Escribir Sin Saltar "Minutos de salida:";
	Leer minpartida;
	Escribir Sin Saltar "Segundos de salida:";
	Leer segpartida;
	Escribir Sin Saltar "Tiempo que has tardado en segundos:";
	Leer segviaje;
	Convierto la hora de salida a segundos
	seginicial <- horapartida * 3600 + minpartida*60 + segpartida;
	Le sumo los segundos que he tardado
	segfinal <- seginicial + segviaje;
	Convierto los segundos totales a hora, minúto y segundos
	horallegada <- trunc(segfinal / 3600);
	minllegada <- trunc((segfinal % 3600) / 60);
	segllegada <- (segfinal % 3600) % 60;
	Muestro la hora de llegada
	Escribir "Hora de llegada";
	Escribir horallegada,":",minllegada,":",segllegada;
	
FinProceso


Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

Análisis
Hay que pedir el nombre y los apellidos, y mostrar las iniciales. 
Primer carácter de cada cadena.
Datos de entrada: nombre y apellidos (cadena)
Información de salida: Iniciales (cadena)
Variables: nombre, apellido1, apellido2, inicial (cadena).

Diseño
1. Leer nombre y apellidos
2. Obtener primer carácter de cada cadena
3. Concatenar los caracteres
4. Mostrar iniciales


Proceso Iniciales
	Definir nombre,apellido1,apellido2,inicial como Cadenas;
	Escribir Sin Saltar "Dime tu nombre:";
	Leer nombre;
	Escribir Sin Saltar "Dime tu primer apellido:";
	Leer apellido1;
	Escribir Sin Saltar "Dime tu segundo apellido:";
	Leer apellido2;
	inicial<-subcadena(nombre,0,0);
	inicial<-concatenar(inicial,subcadena(apellido1,0,0));
	inicial<-concatenar(inicial,subcadena(apellido2,0,0));
	inicial<-Mayusculas(inicial);
	Escribir "Las iniciales son: ",inicial;
FinProceso

Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
blanco 0. Imprime el resultado obtenido por el estudiante.

Análisis
Se piden la cantidad de respuestas correctas, incorrectas. Calculamos la nota 5:
 5 puntos por respuesta correcta, -1 por incorrecta.
Datos de entrada:respuesta correctas, incorrectas y en blanco(entero).
Información de salida: puntos (entero)
Variables: correctas, incorrectas, puntos (entero)

Diseño
1. Leer preguntas correctas, incorrectas y en blanco
2. Calcular nota: número de correctas * 5 + número de incorrectas * -1
3. Mostrar puntos


Proceso CalcularPuntos
	Definir correctas, incorrectas, puntos como Enteros;
	Escribir Sin Saltar "Dime cantidad de respuestas correctas:";
	Leer correctas;
	Escribir Sin Saltar "Dime cantidad de respuestas incorrectas:";
	Leer incorrectas;
	puntos <- correctas * 5 + incorrectas * (-1);
	Escribir "Puntos: ",puntos;
FinProceso

 

Proceso Saludar
	Definir nombre Como Cadena;
	Escribir "Dime tu nombre:";
	Leer nombre;
	Escribir "Hola ",nombre;
FinProceso

Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos 
o 10 céntimos).

Análisis
Se piden la cantidad de monedas que tenemos (de 2e, 1e, 50 céntimos, 
20 céntimos o 10 céntimos) y calculamos el dinero que tenemos (euros y céntimos)
Datos de entrada: monedas de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos) (entero).
Información de salida: total de dinero: euros y céntimos (enteros)
Variables: euro2,euro1,cent50,cent20,cent10, total_euros, total_centimos (entero)

Diseño
1. Leer el monedas de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos.
2. Calcular Euros (sumar monedas de 2 euros * 2 + monedas de 1 euro
3. Calcular céntimos 
	monedas de 50c * 50 + monedas de 30c * 30 + moneda de 20c * 20 + moneda de 10c * 10
4. Convertir céntimos a euros (división entera entre 100)
5. Mostrar euros y céntimos totales


Proceso CalcularDinero
	Definir euro2,euro1,cent50,cent20,cent10 como Entero;
	Definir total_euros, total_centimos Como Entero;
	Escribir Sin Saltar "Monedas de 2 euros:";
	Leer euro2;
	Escribir Sin Saltar "Monedas de 1 euro:";
	Leer euro1;
	Escribir Sin Saltar "Monedas de 50 céntimos:";
	Leer cent50;
	Escribir Sin Saltar "Monedas de 20 céntimos:";
	Leer cent20;
	Escribir Sin Saltar "Monedas de 10 céntimos:";
	Leer cent10;
	2. Calular Euros (sumar monedas de 2 euros * 2 + monedas de 1 euro
	total_euros <- euro2 * 2 + euro1;
	3. Calcular centimos (monedas de 50c * 50 + monedas de 30c * 30 + moneda de 20c * 20 `moneda de 10c * 10
	total_centimos <- cent50 * 50 + cent20 * 20 + cent10 * 10;
	4. Convertir céntimos a euros (división entera entre 100)
	total_euros <- total_euros + trunc(total_centimos / 100);
	total_centimos <- total_centimos % 100;
	Escribir total_euros," euros y ",total_centimos," céntimos.";
FinProceso




Proceso Rectangulo
	Definir base,altura,perimetro,area Como Real;
	Escribir "Introduce la base:";
	Leer base;
	Escribir "Introduce la altura:";
	Leer altura;
	perimetro <- 2 * base + 2 * altura;
	area <- base * altura;
	Escribir "El perí­metro es ",perimetro," y el área es ",area;
FinProceso

Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

Análisis
Tenemos que leer la longitud de los dos catetos y calcular la hipotenusa. 
(Teorema de Pitágoras)
Variables de entrada: cateto1(real), cateto2(real)
Variables de salida: hipotenusa(real)

Diseño
 1. Leer la longitud de los catetos
 2. Calcular hipotenusa (En un triángulo rectángulo el cuadrado de la hipotenusa 
 es igual a la suma de los cuadrados de los catetos. )
 Por lo tanto la hipotenusa es igual a la raí­z cuadrada de la suma de los 
 cuadrados de los catetos.
 3. Mostrar la hipotenusa


Proceso CalcularHipotenusa
	Definir cateto1,cateto2,hipotenusa Como Real;
	Escribir "Introduce el cateto 1:";
	Leer cateto1;
	Escribir "Introduce la cateto 2:";
	Leer cateto2;
	hipotenusa <- raiz(cateto1 ^ 2 + cateto2 ^ 2);
	Escribir "La hipotenusa es ",hipotenusa;
FinProceso

Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

Análisis
Tenemos que leer dos números, calcular la suma, resta, multiplicación y división
Datos de entrada: Los dos números (real)
Información de salida: suma, resta, multiplicación, división(real)
Variables: num1, num2 (Real). 
Considero que las salidas no es necesario guardarla en variables.

Diseño
1. Leer los números
2. Mostrar suma,resta, multiplicación y división


Proceso Calcular
	Definir num1,num2 Como Real;
	Escribir Sin Saltar "Introduce el número 1:";
	Leer num1;
	Escribir Sin Saltar "Introduce el número 2:";
	Leer num2;
	Escribir "La suma es ", num1+num2;
	Escribir "La resta es ", num1-num2;
	Escribir "La multiplicación es ", num1*num2;
	Escribir "La división es ", num1/num2;
FinProceso

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados 
Celsius.

Análisis
Tenemos que leer una temperatura en grados Fahrenheit y devolverla en grados 
celsius.
Datos de entrada: grados Fahrenheit (real)
Información de salida: grado Celsius (real)
Variables: fahrenheit, celsius (Real).

Diseño
1. Leer la temperatura en grados Fahrenheit
2. Calcular los grados celsius (C = (F-32)*5/9)
3. Mostrar grados celsius


Proceso CalcularGradosCelsius
	Definir fahrenheit,celsius Como Real;
	Escribir Sin Saltar "Introduce la temperatura ºF::";
	Leer fahrenheit;
	celsius <- (fahrenheit - 32) * 5 / 9;
	Escribir "La temperatura es ",celsius, " ºC.";
FinProceso

Calcular la media de tres números pedidos por teclado

Análisis
Tenemos que leer tres números y calcular la media. Suma de los tres partido 3.
Datos de entrada: los tres números (real)
Información de salida: la media (real)
Variables: num1,num2,num3, media (Real).

Diseño
1. Leer los tres nÃºmeros
2. Calcular la media: (num1+num2+num3)/3
3. Mostrar la media


Proceso CalcularMedia
	Definir num1,num2,num3, media Como Real;
	Escribir Sin Saltar "Introduce el número 1:";
	Leer num1;
	Escribir Sin Saltar "Introduce el número 2:";
	Leer num2;
	Escribir Sin Saltar "Introduce el número 3:";
	Leer num3;
	media <- (num1 + num2 + num3) /3;
	Escribir "La media es ",media;
FinProceso

Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
cuantas horas y minutos corresponde.

Análisis
Tenemos que leer una cantidad de minutos, y calcular cuantas horas y minutos son.
Datos de entrada: minutos (entero)
Información de salida:horas y minutos (entero)
Variables: minutos, res_horas, res_minutos (entero).

Diseño
1. Leer los minutos
2. Calcular a cuantas horas corresponde, división entera entre 60.
3. calcular los minutos restantes: resto de la división entre 60.
4. Mostrar horas y minutos


Proceso CalcularHoras
	Definir minutos, res_horas, res_min como Entero;
	Escribir "Dime la cantidad de minutos:";
	Leer minutos;
	res_horas<-trunc(minutos / 60);
	res_min<-minutos % 60;
	Escribir res_horas," horas y ",res_min," minutos.";
FinProceso

Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
en cuenta su sueldo base y comisiones.

Análisis
El vendedor tiene un sueldo base mas una comisión del 10% por cada venta. 
Hace tres ventas.
Datos de entrada: sueldo base, las tres ventas (real).
Información de salida: comisiones y sueldo total (real).
Variables: sueldo_base, venta1, venta2, venta3, comision(real).

Diseño
1. Leer sueldo base
2. Leer las tres ventas
3. Calcular las comisiones. Suma del 10 % de cada venta.
4. Mostrar comisión
5. Mostrar sueldo total: sueldo_base+comisión


Proceso CalcularSueldo
	Definir sueldo_base, venta1, venta2, venta3, comision como Real;
	Escribir "Dime el sueldo base:";
	Leer sueldo_base;
	Escribir "Dime precio de la venta 1:";
	Leer venta1;
	Escribir "Dime precio de la venta 2:";
	Leer venta2;
	Escribir "Dime precio de la venta 3:";
	Leer venta3;
	comision<-venta1*0.1+venta2*0.1+venta3*0.1;
	Escribir "Comisión por ventas:",comision;
	Escribir "Sueldo total:", sueldo_base+comision;
FinProceso
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto deberá pagar finalmente por su compra.

Análisis
Debemos preguntar cuanto dinero es la compra, calcular el 15% y restarlo al total.
Datos de entrada: precio (real).
Información de salida: precio final (real).
Variables: precio(real).

Diseño
1. Leer el precio
2. Mostrar precio final: precio - 15% del precio


Proceso CalcularPrecio
	Definir precio como Real;
	Escribir "Dime el precio:";
	Leer precio;
	Escribir "Precio final:", precio- precio*0.15;
FinProceso