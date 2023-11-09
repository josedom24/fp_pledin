---
title: "Práctica: Instalación de un CMS python"
---

En esta tarea vamos a desplegar un CMS python. Tienes que realizar la instalación de un CMS python basado en django (puedes encontrar varios en el siguiente [enlace](https://djangopackages.org/grids/g/cms/). Según la dificultad de la instalación tendrás más o menos notas:

* Fácil (un 7): Django CMS, Wagtail CMS, CodeRed CMS
* Medio (un 8,5): Mezzanine (Es fácil pero la instalación da un error que tendrás que solucionar).
* Difícil (un 10): FeinCMS, Django-Fiber

1. Instala el CMS en el entorno de desarrollo. Debes utilizar un entorno virtual.
2. Personaliza la página (cambia el nombre al blog y pon tu nombre) y añade contenido (algún artículo).
3. Guarda los ficheros generados durante la instalación en un repositorio github. Guarda también en ese repositorio la copia de seguridad de la bese de datos. Ten en cuenta que en el entorno de desarrolla vas a tener una base de datos sqlite, y en el entorno de producción una mariadb, por lo tanto es recomendable para hacer la copia de seguridad y recuperarla los comandos: `python manage.py dumpdata` y `python manage.py loaddata`, para [más información](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata).
4. Realiza el despliegue de la aplicación en tu entorno de producción (servidor web y servidor de base de datos en KVM/openstack). Utiliza un entorno virtual. Utiliza el servidor de aplicaciones python que no hayas usado en la práctica anterior. El contenido estático debe servirlo el servidor web. La aplicación será accesible en la url `python.tunombre.gonzalonazareno.org`.
