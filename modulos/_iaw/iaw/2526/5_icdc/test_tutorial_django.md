---
title: "Tests en la aplicación tutorial Django"
---

Vamos a trabajar con el repositorio de la aplicación [django_tutorial](https://github.com/josedom24/django_tutorial). Esta aplicación tiene definidas una serie de test, que podemos estudiar en el fichero `tests.py` del directorio `polls`.

## Requisitos de la aplicación

En nuestro programa de encuestas que desarrollamos en el tutorial django, se tienen que tener en cuanta los siguiente elementos:

* Cada pregunta se identifica con un identificador.
* Al crear una pregunta de una encuesta se debe indicar la fecha de publicación.
* Se considera que una pregunta está recientemente publicada, si su fecha de publicación es menos de un día.
* Podemos ver en el modelo de datos (`models.py`) que la clase `Question` tiene una función booleana (`was_published_recently`) que devuelve `True` si la pregunta ha sido publicada en el último día.


### ¿Cómo debe funcionar el programa?

1. Si intentamos ver el detalle de una pregunta con fecha de publicación futura  nos debe devolver un 404.

	* **¿Donde se consigue esto?**: En la función `get_queryset` de la `Class DetailView` en el fichero `views.py`, la consulta que se hace es:
			```
	    	Question.objects.filter(pub_date__lte=timezone.now())
	    	```
		Al no seleccionar ninguna pregunta nos da un 404.
	* **¿Dónde se prueba esto?**: En la función `test_future_question` de la `class QuestionDetailViewTests` en el fichero `tests.py`.

2. Al ver el detalle de una pregunta publicada con un fecha pasada se debe mostrar el texto de la pregunta.

	* **¿Donde se consigue esto?**: En el template `detail.html` en la primera línea:
			```
		    <h1>\{\{ question.question_text \}\}</h1>
		    ```
	* **¿Dónde se prueba esto?**: En la función `test_past_question` de la `class QuestionDetailViewTests` en el fichero `tests.py`.
	
3. Si no hay preguntas en la base de datos, en la página principal aparece el mensaje "No polls are available.". 

	* **¿Donde se consigue esto?**: En el template `index.html`.
	* **¿Dónde se prueba esto?**: En la función `test_no_questions` de la `class QuestionIndexViewTests` en el fichero `tests.py`.
	
4. Si hay preguntas con fecha de publicación en el pasado, debe aparecer en la página principal. En la página principal se ven las 5 últimas preguntas publicadas.

	* **¿Donde se consigue esto?**: En el fichero `views.py` en la función `get_queryset` de la `Class IndexView`, la consulta es:
			```
	     	Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	     	```
	* **¿Dónde se prueba esto?**: En la función `test_past_questions` de la `class QuestionIndexViewTests` en el fichero `tests.py`.

5. Si tenemos preguntas con fecha de publicación en el futuro, no deben aparecer en la página principal. En la página principal aparece el mensaje "No polls are available.". 

	* **¿Donde se consigue esto?**: En el mismo código que el requerimiento anterior.
	* **¿Dónde se prueba esto?**: En la función `test_future_question` de la `class QuestionIndexViewTests` en el fichero `tests.py`. 
	* Existen dos pruebas más: 
		* `test_future_question_and_past_question`, que prueba cuando hay una pasada con fecha de publicación pasada y otra con fecha de publicación futura.
		* `test_two_past_questions`, que prueba cuando tenemos dos preguntas con fechas de publicación pasada.
	* **Nota: No hay ninguna prueba que compruebe que en la página principal se vean las 5 últimas preguntas publicadas.**

6. En las preguntas publicadas en una fecha futura, la función `was_published_recently()` debe devolver `False`.
7. En las preguntas publicadas hace más de 1 día, la función `was_published_recently()` debe devolver `False`.
8. En las preguntas publicadas hace un 1 día, la función `was_published_recently()` debe devolver `True`.

	* **¿Donde se consigue esto?**: En la función `was_published_recently` en el modelo de datos, en el fichero `models.py`
	* **¿Dónde se prueba esto?**: En las siguientes funciones de la `class QuestionModelTests`:
		* `test_was_published_recently_with_future_question`
		* `test_was_published_recently_with_old_question`
		* `test_was_published_recently_with_recent_question`

## Ejecución de los test

ara ejecutar los test ejecutamos:

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