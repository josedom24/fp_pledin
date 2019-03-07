---
title: "Ejercicio: Esquema XML para facturas"
permalink: /lmgs/u06/factura.html
---

Utilizando como base el fichero [factura.xml](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u7/fich/factura.xml) que se te facilita, crea un esquema en formato XSD (XMLSchema) que permita validar facturas como la anterior y que tengan en cuenta también los siguientes aspectos:

1. Toda factura tiene un identificador obligatorio
2. Los elementos emision, vendedor, cliente y articulo son obligatorios, mientras que descuento es opcional
3. El elemento articulo puede aparecer varias veces, los demás sólo una vez
4. vendedor tiene el atributo obligatorio id y el elemento obligatorio nombre.
5. cliente tiene el atributo obligatorio id y los elementos nombre, direccion y teléfono.
6. nombre y direccion son obligatorios, mientras que telefono es opcional y además puede aparecer más de una vez
7. Cada articulo tiene los atributos obligatorios id e iva y los elementos obligatorios denominacion, precio y cantidad
8. Descuento puede contener sólo un numero entre 0 y 100

Tienes que incluir todas las restricciones posibles para que los valores permitidos se ajusten al máximo a los adecuados

## Solución

* [factura.sxd](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/modulos/_lmgs/lmgs/u04/fich/factura.xsd)