---
title: "Entrega 1: Ejercicios alternativas y repetitivas"
permalink: /lmgs/u02/entrega1.html
---

1. Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.

	```bash
	DIVISOR DE NÚMEROS
	Escriba el dividendo: 14
	Escriba el divisor: 5
	La división no es exacta. Cociente: 2 Resto: 4	
	```	

	```bash
	DIVISOR DE NÚMEROS
	Escriba el dividendo: 20
	Escriba el divisor: 4
	La división es exacta. Cociente: 5
	```

2. Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2020
	Para llegar al año 2020 faltan 5 años.
	```
	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 1997
	Desde el año 1997 han pasado 18 años.
	```
	```bash
	COMPARADOR DE AÑOS
	¿En qué año estamos?: 2015
	Escriba un año cualquiera: 2015
	¡Son el mismo año!
    ```

3. Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

	Notas:

	* Un número es divisible por otro cuando el resto de su división es cero (``numero % divisor == 0``).
    * Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores (o iguales) que la mitad del número. Es decir, no hace falta probar todos los números entre 1 y el propio número, sino únicamente hasta la mitad. Si se hace así, no hay que olvidarse de añadir el propio número a la lista de divisores.

	```bash
	DIVISORES
	Escriba un número mayor que cero: -5
	¡Le he pedido un número entero mayor que cero!
	```

	```bash
	DIVISORES
	Escriba un número entero mayor que cero: 200
	Los divisores de 200 son 1 2 4 5 8 10 20 25 40 50 100 200
	```

4. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

	```bash
	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? -1
	¡Imposible!
	```
	
	```bash
	MAYORES QUE EL PRIMERO
	¿Cuántos valores va a introducir? 4
	Escriba un número: 6
	Escriba un número más grande que 6: 10
	Escriba un número más grande que 6: 3
	¡3 no es mayor que 6!
	Escriba un número más grande que 6: 9
	Gracias por su colaboración
	```

5.

**Apartado 1**

Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.

Para generar números al azar puedes utilizar el siguiente código:

    from random import randint
    a = randint(2, 10)

Ejemplos:    

    ¿Cuánto es 7 x 8? 56
    ¡Respuesta correcta!
    
    ¿Cuánto es 4 x 9? 35
    ¡Respuesta incorrecta!


**Apartado 2**

Amplie el programa anterior haciendo que el programa pida primero al usuario cuántas multiplicaciones se van a plantear.

	
	Número de preguntas: 0
	El número de preguntas debe ser al menos 1	
	
	Número de preguntas: 2	
	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!
	```

**Apartado 3**

Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado.
Ayuda: La nota se calcula con la fórmula Nota=Correctas / Total * 10.

	Número de preguntas: 2	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 5.0	

	
	Número de preguntas: 3	

	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	
	¿Cuánto es 4 x 9? 35
	¡Respuesta incorrecta!	
	¿Cuánto es 2 x 3? 6
	¡Respuesta correcta!	

	Ha contestado correctamente 2 preguntas
	Le corresponde una nota de 6.7	

	Número de preguntas: 1	
	¿Cuánto es 7 x 8? 56
	¡Respuesta correcta!	

	Ha contestado correctamente 1 pregunta
	Le corresponde una nota de 10.0
	¡Enhorabuena!


NOTA: **Tienes que entregar sólo el código del apartado 3.**