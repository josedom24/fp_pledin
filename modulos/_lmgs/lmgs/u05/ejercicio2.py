import json

## Ejercicio 2
def PruebasMasDeDosHoras(doc):
    titulos = []
    for prueba in doc:
        if prueba["Horas"]>2:
            titulos.append(prueba["Titulo"])
    return titulos

## Ejercicio 3
def UrlPruebasNoPresencial(doc):
    urls = []
    for prueba in doc:
        if prueba["TipoFormacion"]=="NoPresencial":
            urls.append(prueba["URL"])
    return urls

## ejercicio 4
def PruebaTitulosProfesores(doc,id):
    datos = []
    for prueba in doc:
        if prueba["$id"]==id:
            datos.append(prueba["Titulo"])
            for profesor in prueba["Profesorado"]:
                datos.append(profesor["NombreCompleto"])
            return datos
    return datos
## ejercicio 5
def InfoPrueba(doc):
    titulos = []
    profesores=[]
    for prueba in doc:
        titulos.append(prueba["Titulo"])
        lista_prof = []
        for profesor in prueba["Profesorado"]:
                lista_prof.append(profesor["NombreCompleto"])
        profesores.append(lista_prof)
    return zip(titulos,profesores)


########################

with open("ej2.json") as fichero:
	doc=json.load(fichero)

# Ejercicio 1
print("Ejercicio 1")
print("Número de pruebas: %d" % len(doc))

## Ejercicio 2
print("Ejercicio 2")
for titulo in PruebasMasDeDosHoras(doc):
    print(titulo)

## Ejercicio 3
print("Ejercicio 3")
for url in UrlPruebasNoPresencial(doc):
    print(url)

## Ejercicio 4
print("Ejercicio 4")
id = input("Dame el id de una prueba:")
datos=PruebaTitulosProfesores(doc,id)
if len(datos)>0:
    print("Título:",datos[0])
    print("Profesores")
    for profesor in datos[1:]:
        print(profesor)
else:
    print("No existe esa prueba de nivel")

## Ejercicio 5
print("Ejercicio 5")

for titulo,profesores in InfoPrueba(doc):
    print(titulo)
    print("Profesores")
    for profesor in profesores:
        print(profesor)
