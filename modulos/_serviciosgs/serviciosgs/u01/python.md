---
title: Python para sysadmins
---

Para automatizar muchas de las tareas que realizan los administrador de sistemas es necesario crear scripts. Éstos se pueden crear en distintos lenguajes de programación, por ejemplo bash. En este apartado vamos a introducir las posibilidades que nos ofrece python para crear script de administración.

```eval_rst
.. note:: 

	Si quieres más información puedes consultar la página  `Python for system administrators <http://www.ibm.com/developerworks/aix/library/au-python>`_.
```

## Resumen de instrucciones

Veamos algunas instrucciones que nos pueden ayudar en nuestrs scripts de administración:

* **Trabajar con argumentos en la línea de comandos**: La mayoría de los script que realicemos recibiran la entrada por argumentos de la línea de comandos:
	
	```python
	import sys
	len (sys.argv) #Número de argumentos
	sys.argv[1] #Acceso al segundo argumento
	```

* **Salir del programa**: Nos puede interesar que el programa termine baja alguna circunstancia:

	```python
	import sys
	sys.exit(0)
	```

* **La libreía os te permite acceder del sistema operativo**: Esta librería es muy importante para realizar scripts de administración, veamos algunos ejemplos:

	```python
	import os
	print os.getcwd() #Devuelve el directorio donde estás trabajando
	os.chdir("Descargas") #Cambia de directorio
	os.system("clear") #Ejecuta una instrucción pero no podemos obtener el resultado
	```

* **Ejecutar una instrucción y obtener el resultado**: Tenemos tres posibilidades:

	```python
	#Utilizando la librería commands
	import commands
	data = commands.getoutput("ls -l")
	type(data)
	lineas=data.split("\n")

	#Otra manera, pero poco "elegante"
	os.system("ls -l>tmp.txt")
	f=open("tmp.txt","r")

	#Ejecutar la instrucción como si fuera un fichero
	f=popen("ls -l","r")
	```

## Ejercicios

Realiza un script en python que realice la siguiente función:

1. Muestra el directorio de trabajo.
2. Muestra cuantos usuarios hay definido en el sistema
3. Muestra los usuarios conectados al equipo.
4. Script que lea el nombre de un usuario, si existe dice si es administrador o no, si no existe da un mensaje de error. Realiza el script leyendo el usuario por teclado, y realiza otra versión indicándolo como parámetro.
5. Pasa por parámetros una dirección ip y un nombre de máquina e inserta en ``/etc/hosts`` (en la tercera línea) la resolución estática. Si no se introducen dos parámetros se da un error.
6. Para crear un usuario "a mano":

    * Editar ``/etc/passwd`` y agregar una nueva linea por cada nueva cuenta. Teniendo cuidado con la sintaxis. Debería hacer que el campo de la contraseña sea '*', de esta forma es imposible ingresar al sistema.
    * De forma similar, edite ``/etc/group`` para crear también un grupo.
    * Crea el directorio Inicio del usuario con el comando *mkdir*.
    * Copia los archivos de ``/etc/skel`` al nuevo directorio creado 
    * Corrige la pertenencia del dueño y permisos con los comandos *chown* y *chmod* (Ver paginas de manual de los respectivos comandos). La opción ``-R`` es muy útil. Los permisos correctos varían un poco de un sitio a otro, pero generalmente los siguientes comandos harán lo correcto:

	```bash
	cd /home/nuevo-nombre-de-usuario
	chown -R nombre-de-usuario:group .
	chmod -R 755 .
	```
    * Asigne una contraseña con el comando *passwd*
    * Crea un script python que cree un usuario, para ello debe recibir el nombre de usuario y nombre completo por parámetros, por defecto se pone uid y gid a 2000. Mejorar el programa para que:
    * Da un error si se intenta dar de alta un usuario que ya existe
    * Al ir dando de alta a distintos usuarios vaya incrementando automáticamente el uid y el gid a partir de 2000