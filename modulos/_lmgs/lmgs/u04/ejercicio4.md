---
title: "Inventar un lenguaje XML para facturas"
permalink: /lmgs/u04/ejercicio4.html
---

Queremos estructurar la información que genera un proceso de facturación de una empresa en un fichero XML. Para ello tenemos que tener en cuenta los siguientes aspectos:

* Cada factura tiene un código.
* La factura también necesita la fecha de emisión.
* En la factura aparecen los datos del cliente (dni, nombre, dirección, código postal, población).
* De cada producto que se ha comprado debe aparecer la cantidad de productos comprados, la denominación y el precio unitario.
* Se debe guardar el IVA de cada producto.
* Si es necesario se indicara un descuento al importe total de la factura.

Razona la siguiente pregunta: ¿Es necesario guardar el importe total por producto y el importe total de la factura?

* [Una posible solución](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/factura.xml)