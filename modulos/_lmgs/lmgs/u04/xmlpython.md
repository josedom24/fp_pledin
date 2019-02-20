---
title: "XML y python"
permalink: /lmgs/u04/xmlpython.html
---

## ¿Cómo podemos leer y escribir documentos XML?

Lo primero que tenemos que hacer es comprobar si tenemos instalado el paquete `python3-lxml`, si no es así lo instalamos:

    apt-get install python3-lxml

Para leer un documento XML tenemos que usar el método `parse` del objeto `etree`, podemos indicar un fichero que tengamos en el disco duro, o una URL donde se encuentre el fichero:

    from lxml import etree
    doc = etree.parse('books.xml')

Una vez que tenemos creado la estructura `ElementTree`, que en nuestro caso se guarda en el objeto doc, podemos serializar la salida utilizando la siguiente instrucción:

    print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

A partir de este momento podemos leer y escribir el documento XML con distintos métodos que posee la librería `lxml`, para más información puedes leer estos artículos:

* [Trabajar con ficheros xml desde python (1ª parte)](http://www.josedomingo.org/pledin/2015/01/trabajar-con-ficheros-xml-desde-python_1/)
* [Trabajar con ficheros xml desde python (2ª parte)](http://www.josedomingo.org/pledin/2015/01/trabajar-con-ficheros-xml-desde-python_2/)

**Pero nosotros lo único que necesitamos es ejecutar consultas xpath sobre los documentos XML con python.**

## Realizando consultas xpath con lmxl

Podemos realizar consultas xpath utilizando el método `xpath` desde la estructura `ElementTree` (`doc`) o desde cualquier elemento seleccionado. Por ejemplo:

    print(doc.xpath("//price/text()"))
    ['30.00', '29.99', '49.99', '39.95']

Veamos otro ejemplo, si seleccionamos todos los libros:

    libros=doc.xpath("/bookstore/book")

Hemos obtenido una lista de elementos que podemos recorrer:

    for libro in libros:
        print(libro.xpath("./title/text()")[0])
        print(libro.xpath("./@category")[0])
        print(libro.xpath(".//author/text()"))

En este caso hemos mostrado el título, la categoría y la lista de autores de cada libro:

    Everyday Italian
    COOKING
    ['Giada De Laurentiis']
    Harry Potter
    CHILDREN
    ['J K. Rowling']
    XQuery Kick Start
    WEB
    ['James McGovern', 'Per Bothner', 'Kurt Cagle', 'James Linn', 'Vaidyanathan Nagarajan']
    Learning XML
    WEB
    ['Erik T. Ray']
