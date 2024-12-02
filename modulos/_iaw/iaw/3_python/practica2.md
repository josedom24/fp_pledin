---
title: "Práctica 2 / 2: Instalación/migración de aplicaciones web Python"
---

## Modificación de nuestra aplicación

Vamos a realizar cambios en el entorno de desarrollo y posteriormente vamos a subirlas a producción. Vamos a realizar tres modificaciones, pero recuerda que primero lo haces en el entorno de desarrollo, y luego tendrás que llevar los cambios a producción:

1. Modifica la página inicial donde se ven las encuestas para que aparezca tu nombre: Para ello modifica el archivo `django_tutorial/polls/templates/polls/index.html`.
2. Modifica la imagen de fondo que se ve la aplicación.
3. Vamos a crear una nueva tabla en la base de datos, para ello sigue los siguientes pasos:
	
    * Añade un nuevo modelo al fichero `polls/models.py`:

        ```python
		class Categoria(models.Model):	
        	Abr = models.CharField(max_length=4)
        	Nombre = models.CharField(max_length=50)

        	def __str__(self):
        		return self.Abr+" - "+self.Nombre 		
        ```

    * Crea una nueva migración.
    * Y realiza la migración.
    * Añade el nuevo modelo al sitio de administración de django:

        Para ello cambia la siguiente línea en el fichero `polls/admin.py`:
	
	    ```python
        from .models import Choice, Question
        ```

        Por esta otra:

        ```python
	    from .models import Choice, Question, Categoria
        ```

        Y añade al final la siguiente línea:

	    ```python
        admin.site.register(Categoria)
        ```
    * Despliega el cambio producido al crear la nueva tabla en el entorno de producción.

{% capture notice-text %}
Explica los cambios que has realizado en el entorno de desarrollo y cómo lo has desplegado en producción para cada una de las modificaciones. Entrega pantallazos donde se vean las distintas modificaciones y que todo está funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Instalación/migración de uns CMS Python Django

En esta tarea vamos a desplegar un CMS python. Hay varios CMS python basado en django (puedes encontrar varios en el siguiente [enlace](https://djangopackages.org/grids/g/cms/)). Puedes instalar cualquiera, ~~yo he probado Mezzanine~~.

* Instala el CMS en el entorno de desarrollo. Debes utilizar un entorno virtual.
* Personaliza la página (cambia el nombre al blog y pon tu nombre) y añade contenido (algún artículo).
* Realiza la migración de tu aplicación en tu entorno de producción. La aplicación será accesible en la url `https://portal.tudominio.algo`.

{% capture notice-text %}
Explica los pasos fundamentales para hacer la instalación y la migración. Adjunta capturas de pantallas para demostrar que todo está funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>