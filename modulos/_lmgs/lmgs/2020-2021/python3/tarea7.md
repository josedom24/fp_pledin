---
permalink: /lmgs/2020-2021/python3/tarea7.html
layout: single3
---

# Ejercicios

## Ejercicio 1

Queremos guardar el nombre de los artículos de un almacén y sus precios. Como estructura de datos vamos a usar dos listas: artículos, donde vamos a guardar el nombre de los artículos y precios donde vamos a guardar los precios. De tal forma que el artículo en la posición n de la lista artículos tendrá el precio correspondiente a la misma posición en la lista precios.

Realiza un programa que pida por teclado artículos y sus precios (el programa pedirá cuantos artículos se van a introducir), al finalizar dará la siguiente información:

* El precio medio de los artículos.
* El nombre de los artículos que valen más de 100 euros.
* Nos pedirá un nombre de un artículo y si existe nos dará su precio, sino nos dará un error.

## Ejercicio 2

Repite el ejercicio 1 con la siguiente estructura de datos: vamos a usar una lista artículos donde vamos a guardar listas con dos elementos: el nombre del artículo y su precio. Ejemplo:

    articulos=[["fregona",12],["cepillo",14],["recogerdor",23]]


## Ejercicio 3

Queremos hacer un programa que trabaje con las notas de los alumnos de una clase:

* El programa pedirá cuantos alumnos tiene la clase.
* A continuación, pedirá el nombre del alumno, y cuantas notas tiene ese alumno.
* Se pedirán las notas del alumno introducido (cada alumno puede tener una cantidad de notas distintas). Las notas se validarán para que sea un número del 1 al 10).

Piensa en el estructura de datos donde vas a guardar la información.
Al finalizar el programa nos mostrará el siguiente menu:

1. Notas medias: Nos muestra una lista de alumnos y su nota media. Si su nota media es aprobado aparecerá la palabra "APROBADO" en la línea del alumno.
2. Buscar por nombre: Nos pide una cadena y nos muestra todos los alumnos que **comienzan por dicha cadena y la lista de sus notas.
3. Añadir alumno: No pide el nombre de un alumno, cuántas notas tienes y pide las notas.
4. Eliminar alumno: Nos pide un nombre y elimina el primer alumno que encuentre con ese nombre.
5. Salir

## Ejercicio 4

Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

* Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos. Ejemplo: equipos = [["Sevilla","Betis"],["Madrid","Barcelona"],...]
* Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo. Ejemplo: resultados=[[3,0],[0,0],...]

El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

## Ejercicio 5

Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:

* El nombre de usuario y las contraseñas se almacenan en el fichero `/etc/shadow`, al que tiene acceso sólo el usuario root.
* Las contraseñas se almacenan como un hash AES512 con sal

Ayuda:

Supongamos que tenemos en nuestro sistema el usuario `prueba` con contraseña `asdasd`, una línea correspondiente a este usuario en el fichero `/etc/shadow` sería:

	prueba:$y$j9T$bU9gdaTeFdFmE.H6YFABA/$a6tYG9jDZRNbkVaLW48AGbPw9ryIuHsG7PnaiWQmZb5:18977:0:99999:7:::

* La sal de una contraseña cifrada (en debian 11) se indica en linux por los **30** primeros caracteres del hash de la contraseña, en el caso anterior la sal sería **`$y$j9T$bU9gdaTeFdFmE.H6YFABA/$`**.
* La función `crypt` del módulo `crypt` permite formar los hashes con sal utilizados por linux, de la siguiente manera:

    ```python
    >>> from crypt import crypt
	>>> crypt("asdasd","$y$j9T$bU9gdaTeFdFmE.H6YFABA/$")
	'$y$j9T$bU9gdaTeFdFmE.H6YFABA/$a6tYG9jDZRNbkVaLW48AGbPw9ryIuHsG7PnaiWQmZb5'
    ```

donde `asdasd` es la contraseña en claro.

Escribe un programa que lea un usuario y una contraseña, y te informe si el usuario es válido o no.

## Ejercicio 6

Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando los ficheros que puedes encontrar en el [repositorio](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

## Ejercicio 7

Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado. La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles.

	Por ejemplo:

		Cantidad total: 7,17 €
		Cantidad entregada: 100 €
		Cantidad a devolver: 92,83 €

		1  billete de 50 €
		2 billete de 20 €
		1 monedas de 2 €
		1 monda de 50 c
		1 moneda de 20 c
		1 moneda de 10 c
		1 moneda de 2 c
		1 moneda 1 c
