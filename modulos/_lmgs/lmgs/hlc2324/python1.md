---
permalink: /python/python1.html
layout: single3
---

# Introducción a Python

Python es un lenguaje de programación **interpretado** (se ejecutan en orden las instrucciones) que por defecto ya se encuentra instalado en muchos sistemas operativos.

Python es un lenguaje de programación interpretado, multiplataforma y libre.

## Escribir programas Python

Para escribir programa en Python, sólo necesitamos un **editor de textos** y el **intérprete** que será el que haga que las instrucciones escritas en el editor de textos se ejecuten.

Realmente nosotros vamos a usar un **IDE (Entorno de Desarrollo Integrado)**, que son programas que además de ofrecer un editor de texto, posee muchas herramientas que nos facilitan la labor de programar. Por ejemplo: Visual Studio Code, Sublime Text,...

Sin embargo, las herramientas que hemos nombrados tienen tantas funcionalidades, que para personas que están empezando a programar es conveniente usar un IDE más básico. Nosotros  recomendamos usar el el entorno de programación **Thonny**, el cual está diseñado y pensado precisamente para las personas que desean iniciarse en el mundo de la programación en Python.

{% capture notice-text %}

**Ejercicio**

* Instala el entorno de programación **Thonny**, con la herramienta `apt`.
* Configura el entorno para que funcione de manera adecuada, para ello activa la opción **Use cuadros de diálogo de archivos Tk en lugar de Zenety** en la opción **Herramientas->Opciones**.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## El entorno de desarrollo Thonny

El programa inicialmente divide la ventana en 2 partes bien diferenciadas:

### Editor de Texto

La región superior de la ventana, se trata de un **editor de texto** donde vamos a escribir nuestros programas. 

Este editor al estar pensado para escribir texto en Python, tiene además la particularidad de que nos resaltará la sintaxis y nos ayudará con la escritura de instrucciones (pulsando **CTRL + Espacio**).

El editor de código nos permitirá guardar nuestro programa en archivos que deben tener la extensión **.py**. Para ejecutar nuestro programa pulsaremos sobre el botón **Play** o la tecla **F5**.

![ ](../lmgs/hlc2324/img/img1.png)

El resultado de la ejecución del programa se verá en la parte inferior de la pantalla, en la **Consola**.

### Consola

Es la parte inferior de la pantalla. Como hemos indicado en ella se mostrará el resultado de ejecutar nuestro programa. Además la consola, muestra lo que en Python se denomina el **intérprete**. Se trata de una línea de comando donde podemos introducir instrucciones y comprobar el resultado que produce su ejecución.

![ ](../lmgs/hlc2324/img/img2.png)

El **interprete** nos permite ejecutar instrucciones python para ver su funcionamiento.

## Ejecución de un programa a partir del fichero py

Hemos visto como ejecutar un programa python desde el entorno de desarrollo Thonny. Perro, una vez que hemos terminado nuestro programa podemos ejecutarlo desde un terminal bash. Por ejemplo, si el programa lo hemos guardado en un fichero `programa.py`,lo ejecutaríamos de la siguiente manera.

```
$ python3 programa.py
```


## Mi primer programa en python3

Vamos a escribir nuestro primer programa para estudiar la estructura de un programa en python3. El programa que vamos a realizar es el siguiente: **Programa que pida la edad y diga si es mayor de edad**. El código sería el siguiente:

![ ](../lmgs/hlc2324/img/img3.png)

### Estructura del programa

* Un programa python está formado por instrucciones que acaban en un **carácter de “salto de línea”**.
* Una **línea empieza en la primera posición**, si tenemos instrucciones dentro de un bloque de una estructura de control de flujo habrá que hacer una identación.
* La **identación** se puede hacer con **espacios y tabulaciones** pero ambos tipos no se pueden mezclar. Se recomienda usar 4 espacios.
* Se utiliza el carácter # para indicar los comentarios.

{% capture notice-text %}

**Ejercicio**

* Copia el programa en el editor de texto de Thonny.
* Una vez terminado, ejecuta el programa dentro del entorno de desarrollo Thonny.
* Guarda el programa en un fichero llamado `edad.py`.
* Ejecuta el programa desde un terminal.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## ¿Qué tienes que entregar?

Vamos a copiar varios programas en Python:

**Programa 1**

![ ](../lmgs/hlc2324/img/img4.png)

**Programa 2**

![ ](../lmgs/hlc2324/img/img5.png)

**Programa 3**

![ ](../lmgs/hlc2324/img/img6.png)

**Programa 4**

![ ](../lmgs/hlc2324/img/img7.png)

{% capture notice-text %}

**Entrega**

Escribe cada uno de los programas en Thonny. Guárdalos en un fichero con extensión **py** y entrega un documento pdf con lo siguiente:

1. Captura de pantalla ejecutando cada programa en Thonny.
2. Captura de pantalla ejecutando cada programa desde la línea de comandos.
3. Para cad programa, escribe una descripción de lo que hace el programa.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
