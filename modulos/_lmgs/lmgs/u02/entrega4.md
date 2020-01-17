---
title: "Entrega 4: Ejercicios con funciones"
permalink: /lmgs/u02/entrega4.html
---
Necesitamos que se facture el uso de un teléfono. Nos informarán de la tarifa por segundo (en céntimos), cuántas comunicaciones se realizaron, la duración de cada comunicación expresada en horas, minutos y segundos. Como resultado deberemos informar la duración en segundos de cada comunicación y su costo.

Vamos a dividir este problemas en problemas más pequeños:

* Cada comunicación se expresa en horas, minutos y segundos, la tarifa es centimos por segundos, por lo tanto lo primero que vamos a solucionar es convertir las horas, minutos y segundos en segundos. Para ello vamos a crear una función llamada **pasar_a_segundos**. Piensa los parámetros de entrada que tiene esta función y el valor que devuelve. ¿De qué tipo son?
* Una vez que sabemos los segundos que ha tardado una comunicación y la tarifa por segundos vamos a crear una función llamada **calcular_coste** que nos calcule cuanto cuesta, en céntimos, la llamada. Piensa los parámetros y el valor devuelto de la función.
* Por último vamos a crear una función para convertir el coste en céntimos, en una cantidad de dinero expresada en euros y céntimos. Para ello creamos la función **convertir_a_euros**. Piensa los parámetros de entrada y los valores devueltos.

## Ejercicios

1. Crea un programa que te pregunte por teclado la tarifa por segundos en céntimos, el número de comunicaciones que se han realizado, y te vaya pidiendo horas, minutos y segundo que han durado cada una de las comunicaciones. Finalmente te mostrará cuanto ha costado cada una de las comunicaciones y el total de dinero de todas las comunicaciones.

2. Realiza un programa que te informe de cuanto vale cada comunicación y el total de dinero de todas las comunicaciones. En esta ocasión los datos de la duración de las comunicaciones y la tarifa por segundos se encuentran en este [fichero](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u3/comunicaciones.txt) donde en la primera línea te encuentras la tarifa, y en las restantes la duración de cada una de las comunicaciones expresadas en horas, minutos y segundos.

