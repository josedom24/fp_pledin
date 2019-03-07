---
title: "Ejercicio: Esquema XML para panales de autopistas"
permalink: /lmgs/u04/autopista.html
---

Implementa un esquema XML adecuado para almacenar información de paneles de autopista como el del fichero [autopistas.xml](https://raw.githubusercontent.com/josedom24/lmgs_doc/master/unidades/u7/fich/autopistas.xml) con las siguientes características:

1. El elemento raíz se denomina "paneles"
2. "paneles" contiene un número indeterminado de elementos denominados "evento"
3. Cada "evento" tiene dos atributos obligatorios "tipo" y "fecha"
	* "tipo" puede tener sólo dos valores "Accidente" o "Retención"
	* "fecha" tiene que ser de tipo fecha normalizado
4. Cada "evento" tiene los elementos obligatorios "via", "pk" y "sentido" y los elementos opcionales "retencion" y "corte".
    * "via" tiene los elementos opcionales "nombre", "ref", "origen", "destino", "doble" y "carrilescortados".
        * "nombre" puede contener una cadena de texto de 50 caracteres como máximo
        * "ref" está compuesto por una cadena de 3 caracteres como máximo, un guión y un número comprendido entre 1 y 9999, por ejemplo SE-4100 o A-92.
        * "origen" y "destino" puede contener una cadena de texto de 30 caracteres como máximo.
        * "doble" no tiene contenido
        * "carriles" tiene que ser un número entre 1 y 8
    * "pk" es un número con tres decimales.
    * "sentido" puede tener los valores -1, 0 ó 1.
    * "retencion" tiene el atributo opcional "long" que es del mismo tipo que pk
    * "carrilescortados" tiene el atributo obligatorio "valor" que tiene que ser un número entre 1 y 8.