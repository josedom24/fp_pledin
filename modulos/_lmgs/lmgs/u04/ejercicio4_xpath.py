from lxml import etree


#Ejercicio 1
def calles(arbol):
	return arbol.xpath('//way/tag[@k="highway"]/../@id')

# Ejercicio 2

def calles_con_nombre(arbol):
		return arbol.xpath('//way/tag[@k="highway"]/../tag[@k="name"]/@v')
		
# Ejercicio 3

def nodos(arbol):
	return arbol.xpath('//node[@uid="384182" and count(tag)>0]/@id')

def supermecados(arbol):
	return int(arbol.xpath('count(//way/tag[@k="shop"]/../tag[@v="supermarket"])'))
	
arbol = etree.parse('utrera.xml')

## Ejercicio1
print(calles(arbol))

## Ejercicio2
print(calles_con_nombre(arbol))

## Ejercicio3
print(nodos(arbol))

## Ejercicio4
print(supermecados(arbol))
