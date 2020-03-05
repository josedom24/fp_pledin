---
title: "Trabajando con YAML desde python3: pyyaml"
permalink: /lmgs/u07/pyyaml.html
---

## Instalación

En debian/Ubuntu instalamos el gestor de paquetes python pip:

	apt-get install python3-pip

E instalamos el páquete:

	pip install PyYAML

Con apt en Debian 10:

	apt install python3-yaml

## Leer un fichero YAML

Si tenemos el fichero books.yaml:

```
---
bookstore:
	book: 
	- title: 
        lang: "en"
        text: "Everyday Italian"
      author: "Giada De Laurentiis"
      year: "2005"
      price: "30.00"
      category: "COOKING"
    
    - title: 
        lang: "en"
        text: "Harry Potter"
      author: "J K. Rowling"
      year: "2005"
      price: "29.99"
      category: "CHILDREN"
    
    - title: 
        lang: "en"
        text: "XQuery Kick Start"
      author: 
        - "James McGovern"
        - "Per Bothner"
        - "Kurt Cagle"
        - "James Linn"
        - "Vaidyanathan Nagarajan"
      year: "2003"
      price: "49.99"
      category: "WEB"
    
    - title: 
        lang: "en"
        text: "Learning XML"
      author: "Erik T. Ray"
      year: "2003"
      price: "39.95"
      category: "WEB"
```

Podríamos hacer un programa como este:

	import yaml   
	with open("books.yaml") as fichero:
		doc=yaml.load(fichero)

	>>> type(doc)
	dict

## Obteniendo información

### Cantidad de libros

	>>> len(doc["bookstore"]["book"])
	4

### Títulos de los libros

	for libro in doc["bookstore"]["book"]:
   		print(libro["title"]["text"])

### Autores de los libros

	for libro in doc["bookstore"]["book"]:
        if isinstance(libro["author"],list):
            for autor in libro["author"]:
                print(autor)
        else:
            print(libro["author"])
