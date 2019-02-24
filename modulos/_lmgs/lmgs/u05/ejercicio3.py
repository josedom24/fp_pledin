import json

def ListaProvincias(doc):
    prov = []
    for provincia in doc["lista"]["provincia"]:
        prov.append(provincia["nombre"]["__cdata"])
    return prov

def ListaLocalidades(doc):
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if type(provincia["localidades"]["localidad"])==list:
            for localidad in provincia["localidades"]["localidad"]:
                loc.append(localidad["__cdata"])
        else:
            loc.append(provincia["localidades"]["localidad"]["__cdata"])
        
    return loc

def ListaProvinciasLocalidades(doc):
    prov = []
    cantidades = []
    for provincia in doc["lista"]["provincia"]:
        prov.append(provincia["nombre"]["__cdata"])
        if type(provincia["localidades"]["localidad"])==list:
            cantidades.append(len(provincia["localidades"]["localidad"]))
        else:
            cantidades.append(1)
    return zip(prov,cantidades)

def LocalidadesProvincia(doc,nombre):
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if provincia["nombre"]["__cdata"]==nombre:
            if type(provincia["localidades"]["localidad"])==list:
                for localidad in provincia["localidades"]["localidad"]:
                    loc.append(localidad["__cdata"])
            else:
                loc.append(provincia["localidades"]["localidad"]["__cdata"])
    return loc


def ProvinciaLocalidades(doc,nombre):

    for provincia in doc["lista"]["provincia"]:
        if type(provincia["localidades"]["localidad"])==list:
            for localidad in provincia["localidades"]["localidad"]:
                if localidad["__cdata"]==nombre:
                    return provincia["nombre"]["__cdata"]
        else:
            if provincia["localidades"]["localidad"]["__cdata"]==nombre:
                return provincia["nombre"]["__cdata"]
    return ""

def ProvinciasLocalidadesID(doc,ids):
    prov = []
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if provincia["_id"] in ids:
            prov.append(prov.append(provincia["nombre"]["__cdata"]))
            lista_localidad=[]
            if type(provincia["localidades"]["localidad"])==list:
                for localidad in provincia["localidades"]["localidad"]:
                    lista_localidad.append(localidad["__cdata"])
            else:
                lista_localidad.append(provincia["localidades"]["localidad"]["__cdata"])
            loc.append(lista_localidad)
    return zip(prov,loc)


########################

with open("ej3.json") as fichero:
	doc=json.load(fichero)

# Ejercicio 1
print("Ejercicio 1")

for prov in ListaProvincias(doc):
    print(prov)

# Ejercicio 2
print("Ejercicio 2")

for localidad in ListaLocalidades(doc):
    print(localidad)

# Ejercicio 3
print("Ejercicio 3")
for prov,cant in ListaProvinciasLocalidades(doc):
    print(prov,cant)

# Ejercicio 4
print("Ejercicio 4")
nombre=input("Nombre de provincia:")
localidades = LocalidadesProvincia(doc,nombre)
if len(localidades)>0:
    for localidad in localidades:
        print(localidad)
else:
    print("No existe la provincia")

# Ejercicio 5
print("Ejercicio 5")
nombre=input("Nombre de localidad:")
provincia = ProvinciaLocalidades(doc,nombre)
if provincia!="":
    print(provincia)
else:
    print("No existe localidad.")

# Ejercicio 6
print("Ejercicio 6")

ids = []
id = input("Id. de provincia. 0 para salir")
while id!="0":
    ids.append(id)
    id = input("Id. de provincia. 0 para salir")

for provincia,localidades in ProvinciasLocalidadesID(doc,ids):
    print (provincia)
    for localidad in localidades:
        print(localidad)

