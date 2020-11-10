---
permalink: /lmgs/2020-2021/python3/validacion_datos_entrada.html
layout: single3
---

# Validación de datos de entrada

El objetivo de la validación de los datos de entrada es comprobar y asegurarnos que el dato que estamos leyendo cumple una condición que nos asegura que es válido.

A la lectura de un dato, le vamos a añadir un bucle while que no asegura que el dato va a ser válido. En leguja natural sería algo parecido a esto:

	Leer Dato
	Mientras Dato se incorrecto:
		Escribir "Error en el dato"
		Leer Dato

Por ejemplo, leer un número positivo, sería:

	num = int(input("Dime un número:"))
	while num<=0:
		print("El número debe ser positivo.")
		num = int(input("Dime un número:"))

Cuando salimos del bucle, podemos estar seguro de que el número es positivo.

Otro ejemplo, leer dos números y aseguraRnos que el primero es menor o igual que el segundo:

	num1 = int(input("Dime el número 1:"))
	num2 = int(input("Dime el número 2:"))
	while num1>num2:
		print("El número 1 debe ser menor o igual que el número 2.")
		num1 = int(input("Dime el número 1:"))
		num2 = int(input("Dime el número 2:"))

