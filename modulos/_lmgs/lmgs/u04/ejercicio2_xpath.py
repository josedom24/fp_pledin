from lxml import etree

### Ejercicio 1
def usuarios(arbol):
	nombres=arbol.xpath("//user/firstname/text()")
	apellidos=arbol.xpath("//user/lastname/text()")
	for indice in range(len(nombres)):
		nombres[indice]=nombres[indice]+" "+apellidos[indice]
	return nombres

### Ejercicio2
def avatar(arbol):
	nombres=arbol.xpath('//user[picture="1"]/firstname/text()')
	apellidos=arbol.xpath('//user[picture="1"]/lastname/text()')
	for indice in range(len(nombres)):
		nombres[indice]=nombres[indice]+" "+apellidos[indice]
	return nombres

### Ejercicio3
def acceso_desde_fuera(arbol):
	usuarios=arbol.xpath('//user[contains(lastip,"172.22")=false]/email/text()')
	return usuarios

### Ejercicio4
def buscar(cadena,arbol):
	nombres=arbol.xpath('//user[starts-with(firstname,"A")]/firstname/text()')
	apellidos=arbol.xpath('//user[starts-with(firstname,"A")]/lastname/text()')
	for indice in range(len(nombres)):
		nombres[indice]=nombres[indice]+" "+apellidos[indice]
	return nombres


### Ejercicio 5
### Voy a hacer un diccionario, cada elemento del diccionario tendrá como clave el nombre de la localidad y como valor 
### tendrá una lista con los usuarios

def lista_por_localidad(arbol):
	dic_usuarios={}
	lista_localidades=list(set(arbol.xpath('//user/city/text()')))
	for loc in lista_localidades:
		# Voy creando el diccionario, creo un elemento con la key igual a la localidad y como valor una lista vacia
		nombres=arbol.xpath('//user[city="%s"]/firstname/text()'%loc)
		apellidos=arbol.xpath('//user[city="%s"]/lastname/text()'%loc)
		dic_usuarios[loc]=[]
		for indice in range(len(nombres)):
			dic_usuarios[loc].append(nombres[indice]+" "+apellidos[indice])
	return dic_usuarios

### Ejercicio 6
def ultimo_acceso(arbol):
	lista=[]
	lua=sorted(list(map(int,arbol.xpath("//user/lastaccess/text()"))),reverse=True)
	for ua in lua:
		nombre=arbol.xpath('//user[lastaccess="%s"]/firstname/text()'%ua)
		apellido=arbol.xpath('//user[lastaccess="%s"]/lastname/text()'%ua)
		lista.append(nombre[0]+" "+apellido[0])
		
	return lista

arbol = etree.parse('users.xml')

### Ejercicio 1
print(usuarios(arbol))

### Ejercicio 2
print(avatar(arbol))

### Ejercicio 3
print(acceso_desde_fuera(arbol))

### Ejercicio 4
cad=input("Dame el nombre:")
print(buscar(cad,arbol))

### Ejercicio 5
dic=lista_por_localidad(arbol)
for key,value in dic.items():
	print(key)
	print("="*len(key))
	for user in value:
		print(user)

### Ejercicio 6
print(ultimo_acceso(arbol))
