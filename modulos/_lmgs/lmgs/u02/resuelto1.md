---
title: "Solución Boletín 1: Ejercicios fáciles"
permalink: /lmgs/u02/resuleto1.html
---

1. Calcular el perímetro y área de un círculo dado su radio.

		import math
		radio=float(input("Dime el radio:"))
		print("Resultado: Area=%.2f Perimetro=%.2f" % (math.pi*radio**2,2*math.pi*radio))		

2. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.

		palabra=input("Dime una palabra:")
		print((palabra+" ")*1000)

3. Escribir un programa que le pregunte al usuario una cantidad de euros, una tasa de interés y un número de años y muestre como resultado la cantidad final a pagar. La fórmula a utilizar es:

		Cn = C * (1 + x/100) ^ n

	Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

		cant=float(input("Euros:"))
		interes=float(input("Interes:"))
		year=int(input("Years:"))
		a_pagar=cant*(1+interes/100)**year
		print("A pagar %.2f euros." % a_pagar)


4. Realiza un programa que pida una nota numéricas enteras e imprima sus equivalentes en texto (0-2 => MD, 3-4 => I, 5 => Suf, 6 => B, 7-8 => Not, 9-10 => Sob, otro => Error)

		nota=int(input("Nota:"))		

		if nota>=0 and nota<=2:
			print("MD")
		elif nota==3 or nota==4:
			print("I")
		elif nota==5:
			print("Suf")
		elif nota==6:
			print("B")
		elif nota==7 or nota==8:
			print("Not")
		elif nota==9 or nota==10:
			print("Sob")
		else:
			print("Error")


5. Escribe un programa que lea una lista de diez números y determine cuántos son positivos, y cuántos son negativos.

		cont_pos=0
		cont_neg=0;
		for cont in range(1,11):
			num=int(input("Número:"))
			if num>=0:
				cont_pos=cont_pos+1
			else:
				cont_neg=cont_neg+1
		print("%d positivos,%d negativos"%(cont_pos,cont_neg))   