---
title: "Boletín 4: Ejercicios de funciones"
permalink: /lmgs/u02/boletin4.html
---

**Te recuero que tienes un boletín de ejercicios de funciones resueltos es esta [página](https://gitlab.com/josedom24/curso_programacion_python3/tree/master/curso/u37).**
{: .notice--warning}

1. Escribir dos funciones que permitan calcular:

    * La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    * La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

2. Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:

    * Si recibe un argumento, supone que son segundos y convierte a horas, mintos y segundos.
    * Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

3. Queremos hacer una función que añada a una lista los contactos de una agenda. Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, aunque puede tener más campos. Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar. Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el `*`. 

4. Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista.

5. Vamos a crear un programa que lea los resultados de los partidos de la liga española en el año 2016-2017, y nos devuelva información sobre estos datos.

    El programa leerá la información del siguiente [fichero](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u3/liga.csv), que tiene la siguiente estructura: Fecha, Equipo que juega en casa, Equipo que juega fuera, resultado al final del partido y resultado en el intermedio.

    El programa ofrecerá un menú, para seleccionar la información deseada:

    1. **Estadística de un equipo**: Nos pide por teclado el nombre de un equipo y nos muestra el número de goles que ha metido, los paridos ganados, perdidos y empatados.
    2. **Nombres de equipos**: Nos muestra la lista de equipos que juegan.
    3. **Clasificación de la liga**: Nos muestra los tres primeros equipos de la liga.
    4. **Quiniela por fecha**: Introducimos una fecha y nos dice los resultados de la quiniela de ese día.
    5. **Salir**

    Para realizar este programa podemos realizar las siguientes funciones:

    * `menu()`: Muestra el menú y devuelve un entero con la opción escogida.
    * `LeerPartidos()`: Función que lee el fichero y devuelve una lista con los partidos (cada partido se va a guardar en un diccionario).
    * `SumarGoles(equipo)`: Función que recibe un nombre de un equipo y devuelve el total de goles metidos.
    * `InfoEquipos(equipo)`: Función que recibe un nombre de un equipo y devuelve una  lista con los paridos ganados, perdidos y empatados.
    * `Equipos()`: Función que devuelve una lista con todos los equipos.
    * `Quiniela(dia,mes,año)`: Función que recibe el día, el mes y el año. Y devuelve una lista con los partidos y resultados de la quiniela.

