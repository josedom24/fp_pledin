---
permalink: /lmgs/2020-2021/python3/contadores_acumuladores_indicadores.html
layout: single3
---

# Uso específico de variables: contadores, acumuladores e indicadores

<iframe width="560" height="315" src="https://www.youtube.com/embed/R0eJ-zNsRf0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Contadores

Un contador es una variable entera que la utilizamos para contar cuando ocurre un suceso. Un contador:

* Se **inicializa** a un valor inicial.

		cont = 0;

* Se **incrementa**, cuando ocurre el suceso que estamos contado se le suma 1.

		cont = cont + 1;

* Otra forma de incrementar el contador:

        cont += 1


### Ejemplo

Introducir 5 número y contar los números pares.


	cont = 0;
	for var in range(1,6):
		num = int(input("Dime un número:"))
		if num % 2 == 0:
			cont = cont + 1
	print("Has introducido ",cont," números pares.")

## Acumuladores

Un acumulador es una variable numérica que permite ir acumulando operaciones. Me permite ir haciendo operaciones parciales. Un acumulador:

* Se **inicializa** a un valor inicial según la operación que se va a acumular: a 0 si es una suma o a 1 si es un producto.
* Se **acumula** un valor intermedio.
		
		acum  =  acum + num;

### Ejemplo

Introducir 5 número y sumar los números pares.

	suma = 0;
	for var in range(1,6):
		num = int(input("Dime un número:"))
		if num % 2 == 0:
			suma = suma + num
	print("La suma de los números pares es ",suma)

## Indicadores

Un indicador es una variable lógica, que usamos para recordar o indicar algún suceso. Un indicador:

* Se **inicializa** a un valor lógico que indica que el suceso no ha ocurrido.

	indicador = False

* Cuando ocurre el suceso que queremos recordar cambiamos su valor.

	indicador = True

### Ejemplo

Introducir 5 número e indicar si se ha introducido algún número par.

	indicador  =  False;
	for var in range(1,6):
		num = int(input("Dime un número:"))
		if num % 2 == 0:
			indicador  = True
	if indicador:
		print("Has introducido algún número par")
	else:
		print("No has introducido algún número par")
	