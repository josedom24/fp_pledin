---
title: Introducción al protocolo WSGI
---

¿Cómo podemos hacer que un servidor web como apache2 sea capaz de servir una aplicación escrita en python? Para ello se utiliza un protocolo que nos permite comunicar al servidor web con la aplicación web: [**WSGI (Web Server Gateway Interface)**](http://wsgi.readthedocs.io/en/latest/).

Es decir, el protocolo WSGI define las reglas para que el servidor web se comunique con la aplicación web. Cuando al servidor llega una petición que tenemos que mandar a la aplicación web python tenemos al menos dos cosas que tener en cuenta:

* Tenemos un fichero de entrada, es decir la petición siempre se debe enviar un único fichero. Este fichero se llama fichero WSGI.
* La aplicación web python con la que se comunica el servidor web utilizando el protocolo WSGI se debe llamar `application`. Por lo tanto el fichero WSGI entre otras cosas debe nombrar a la aplicación de esta manera.