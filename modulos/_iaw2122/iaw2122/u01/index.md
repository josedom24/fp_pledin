---
title: Introducción a la implantación de aplicaciones web
---
## Objetivos

* Aprender a trabajar con git
* Aprender lenguaje de marcas markdown
* Comprender que existe un integración continua y un despliegue continuo en el proceso de despliegue de la página

## Presentación

* [Presentación del módulo](http://josedom24.github.io/mod/iaw/presentacion#/)

## Recordamos Git/GitHub
    
Para recordar git/github puedes repasar [git - la guía sencilla](https://rogerdudler.github.io/git-guide/index.es.html), y para profundizar [Pro Git, el libro oficial de Git](http://librosweb.es/pro_git/).
   
{% capture notice-text %}
* Realiza las tareas indicadas en [Introducción a  git/github](github.html), para preparar tu cuenta en GitHub y recordar los comandos básicos de git.	
* Markdown es un lenguaje de marcas que nos facilita la escritura de documentos. Se suele usar normalmente para escribir la información en GitHub (normalmente en ficheros `README.md`, por ejemplo). Repasa la sintáxis básica de Markdown usando este [CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) (o alguno similar) y práctica la escritura de documentos usando algún editor online, por ejemplo: [stackedit](https://stackedit.io/app#), [dillinger](https://dillinger.io),...
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

{% capture notice-text %}
**Ejercicio 1: ¿Cómo colaborar en un proyecto de software libre? ¿Qué es un Pull Request (PR)?**

Un pull request es una petición que se hace al propietario de un repositorio original para que este último incorpore los cambios que se sugieren.

En este ejercicio tienes que hacer un pull request sobre el siguiente repositorio: [https://github.com/josedom24/prueba-pr-asir](https://github.com/josedom24/prueba-pr-asir). Para ello:

* Realiza un pull request a este repositorio para solicitar dos cambios:

    * Debes cambiar el fichero `README.md` para añadir un enlace a la lista, donde ponga tus iniciales y vaya al fichero que vas a crear en el directorio `files`.
    * Crea un  fichero en el directorio `files`, que se llame `tus_iniciales.md` (en mi caso se llama `jdmr.md`) y donde escribas en markdown la respuesta a la pregunta: **¿Qué asignatura te gusta más? Y ¿por qué?** (se debe utilizar al menos 5 marcas distintas de markdown).

Realiza el pull request (con un mensaje de commit significativo) y espera a que sea aceptado por mí. Al finalizar el ejercicio debes sincronizar tu repositorio para que tenga todos los ficheros de todos tus compañeros.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Páginas web dinámicas us páginas web estáticas

Para estudiar las diferencias entre páginas web dinámicas y estáticas, puedes seguir estos enlaces u otros parecidos:

* [Aspectos básicos de las aplicaciones Web](https://helpx.adobe.com/es/dreamweaver/using/web-applications.html)
* [Evolución de la web (Pablo E. Lozada Y.)](http://profesores.elo.utfsm.cl/~tarredondo/info/networks/Evolucion_Web.pdf)
* [Aplicaciones web en la Wikipedia](https://es.wikipedia.org/wiki/Aplicaci%C3%B3n_web)
* [Diferencias y beneficios entre páginas estáticas y dinámicas](http://nilclass.com/courses/what-is-a-static-website/#1)

{% capture notice-text %}
* Realiza el ejercicio [Pagínas web estáticas y dinámicas](ejercicio_estatica_dinamica.html).	
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



<!--
### Sesión 4: Presentación de la práctica

* [Práctica: Implantación y despliegue de una aplicación web estática](estatica.html)

### Sesión 5: Trabajo Práctica 1

### Sesión 6: Trabajo Práctica 1
-->