from lxml import etree

### Ejercicio 1
def lista_provincias(arbol):
	nombres = arbol.xpath('//nombre/text()')	
	return nombres

### Ejercicio 2
def lista_poblaciones(arbol):
	nombres = arbol.xpath('//localidad/text()')
	return nombres

### Ejercicio 3
def lista_provincias_total_poblaciones(arbol):
	lista=[]
	nombres = arbol.xpath('//nombre/text()')
	for provincia in arbol.xpath('//provincia'):
		localidades=provincia.xpath('count(./localidades/localidad)')	
		lista.append(int(localidades))
	return zip(nombres,lista)

### Ejercicio 4
def poblaciones(prov,arbol):
	nombres = arbol.xpath('/lista/provincia[nombre="%s"]//localidad/text()'%prov)
	return nombres



### Ejercicio 5
def provincia(nombre_localidad,arbol):
	localidades=arbol.xpath('//localidades[localidad="%s"]/../nombre/text()'%nombre_localidad)
	return localidades[0]

### Ejercicio 6
def provincias_por_identificador(lista_id,arbol):
	lista=[]
	for id in lista_id:
		provincia=arbol.xpath('//provincia[@id="%s"]/nombre/text()'%id)
		lista_localidades=arbol.xpath('//provincia[@id="%s"]/localidades/localidad/text()'%id)
		lista.append((nombre[0],lista_localidades))
	return lista

### Ejercicio 7
def localidades_grandes(prov,arbol):
	localidades= arbol.xpath('/lista/provincia[nombre="%s"]//localidad[@c="1"]/text()'%prov)
	return(localidades)

### Ejercicio 8
def localidad_grande(nombre_localidad,arbol):
	localidades= arbol.xpath('/lista/provincia/localidades/localidad[text()="%s" and @c="1"]/text()'%nombre_localidad)
	if len(localidades)>0:
		return arbol.xpath('//localidades[localidad="%s"]/../nombre/text()'%nombre_localidad)[0]
	return None

# Creamos el objeto arbol desde el fichero XML
# Este objeto es de tipo ElementTree
arbol = etree.parse('provinciasypoblaciones.xml')


#Ejercicio 1
for nombre in lista_provincias(arbol):
	print (nombre)


##Ejercicio 2
for nombre in lista_poblaciones(arbol):
	print (nombre)

## Ejercicio 3
for nombre ,total in lista_provincias_total_poblaciones(arbol):
	print (nombre,total)

## Ejercicio 4
for nombre in poblaciones("Sevilla",arbol):
	print (nombre)

## Ejercicio 5
print(provincia("Utrera",arbol))

## Ejercicio 6
lista_id=[]
id=input("id:")
while id!="0":
	lista_id.append(id)
	id=input("id:")

lista=provincias_por_identificador(lista_id,arbol)
for prov in lista:
	nombre=prov[0]
	localidades=prov[1]
	print(nombre)
	for loc in localidades:
		print(loc)


## Ejercicio 7
print(localidades_grandes("Sevilla",arbol))

## Ejercicio 8
print(localidad_grande("Sevilla",arbol))
