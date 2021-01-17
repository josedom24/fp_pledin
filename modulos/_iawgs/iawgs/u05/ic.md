---
title: "Práctica: Introducción a la integración continua"
permalink: /iawgs/u05/ic.html
---

Debes realizar **una de las siguientes tareas**, utilizando una herramienta de CI/CD: GitHub Actions, GiLab CI/CD, CircleCI, Jenkins, ... (No uses Travis CI).

## Tarea: Despliegue de una página web estática (build, deploy) 

{% capture notice-text %}
En esta práctica investiga como generar una página web estática con la herramienta que elegiste en la práctica 1 de la asignatura y desplegarla en el servicio que utilizaste en esa práctica. 

* En el repositorio GitHub/GitLab sólo tienen que estar los ficheros markdown.
* La página se debe generar en el sistema de integración continúa, por lo tanto debemos instalar las herramientas necesarias.
* Investiga si podemos desplegar de forma automática en el servicio elegido (si es necesario cambia el servicio de hosting para el despliegue).
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Tarea: Integración continúa de aplicación django (Test + Deploy) 

Vamos a trabajar con el repositorio de la aplicación [`django_tutorial`](https://github.com/josedom24/django_tutorial). Esta aplicación tiene definidas una serie de test, que podemos estudiar en el fichero `tests.py` del directorio `polls`.

Para ejecutar las pruebas unitarias, ejecutamos la instrucción `python3 manage.py test`.

{% capture notice-text %}
Estudia las distintas pruebas que se han realizado, y modifica **el código de la aplicación (debes modificar el fichero `views.py` o los templates, no debes cambiar el fichero `tests.py`**  para que al menos una de ella no se ejecute de manera exitosa. 
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

A continuación vamos a configurar la integración continúa para que cada vez que hagamos un commit se haga la ejecución de test en la herramienta de CI/CD que haya elegido.

{% capture notice-text %}
Crea el pipeline en el sistema de CI/CD para que pase automáticamente los tests. Muestra el fichero de configuración y una captura de pantalla con un resultado exitoso de la IC y otro con un error.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

A continuación vamos a realziar el despliegue coontinuo en un servicio de hosting, por ejemplo heroku.

{% capture notice-text %}
Entrega un breve descripción de los pasos más importantes para realizar el despliegue desde el sistema de CI/CS y entrega una prueba de funcionamiento donde se compruebe cómo se hace el despliegue automático.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

