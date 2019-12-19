---
title: "Entrega 3: Ejercicios diccionarios, ficheros, ..."
permalink: /lmgs/u02/entrega3.html
---

### Ejercicio 1

El Código Cuenta Cliente (CCC) es el código que identifica en España las cuentas corrientes de los clientes de bancos. El CCC tiene 20 dígitos en formato AAAA-BBBB-CC-
DDDDDDDDDD.

* AAAA son cuatro dígitos que identifican la entidad bancaria.
* BBBB son cuatro dígitos que identifican la oficina.
* CC se denomina dígito de control (DC).
* DDDDDDDDDD son 10 dígitos de la cuenta del cliente en el banco.

Según la Wikipedia:
Los dígitos situados en las posiciones novena y décima se generan a partir de los demás dígitos del CCC, permitiendo comprobar la validez del mismo
y reducir la posibilidad de errores de manipulación. El primero de ellos valida conjuntamente los códigos de entidad y de oficina; el segundo, valida el número de cuenta.
Cada uno de los dígitos del DC se calcula utilizando el mismo algoritmo, para lo que se complementa con dos ceros a la izquierda la entidad y oficina.

La siguiente función en Python calcula el DC correspondiente para una lista de 10 número enteros:

	def calcula_dc(lista):
		"""Calcula el dígito de control de una CCC.
		Recibe una lista con 10 numeros enteros y devuelve el DC
		correspondiente"""
		pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
		aux = []
		for i in range(10):
			aux.append(lista[i]*pesos[i])
		resto = 11 - sum(aux) %11
		if resto == 10:
			return 1
		elif resto == 11:
			return 0
		else:
			return resto

Por ejemplo:

	>>> lista = [1, 6, 7, 0, 0, 0, 0, 3, 3, 2]
	>>> calcula_dc(lista)
	5

Escribe un programa que pida al usuario un CCC en el formato arriba indicado y compruebe su validez.

Mejora: Además de decirte si el número de cuenta es válido, te tiene que mostrar el nombre de la identidad bancaria que leerá del fichero [bancos.txt](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u3/doc/bancos.txt). 

### Ejercicio 2

Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:

* El nombre de usuario y las contraseñas se almacenan en el fichero `/etc/shadow`, al que tiene acceso sólo el usuario root.
* Las contraseñas se almacenan como un hash AES512 con sal

Ayuda:

Supongamos que tenemos en nuestro sistema el usuario `prueba` con contraseña `asdasd`, una línea correspondiente a este usuario en el fichero `/etc/shadow` sería:

	prueba:$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxulWX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.:15059:0:99999:7::::

* La sal de una contraseña cifrada se indica en linux por los 20 primeros caracteres del hash de la contraseña, en el caso anterior la sal sería **$6$aiozD6dU.MJeURsH$**.
* La función `crypt` del módulo `crypt` permite formar los hashes con sal utilizados por linux, de la siguiente manera:

    ```python
    >>> from crypt import crypt
	>>> crypt("asdasd","$6$aiozD6dU.MJeURsH$")
	'$6$aiozD6dU.MJeURsH$g.syV5NgBk7VqWiekTbhwZsfJwDNuujx76P.bUBUMoKpTVVCXAQ84JlQVdd85fPyIO5fYiJjd2DJObWNu.o/R0'

    ```

donde `asdasd` es la contraseña en claro.

Escribe un programa que lea un usuario y una contraseña, y te informe si el usuario es válido o no.

### Ejercicio 3

Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando los ficheros que puedes encontrar en el [repositorio](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

### Ejercicio 4

Utilizando el fichero [notas.csv](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u3/doc/notas.csv), realiza un programa en python que lea los datos de ese fichero y construya la siguiente estructura: 

    alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
                {"nombre":"Rafaela", ... },...]

Crea un programa que muestre un menú y puedas elegir una de estas opciones:
    
* Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para realizar el cálculo de la nota media.
* Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
* Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
* Pide un curso, y crea un fichero *nombredelcurso*.txt con los alumnos y la nota media.

### Ejercicio 5

Descarga el fichero [zips.json](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u3/doc/zips.json) del sitio de mongodb. Se trata de un listado de los códigos postales de EEUU en formato JSON (lo que Python denomina diccionarios y listas). Realiza los siguientes ejercicios

* Cuenta el número de códigos postales que aparecen
* Cuenta el número de códigos postales de cada estado
* Obtén la URL del mapa de OpenStreetMap de la ciudad de "Akaska" en el estado de Dakota del Sur (SD). Nota: Las coordenadas que aparecen en el fichero zips.json vienen en formato [longitud,latitud] y la url genérica que utiliza OpenStreetMap es:

        http://www.openstreetmap.org/#map=zoom/latitud/longitud

Por ejemplo:

[http://www.openstreetmap.org/#map=19/37.27058/-5.91958](http://www.openstreetmap.org/#map=19/37.27058/-5.91958) para ver con un zoom de nivel 19 la ubicación con latitud 37.27058 y longitud -5.91958

Modifica el programa anterior para que ahora se pida por teclado la ciudad y el estado que se quiere localizar en OpenStreetMap. El programa te pide una ciudad, si existe te devuelve la URL.

### Ejercicio 6

[Web scraping](https://es.wikipedia.org/wiki/Web_scraping) es una técnica utilizada mediante programas de software para extraer información de sitios web. Por ejemplo, con el siguiente código podemos leer el HTML de una página web.

    from urllib.request import urlopen
    response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
    lineas=response.readlines()

En el ejemplo anterior, la página nos da información meteorológica de Dos Hermanas. Haz un programa que te muestre la temperatura, presión y humedad actual de Dos Hermanas.

### Ejercicio 7

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
