---
title: Introducción a django
---

[Django](https://www.djangoproject.com/) es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como modelo–vista–controlador (MVC). 

El modelo MVC es un patrón de diseño software que separa los datos de la aplicación, la lógica del programa y la representación de la información:

* El **Modelo**: Es la representación de la información con la cual el sistema opera, por lo tanto gestiona todos los accesos a dicha información.
* El **Controlador**: Es la parte del programa donde se implementa la lógica y las funciones de la aplicación.
* La **Vista**: Representa la información ofrecida por la aplicación en un formato adecuada.

## Instalación de django

Como siempre cuando trabajamos en Python vamos a usar un entorno virtual:

```bash
$ python3 -m venv django
$ source django/bin/activate
(django)$ pip install django
(django)$ python -m django --version
3.2.9
```

## Creando un proyecto django

En un primer paso, vamos a ver cómo sería la creación de una aplicación django, posteriormente trabajaremos con una aplicación ya desarrollada. Si vamos a crear una aplicación django lo primero sería la creación de un proyecto:

```bash
(django)$ django-admin startproject mysite
```

Esto crearía el directorio del proyecto `mysite` que tendría los siguientes ficheros:

```bash
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

* `manage.py`: La utilidad de terminal que vamos a usar para manejar nuestra aplicación.
* El directorio `mysite` es un paquete python (agrupa distintos módulos (ficheros python)). Esto se indica con un fichero vacio que se de be llamar `__init__.py`.
* `settings.py`: La configuración de la aplicación.
* `urls.py`: Donde se declaran las rutas que va tener la aplicación.
* `wsgi.py`: Fichero wsgi para el despliegue de la aplicación utilizando el protocolo wsgi.
* `asgi.py`: Fichero asgi para el despliegue de la aplicación utilizando el protocolo asgi.

## Ejecución del servidor web de desarrollo

Si queremos iniciar el servidor web de desarrollo para ver cómo va quedando la aplicación, ejecutamos:

```bash
(django)$ python3 manage.py runserver
```

Si queremos que el servidor escuche en todas las direcciones y en un puerto determinado:

```bash
(django)$ python3 manage.py runserver 0.0.0.0:8000
```

## Creando una aplicación

Hasta ahora tenemos un proyecto django, pero no tiene ninguna funcionalidad. En un proyecto django podemos ir añadiendo distintas aplicaciones que  donde vamos implementando las distintas funcionalidades del programa. Siguiendo el tutorial de django, vamos a crear la aplicación polls (encuestas), para ello:

```bash
(django)$ python3 startapp polls
```

Esto creará un directorio `polls` en el proyecto con los siguientes ficheros:

```bash
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Ahora iremos estudiando cada uno de estos ficheros. Es muy recomendable que hagáis el [tutorial de django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/) que tiene 7 apartados os da una visión general del desarrolla de una aplicación en django.

En el siguiente apartado seguiremos estudiando las aplicaciones django pero utilizando la aplicación desarrolla en el tutorial, que podeis encontrar en: [https://github.com/josedom24/django_tutorial](https://github.com/josedom24/django_tutorial).

## La configuración del proyecto

Veamos el ficheros `settings.py` que encontramos dentro del directorio `django_tutorial`:

* `DEBUG = True`: Si está activo los errores que se produzcan en la aplicación se verán con todo lujo de detalles en el navegador. Si tenemos la aplicación en producción debería ser `False`.
* `ALLOWED_HOSTS = []`: Una lista con los nombres con los que se va a permitir el acceso a la aplicación.
* `INSTALLED_APPS = [...`: La lista de las aplicaciones que tiene instalada el proyecto, por ejemplo vemos que se ha incluido la aplicación polls (`polls.apps.PollsConfig`). También tenemos una aplicación que nos permite tener un panel de control de la aplicación (`django.contrib.admin`). Y otras cuantas aplicaciones...
* `DATABASES`: Configuración de la base de datos que se va a utilizar en el proyecto. Por defecto se utiliza una base de datos sqlite llamada `db.sqlite3`.

## El modelo de la aplicación

## La aplicación de administración de la aplicación

## Las rutas y el controlador de la aplicación

Las rutas virtuales que vamos a usar para acceder a las distintas funciones de la aplicación se definen a nivel de proyecto y a nivel de aplicación:

* A nivel de proyecto estudiamos el fichero `django_tutorial/urls.py`: 
    * Donde se ha definido que cuando se acceda a la ruta `polls/` se utilizaran las rutas definidas en la aplicación `polls`.
    * Y cuando se acceda a la ruta `admin/` se utilizarán las rutas definidas en la aplicación `admin` (panel de administración).
* A nivel de aplicación, vemos el fichero `polls/urls.py` y comprobamos que se han definido 4 rutas:
    * La ruta principal '': Donde se va a ejecutar la función `index`, que muestra la lista de encuestas. Ejemplo: `http://localhost:8000/polls`.
    * La ruta `<int:pk>/`: Cuando se ponga un entero se mostrará información de esa encuesta. Esto se hace en la función `detail`. Ejemplo: `http://localhost:8000/polls/1/`.
    * La ruta `'<int:pk>/results/`: Donde se nos mostrará los resultados de la encuesta identificada por su código. Esto se realiza con la función `results`. Ejemplo: `http://localhost:8000/polls/1/results/`.
    * La ruta `<int:question_id>/vote/`: Nos permite votar una opción de una encuesta. Esto lo realiza la función `vote`. Por ejemplo: `http://localhost:8000/polls/100/vote/`.

Después lo estudiaremos con más detenimiento, pero las funciones que se realizan en cada una de las rutas forman parte del **controlador** de la aplicación que están implementadas en el fichero `polls/views.py`.

## Las vistas de la aplicación 

Las vistas en djando se implementan usando plantillas (`templates`). django tiene un motor de plantillas propio. Podemos encontrar las vistas de la plicación `polls` en el directorio `polls\templatees\polls`.