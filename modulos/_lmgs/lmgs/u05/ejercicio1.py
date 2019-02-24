import json

def contar_libros(doc):
	return len(doc["bookstore"]["book"])

def seleccionar_por_precios(doc,pmax,pmin):
	libros=[]
	for libro in doc["bookstore"]["book"]:
		precio=float(libro["price"])
		if precio<=pmax and precio>=pmin:
			libros.append(libro["title"]["__text"])
	return libros

def seleccionar_por_titulo(doc,titulo):
	libros=[]
	for libro in doc["bookstore"]["book"]:
		if libro["title"]["__text"].startswith(titulo):
			libros.append((libro["title"]["__text"],libro["year"]))
	return libros	

def seleccionar_autores(doc):
	libros=[]
	for libro in doc["bookstore"]["book"]:
		autores=[]
		if isinstance(libro["author"],list):
			for autor in libro["author"]:
				autores.append(autor)
		else:
			autores.append(libro["author"])
		libros.append((libro["title"]["__text"],autores))
	return libros

########################

with open("ej1.json") as fichero:
	doc=json.load(fichero)


# Ejercicio 1
print(contar_libros(doc))

# Ejercicio 2
precio_max=float(input("Precio máximo:"))
precio_min=float(input("Precio mínimo:"))
for libro in seleccionar_por_precios(doc,precio_max,precio_min):
	print(libro)

#Ejercicio 3
cadena=input("Dime el nombre del libro:")
for titulo,año in seleccionar_por_titulo(doc,cadena):
	print(año,titulo)

# Ejercicio 4
for titulo,autores in seleccionar_autores(doc):
	print(titulo)
	for autor in autores:
		print(autor)	
	print("")

