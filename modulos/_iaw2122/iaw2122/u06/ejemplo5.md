---
title: "Ejemplo 5: Integración continua de aplicación django (Test)"
---

Vamos a trabajar con el repositorio de la aplicación [django_tutorial](https://github.com/josedom24/django_tutorial). Esta aplicación tiene definidas una serie de test, que podemos estudiar en el fichero `tests.py` del directorio `polls`.

Cada test viene definido por una función. en el fichero puedes leer los comentarios para saber que es lo que prueba cada test.

Para ejecutar los test ejecutamos:

```
python3 manage.py test
```

En ese momento se crea una base de datos temporal, donde se van a ir realizando las pruebas que están definidas:

```
python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.024s

OK
Destroying test database for alias 'default'...
```

Por ejemplo, hay dos tests definidos en la función `test_no_questions` y en la función `test_future_question` que comprueban que si no hay preguntas en la base de datos debe aparecer el mensaje **"No polls are available"**. Si un programador modifica la aplicación y en el fichero `polls/templates/polls/index.html` y cambia el mensaje:

```
...
    <p>No hay encuestas disponibles.</p>
...
```

Al pasar los test, tendremos dos errores en los dos tests:

```
python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..F.F.....
======================================================================
FAIL: test_future_question (polls.tests.QuestionIndexViewTests)
Questions with a pub_date in the future aren't displayed on
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jose/github/django_tutorial/polls/tests.py", line 143, in test_future_question
    self.assertContains(response, "No polls are available.")
  File "/home/jose/virtualenv/django_tutorial/lib/python3.9/site-packages/django/test/testcases.py", line 471, in assertContains
    self.assertTrue(real_count != 0, msg_prefix + "Couldn't find %s in response" % text_repr)
AssertionError: False is not true : Couldn't find 'No polls are available.' in response

======================================================================
FAIL: test_no_questions (polls.tests.QuestionIndexViewTests)
If no questions exist, an appropriate message is displayed.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jose/github/django_tutorial/polls/tests.py", line 115, in test_no_questions
    self.assertContains(response, "No polls are available.")
  File "/home/jose/virtualenv/django_tutorial/lib/python3.9/site-packages/django/test/testcases.py", line 471, in assertContains
    self.assertTrue(real_count != 0, msg_prefix + "Couldn't find %s in response" % text_repr)
AssertionError: False is not true : Couldn't find 'No polls are available.' in response

----------------------------------------------------------------------
Ran 10 tests in 0.022s

FAILED (failures=2)
```

**Recuerda que para hacer fallar un test, no hay que tocar el fichero `test.py`. Los test no se pasan porque al modificar el código de la aplicación se dejan de cumplir las condiciones indicadas en los test.**

## Pipeline para realizar un test automático

Sabiendo como se ejecutan los test, es fácil hacer un pipeline que lo haga por nosotros de forma automática:

```groovy
pipeline {
    agent {
        docker { image 'python:3'
        args '-u root:root'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/josedom24/django_tutorial.git'
            }
        }
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test')
        {
            steps {
                sh 'python3 manage.py test'
            }
        }
    }
}
```

1. Para poder instalar los paquetes con pip necesitamos ejecutar las instrucciones en el contenedor como root (`args '-u root:root'`).
2. Clonamos el repositorio.
3. Instalamos los requerimientos.
4. Realizamos los test.

Prueba a cambiar el código para que un test falle y comprueba como el pipeline falla.



