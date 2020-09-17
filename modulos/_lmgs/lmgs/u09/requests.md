---
title: "Ejercicios librería requests"
permalink: /lmgs/u09/requests.html
---

Realiza programas en python que utilizando la librería `requests`, realicen las siguientes acciones.

1. Programa que muestre el nombre de los proyectos públicos de la aplicación redmine de nuestro ciclo. Utiliza la respuesta XML.

2. Programa que muestre el nombre de los proyectos de la aplicación redmine de nuestro ciclo. Para ello necesitas autentificarte con la API key. Utiliza la respuesta XML. 

	Si queremos subir este programa a github, debería buscar algún mecanismo para no guardar nuestra **key** en el repositorio público de github. Tenemos dos soluciones:

	* **Usar un fichero de configuración**:

	Guardamos la key en un fichero de configuración (por ejemplo que llamamos key.cfg) que nunca subimos a github (el nombre de este fichero se guarda en un fichero .gitignore). En nuestro programa podemos utilizar un código de esta forma:

		with open("key.cfg", "r") as archivo: 
			key = archivo.read() 

	* **Usar variables de entorno**:

	Guardamos la key en una variable de entorno del sistema operativo y la leemos en el programa. Para crear la clave:

		export key="466f4055fe2f206676793d544b06ddee64b45432"

	Y desde el programa python:

		import os
		...
		key=os.environ['key']

3. Realiza el ejercicio 2, pero utilizando la respuesta JSON.

4. Programa que pida el nombre de un proyecto del redmine de nuestro ciclo y que muestre las 5 últimas tareas abiertas del proyecto indicado. Si no existe el proyecto da un error.

5. Crear un programa que utilizando la API de openwheathermap pida el nombre de una ciudad por teclado y muestre su temperatura actual.	

6. Programa que utilizando la API swapi muestre la lista de personajes, cada vez que muestre la información de una página preguntará si quiere seguir mostrando más personajes. A continuación pedirá el nombre de un personaje y te dará información sobre él.

7. Programa que cree un proyecto, llamado "test project" en el redmine de nuestro ciclo.

8. Programa que borre el proyecto creado en el ejercicio anterior.

9. Realizar un programa que te pida el nombre de un proyecto de nuestro Redmine y muestre las 5 últimas tareas y sus descripciones.

