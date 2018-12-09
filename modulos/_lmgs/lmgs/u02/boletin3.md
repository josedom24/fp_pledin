---
title: "Boletín 3: Ejercicios variados"
permalink: /lmgs/u02/boletin3.html
---

1. Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

	* Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos. Ejemplo: 
	``equipos = [["Sevilla","Betis"],["Madrid","Barcelona"],...]``
	* Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo. Ejemplo: 
	``resultados=[[3,0],[0,0],...]``

	El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

2. La letra del DNI se calcula a partir de su número. Para ello se divide el número entre 23 y el resto (que tiene que ser un número entre 0 y 22 se sustituye por la letra
correspondiente de la siguiente tabla:

		0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		T R W A G M Y F P D X  B  N  J  Z  S  Q  V  H  L  C  K  E

	Escribe un programa que te pida un número de DNI y una letra y te diga si es correcto o no.

3. El módulo `random` incluye la función `random()` que genera un número seudo-aleatorio entre 0 y 1:
	
		>>> from random import random
		>>> random()
		0.51605767814317494

	Crea un programa que pida al usuario un número n y genere una lista con n elementos con valores aleatorios y muestre como salida:

	* La lista de los n números aleatorios con una precisión de 3 decimales.
	* La suma de todos los elementos con una precisión de 2 decimales.

	Nota: Los valores deben redondearse a la precisión solicitada, no truncarse.

	Ejemplo

		Dame un numero: 4
		La lista de 4 numeros aleatorios es: (0.123, 0.432, 0.335, 0.456)
		La suma de estos 4 elementos es: 1.3

4. Escribe un programa que pida al usuario su fecha de nacimiento y le responda el día de la semana correspondiente (para ello debes utilizar la función adecuada del módulo calendar). Ejemplo:

	Ejemplo

		Introduce tu fecha de nacimiento (DD-MM-YYYY): 29-02-1992
		Naciste en sabado

5. Una dirección 6to4 es una dirección IPv6 reservada para equipos que tienen actualmente una dirección IPv4 pública. Un ejemplo de dirección 6to4 sería:

		2002:503b:198:0:219:66ff:fea8:db3

	El campo 2002: es fijo y el bloque importante para esta discusión es el que determina la parte de red de la dirección, es decir, los campos `503b:198` que son la representación hexadecimal de la dirección IPv4 correspondiente:

		80.59.1.152 = 0x50.0x3b.0x1.0x98 = 503b:198

	el resto de campos se corresponden con la dirección de subred y la dirección de host, y no son relevantes para este ejercicio.

	Escribe un programa que pida una dirección IPv4 pública y nos dé la parte de red correspondiente de la dirección 6to4 asociada:

	Ejemplo:

		Dame una dirección IPv4 publica: 85.135.34.12
		La parte de red 6to4 correspondiente es: 2002:5587:220

