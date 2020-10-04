---
permalink: /lmgs/2020-2021/python/mi_primer_programa.html
layout: single3
---

# Mi primer programa en Python3

Podemos ejecutar código python de varia maneras:

## Uso del interprete

Al instalar python3 el ejecutable del interprete lo podemos encontrar en `/usr/bin/python3` (en debian Stretch). Este directorio por defecto está en el PATH, por lo tanto lo podemos ejecutar directamente en el terminal, para ello ejecutamos:

	$ python3
    Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
    [GCC 6.3.0 20170118] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

## A partir de un fichero con el código fuente

Si tenemos nuestro programa en un fichero fuente (suele tener extensión `py`), por ejemplo `programa.py`,lo ejecutaríamos de la siguiente manera.
	
	$ python3 programa.py

Para escribir un fichero con el código fuente de nuestro programa tenemos varias opciones:

* Podemos usar un IDE (entorno de desarrollo integrado), que además de la posibilidad  de editar el código, nos ofrezca otras herramientas: depuración de código, generación automático de código, ayuda integrada, manejo del proyecto, gestión de los sistemas de control de versiones,..). Existen muchos IDE a nuestra disposición: [Entornos de desarrollo para python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).
* En este curso vamos usar un editor de texto: Nos permiten escribir nuestro código fuente de manera eficiente, además los nuevos editores de texto permiten añadir funcionalidades a través de plugin, algunos ejemplos: Sublime Text, Atom, Visual Studio Code, vim, emacs,... aunque hay muchos más:  [Editores de texto para python](https://wiki.python.org/moin/PythonEditors).

{% capture notice-text %}

**Ejercicios**

* Elige un editor de texto (si no tienes criterio para elegir uno, pregunta a los compañeros oo al profesor). Instalalo para escribir nuestro primer programa python.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>