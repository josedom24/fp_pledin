---
title: "Solución Boletín 2: Ejercicios listas"
permalink: /lmgs/u02/resuelto2.html
---

1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.

		num=int(input("Número:"))
		lista=[]
		while num>0:
			lista.append(num)
			num=int(input("Número:"))		

		print(max(lista))
		for n in lista:
			if n % 2 ==0:
				print(n)

2. Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

		num=int(input("Número de palabras:"))
		lista=[]
		for i in range(1,num+1):
			lista.append(input("Palabra:"))
			
		print(lista)

3. Dada una lista de números enteros (guarda la lista en una variable) y un entero *k*, escribir un programa que:

	* Cree tres listas listas, una con los menores, otra con los mayores y otra con los iguales a *k*.
	* Crea otra lista lista con aquellos que son múltiplos de *k*.

			lista=[2,4,6,1,3,4,5,7,8]
			k=4
			lmenor=[]
			ligual=[]
			lmayor=[]
			lmultiplo=[]
			for num in lista:
				if num<k:
					lmenor.append(num)
				if num>k:
					lmayor.append(num)
				if num==k:
					ligual.append(num)
				if num%k==0:
					lmultiplo.append(num)
			print(lmayor)
			print(lmenor)
			print(ligual)
			print(lmultiplo)

4. Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

		lista=['Di', 'buen', 'dia', 'a', 'papa']
		print(lista[::-1])

5. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

		palabra=input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=input("Palabra:")		

		buscar=input("Palabra a buscar:")
		print("La he encontrado %d veces"% lista.count(buscar))

6. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.

		palabra=input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=input("Palabra:")		

		buscar=input("Palabra a buscar:")
		sustituir=input("Palabra a sustituir:")		

		cont=0
		for cad in lista:
			if cad==buscar:
				lista[cont]=sustituir
			cont=cont+1		

		print(lista)

7. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

		palabra=input("Palabra:")
		lista=[]
		while palabra != " ":
			lista.append(palabra)
			palabra=input("Palabra:")		

		eliminar=input("Palabra a eliminar:")		

		while eliminar in lista:
			lista.remove(eliminar)		

		print(lista)

8. Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

		palabra=input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=input("Palabra lista 1:")		

		palabra=input("Palabra lista 2:")
		lista2=[]
		while palabra != " ":
			lista2.append(palabra)
			palabra=input("Palabra lista 2:")		

		for cad in lista2:
			while cad in lista1:
				lista1.remove(cad)		

		print(lista1)

9. Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

		palabra=input("Palabra lista 1:")
		lista1=[]
		while palabra != " ":
			lista1.append(palabra)
			palabra=input("Palabra lista 1:")		

		lista2=[]
		for cad in lista1:
			if not cad in lista2:
				lista2.append(cad)
		lista1=lista2[:]
		print(lista1)

10. Escribir una función que reciba una lista de elementos e indique si se encuentran ordenados de menor a mayor o no.

		num=int(input("Número:"))
		lista=[]
		while num>0:
			lista.append(num)
			num=int(input("Número:"))
		lista2=lista[:]
		lista.sort()
		if lista==lista2:
			print("Ordenada")
		else:
			print("No ordenada")